# U2 L13: Badge Log Analysis Lab (Oct 16, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 4 MCQ on alerting thresholds and what each log source does and does not prove.

**Learning Objectives:**
- 2.4.A Analyze a multi-hundred-entry access log programmatically to identify anomalous access patterns
- 2.4.A Detect four specific attack classes: shared badges, tailgating, failed-then-success attempts, after-hours access
- 2.4.C Evaluate detection output and distinguish a real signal from a false positive

**Materials:** VS Code connected to the class server (`code-server` at `vscode.ivycollegiate.org` — log in with your school account), repo `ap-cyber/unit2-labs`, file `badge_log.csv` (~500 entries, 5 doors, 3 weeks), starter file `badge_analysis.py`, slides

**Environment note:** the server has Python 3.11 with **pandas** preinstalled. Use pandas. Run everything in the terminal panel (`python3 badge_analysis.py`), not in a notebook — you want to see the script fail and fix it. `git pull` first, always.

---

## Activities

1. **Hook (5 min):** Board the raw number: **~500 badge events across 5 doors over 15 school days.** Ask how long it takes to read that by eye at the rate of a security operator at 3 AM. Then ask what four things they would be looking for. That is the lab.

   Emphasize the framing: you are not hunting for a single event. You are writing **detection rules** — and the rules you write are what an automated monitoring system would run at scale. If you cannot express the check in code, nobody downstream can run it either.

2. **Starter code walkthrough (8 min):** Project the schema. Four columns, all strings, no index column:

   ```
   timestamp, badge_id, door, result
   2026-09-29T07:41:12, B-1042, MAIN-EAST, granted
   ```

   `result` is `granted` or `denied`. `door` is one of `MAIN-EAST`, `MAIN-WEST`, `LIB-ENTRY`, `SCI-ANNEX`, `SERVER-RM`. Timestamps are ISO local, 24-hour, no timezone.

   Walk the three lines that always break a first script:
   - The file is **not sorted by time.** Sort it first, or every windowing calculation is wrong. This is the bug that costs the most time in this lab.
   - `timestamp` is a string until you tell pandas it is a timestamp. Everything downstream depends on it.
   - A `granted` event does not mean someone walked through. It means a credential was accepted. Keep that assumption in mind for task 1.

3. **Four detections (24 min):** Work through the tasks in the starter file, which has the CSV load and a helper for pairwise time gaps already written. Each task has a comment block with the question it answers.

   **Task 1 — Shared badges (simultaneous use at distant doors).** One credential used at two doors that are far apart, within a time window too short to walk between them. Output the badge, both doors, both timestamps, and the gap in seconds. Then look at how many hits come back. Most groups get a handful — but check whether some of those are legitimately a person who walked. Decide: which hits are you reporting, and why is the rest noise?

   ```python
   import pandas as pd

   log = pd.read_csv("badge_log.csv", parse_dates=["timestamp"])
   log = log.sort_values("timestamp").reset_index(drop=True)

   # distance in seconds between the two ends of each building
   TRAVEL_SECONDS = 240
   DOOR_ZONE = {"MAIN-EAST": "A", "MAIN-WEST": "A", "LIB-ENTRY": "B",
                "SCI-ANNEX": "C", "SERVER-RM": "D"}

   def shared_badges(df, window_minutes=5):
       hits = []
       for badge, grp in df.groupby("badge_id"):
           rows = grp.to_dict("records")
           for i, a in enumerate(rows):
               for b in rows[i + 1:]:
                   gap = (b["timestamp"] - a["timestamp"]).total_seconds()
                   if gap > window_minutes * 60:
                       break
                   if a["door"] == b["door"]:
                       continue
                   if DOOR_ZONE[a["door"]] == DOOR_ZONE[b["door"]]:
                       continue
                   if gap < TRAVEL_SECONDS:
                       hits.append({"badge_id": badge, "door_a": a["door"],
                                    "ts_a": a["timestamp"], "door_b": b["door"],
                                    "ts_b": b["timestamp"], "gap_seconds": int(gap)})
       return pd.DataFrame(hits)
   ```

   `DOOR_ZONE` is the key idea: a shared badge means the *same credential* at *two places*, so you need a notion of which doors are far apart. Supplying the zone map is a scaffolding decision — a group that argues about it is arguing about the right thing, so let them.

   **Task 2 — Tailgating (rapid successive entries).** Successive granted events within a few seconds of each other at the *same* reader, with only one credential. Each pair is a credential plus an unlogged person. Output the reader, the times, and the count of events in each burst. Bursts of 3+ at a server room or staff entrance are the ones worth reading out.

   ```python
   def tailgating(df, gap_seconds=10):
       hits = []
       for door, grp in df[df["result"] == "granted"].groupby("door"):
           rows = grp.to_dict("records")
           burst = [rows[0]] if rows else []
           for prev, cur in zip(rows, rows[1:]):  # consecutive granted events
               if (cur["timestamp"] - prev["timestamp"]).total_seconds() <= gap_seconds:
                   burst.append(cur)
               else:
                   if len(burst) > 1:
                       hits.append({"door": door, "start": burst[0]["timestamp"],
                                    "end": burst[-1]["timestamp"],
                                    "events": len(burst)})
                   burst = [cur]
           if len(burst) > 1:
               hits.append({"door": door, "start": burst[0]["timestamp"],
                            "end": burst[-1]["timestamp"], "events": len(burst)})
       return pd.DataFrame(hits)
   ```

   **Task 3 — Failed then success.** A `denied` event followed within 5 minutes by a `granted` event **on the same badge**. This is the credential-probing pattern: someone tries a badge that isn't authorized, then uses one that is. Output badge, door, both timestamps, and the count of denied attempts before the success — the count is what distinguishes one fumble from a systematic attempt.

   ```python
   def failed_then_success(df, window_minutes=5):
       hits = []
       for badge, grp in df.groupby("badge_id"):
           rows = grp.sort_values("timestamp").to_dict("records")
           denied = 0
           for r in rows:
               if r["result"] == "denied":
                   denied += 1
               elif denied:
                   hits.append({"badge_id": badge, "door": r["door"],
                                "granted_at": r["timestamp"], "prior_denials": denied})
                   denied = 0
       return pd.DataFrame(hits)
   ```

   **Task 4 — After-hours access.** Anything outside 07:00–18:00 on a weekday, and anything on a weekend. Output badge, door, timestamp. Then subtract the legitimate population: cleaners, the security guard, staff with known early schedules. What is left is your real candidate list, and subtracting the known-benign is the actual analyst skill in this task — the code is trivial, the judgment is not.

   ```python
   def after_hours(df, start="07:00", end="18:00"):
       out = df[df["timestamp"].dt.dayofweek < 5].copy()
       mins = out["timestamp"].dt.hour * 60 + out["timestamp"].dt.minute
       lo = int(start[:2]) * 60 + int(start[3:])
       hi = int(end[:2]) * 60 + int(end[3:])
       return out[(mins < lo) | (mins > hi)]
   ```

4. **Debrief (8 min):** Each group reports: how many hits from each of the four detections, and which single detection produced the most *useful* output.

   Then the two questions that matter, and give them time:
   - **What would a false positive look like here?** Name a specific one from your own results. A student who left early and badged out at the far door; a guard doing a patrol sweep; a teacher who badged into the annex on the way to the gym; a delivery driver badging the service door. Every one of your detections has a benign twin, and the detections that produce 200 hits are the ones that will be switched off within a month.
   - **How do you avoid alert fatigue?** Baseline first (what does normal look like for this door, this badge, this hour), then thresholds that key on *deviation* rather than on absolute events, then a hard volume budget. If the rule fires more than a handful of times a week, it is a report, not an alert — and a report can wait until morning while an alert cannot. Note the 2.4.C connection to Thursday's discussion: the alert at 3 AM is worthless if there is nobody to receive it.

   Close on the honest limitation: all four detections read a log, and a log records credentials, not people. Monday's capstone is where these detections meet video and the gap gets visible.

**Homework (due Mon 20:30 — Monday quiz):** Finish all four tasks and save your results to `results_task1.csv` … `results_task4.csv` in the repo. Read the correlation evidence packet structure before Monday — you will be reconstructing a timeline from four sources, which is the version of this skill that shows up on the test.

**Differentiation / ELL support:** The starter file supplies the CSV load, the sort, the zone map, and a working function per task with the bugs already removed — groups modify and extend rather than writing from scratch, which puts the cognitive load on the detection logic where it belongs. `zone_distance.txt` in the repo has a rough door-to-door walk time table if a group wants to replace the zone map with real distances. Students who need a narrower target can run tasks 1 and 4 only; tasks 2 and 3 are the ones where the pandas idiom is hardest. A finished output example for task 4 is in the repo as `example_task4_output.csv` for students who need to see the target shape. The debrief questions work well in pairs before the whole-group report.