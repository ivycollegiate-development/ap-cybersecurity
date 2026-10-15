# U2 L13: Badge Log Analysis Lab (Oct 16, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 4 MCQ on alerting thresholds and what each log source does and does not prove.

**Learning Objectives:**
- 2.4.A Analyze a multi-hundred-entry access log programmatically to identify anomalous access patterns
- 2.4.A Run and interpret four detection rules: shared badges, tailgating, failed-then-success attempts, after-hours access
- 2.4.C Evaluate detection output and distinguish a real signal from a false positive

**Materials:** VS Code connected to the class server (`code-server` at `vscode.ivycollegiate.org` — log in with your school account), repo **`ivycollegiate-development/apcyber-u2-badge-log-analysis-lab`**, files `badge_log.csv` (**834 events, 60 badges, 5 doors, 15 school days**), the four detections in `badge_analysis.py`, `evidence_packet_template.md`, slides

**Environment note:** the server has Python 3.11 with **pandas** preinstalled. **Students do not write code in this lab — the four detections are already written.** They run it in the terminal panel (`python3 badge_analysis.py`), not in a notebook, so they watch the four CSVs land on disk. `git pull` first, always.

---

## Activities

1. **Hook (5 min):** Board the raw number: **834 badge events across 5 doors over 15 school days.** Ask how long it takes to read that by eye at the rate of a security operator at 3 AM — then ask what four things they would look for. That list is what a detection rule *is*: a question precise enough that a machine can answer it. Today they run four of those questions over the whole log, and the grade is on what they make of the answers.

2. **Read the script (8 min):** Project the schema. Four columns, all strings, no index column:

   ```
   timestamp, badge_id, door, result
   2026-09-29T07:41:12, B-1042, MAIN-EAST, granted
   ```

   `result` is `granted` or `denied`. `door` is one of `MAIN-EAST`, `MAIN-WEST`, `LIB-ENTRY`, `SCI-ANNEX`, `SERVER-RM`. Timestamps are ISO local, 24-hour, no timezone.

   Then walk the lines that make the script work, because reading them is how students learn what the output can and cannot tell them:
   - The file is **not sorted by time.** The script sorts it on load. Every windowing calculation depends on that line.
   - `timestamp` is a string until you tell pandas it is a timestamp. Everything downstream depends on it.
   - A `granted` event does not mean someone walked through. It means a credential was accepted. That distinction is the whole of task 1.

   Point out the two judgement calls sitting in the file — `TRAVEL_SECONDS = 240` and `gap_seconds=15` — and ask the room what would change if they moved. Nobody is writing these rules today, so the argument about thresholds replaces the argument about syntax, and that is the better argument.

3. **Run the four detections and read the output (24 min):** Students run the script and read the four CSVs. The script works from a clean clone, so anything broken is an environment problem (`git pull`, wrong folder), not a code problem — solve those fast and keep the room on the output. **The row counts are not published anywhere: they come from the students' own run.** Circulate and raise the one thing per task:

   **Task 1 — Shared badges.** One credential at two doors far enough apart that the gap between them is too short to walk. Ask how many hits came back and whether each one is really a second person. The line to repeat: *a `granted` is a credential, not a body.* Also note the shape the rule is blind to — it compares one badge's own events, so a sequence spread across four different doors inside a minute is not a shared badge, it is a different question.

   **Task 2 — Tailgating.** Bursts of `granted` events seconds apart at the same reader. Each extra event in a burst is one credential plus one person who did not badge. Ask what the rule does with three *different* badges at one door inside 30 seconds, and then ask whether the 15-second threshold is defensible. It is the clearest example of a rule that finds something and still misses the interesting thing.

   **Task 3 — Failed then success.** This is where alert fatigue becomes visible on the board. The rule returns a long list of hits and **one column** — `prior_denials` — separates the rows worth acting on from the rest. Ask them which value of that column they would wake someone at 3 AM for, and why. One denial then a success is a fumbled door code; it happens to everyone every week. Three or four in a row followed by a success is somebody working out which badge works where.

   **Task 4 — After-hours access.** The code is trivial; the judgement is not. The list includes the legitimate overnight population — cleaners, the guard's patrol sweep, staff with known early or late schedules. Subtract the known-benign and report what is left. Make them do the subtraction visibly, so the debrief can talk about it.

4. **Debrief (8 min):** Each group reports hits per detection, which single detection produced the most *useful* output, and **one specific false positive from their own output**.

   Then the two questions that matter, and give them time:
   - **What would a false positive look like here?** Name a specific one from your own results. A guard doing a patrol sweep; a janitor on the same round every night; a teacher who badged into the annex on the way to the gym and badged out the far door because it is closer to the car park; three people leaving a staff meeting together. Every one of the four detections has a benign twin in this log, and the detection with the longest output is not the one with the most findings — it is the one that will be switched off within a month.
   - **How do you avoid alert fatigue?** Baseline first (what does normal look like for *this* door, *this* badge, *this* hour), then thresholds that key on *deviation* rather than on absolute events, then a hard volume budget. If the rule fires more than a handful of times a week, it is a report, not an alert — and a report can wait until morning while an alert cannot. Note the 2.4.C connection to Thursday's discussion: the alert at 3 AM is worthless if there is nobody to receive it.

   Close on the honest limitation: all four detections read a log, and a log records credentials, not people. Monday's capstone is where these detections meet video and the gap gets visible.

**Homework (due Mon 20:30 — Monday quiz):** Commit the four `results_taskN.csv` files — that is the deliverable, and an unrun placeholder is not it. Name a specific false positive from your own output. Read `evidence_packet_template.md` before Monday — you will be reconstructing a timeline from four sources, which is the version of this skill that shows up on the test.

**Differentiation / ELL support:** Because the detections ship complete, no student can be blocked by a code error and the whole 24 minutes goes to reading output and arguing about it — the cognitive load sits on the reasoning, which is where 2.4.C lives. Students who need a narrower target: run task 1 and task 4 first, then task 3; task 2's output is the smallest and the least ambiguous, so it is a good place to start a group that is unsure. The debrief questions work well in pairs before the whole-group report. **Note:** the lab repo no longer ships an answer key — `SOLUTIONS.md` was removed when the detections moved into the script. If a student asks for "the answers", the answers are their own four CSVs plus the argument about which rows matter.
