# Unit 2 — Securing Spaces: Detailed Lesson Plans

**Time Allotment:** 29 periods, Sep 29 - Nov 13 (Unit 2 Test on Mon Nov 13)  
**CED Topics:** 2.1–2.4 (Phases of a Cyberattack, Risk Assessment, Defense in Depth, Physical Security)  
**Course Skills:** Analyze Risk (Skill 1), Mitigate Risk (Skill 2), Detect Attacks (Skill 3), Collaborate (Skill 4)  
**Labs:** 3 GitHub labs (risk register, physical audit, badge log analysis) + 1 mini-project + 1 paper break assignment  
**Tech Days:** Mon/Wed/Fri — full internet + Google Sheets + Python/spreadsheet analysis  
**Paper Days:** Tue/Thu — no computers; case studies, scenario analysis, physical activities  
**⚡ Graded HW Quiz Convention:** Every class period opens with a 5-10 min graded quiz on the previous night's homework (homework assigned in class, due 20:30 the night before; weekend homework due Sun 20:30). Tech days = quick MCQ; paper days = written quiz. Test days skip the quiz.

**🇹🇼 Taiwan Threat Brief format (recurring):** Every unit opener starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to the unit's topic. Keeps threat awareness local and current across the full year.

**🧩 Saturday CTF Alignment:** *Saturday sessions do not run in the fall — the CTF series runs in spring 2027 (Jan 16 – May 22); see Saturday-CTF-Sessions.md.* Sessions relevant to Unit 2: **Session 3 (Feb 27: Recon & OSINT)** aligns with physical security audits and surveillance detection (U1 L10-U1 L11); **Session 4 (Mar 6: OverTheWire Bandit)** builds the CLI/terminal skills used in badge log analysis (U2 L12); **Session 5 (May 1: Password cracking fundamentals)** directly supports authentication and access control topics (U2 L6, U2 L8). Students should maintain their CTF writeup repo throughout — the writeup habit is the portfolio thesis.

**Unit 2 Period Map:**

*Canonical dates: this map and the `26-27 AP CyberSecurity` tab of the Jones Lesson Plans sheet agree. The sheet wins on any conflict.*

*AP Cyber is seniors-only — no PSAT block affects this section, so Oct 14-15 are normal class days. The Oct 15 paper day is real content, not a testing accommodation.*

| Period | Lesson | Date | Day | Type | Topic |
|--------|--------|------|-----|------|-------|
| P1 | (case study) | Sep 29 | Tue | Paper | Case Study: Colonial Pipeline Physical Breach |
| P2 | U2 L1 | Sep 30 | Wed | Tech | Phases of a Cyberattack |
| P3 | U2 L2 | Oct 1 | Thu | Paper | Risk Assessment |
| P4 | U2 L3 | Oct 2 | Fri | Tech | Defense in Depth |
| P5 | U2 L4 | Oct 5 | Mon | Tech | Flex / Catch-Up Day |
| P6 | U2 L5 | Oct 6 | Tue | Paper | Risk Management Options |
| P7 | U2 L6 | Oct 7 | Wed | Tech | Risk Register Lab |
| P8 | U2 L7 | Oct 8 | Thu | Paper | Physical Vulnerabilities & Attacks |
| P9 | U2 L8 | Oct 9 | Fri | Tech | Physical Attack Case Studies |
| P10 | U2 L9 | Oct 12 | Mon | Tech | Protecting Physical Spaces |
| P11 | U2 L10 | Oct 13 | Tue | Paper | Physical Security Audit Lab |
| P12 | U2 L11 | Oct 14 | Wed | Tech | Video Surveillance & Access Logs |
| P13 | U2 L12 | Oct 15 | Thu | Paper | Detecting Physical Attacks: Log Analysis and Alerting |
| P14 | U2 L13 | Oct 16 | Fri | Tech | Badge Log Analysis Lab |
| P15 | U2 L14 | Oct 19 | Mon | Tech | Video & Log Correlation |
| P16 | U2 L15 | Oct 20 | Tue | Tech | Mini-Project: Day 1 — Design |
| P17 | U2 L16 | Oct 21 | Wed | Tech | Mini-Project: Day 2 — Peer Review |
| P18 | U2 L17 | Oct 22 | Thu | Tech | Mini-Project: Day 3 — Presentations |
| P19 | U2 L18 | Oct 23 | Fri | Tech | Unit 2 Review |
| **P20** | **U2 L19** | **Oct 26** | **Mon** | **Test** | **~~Unit 2 Test~~ — MOVED to Nov 13, see P29** |
| P21 | U2 L20 | Oct 27 | Tue | Paper | Mock MCQ Sprint: Unit 2 |
| P22 | U2 L21 | Oct 28 | Wed | Paper | Unit 2 Synthesis: Build a Physical Security Program |
| P23 | U2 L22 | Oct 29 | Thu | Paper | Break Prep: Fall Break audit launch + unit recap |
| P24 | U2 L23 | Oct 30 | Fri | Tech | Flex / Catch-Up Day [HALF DAY] |
| — | — | Oct 31 - Nov 8 | — | — | **FALL BREAK** — home physical-security audit, paper, no tech |
| P25 | U2 L24 | Nov 9 | Mon | Paper | Unit 2 Review Day 1 + Fall Break audit quiz |
| P26 | U2 L25 | Nov 10 | Tue | Paper | Unit 2 Review Day 2 — FRQ practice + targeted re-teach |
| P27 | U2 L26 | Nov 11 | Wed | Paper | Mock MCQ Sprint: Unit 2 |
| P28 | U2 L27 | Nov 12 | Thu | Paper | Unit 2 Review Day 4 — targeted review, study guide |
| **P29** | **U2 L28** | **Nov 13** | **Fri** | **Test** | **📝 UNIT 2 TEST** |

**Why the test moved:** it was scheduled Oct 26, which put four days of 2.4 content and five days of review *after* the exam. Every Unit 2 learning objective is now taught (through Oct 28) and re-taught (Nov 9-12) before the test on Nov 13.

--------|------|-----|------|-------|
| U2 L1 | Sep 30 | Wed | Tech | Phases of a Cyberattack |
| U2 L2 | Oct 1 | Thu | Paper | Risk Assessment |
| U2 L3 | Oct 2 | Fri | Tech | Defense in Depth |
| U2 L4 | Oct 5 | Mon | Tech | Flex / Catch-Up Day |
| U2 L5 | Oct 6 | Tue | Paper | Risk Management Options |
| U2 L6 | Oct 7 | Wed | Tech | Risk Register Lab |
| U2 L7 | Oct 8 | Thu | Paper | Physical Vulnerabilities & Attacks |
| U2 L8 | Oct 9 | Fri | Tech | Physical Attack Case Studies |
| U2 L9 | Oct 12 | Mon | Tech | Protecting Physical Spaces |
| U2 L10 | Oct 13 | Tue | Paper | Physical Security Audit Lab |
| U2 L11 | Oct 14 | Wed | Tech | Video Surveillance & Access Logs |
| U2 L12 | Oct 15 | Thu | Paper | Detecting Physical Attacks |
| U2 L13 | Oct 16 | Fri | Tech | Badge Log Analysis Lab |
| U2 L14 | Oct 19 | Mon | Tech | Video & Log Correlation |
| U2 L15 | Oct 20 | Tue | Tech | Mini-Project: Day 1 — Design |
| U2 L16 | Oct 21 | Wed | Tech | Mini-Project: Day 2 — Peer Review |
| U2 L17 | Oct 22 | Thu | Tech | Mini-Project: Day 3 — Presentations |
| U2 L18 | Oct 23 | Fri | Tech | Unit 2 Review |
| U2 L19 | Oct 26 | Mon | Test | Unit 2 Test |

---

## U2 L1: Phases of a Cyberattack (Sep 30, Wed — TECH DAY)

**Period:** 11  |  **LOs:** 1.A

**Materials:** Unit 2 vocabulary worksheet ([GDoc](https://docs.google.com/document/d/1G9xYu19JC8glSZsN7wcSDHrIOXMo5vQ27mm3yEwAlRU/edit)), Slides, whiteboard, attack phase cards

**Activities:**
1. **Hook (5 min):** "How does a hacker go from 'I want to break in' to 'I have the data'?"
2. **Direct instruction (20 min):** Six phases — Reconnaissance → Initial Access → Persistence → Lateral Movement → Taking Action → Evading Detection. Walk through a real example (e.g., SolarWinds or a Taiwan-targeted APT).
3. **Activity — attack phase sorting (15 min):** Cards with actions (e.g., "scan ports", "install backdoor", "exfiltrate data") — students arrange in correct phase order.
4. **Exit ticket (5 min):** "Why does understanding attack phases help defenders?"

---

## U2 L2: Risk Assessment (Oct 1, Thu — PAPER DAY)

**Period:** 12  |  **LOs:** 1.C, 1.D

**Materials:** Slides, risk matrix handouts ([GDoc](https://docs.google.com/document/d/1Gw3Xa60zTpQIgZik17NBuQK-FMhtpDHg6X52PBNix2M/edit)), PBS NewsHour video (6:33, projector), quiz ([GDoc](https://docs.google.com/document/d/1XE6ncP4VkZ3LPqaJw0zndRZf97nopI5gFu1RMDhu4zI/edit))

**Activities:**
1. **Hook (5 min):** Play **PBS NewsHour — "What we know about the cyberattacks on water systems in 7 states"** (https://youtu.be/4cqSk0EGH10, 6:33, Aug 3 2026; free, no paywall): FBI confirms at least 7 states targeted; Iran the likely culprit; former FBI cyber official Cynthia Kaiser on the scale and attribution. Then the framing: **"In Aug 2026, state-linked hackers hit U.S. water systems in at least 7 states. Nobody died and the water stayed safe — but utilities ran manual operations for days. How do you put a number on a risk that could, in a worse case, contaminate a city's water? That's what risk assessment is for."** (Background: NYT, Aug 1 2026 — teacher print/PDF; students get the video instead of the paywalled article.)
2. **Direct instruction (15 min):** Risk = Likelihood × Impact. Qualitative (High/Med/Low) vs quantitative ($$). Documentation formats.
3. **Activity — risk matrix exercise (20 min):** Given 6 threat scenarios for a school (ransomware, stolen device, phishing, power outage, physical break-in, insider threat), rate likelihood + impact, plot on matrix, prioritize. **Extension:** add the Aug 2026 water-system hack as a 7th scenario (internet-exposed SCADA/PLC controllers at a small utility). Discuss: the likelihood of a foreign-power attack on a small town seemed low a year ago — how does a real incident change the likelihood rating for every other utility? Also covers the CIA triad — availability (manual operations, boil water notices) and integrity (chemical treatment levels) impacts.
4. **Exit ticket (5 min):** "What's the difference between inherent risk and residual risk?"

---

## U2 L3: Defense in Depth (Oct 2, Fri — TECH DAY)

**Period:** 13  |  **LOs:** 2.B

**Materials:** Slides, diagram templates ([GDoc](https://docs.google.com/document/d/18Iiy63w55sCT4jyE4ulqMQ6D3pzKmjJb0pvc8ekH_hk/edit))

**Activities:**
1. **Hook (5 min):** "One lock on your door or three?"
2. **Direct instruction (15 min):** Defense-in-depth layers — physical, technical, managerial. Preventative, detective, corrective controls. The "castle" analogy.
3. **Activity — layered defense mapping (20 min):** Given a scenario (protecting the school's grade database), identify controls at each layer. Label each as preventative/detective/corrective.
4. **Exit ticket (5 min):** "Why is defense-in-depth more effective than a single strong control?"

---

## U2 L4: Flex / Catch-Up Day (Oct 5, Mon — TECH DAY)

**Period:** 14  |  **LOs:** Review

**Materials:** None required

**Activities:**
Work time to catch up on any unfinished lab work, vocabulary, or pre-reading. Teacher circulates to check progress on individual students.

---

## U2 L5: Risk Management Options (Oct 6, Tue — PAPER DAY)

**Period:** 15  |  **LOs:** 1.C, 2.C

**Materials:** Slides, scenario cards

**Activities:**
1. **Hook (5 min):** "If a risk costs $50K to fix and the loss would be $10K, should you fix it?"
2. **Direct instruction (15 min):** Four options — Avoid, Transfer (insurance), Mitigate (controls), Accept (residual risk). When each is appropriate.
3. **Activity — risk treatment decisions (20 min):** Given 6 scenarios with cost/loss estimates, decide which option to use and justify.
4. **Exit ticket (5 min):** "What's residual risk, and why can't it be zero?"

---

## U2 L6: Risk Register Lab (Oct 7, Wed — TECH DAY)

**Period:** 16  |  **LOs:** 1.D, 2.C, 4.A

**Materials:** Google Sheets or paper template ([GDoc](https://docs.google.com/document/d/10MbSe4Af18mXFv7EoqaxsAG9JM2q_i7p1dJtH8xXTYI/edit)), quiz ([GDoc](https://docs.google.com/document/d/1x-Zbq5JKjA-1clbB4DJpvmreGe_D0gNu54d1JTx2ah0/edit))

**Lab spec:** No accounts needed if paper-based. Google Sheets if students have school accounts.

**Activities:**
1. **Setup (5 min):** Show risk register template — Asset, Threat, Vulnerability, Likelihood, Impact, Risk Score, Control, Residual Risk, Owner.
2. **Lab — Create a risk register (30 min):** In groups of 3, students create a risk register for a Taiwan semiconductor company (scenario provided). Must: identify 8+ assets, assess threats/vulnerabilities, score risks, propose controls, calculate residual risk.
3. **Gallery walk (10 min):** Post registers on walls. Groups review each other's — what did they catch that you missed?

---

## U2 L7: Physical Vulnerabilities and Attacks (Oct 8, Thu — PAPER DAY)

**Period:** 17  |  **LOs:** 1.A, 1.B

**Materials:** Slides, video clips, quiz ([GDoc](https://docs.google.com/document/d/1zUAM8VU3WmOtb2AaODsRaPOB04MxzS0CJ-_ZHSUnkaI/edit))

**Activities:**
1. **Hook (5 min):** Video — tailgating at a data center (real security footage).
2. **Direct instruction (20 min):** Piggybacking, tailgating, shoulder surfing, dumpster diving, card cloning, lock picking. How each works, what they enable.
3. **Activity — "How would you get in?" (15 min):** Given a building floor plan, identify 3 physical attack vectors and how you'd exploit each.
4. **Exit ticket (5 min):** "Which physical attack is hardest to defend against? Why?"

---

## U2 L8: Physical Attack Case Studies (Oct 9, Fri — TECH DAY)

**Period:** 18  |  **LOs:** 1.A, 1.B

**Materials:** Printed case study summaries

**Activities:**
1. **Setup (5 min):** Review yesterday's physical attack types.
2. **Jigsaw activity — case studies (25 min):** 4 groups, each reads a different real breach (e.g., RSA SecurID, Snowden, Stuxnet physical vector, Taiwan semiconductor fab incident). Each group identifies: attack method, vulnerability exploited, control that would have stopped it.
3. **Share out (10 min):** Each group presents their case in 2 min.
4. **Debrief (5 min):** Patterns? Which controls appear across multiple cases?

---

## U2 L9: Protecting Physical Spaces (Oct 12, Mon — TECH DAY)

**Period:** 19  |  **LOs:** 2.A, 2.B

**Materials:** Slides, equipment photos

**Activities:**
1. **Hook (5 min):** Show a $20 lock vs a $2000 biometric reader — what do you get for the price difference?
2. **Direct instruction (20 min):** Physical controls — locks (classes), card readers, access control vestibules/man traps, CCTV (placement, retention), motion sensors, security guards, UPS/generators. Pros, cons, cost tradeoffs.
3. **Activity — control matching (15 min):** Given a set of threats, match each to the most cost-effective physical control.
4. **Exit ticket (5 min):** "What's the most overlooked physical control in most schools?"

---

## U2 L10: Physical Security Audit Lab (Oct 13, Tue — PAPER DAY)

**Period:** 20  |  **LOs:** 2.A, 2.D, 4.B

**Materials:** Audit checklist worksheet ([GDoc](https://docs.google.com/document/d/1I5wfBCFp4k8xpopVhoEbFrmx4dQIa8DcoVh1EkpqHzs/edit)), clipboards, quiz ([GDoc](https://docs.google.com/document/d/1tmrrlv3197TPiuloahHbgpguVxz2qF1WY0Elm02rmog/edit))

**Lab spec:** Campus walk-around. Coordinate with admin in advance.

**Activities:**
1. **Setup (5 min):** Distribute audit checklist. Review: what to look for (door locks, badge readers, camera placement, visitor check-in, server room access, tailgating risk). Safety rules: don't touch anything, don't open doors you don't have access to.
2. **Lab — Campus walk audit (25 min):** Groups walk a prescribed route through campus wings (admin, classrooms, server room hallway, entrances). Mark observed controls on checklist. Rate each: Present & Effective / Present but Weak / Missing.
3. **Debrief (10 min):** Share findings. What surprised you? What's one change you'd recommend?
4. **Write-up (5 min):** Each student writes 3 recommendations (due next class).

---

## U2 L11: Video Surveillance & Access Logs (Oct 14, Wed — TECH DAY)

**Period:** 21  |  **LOs:** 2.A, 2.B

**Materials:** Slides, sample camera layout diagrams

**Activities:**
1. **Hook (5 min):** "If a badge is used at 3 AM, does anyone notice?"
2. **Direct instruction (15 min):** Camera placement principles (overlap, choke points, coverage vs cost), retention policies, badge audit trails. What a good access control policy includes.
3. **Activity — camera placement (15 min):** Given a floor plan, place 8 cameras optimally. Justify each placement.
4. **Activity — badge audit (10 min):** Sample badge swipes for a week. Identify: after-hours access, unusual patterns, possible tailgating indicators.

---

## U2 L12: Detecting Physical Attacks (Oct 15, Thu — PAPER DAY)

**Period:** 22  |  **LOs:** 3.A, 3.B

**Materials:** Sample logs ([GDoc](https://docs.google.com/document/d/17j4biu8_Pih7I8pZMv9zTLz2LE9wdfOpwgQGMyjc22M/edit)), slides, quiz ([GDoc](https://docs.google.com/document/d/1HL6y_AcsFBvXARysHSSOzyS1jmQI4VZyjjqPXU-DHhw/edit))

**Activities:**
1. **Hook (5 min):** "A badge was used 47 times in one day — normal?"
2. **Direct instruction (15 min):** Detection methods — log analysis (badge, CCTV), motion sensor alerts, guard patrol reports, entry/exit reconciliation. Alert thresholds.
3. **Activity — log review (20 min):** Given a week of badge access logs for **ICA's own building** (door locations include Main Entrance, Classroom Wing, IT Office, Server Room, Admin Office), find: (a) a tailgating pattern (two badges at same door <3 seconds apart), (b) a shared badge (simultaneous entries at physically distant doors), (c) an after-hours anomaly (entry after 9 PM for a door that has no night shift), (d) a door left propped open (multiple entries with no exit). Students annotate each finding with confidence level (high/medium/low) — just like a real SOC analyst flags alerts for review. Materials: [GDoc](https://docs.google.com/document/d/17j4biu8_Pih7I8pZMv9zTLz2LE9wdfOpwgQGMyjc22M/edit).
4. **Exit ticket (5 min):** "What's one detection method that doesn't require any technology?"

---

## U2 L13: Badge Log Analysis Lab (Oct 16, Fri — TECH DAY)

**Period:** 23  |  **LOs:** 3.C, 3.D, 4.D

**Materials:** Simulated badge log CSV, lab worksheet ([GDoc](https://docs.google.com/document/d/1vu1NYhc2rGKvWRYpOK8KILg3dLghV7TgG0JgMw-Bbvc/edit))

**Lab spec:** CSV file with ~500 entries. Python or spreadsheet analysis.

**Activities:**
1. **Setup (5 min):** Explain the log format — timestamp, badge ID, door, granted/denied.
2. **Lab — Analyze badge logs (30 min):** Given the CSV, identify: (a) simultaneous entries at distant doors (shared badge), (b) rapid successive entries (tailgating), (c) failed attempts followed by success (brute-force or found badge), (d) after-hours access with no overtime request. Document findings.
3. **Debrief (10 min):** Compare findings. Did everyone find the same anomalies? What would a false positive look like?

---

## U2 L14: Video & Log Correlation (Oct 19, Mon — TECH DAY)

**Period:** 24  |  **LOs:** 3.D

**Materials:** Incident scenario packet ([GDoc](https://docs.google.com/document/d/1aYIuiU2N_UvsH2AftpngUZTtWr7h9Xp_Tef3YxOsHRg/edit))

**Activities:**
1. **Setup (5 min):** "An alarm went off in the server room at 2 AM. The badge log shows Door C opened. What else do you need to know?"
2. **Investigation — reconstruct the timeline (25 min):** Given badge logs, visitor logs, guard patrol records, and camera footage descriptions, students reconstruct the sequence of events for a simulated physical breach. Determine: what happened, who was involved, which controls failed, which controls worked.
3. **Report writing (15 min):** Write an incident summary: timeline, findings, recommendations (max 1 page).
4. **Exit ticket (5 min):** "What evidence would you collect first after a physical breach?"

---

## U2 L15: Mini-Project — Design (Oct 20, Tue — TECH DAY)

**Period:** 25  |  **LOs:** 2.B, 4.A, 4.B, 4.D

**Materials:** Scenario packets ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides

**Scenario:** "You're the security director for a TSMC subcontractor in Taichung. Current controls: basic key locks, one camera at front desk. Budget: NT$2M. Design a defense-in-depth physical security plan."

**Deliverable:** Google Slides deck (5-8 slides) covering: threat model, control selections with costs, detection methods, defense-in-depth rationale.

**Activities:**
1. **Launch (5 min):** Introduce the scenario, budget constraint, and requirements.
2. **Design phase (25 min):** Groups design a physical security plan for a Taiwan semiconductor fab. Must include: perimeter, entry points, interior, server room, policies, detection methods. Budget: NT$2M.
3. **Research + resource gathering (10 min):** Student teams research costs and solutions.
4. **Group role assignments (5 min):** Security Director, Technical Lead, Budget Officer, Presenter(s).

---

## U2 L16: Mini-Project — Peer Review (Oct 21, Wed — TECH DAY)

**Period:** 26  |  **LOs:** 2.B, 4.A, 4.B, 4.D

**Materials:** Scenario packets ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides

**Activities:**
1. **Setup peer review (5 min):** Explain review criteria and expectations.
2. **Work + peer review (25 min):** Draft complete. Swap with another group for a 15-min review. Address feedback in remaining time.
3. **Refinement (10 min):** Iterate based on peer feedback.
4. **Check-in (5 min):** Teacher checks group progress.

---

## U2 L17: Mini-Project — Presentations (Oct 22, Thu — TECH DAY)

**Period:** 27  |  **LOs:** 2.B, 4.A, 4.B, 4.D

**Materials:** Scenario packets ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides

**Activities:**
1. **Setup presentations (5 min):** Presentation order, timing, Q&A expectations.
2. **Presentations (25 min):** 5 min per group + 2 min Q&A.
3. **Judging / feedback (10 min):** Class vote on best plan. Teacher provides rubric-based feedback.
4. **Wrap up (5 min):** Key takeaways, connection to Unit 2 content.

---

## U2 L18: Unit 2 Review (Oct 23, Fri — TECH DAY)

**Period:** 28  |  **LOs:** All Unit 2

**Activities:**
1. **Scenario review (15 min):** "A USB drive found in the parking lot contains malware. Walk through: phase of attack, risk assessment, physical controls that could prevent, detection method."
2. **Sample FRQ (20 min):** Work through an AP-style free-response question for Unit 2. Grade using rubric.
3. **Study guide / Q&A (10 min):** Students review weak areas.

---

## U2 L19: Flex / Catch-Up + Review Day (Oct 26, Mon — TECH DAY)

**Period:** 20  |  **LOs:** All Unit 2 (consolidation)

**Note:** This slot previously held the Unit 2 Test. The test moved to Nov 13 (P29) so that all of 2.4 and the full review block land before the exam. The date is preserved as a consolidation day.

**Activities:**
1. **⚡ Graded HW quiz** (5-10 min, MCQ) on the mini-project presentation homework.
2. **Guided re-read** of 2.4 (detection) — the objective students most often miss on the CED practice items.
3. **Open lab / catch-up** for anyone behind on a Unit 2 lab submission.
4. **Exit ticket:** one written sentence — which Unit 2 objective do you still not own?

---

## U2 L20: Mock MCQ Sprint: Unit 2 (Oct 27, Tue — PAPER DAY)

**Period:** 21  |  **LOs:** 2.1-2.4

**Activities:**
1. **5 timed MCQs** on Unit 2 (5 min total, one pass, no notes).
2. **Peer-grade** against the answer key, then re-read the CED rationale for every miss.
3. **Re-teach board:** teacher records the objective codes of the most-missed items; these drive the Nov 9-12 review block.
4. **Self-assessment:** students file their misses in the Unit 2 study guide, which is distributed today.

**Assessment:** Mock MCQ score recorded, not a test grade. Feeds re-teach targeting.

---

## U2 L21: Unit 2 Synthesis — Build a Physical Security Program (Oct 28, Wed — PAPER DAY)

**Period:** 22  |  **LOs:** 2.1.A, 2.2.A, 2.3.A, 2.4.A

**Scenario:** A Taiwanese semiconductor firm is moving into a new Taichung office. Design the physical security program.

**Activities:**
1. **Group design (20 min):** groups build a layered program — perimeter, entry control, interior zones, monitoring, detection, response. Each control must be justified by naming the Unit 2 LO it satisfies.
2. **Group presentations (15 min):** each group walks the class through its layer stack.
3. **Gap hunt:** class identifies which LO no group covered. Usually 2.3 environmental controls — call that out explicitly.
4. **Study guide issued** to open the Nov 9-13 review block.

**Assessment:** Design sheets collected; coverage gaps used to set review priorities.

**🇹🇼 Taiwan context:** semiconductor supply-chain context gives the physical-security stakes real weight — a fab is both a high-value target and a hard target because of the clean-room layering.

---

## U2 L22: Break Prep — Fall Break Audit Launch (Oct 29, Thu — PAPER DAY)

**Period:** 23  |  **LOs:** 2.2, 2.3, 2.4 (applied)

**Activities:**
1. **⚡ Graded HW quiz** (5-10 min, paper) on mini-project homework.
2. **Fall Break assignment launch (20 min):** distribute the home physical-security audit. Walk the checklist requirement by requirement, show a completed sample, state the due date (first class back, Mon Nov 9) and the format.
3. **Taiwan-specific requirements** — students must additionally note (a) one risk from shared building network infrastructure common in Taiwanese apartments and communities, and (b) one physical-resilience gap relevant to typhoon and flood seasons.
4. **Clarify it is a paper exercise** — notebook, no technology required, no GitHub over the break.
5. **Unit 2 recap** for the remaining time: open Q&A on any objective students flag as shaky.

**Assessment:** Graded HW quiz. Fall Break audit assignment issued (Google Classroom, due Nov 9 before class).

---

## U2 L23: Flex / Catch-Up Day (Oct 30, Fri — HALF DAY, DISMISS 12:30)

**Period:** 24  |  **LOs:** None — buffer

**Activities:**
1. Catch-up time for outstanding Unit 2 lab submissions.
2. Quiet reading: Unit 3 preview (Securing Networks), first CED excerpt.
3. No new content. Dismissal 12:30 — Fall Break begins.

---

## 🍂 FALL BREAK — Oct 31 to Nov 8

**Assignment:** home physical-security audit (paper, no technology).
**Assigned:** Oct 29 (P23)  |  **Collected:** Nov 9 (P25)  |  **Quized:** Nov 9 HW quiz.

**Format:** student notebook or loose-leaf. Notebooks are not collected over the break.

---

## U2 L24: Unit 2 Review Day 1 (Nov 9, Mon — PAPER DAY)

**Period:** 25  |  **LOs:** 2.1, 2.2

**Activities:**
1. **⚡ Graded HW quiz (10 min)** on the Fall Break physical-security audit. This is the one graded assessment of the break work.
2. **Audit debrief (15 min):** anonymize the class findings — the most common weakness across the section gets named, and the strongest finds get read out.
3. **Review Day 1 (20 min):** 2.1 attack phases and 2.2 physical vulnerabilities, driven by what the audit quiz revealed.
4. **Study guide work time** for the remaining minutes.

**Assessment:** Fall Break audit quiz (graded) — sets the re-teach agenda for the week.

---

## U2 L25: Unit 2 Review Day 2 (Nov 10, Tue — PAPER DAY)

**Period:** 26  |  **LOs:** all Unit 2, weighted to quiz misses

**Activities:**
1. **⚡ Graded HW quiz** (5-10 min, paper).
2. **FRQ practice (25 min):** one physical-security FRQ. Deconstruct the prompt, 10 min writing, peer-score against the rubric, then read the model answer.
3. **Targeted re-teach (15 min):** the two weakest LOs from the Nov 9 quiz.

**Assessment:** Graded HW quiz; FRQ practice scored with the rubric (practice, not a test grade).

---

## U2 L26: Mock MCQ Sprint: Unit 2 (Nov 11, Wed — PAPER DAY)

**Period:** 27  |  **LOs:** 2.1-2.4

**Activities:**
1. **5 timed MCQs** on Unit 2, parallel to the Oct 27 sprint so students see their own delta.
2. **Peer-grade**, re-read rationales for every miss.
3. **Re-teach the most-missed objective** immediately, in the same period.
4. **Delta check:** each student writes down which objective moved from red to yellow since Oct 27.

**Assessment:** Mock MCQ score recorded, not a test grade.

---

## U2 L27: Unit 2 Review Day 4 (Nov 12, Thu — PAPER DAY)

**Period:** 28  |  **LOs:** all Unit 2

**Activities:**
1. **⚡ Graded HW quiz** (5-10 min, paper).
2. **Targeted weak-area review** driven by the Nov 11 sprint results.
3. **Open Q&A** — the last chance to ask anything before the test.
4. **Study guide finalization** and test logistics (Friday Nov 13, 20 MCQ + 1 FRQ, paper-based).

**Assessment:** Graded HW quiz; study guide complete.

---

## U2 L28: Unit 2 Test (Nov 13, Fri — TEST DAY)

**Period:** 29  |  **LOs:** 2.1-2.4

**Activities:**
1. **Test (40 min):** 20 MCQ (2 min each) + 1 FRQ. Covers attack phases, risk assessment, risk treatment options, physical vulnerabilities, physical protections, and detection methods.
2. **Early finishers:** read the Unit 3 preview.
3. No HW quiz on test day.

**Assessment:** Unit 2 Test (paper) — graded.

---

## Unit 2 — Lab Infrastructure Summary

| Lab | Tech Needed | Accounts Required | Setup Time |
|-----|-------------|-------------------|------------|
| Risk register | Google Sheets or paper | None (or school Google) | 5 min template |
| Physical audit | Checklist printout | None | 10 min |
| Badge log analysis | CSV + spreadsheet | None | 10 min |
| Video/log correlation | Printed scenario packet | None | 5 min |
| Mini-project | Google Slides | School Google account | Launch materials |
| Fall Break audit | **None — paper only** | None | 0 |

**Do not add a fourth/fifth GitHub lab to Unit 2.** The three existing labs (risk register, physical audit, badge log analysis) plus the mini-project are sufficient; the four Unit 2 weeks are already the tightest stretch of the term.