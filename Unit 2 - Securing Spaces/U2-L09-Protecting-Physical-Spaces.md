# U2 L9: Protecting Physical Spaces (Oct 12, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 4 MCQ on the case studies — identify the vulnerability and the control that would have stopped each.

**Learning Objectives:**
- 2.3.A Compare locks, badge readers, mantraps, and guards as access controls, including their costs and failure modes
- 2.3.B Explain how CCTV coverage, placement, and retention length determine whether footage is usable
- 2.3.C Describe environmental and monitoring controls including motion sensors, alarms, and UPS/generator backup

**Materials:** Slides, control catalog handout with prices ([GDoc](https://docs.google.com/document/d/1Gw3Xa60zTpQIgZik17NBuQK-FMhtpDHg6X52PBNix2M/edit)), threat-to-control matching worksheet, CCTV placement floor plan from Friday

---

## Activities

1. **Hook (5 min):** "$20 lock vs $2,000 biometric reader." Put both on the board. Ask which door gets the biometric reader. Then change the question: *the biometric reader is on the server closet, which holds $500,000 of equipment and the grade database. The $20 lock is on the supply closet, which holds $200 of paper.* Reordering the two numbers reverses the answer, and that is the whole skill — matching control cost to asset value and to the threat, not to how impressive the control looks. A $2,000 fingerprint reader on a supply closet is theater.

2. **Direct instruction (15 min):** Walk the catalog. Keep cost in NT$ and be honest about the ranges.
   - **Locks and access controls (2.3.A).** Pin tumbler, deadbolt, mortise, and electronic keypad. Keypad logs an identity if the code is shared it logs nobody — shared codes are the failure mode. Mechanical advantage: an attacker with a long screwdriver and 30 seconds beats most residential deadbolts. Then **badge readers** (proximity, 125 kHz, cheap and clonable; smart/EM cards and mobile credentials, harder to clone), **biometrics** (fingerprint, face, iris — high cost, and note the failure modes: fingerprint readers defeated by a gelatin finger, face recognition defeated by a mask before modern liveness checks, and every one of them fail closed or fail open depending on configuration), and **mantraps** — the two-door interlock that physically cannot admit two people at once. The mantrap is the direct answer to tailgating, and it is also the answer a $20 lock can never be.
   - **Guards.** A human being is the only control that can evaluate a situation rather than match a credential. A guard at the front desk stops the "I'm with the vendor" attack that no reader will. Cost is the highest recurring cost in the catalog and guards are also the control most likely to be phoned in.
   - **CCTV and surveillance (2.3.B).** Placement beats resolution: coverage of the *approach* and the *door*, not just the room inside. Blind spots, camera height, and lighting decide whether a face is identifiable. **Retention is the control that gets skipped** — 30 days of footage at 4 Mbps per camera is real storage, and footage deleted before an investigation is evidence that never existed. A camera with no retention policy is a decoration. Also: notification and live monitoring change what cameras are for, because recorded footage only helps after the fact.
   - **Environmental and monitoring controls (2.3.C).** Motion sensors and door contacts, alarm zones, glass-break and vibration sensors on high-value windows. Environmental: temperature, humidity, and water-leak detection in a server closet. **UPS and generators** — a UPS buys you minutes, it is not a generator, and a generator without a tested transfer switch and fuel contract is a very expensive building ornament. Add Taiwan specifics: typhoon and flood exposure, and why a fab's water and power resilience is a physical security problem and not just a facilities one.

3. **Activity — threat-to-control matching (18 min):** Worksheet, individually then compare in pairs. Twenty threats, twenty controls from the catalog. For each: name the control, give its cost, and state the asset you are protecting. Then the harder half: **five of the twenty are deliberately ambiguous** — a threat that two different controls would genuinely address. For those, write both, cost both, and say which you would buy first and why.

   Sample rows to set up the format:
   - Someone holds the stairwell door for a stranger → mantrap (highest cost, eliminates the vector) or a staffed door (partial, and the guard can be phoned in). Cost: mantrap NT$250,000 installed; staffed door NT$1.4M/yr.
   - A stolen badge used on Saturday → smart/EM card instead of 125 kHz proximity (reduces cloning), or photo-badge check at a staffed gate (detective, not preventative). Say which.
   - Theft discovered 60 days later → retention policy. Cheapest row on the sheet and the most commonly missed.
   - Break-in during a power outage → UPS on the badge reader, or a mechanical lock, or a guard. All three defensible, three different cost profiles.
   - Camera footage too dark to identify anyone → lighting, not a better camera. Add NT$3,000 of lighting rather than NT$30,000 of resolution, and justify it.

4. **Close and exit ticket (7 min):** Two-minute pair share on the most expensive control in the catalog, and whether it earned its cost. Then exit ticket, collected on paper:

   **"This building has a $2,000 biometric reader on the supply closet and a $20 lock on the server closet. Name the vulnerability, the risk it creates, and the one control you would change first — with a cost."**

   The expected answer reorders the two controls. If a student writes "get more cameras," the response is *what does the camera do that the lock was supposed to do* — detection and prevention are not the same function, and this is the distinction from Friday's defense-in-depth lesson reappearing here.

**Homework (due Tue 20:30 — Wednesday quiz):** CED 2.3 reading, plus one paragraph on which physical control this building is missing and what it would cost. Bring the CCTV floor plan — Wednesday's paper day audit walk uses it.

**Differentiation / ELL support:** The catalog handout lists every control with a price range and a one-line failure mode, so the knowledge load is matching, not recall. Matching is a two-stage task: pairs may complete the first ten rows on their own and compare at row ten before finishing the ambiguous five. A printed control-category index (access / surveillance / environmental / personnel, with the CED codes 2.3.A–C alongside) is on the front desk. The exit ticket is a single prompt with a three-part structure; students may bullet the three parts rather than writing prose, and may say the answer aloud to a partner first. Cost reasoning is the target skill — if a student has the control right but no cost, give half credit and have them attach the number.
