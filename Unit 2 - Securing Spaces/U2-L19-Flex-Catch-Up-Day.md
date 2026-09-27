# U2 L19: Flex / Consolidation Day (Oct 26, Mon — TECH DAY)

> **Schedule change.** This slot originally held the Unit 2 Test. The test has been **moved to Friday, Nov 13 (L28)** so that the Nov 9–12 review block sits *before* the test rather than after it. There is no test today.

**⚡ HW Quiz (8 min):** 8 MCQ from the Unit 2 study guide objective list — one per learning objective, hardest items from the mini-project and the FRQ packet.

**Learning Objectives:**
- 2.4.A Monitor access and badge logs to identify anomalous physical access
- 2.4.B Correlate video and log data to identify physical attacks
- 2.4.C Set an alerting threshold and name the response it triggers

**Materials:** Slides, badge log extract from the L13 lab, detection reference sheet, re-teach board

---

## Activities

1. **HW quiz (8 min):** Cold, no notes, from the study guide objective list. This is the same list students will be held to on Nov 13.

2. **Guided re-read — 2.4 detection (12 min):** The objective students most often miss, because they assume the logs will simply tell them what happened. Re-read 2.4.A–C together, using the L13 badge log extract.
   - **2.4.A** — what a badge log shows: who badged in, where, when. What it cannot show: whether the person was the person, whether anyone else came through the door behind them, and anything at all about an unbadged entry.
   - **2.4.B** — the point of correlation. Walk the extract: a badged-in event at 22:40 in a restricted zone, no video coverage of the corridor at that time. One source is silent. Cross-referenced, that is a finding.
   - **2.4.C** — a threshold has to be a value someone chose, and a response has to be a named action with an owner. "Alert on after-hours restricted-zone access → notify the facilities lead, who checks the corridor camera and the zone's asset inventory." Compare against "we monitor it."

3. **Open lab time (20 min):** Any student behind on a Unit 2 lab submission finishes it here — risk register (L06), campus physical security audit (L10), badge log analysis (L13). Students who are current use the time to redo the one they scored lowest on. Talk to me if you are not sure where you stand.

4. **Exit ticket (5 min):** "Which Unit 2 learning objective do you still not own?" One objective code, one sentence on what is still unclear. Sort these at the end of class — they set the re-teach order for Nov 9–12.

**Homework (due Tue 20:30 — Oct 27 quiz):** Nothing new. Review your Unit 2 study guide ahead of tomorrow's mock MCQ sprint. Bring it.

**Differentiation / ELL support:** The re-read section is built around one specific log extract, so students work from a concrete artifact rather than an abstraction. Exit tickets may be written in Chinese; the objective code is what I sort on, so write the code even if the sentence is short.
