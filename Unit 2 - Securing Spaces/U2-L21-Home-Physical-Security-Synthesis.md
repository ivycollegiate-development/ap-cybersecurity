# U2 L21: Home Physical Security Synthesis + Audit Launch (Oct 28 — PAPER DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on the mock sprint rationales, weighted to the objectives that were most-missed on the previous sprint.

**Learning Objectives:**
- 2.1.A–2.1.D the four phases of a cyberattack, applied to a physical entry point at home
- 2.1.E Assess risk for a named threat to the student's own building
- 2.1.F Select and justify a treatment option for each top risk
- 2.2.A Physical attack vectors — tailgating, lock bypass, social engineering at the door
- 2.2.B Physical vulnerabilities — unsecured doors, poor lighting, exposed cabling, no mantraps
- 2.2.C Environmental threats — fire, flood, power loss, HVAC failure, typhoon/flood resilience
- 2.3.A Perimeter & Building layer controls — fences, lighting, CCTV, guards, reception, badges
- 2.3.B Room layer controls — server/gear closet locks, **environmental controls** (HVAC, fire suppression, humidity), motion sensors
- 2.3.C Rack/Asset layer controls — cable locks, port locks, asset tags, mantraps, biometric access
- 2.4.A Log sources — badge logs, guard patrol logs, CCTV, visitor logs, sensor alerts, doorbell events, router logs
- 2.4.B Correlation & anomaly detection — off-hours access, impossible travel, missing patrols, CCTV gaps, multi-source correlation
- 2.4.C Alerting & response — alert design (thresholds, enrichment), escalation, incident documentation

**Materials:** Slides, layered program design sheet (six zones, one control column and one objective-code column per control, audit checklist on reverse), peer-check rubric, Unit 2 study guide issued at the end of class, teacher's completed sample audit (2 pages, own apartment)

**No computers today.** Paper day — the program is designed on the handout. Students work individually (3 students = 3 distinct home sites).

**Google Classroom Assignment (single, covers both days + break):**
- **Title:** U2 L21–L22: Home Physical Security Synthesis + Fall Break Audit
- **Posted:** Oct 28 (start of class)
- **Due:** Nov 9 (first class back, brought physically)
- **Topic:** Unit Tests  (matches grading category — the audit is graded as a HW quiz on Nov 9)
- **Description:** Two-day in-class synthesis (Oct 28–29) plus Fall Break take-home audit. Oct 28: design your 6-zone layered program for your actual home, every control justified by Unit 2 LO code. Oct 29: clarification, independent audit work time, teacher check-ins. Fall Break: complete the audit checklist (on back of design sheet) for your building — 2–4 pages handwritten, both Taiwan addenda. Collected Nov 9, graded as HW quiz.
- **Attachments:** Design sheet (double-sided with audit checklist), Peer-Check Rubric, Unit 2 Study Guide
- **Points:** 100 (audit quiz score recorded in Unit Tests category)
- **Turn in:** "Hand in" button — students mark done when they bring the physical packet Nov 9. No digital submission.

---

## Activities

1. **Hook + Threat Model (10 min):** "Describe your building's entry sequence from street to your door. What does the log show vs. what actually happened?" Take two or three answers, then push: **The vulnerability and the detection failure are the same event.** Each student articulates how their home's threat model shifts when viewed through Unit 2 lenses — what's worth protecting, who wants in, what the building already does, and what it doesn't.

2. **Individual Design — Layered Physical Security Program (35 min):** Each student designs a layered program across six zones for their **actual home / apartment building / dorm**. Every control must be justified by **naming the learning objective it satisfies** — the code goes in the second column. A control with no objective code does not go on the sheet.

   **Zone mappings for residential context:**
   - **Zone 1: PERIMETER** — Building exterior, property line, parking, lobby entrance, shared building envelope
   - **Zone 2: ENTRY CONTROL** — Building entry (guard, intercom, keypad, fob), apartment/room door, tailgating exposure
   - **Zone 3: INTERIOR ZONES** — Rooms, network gear closet, NAS/server shelf, work-from-home desk, clean-room equivalent (if any)
   - **Zone 4: MONITORING** — Building CCTV (if any), hallway cameras, doorbell cam, smart sensors, environmental sensors
   - **Zone 5: DETECTION** — Badge/access logs (building), doorbell events, router/log sources, sensor alerts, guard patrol logs
   - **Zone 6: RESPONSE** — Who you call, escalation path, landlord/management contact, personal incident log, named owner + action

   Push students past the obvious. If a student's entry control is a keypad code, ask which physical attack the keypad does nothing about (2.2.A tailgating, 2.2.C shoulder surfing). If their monitoring is a doorbell camera, ask what the camera does not generate (2.4.A — cameras are not logs; the badge/access log is where the correlation of 2.4.B comes from). If their response is "call the landlord," ask for the named owner and the specific action.

   Local texture worth using: **typhoon/flood resilience** for gear closet and ground-floor equipment (2.3.C), **shared lobby** where one entrance serves multiple households, **building network infrastructure** (shared switch, flat VLAN, management interface reachable from tenant Wi-Fi) as an access path nobody in the unit owns (2.4.B).

3. **Peer Cross-Check (15 min):** Students swap sheets in a trio rotation (A→B, B→C, C→A). Each reviewer finds:
   - 1 missing LO code (a control with no code)
   - 1 control with a mismatched code
   - 1 zone that is empty or has only generic controls ("locks", "cameras")
   Reviewers write the code/zone on a sticky note and place it on the sheet. Authors then have 3 minutes to add/correct.

4. **Gap Hunt (Whole Class, 10 min):** Read the LO codes off the boards/sheets and compare against the full objective list. **Which learning objective did no student cover?** That gap is the honest result of today, and it is the first item on the re-teach board for Nov 9.

5. **Audit Packet Walkthrough + Launch (10 min):** Project the two-page completed sample audit (teacher's apartment). Narrate the reasoning in the margin: why this is 2.2.A and not 2.2.C, why likelihood is medium not high, why treatment on the switch closet is avoid rather than mitigate. Make the standard explicit: **describe, assess, treat, evidence.** Four lines minimum per finding. A finding with no evidence line is an opinion, and opinions do not earn credit.

   Then walk the **audit checklist (on the back of the design sheet)** requirement by requirement:
   - Perimeter and door — who can reach the door unchallenged?
   - Access control — keypad, fob, card, guard, intercom, or nothing. How are codes distributed, changed, revoked?
   - Tailgating exposure (2.2.A) — count how many people enter behind one badgeholder/resident during a normal evening. What does the log record?
   - Shoulder surfing and door social engineering (2.2.B, 2.2.C) — propped door, unverified "I'm here to fix the router," delivery held open.
   - Cloning and lock picking (2.2.C) — proximity cards copyable; tubular pin tumbler pickable in seconds.
   - Surveillance (2.3.B) — CCTV placement: entry or parking lot?
   - Environmental and monitoring (2.3.C) — lighting, signage, landscaping sightlines, fire doors wedged open, log nobody reviews.
   - **Taiwan Addendum A — Shared Building Network (2.4.B):** Record one risk from shared building network infrastructure + evidence that would reveal it.
   - **Taiwan Addendum B — Typhoon/Flood Season (2.3.C):** Record one physical-resilience gap relevant to typhoon/flood + what it would break.
   - Risk line (2.1.E) — every finding gets likelihood and impact, not just description.
   - Treatment line (2.1.F) — every finding gets avoid/transfer/mitigate/accept with one sentence of reasoning.

6. **Due Date, Format, and Unit 2 Recap (8 min):**
   - **Due:** First class back — **Nov 9**. Brought physically, not a photo. Graded as HW quiz at start of day.
   - **Length:** 2–4 pages, hand-written. One page minimum per addendum.
   - **Bring:** The audit checklist (back of today's sheet), plus a two-sentence answer to each of the two Taiwan addenda.
   - **The graded thing is the reasoning, not the building.** A student who finds a serious flaw in a modest building and treats it well outscores a student who finds nothing at a gated complex.
   - Unit recap: 2.1 attack phases and risk, 2.2 physical vulnerabilities, 2.3 protections, 2.4 detection. Flag that Nov 9–12 is four straight review days driven by the class's own audits. Test is **Nov 13**.

7. **Study Guide Section 1 Start (5 min):** Issue Unit 2 study guide. Students complete section 1 tonight: every objective code, and for each one the control they would build first at their home site. One line each. The break audit quiz on Thursday (Nov 9) uses Unit 2 objectives alongside the audit content.

**Homework (due Nov 9, brought to class — graded HW quiz that day):**
- Complete the Fall Break physical security audit, 2–4 pages, by hand. Both Taiwan addenda included.
- Study Guide Section 1: every objective code + first control for home site.
- Read the first CED excerpt of Unit 3 (Securing Networks) — quiet read only.

**Differentiation / ELL support:** The design sheet is pre-formatted with six zones and both columns labelled. Objective codes printed in a reference strip along the edge. Audit checklist on reverse is fillable as a table. A one-page bank of likelihood/impact phrasings and a treatment-selection table provided for students who find the risk vocabulary harder than the observation work. Students who cannot revisit their building may audit a shared common area (lobby, mailroom, bike room, stairwell) — vulnerability categories are identical. For the two addenda, give a worked example of each so required specificity is clear.