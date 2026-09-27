# U2 L14: Video and Log Correlation (Oct 19, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on access log monitoring and alerting thresholds from the lab.

**Learning Objectives:**
- 2.4.B Correlate badge logs, visitor logs, patrol records, and camera records into a single incident timeline
- 2.4.B Identify what correlation resolves that any single source cannot — and what it still cannot resolve
- 2.4.C Write an incident report that states findings, evidentiary limits, and recommended response

**Materials:** Printed evidence packet per group (badge log, visitor log, guard patrol report, CCTV descriptions, floor plan with camera IDs), timeline worksheet, printed 1-page report template, slides

---

## Activities

1. **Hook (5 min):** **"02:14. Server room door opens. The alarm fires at 02:15. At 03:40 a guard walks past the server room, notes the door 'ajar,' and closes it. At 04:05 an entry is recorded at MAIN-EAST. At 08:15 someone asks why the server room log shows an entry at 02:14 when the guard reported nothing entered the building overnight."**

   The guard's report is not wrong. Nobody entered through the front door. Ask the room: so what happened? That is the whole lesson — the answer is a badge that was cloned, a door that was propped, a service hatch nobody logs, or a guard who was looking at the wrong thing. Four sources, four partial truths, one timeline.

   Frame it: **no single record is an incident. Correlation is what turns a set of records into a story — and the story still has to survive being written down.**

2. **Evidence packet walkthrough (6 min):** Walk the printed packet structure, and make clear this is the deliverable format:
   - **Section 1 — Incident summary.** Two sentences. What happened, where, and when it started and ended. Written last.
   - **Section 2 — Timeline.** Every record, all four sources, in one merged time-ordered list. Columns: timestamp, source, what the record says, and an evidence column noting *what it does not establish*. Nothing gets dropped because it looks irrelevant — the 01:52 loading dock entry that means nothing is in the timeline and marked as meaning nothing.
   - **Section 3 — Findings.** The anomalies, each tied to the timeline entries that support it, with a confidence level: confirmed, probable, or unverified.
   - **Section 4 — Gaps.** What is missing and why it matters. This is the section that separates an incident report from a guess. "No camera covers the server room stairwell landing — the badge event at 02:14 cannot be visually confirmed" is a legitimate, valuable finding.
   - **Section 5 — Recommended response.** Immediate actions, then follow-up, each tied to a finding.
   - **Section 6 — Source records.** Copies of the four logs as received, unmodified, with a note on who provided each and when.

3. **Reconstruct the timeline (20 min):** Groups merge all four sources into one time-ordered list, then answer these in order:
   - **Establish the boundary.** First record in the incident window and last. Everything before 01:30 is context, not evidence — mark it as context.
   - **Reconcile the people.** Cross the visitor log against the badge log. Everyone who signed in, against everyone who badged. Is anyone in a video description who appears in neither log? Is anyone in a log whose movement the cameras never saw?
   - **Test the timing claims.** The guard's "no entry overnight" and the 04:05 MAIN-EAST entry have to be reconciled. Either the guard is wrong, or the entry used a credential that is not that person's, or the 04:05 entry is a *response* to something. Push groups to commit to a reading, not a shrug.
   - **Locate the gap.** Where is the moment that no source covers? The most valuable output of this exercise is the specific interval the evidence cannot speak for — 02:22 to 03:40 is an hour with a server room open and no record of anyone in it.
   - **Name the mechanisms.** For the entry that happened without a logged person, list every physical mechanism from Unit 2 that could explain it: cloned badge, tailgating through a door with a faulty latch, propped service door, an unlogged contractor with a temporary badge that was never deactivated, or someone already inside who never left. The evidence narrows it; it does not eliminate all but one.

   Circulate and push on the last one. The honest answer is usually two or three surviving mechanisms, and a group that reaches for a single tidy explanation has over-read the evidence.

4. **Write the 1-page incident report (10 min):** Individually, using the six-section template. Hard limit: one page. Section 1 is the two-sentence summary; the rest is headings and bullets, not paragraphs.

   The test for a good report: someone who was not in the room can reconstruct the same timeline from it, and knows exactly which claims are solid and which are inferences. Confidence labels in Section 3 are required, not optional — an unlabeled inference is a claim.

5. **Exit debrief (4 min):** Two groups read their Section 1 summaries and their Gaps section. Ask the room which mechanism each group converged on, and whether the evidence actually rules out the others.

**Homework (due Tue 20:30 — Tuesday quiz):** Bring your mini-project role assignment and a first cost estimate. Tomorrow the groups build the whole defense-in-depth plan and you need to know who is doing what before period starts.

**Differentiation / ELL support:** The evidence packet is printed with source headers and a field key, and the timeline worksheet is pre-built with the time column and the four source columns — students fill rows rather than construct the table. Camera descriptions are written in plain observational language ("adult, dark jacket, no visible badge, moving from the landing toward the SERVER-RM door") so the reasoning load is on interpretation, not on parsing. Provide a filled Section 1 example for students who need to see the register of a two-sentence summary. Groups of four can assign timeline, reconciliation, and report roles, which also gives a quieter student a defined part. The "name the mechanisms" question works well orally and is a good place to let students argue.