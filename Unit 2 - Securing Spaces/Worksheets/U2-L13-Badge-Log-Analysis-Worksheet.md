# U2 L13 — Badge Log Analysis Lab (Unit 2)

AP Cybersecurity — Unit 2					Name: ______________	Date: ______________

GitHub repo: **ivycollegiate-development/apcyber-u2-badge-log-analysis-lab**

## The Scenario

You work in ICA's security office. The principal has received a report that someone may have accessed the server room without authorization. You have the badge access log — **~500 events across 5 doors over 3 weeks** — and a starter script with four detection rules to write.

Your job is not to find one bad event. It is to write the **detection rules** an automated monitoring system would run at scale. If you cannot express the check in code, nobody downstream can run it either.

## Before You Start

- **Fork** the repo to your own account.
- Open `badge_analysis.py` in VS Code — on the class server at `vscode.ivycollegiate.org` (log in with your school account), or in Codespaces. `git pull` first, always.
- Run it in the **terminal panel**, not a notebook: `python3 badge_analysis.py`. The server has Python 3.11 with **pandas** preinstalled — use pandas.

### The Schema

```
timestamp, badge_id, door, result
2026-09-29T07:41:12, B-1042, MAIN-EAST, granted
```

- `result` is `granted` or `denied`
- `door` is one of `MAIN-EAST`, `MAIN-WEST`, `LIB-ENTRY`, `SCI-ANNEX`, `SERVER-RM`
- Timestamps are ISO local, 24-hour, no timezone

**Three things that break a first script:**

- The file is **not sorted by time.** Sort it first, or every windowing calculation is wrong. This is the bug that costs the most time in this lab.
- `timestamp` is a string until you tell pandas it is a timestamp. Everything downstream depends on it.
- A `granted` event does not mean someone walked through. It means a **credential** was accepted. Keep that in mind for Task 1.

## Part 1: Write the Four Detections (24 min)

Each task in `badge_analysis.py` is a function with a `# TODO` body and a comment block stating the question it answers and the columns it must output.

| Task | Detection | Output file |
|---|---|---|
| 1 | **Shared badges** — one credential used at two doors far apart, inside a window too short to walk between them | `results_task1.csv` |
| 2 | **Tailgating** — successive `granted` events within seconds at the same reader, one credential | `results_task2.csv` |
| 3 | **Failed then success** — a `denied` event followed within 5 minutes by a `granted` event on the same badge | `results_task3.csv` |
| 4 | **After-hours access** — anything outside 07:00–18:00 on a weekday, and anything on a weekend | `results_task4.csv` |

**Output columns required:**

| Task | Columns |
|---|---|
| 1 | badge_id, door_a, ts_a, door_b, ts_b, gap_seconds |
| 2 | door, start, end, events |
| 3 | badge_id, door, granted_at, prior_denials |
| 4 | badge_id, door, timestamp |

`DOOR_ZONE` in the starter is the key idea for Task 1: a shared badge means the *same credential* at *two places*, so you need a notion of which doors are far apart. Supplying the zone map is a scaffolding decision — if you think it is wrong, argue about it, because you are arguing about the right thing.

**The real skill is subtraction.** Every one of these detections has a benign twin in the data — a guard on a patrol sweep, a janitor, a teacher who badged into the annex on the way to the gym, a person who badged out at the far door because it is closer to the car park. Your job is not to report every hit. Your job is to decide which hits you are reporting, and to say why the rest is noise.

## Part 2: Findings and Debrief (8 min)

Answer in the space below.

- **Hits per detection:** how many did each of your four rules produce?
- **Most useful detection:** which single rule produced the most *useful* output, and why?
- **False positive:** name one specific benign hit from your own output and explain why it is not a finding.
- **Alert fatigue:** if a rule fires more than a handful of times a week, is it a *report* or an *alert*? Why does that distinction matter at 3 AM?
- **The honest limitation:** all four detections read a log, and a log records **credentials, not people**.

Findings:

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

## The Gate — What "Done" Means

- All four `results_taskN.csv` files exist and are committed.
- Each contains what its task comment says it should — not just a bare count.
- Task 1's output shows the gap in seconds; Task 2's shows the events per burst; Task 3's shows the count of prior denials; Task 4's shows badge, door, and timestamp.
- You can name a specific false positive from your own output and explain why it is not a finding.

**Homework:** finish all four tasks, commit the four CSVs, and read `evidence_packet_template.md` before Monday — you will be reconstructing a timeline from four sources.
