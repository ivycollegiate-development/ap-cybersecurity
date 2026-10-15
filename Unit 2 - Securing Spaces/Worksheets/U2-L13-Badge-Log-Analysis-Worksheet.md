# U2 L13 — Badge Log Analysis Lab (Unit 2)

AP Cybersecurity — Unit 2					Name: ______________	Date: ______________

GitHub repo: **ivycollegiate-development/apcyber-u2-badge-log-analysis-lab**

## The Scenario

You work in ICA's security office. The principal has received a report that someone may have accessed the server room without authorization. You have the badge access log — **834 events, 60 badges, 5 doors, 15 school days** — and four detection rules that are already written.

Your job is not to find one bad event. It is to run the four rules an automated monitoring system would run at scale, and then say which of the hits are findings. A rule that finds something is not the same as a rule that found the right thing.

## Before You Start

- **Fork** the repo to your own account.
- Open the repo in VS Code — on the class server at vscode.ivycollegiate.org (log in with your school account), or in Codespaces. git pull first, always.
- Run it in the **terminal panel**, not a notebook: `python3 badge_analysis.py`. **Do not edit the script — it already works.**

### The Schema

```
timestamp, badge_id, door, result
2026-09-29T07:41:12, B-1042, MAIN-EAST, granted
```

- `result` is `granted` or `denied`
- `door` is one of `MAIN-EAST`, `MAIN-WEST`, `LIB-ENTRY`, `SCI-ANNEX`, `SERVER-RM`
- Timestamps are ISO local, 24-hour, no timezone

**Three things to notice before you trust any output:**

- The file is **not sorted by time.** The script sorts it on load, and every windowing calculation depends on that line.
- `timestamp` is a string until you tell pandas it is a timestamp. Everything downstream depends on it.
- A `granted` event does not mean someone walked through. It means a **credential** was accepted. That distinction is the whole of Task 1.

## Part 1: Run the Four Detections (24 min)

The four detections are already written in `badge_analysis.py`. Run the script, then read what they produce.

| Task | Detection | Output file |
|---|---|---|
| 1 | **Shared badges** — one credential used at two doors far apart, inside a window too short to walk between them | `results_task1.csv` |
| 2 | **Tailgating** — successive `granted` events within seconds at the same reader, one credential | `results_task2.csv` |
| 3 | **Failed then success** — a `denied` event followed by a `granted` event on the same badge, and the count of denials that came first | `results_task3.csv` |
| 4 | **After-hours access** — anything outside 07:00–18:00 on a weekday, and anything on a weekend | `results_task4.csv` |

**What each output file must contain:**

| Task | Columns |
|---|---|
| 1 | badge_id, door_a, ts_a, door_b, ts_b, gap_seconds |
| 2 | door, start, end, events |
| 3 | badge_id, door, granted_at, prior_denials |
| 4 | badge_id, door, timestamp |

The two thresholds sitting in the script are judgement calls, not facts: `TRAVEL_SECONDS = 240` for Task 1 and `gap_seconds=15` for Task 2. If you think one of them is wrong, say so with evidence — that argument is worth more than the output.

Watch for what the rules cannot see. Task 1 compares one badge's own events, so a sequence spread across four different doors inside a minute is not a shared badge to that rule. Task 2 looks at one reader at a time, so three different badges at one door is a burst only if they land inside the threshold. Name a shape from your own output that a rule missed and you have found something real.

`DOOR_ZONE` in the script is the key idea for Task 1: a shared badge means the same credential at two places, so you need a notion of which doors are far apart. Two doors on the same facade should never fire the rule — the zone map is what stops them.

**The real skill is subtraction.** Every one of these detections has a benign twin in the data — a guard on a patrol sweep, a janitor, a teacher who badged into the annex on the way to the gym, a person who badged out at the far door because it is closer to the car park, three people leaving a staff meeting together. Your job is not to report every hit. Your job is to decide which hits you are reporting, and to say why the rest is noise.

## Part 2: Findings and Debrief (8 min)

Answer in the space below.

- **Hits per detection:** how many did each of your four rules produce?
- **Most useful detection:** which single rule produced the most useful output, and why?
- **False positive:** name one specific benign hit from your own output and explain why it is not a finding.
- **Alert fatigue:** if a rule fires more than a handful of times a week, is it a report or an alert? Why does that distinction matter at 3 AM?
- **The honest limitation:** all four detections read a log, and a log records **credentials, not people**.

Findings:

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

## The Gate — What "Done" Means

- All four `results_taskN.csv` files exist and are committed. An unrun placeholder is not it.
- Each contains what its task says it should — not just a bare count.
- Task 1's output shows the gap in seconds; Task 2's shows the events per burst; Task 3's shows the count of prior denials; Task 4's shows badge, door, and timestamp.
- You can name a specific false positive from your own output and explain why it is not a finding.

**Homework:** commit the four CSVs and name a specific false positive from your own output. Read `evidence_packet_template.md` before Monday — you will be reconstructing a timeline from four sources.
