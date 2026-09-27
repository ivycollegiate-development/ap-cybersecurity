# U2 L18: Unit 2 Review — FRQ Walk-Through (Oct 23, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on the mini-project's weak spots from yesterday — detection specifically. Badge log anomaly, video/log correlation, and alerting threshold.

**Learning Objectives:**
- 2.1.A preparatory / reconnaissance, 2.1.B establishing access, 2.1.C lateral movement, 2.1.D exfiltration
- 2.1.E risk assessment (likelihood × impact, inherent vs residual)
- 2.1.F risk treatment (avoid / transfer / mitigate / accept)
- 2.2.A tailgating / piggybacking, 2.2.B shoulder surfing, 2.2.C social engineering at the door, cloning, lock picking
- 2.3.A locks and access controls, 2.3.B surveillance / CCTV, 2.3.C environmental and monitoring controls
- 2.4.A access/badge log monitoring, 2.4.B video and log correlation, 2.4.C alerting thresholds and response

**Materials:** Slides, USB scenario handout, AP-style FRQ packet, self-scoring rubric, Unit 2 study guide, re-teach board

---

## Activities

1. **Hook — the USB in the parking lot (5 min):** "A USB drive is found in the ICA parking lot on Monday morning. It is not a student's. It has a logo on it. What do you do?" Take three answers before moving on — the fast ones are "hand it to the office" and "plug it in." Hold those; both are wrong, for different reasons, and both reasons are Unit 2 content.

2. **Scenario walk-through (15 min):** Work the class through the phases and the controls, in order, on the board.

   - **Phase 2.1.A — preparatory/reconnaissance.** Someone seeded that drive knowing staff would be curious. What were they learning about this school? Parking layout, shift patterns, whether anyone works weekends, that staff help people with flat batteries. The drive is the reconnaissance payload, not the attack.
   - **Phase 2.1.B — establishing access.** Physical access first, logical access second. A found drive is a physical delivery; the payload still needs someone to execute it. This is why the rule is: do not plug it in, hand it to IT, and let IT handle it in an isolated environment.
   - **Risk, 2.1.E.** Likelihood: high — it is free, it needs no account, no password, no network access from outside. Impact: high — a workstation that executes a payload can become the entry point for 2.1.C lateral movement. Inherent risk is high; after controls (no local auto-run, USB device control, awareness training, isolated analysis) residual risk is lower.
   - **Physical controls, 2.2 / 2.3.** 2.2.C social engineering at the door — curiosity is the social engineering vector here, not a credential. 2.3.A locks and access controls — the server room and the network closet are the rooms that matter, not the front door. 2.3.B CCTV on the entry and the parking area; 2.3.C environmental and monitoring — the server room's environmental controls are what stop a ransomware payload from becoming a hardware loss.
   - **Detection, 2.4.** 2.4.A badge and access logs: a drive tells you nothing in a badge log — this is the objective students most often assume covers more than it does. What does show up is the follow-on activity. 2.4.B correlation: a badge event at the network closet at 22:40 with no corresponding video, or video with no badge, is the signal. 2.4.C the threshold and response: alert on after-hours access to restricted zones, and the response is a defined action, not an email.

   Land the takeaway: **a physical attack is only half the answer.** The other half is what the logs show afterwards, and 2.4 is where most points are lost.

3. **AP-style FRQ, independent work (15 min):** Distribute the FRQ packet. Students work it alone, closed notes. The packet is written to the real CED format — a scenario, then parts (a) through (d), each tied to a specific learning objective. Read the directions aloud once, then let the room work in silence.

4. **Self-score against the rubric (10 min):** Students swap packets with a partner and score using the rubric provided — one point per correct response, half for a response that names the right control for the wrong reason. The point of peer grading is not the score; it is finding the parts where you did not know the objective. Students mark the rubric row that lost points and write the objective code at the top of their study guide.

**Homework (due Mon 20:30 — Oct 26 quiz):** Complete the FRQ you ran out of time on, correctly this time, using the rubric as the model. Then finish the study guide section you started for the mini-project. Oct 26 opens with a quiz on the objective list.

**Differentiation / ELL support:** The FRQ packet includes the scenario paragraph twice — once in full prose, once as bulleted facts — so students can work from whichever is easier to parse. Part (a) is a recall item and a safe on-ramp; direct students who are stuck to that part first. A printed objective-to-question crosswalk tells each student which learning objective each rubric row belongs to. For peer grading, allow a student to score a partner's packet orally with the rubric read aloud.
