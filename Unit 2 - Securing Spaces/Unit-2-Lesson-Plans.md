# Unit 2 — Securing Spaces: Detailed Lesson Plans

**Time Allotment:** 19 periods (14 tech + 5 paper), Sep 30–Oct 26  
**CED Topics:** 2.1–2.4 (Phases of a Cyberattack, Risk Assessment, Defense in Depth, Physical Security)  
**Course Skills:** Analyze Risk (Skill 1), Mitigate Risk (Skill 2), Detect Attacks (Skill 3), Collaborate (Skill 4)  
**Labs:** 5 (risk register, physical audit, badge log analysis, video/log correlation, mini-project)  
**Tech Days:** Mon/Wed/Fri — full internet + Google Sheets + Python/spreadsheet analysis  
**Paper Days:** Tue/Thu — no computers; case studies, scenario analysis, physical activities  
**⚡ Graded HW Quiz Convention:** Every class period opens with a 5-10 min graded quiz on the previous night's homework (homework assigned in class, due 20:30 the night before; weekend homework due Sun 20:30). Tech days = quick MCQ; paper days = written quiz. Test days skip the quiz.

**🇹🇼 Taiwan Threat Brief format (recurring):** Every unit opener starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to the unit's topic. Keeps threat awareness local and current across the full year.

**🧩 Saturday CTF Alignment:** Three Saturday CTF sessions fall during Unit 2 — **Oct 3 (SESSION 3: Recon & OSINT)** aligns with physical security audits and surveillance detection (P8-P9). **Oct 10 (SESSION 4: OverTheWire Bandit)** builds CLI/terminal skills used in badge log analysis (P22). **Oct 24 (SESSION 5: Password cracking fundamentals)** directly supports authentication and access control topics (P16, P18). Students should maintain their CTF writeup repo throughout — the writeup habit is the portfolio thesis.

**Unit 2 Period Map:**

| Period | Date | Day | Type | Topic |
|--------|------|-----|------|-------|
| P11 | Sep 30 | Wed | Tech | Phases of a Cyberattack |
| P12 | Oct 1 | Thu | Paper | Risk Assessment |
| P13 | Oct 2 | Fri | Tech | Defense in Depth |
| P14 | Oct 5 | Mon | Tech | Flex / Catch-Up Day |
| P15 | Oct 6 | Tue | Paper | Risk Management Options |
| P16 | Oct 7 | Wed | Tech | Risk Register Lab |
| P17 | Oct 8 | Thu | Paper | Physical Vulnerabilities & Attacks |
| P18 | Oct 9 | Fri | Tech | Physical Attack Case Studies |
| P19 | Oct 12 | Mon | Tech | Protecting Physical Spaces |
| P20 | Oct 13 | Tue | Paper | Physical Security Audit Lab |
| P21 | Oct 14 | Wed | Tech | Video Surveillance & Access Logs |
| P22 | Oct 15 | Thu | Paper | Detecting Physical Attacks |
| P23 | Oct 16 | Fri | Tech | Badge Log Analysis Lab |
| P24 | Oct 19 | Mon | Tech | Video & Log Correlation |
| P25 | Oct 20 | Tue | Tech | Mini-Project: Day 1 — Design |
| P26 | Oct 21 | Wed | Tech | Mini-Project: Day 2 — Peer Review |
| P27 | Oct 22 | Thu | Tech | Mini-Project: Day 3 — Presentations |
| P28 | Oct 23 | Fri | Tech | Unit 2 Review |
| P29 | Oct 26 | Mon | Test | Unit 2 Test |

---

## P11: Phases of a Cyberattack (Sep 30, Wed — TECH DAY)

**Period:** 11  |  **LOs:** 1.A

**Materials:** Slides, whiteboard, attack phase cards

**Activities:**
1. **Hook (5 min):** "How does a hacker go from 'I want to break in' to 'I have the data'?"
2. **Direct instruction (20 min):** Six phases — Reconnaissance → Initial Access → Persistence → Lateral Movement → Taking Action → Evading Detection. Walk through a real example (e.g., SolarWinds or a Taiwan-targeted APT).
3. **Activity — attack phase sorting (15 min):** Cards with actions (e.g., "scan ports", "install backdoor", "exfiltrate data") — students arrange in correct phase order.
4. **Exit ticket (5 min):** "Why does understanding attack phases help defenders?"

---

## P12: Risk Assessment (Oct 1, Thu — PAPER DAY)

**Period:** 12  |  **LOs:** 1.C, 1.D

**Materials:** Slides, risk matrix handouts ([GDoc](https://docs.google.com/document/d/1Gw3Xa60zTpQIgZik17NBuQK-FMhtpDHg6X52PBNix2M/edit)), PBS NewsHour video (6:33, projector), quiz ([GDoc](https://docs.google.com/document/d/1XE6ncP4VkZ3LPqaJw0zndRZf97nopI5gFu1RMDhu4zI/edit))

**Activities:**
1. **Hook (5 min):** Play **PBS NewsHour — "What we know about the cyberattacks on water systems in 7 states"** (https://youtu.be/4cqSk0EGH10, 6:33, Aug 3 2026; free, no paywall): FBI confirms at least 7 states targeted; Iran the likely culprit; former FBI cyber official Cynthia Kaiser on the scale and attribution. Then the framing: **"In Aug 2026, state-linked hackers hit U.S. water systems in at least 7 states. Nobody died and the water stayed safe — but utilities ran manual operations for days. How do you put a number on a risk that could, in a worse case, contaminate a city's water? That's what risk assessment is for."** (Background: NYT, Aug 1 2026 — teacher print/PDF; students get the video instead of the paywalled article.)
2. **Direct instruction (15 min):** Risk = Likelihood × Impact. Qualitative (High/Med/Low) vs quantitative ($$). Documentation formats.
3. **Activity — risk matrix exercise (20 min):** Given 6 threat scenarios for a school (ransomware, stolen device, phishing, power outage, physical break-in, insider threat), rate likelihood + impact, plot on matrix, prioritize. **Extension:** add the Aug 2026 water-system hack as a 7th scenario (internet-exposed SCADA/PLC controllers at a small utility). Discuss: the likelihood of a foreign-power attack on a small town seemed low a year ago — how does a real incident change the likelihood rating for every other utility? Also covers the CIA triad — availability (manual operations, boil water notices) and integrity (chemical treatment levels) impacts.
4. **Exit ticket (5 min):** "What's the difference between inherent risk and residual risk?"

---

## P13: Defense in Depth (Oct 2, Fri — TECH DAY)

**Period:** 13  |  **LOs:** 2.B

**Materials:** Slides, diagram templates ([GDoc](https://docs.google.com/document/d/18Iiy63w55sCT4jyE4ulqMQ6D3pzKmjJb0pvc8ekH_hk/edit))

**Activities:**
1. **Hook (5 min):** "One lock on your door or three?"
2. **Direct instruction (15 min):** Defense-in-depth layers — physical, technical, managerial. Preventative, detective, corrective controls. The "castle" analogy.
3. **Activity — layered defense mapping (20 min):** Given a scenario (protecting the school's grade database), identify controls at each layer. Label each as preventative/detective/corrective.
4. **Exit ticket (5 min):** "Why is defense-in-depth more effective than a single strong control?"

---

## P14: Flex / Catch-Up Day (Oct 5, Mon — TECH DAY)

**Period:** 14  |  **LOs:** Review

**Materials:** None required

**Activities:**
Work time to catch up on any unfinished lab work, vocabulary, or pre-reading. Teacher circulates to check progress on individual students.

---

## P15: Risk Management Options (Oct 6, Tue — PAPER DAY)

**Period:** 15  |  **LOs:** 1.C, 2.C

**Materials:** Slides, scenario cards

**Activities:**
1. **Hook (5 min):** "If a risk costs $50K to fix and the loss would be $10K, should you fix it?"
2. **Direct instruction (15 min):** Four options — Avoid, Transfer (insurance), Mitigate (controls), Accept (residual risk). When each is appropriate.
3. **Activity — risk treatment decisions (20 min):** Given 6 scenarios with cost/loss estimates, decide which option to use and justify.
4. **Exit ticket (5 min):** "What's residual risk, and why can't it be zero?"

---

## P16: Risk Register Lab (Oct 7, Wed — TECH DAY)

**Period:** 16  |  **LOs:** 1.D, 2.C, 4.A

**Materials:** Google Sheets or paper template ([GDoc](https://docs.google.com/document/d/10MbSe4Af18mXFv7EoqaxsAG9JM2q_i7p1dJtH8xXTYI/edit)), quiz ([GDoc](https://docs.google.com/document/d/1x-Zbq5JKjA-1clbB4DJpvmreGe_D0gNu54d1JTx2ah0/edit))

**Lab spec:** No accounts needed if paper-based. Google Sheets if students have school accounts.

**Activities:**
1. **Setup (5 min):** Show risk register template — Asset, Threat, Vulnerability, Likelihood, Impact, Risk Score, Control, Residual Risk, Owner.
2. **Lab — Create a risk register (30 min):** In groups of 3, students create a risk register for a Taiwan semiconductor company (scenario provided). Must: identify 8+ assets, assess threats/vulnerabilities, score risks, propose controls, calculate residual risk.
3. **Gallery walk (10 min):** Post registers on walls. Groups review each other's — what did they catch that you missed?

---

## P17: Physical Vulnerabilities and Attacks (Oct 8, Thu — PAPER DAY)

**Period:** 17  |  **LOs:** 1.A, 1.B

**Materials:** Slides, video clips, quiz ([GDoc](https://docs.google.com/document/d/1zUAM8VU3WmOtb2AaODsRaPOB04MxzS0CJ-_ZHSUnkaI/edit))

**Activities:**
1. **Hook (5 min):** Video — tailgating at a data center (real security footage).
2. **Direct instruction (20 min):** Piggybacking, tailgating, shoulder surfing, dumpster diving, card cloning, lock picking. How each works, what they enable.
3. **Activity — "How would you get in?" (15 min):** Given a building floor plan, identify 3 physical attack vectors and how you'd exploit each.
4. **Exit ticket (5 min):** "Which physical attack is hardest to defend against? Why?"

---

## P18: Physical Attack Case Studies (Oct 9, Fri — TECH DAY)

**Period:** 18  |  **LOs:** 1.A, 1.B

**Materials:** Printed case study summaries

**Activities:**
1. **Setup (5 min):** Review yesterday's physical attack types.
2. **Jigsaw activity — case studies (25 min):** 4 groups, each reads a different real breach (e.g., RSA SecurID, Snowden, Stuxnet physical vector, Taiwan semiconductor fab incident). Each group identifies: attack method, vulnerability exploited, control that would have stopped it.
3. **Share out (10 min):** Each group presents their case in 2 min.
4. **Debrief (5 min):** Patterns? Which controls appear across multiple cases?

---

## P19: Protecting Physical Spaces (Oct 12, Mon — TECH DAY)

**Period:** 19  |  **LOs:** 2.A, 2.B

**Materials:** Slides, equipment photos

**Activities:**
1. **Hook (5 min):** Show a $20 lock vs a $2000 biometric reader — what do you get for the price difference?
2. **Direct instruction (20 min):** Physical controls — locks (classes), card readers, access control vestibules/man traps, CCTV (placement, retention), motion sensors, security guards, UPS/generators. Pros, cons, cost tradeoffs.
3. **Activity — control matching (15 min):** Given a set of threats, match each to the most cost-effective physical control.
4. **Exit ticket (5 min):** "What's the most overlooked physical control in most schools?"

---

## P20: Physical Security Audit Lab (Oct 13, Tue — PAPER DAY)

**Period:** 20  |  **LOs:** 2.A, 2.D, 4.B

**Materials:** Audit checklist worksheet ([GDoc](https://docs.google.com/document/d/1I5wfBCFp4k8xpopVhoEbFrmx4dQIa8DcoVh1EkpqHzs/edit)), clipboards, quiz ([GDoc](https://docs.google.com/document/d/1tmrrlv3197TPiuloahHbgpguVxz2qF1WY0Elm02rmog/edit))

**Lab spec:** Campus walk-around. Coordinate with admin in advance.

**Activities:**
1. **Setup (5 min):** Distribute audit checklist. Review: what to look for (door locks, badge readers, camera placement, visitor check-in, server room access, tailgating risk). Safety rules: don't touch anything, don't open doors you don't have access to.
2. **Lab — Campus walk audit (25 min):** Groups walk a prescribed route through campus wings (admin, classrooms, server room hallway, entrances). Mark observed controls on checklist. Rate each: Present & Effective / Present but Weak / Missing.
3. **Debrief (10 min):** Share findings. What surprised you? What's one change you'd recommend?
4. **Write-up (5 min):** Each student writes 3 recommendations (due next class).

---

## P21: Video Surveillance & Access Logs (Oct 14, Wed — TECH DAY)

**Period:** 21  |  **LOs:** 2.A, 2.B

**Materials:** Slides, sample camera layout diagrams

**Activities:**
1. **Hook (5 min):** "If a badge is used at 3 AM, does anyone notice?"
2. **Direct instruction (15 min):** Camera placement principles (overlap, choke points, coverage vs cost), retention policies, badge audit trails. What a good access control policy includes.
3. **Activity — camera placement (15 min):** Given a floor plan, place 8 cameras optimally. Justify each placement.
4. **Activity — badge audit (10 min):** Sample badge swipes for a week. Identify: after-hours access, unusual patterns, possible tailgating indicators.

---

## P22: Detecting Physical Attacks (Oct 15, Thu — PAPER DAY)

**Period:** 22  |  **LOs:** 3.A, 3.B

**Materials:** Sample logs ([GDoc](https://docs.google.com/document/d/17j4biu8_Pih7I8pZMv9zTLz2LE9wdfOpwgQGMyjc22M/edit)), slides, quiz ([GDoc](https://docs.google.com/document/d/1HL6y_AcsFBvXARysHSSOzyS1jmQI4VZyjjqPXU-DHhw/edit))

**Activities:**
1. **Hook (5 min):** "A badge was used 47 times in one day — normal?"
2. **Direct instruction (15 min):** Detection methods — log analysis (badge, CCTV), motion sensor alerts, guard patrol reports, entry/exit reconciliation. Alert thresholds.
3. **Activity — log review (20 min):** Given a week of badge access logs for **ICA's own building** (door locations include Main Entrance, Classroom Wing, IT Office, Server Room, Admin Office), find: (a) a tailgating pattern (two badges at same door <3 seconds apart), (b) a shared badge (simultaneous entries at physically distant doors), (c) an after-hours anomaly (entry after 9 PM for a door that has no night shift), (d) a door left propped open (multiple entries with no exit). Students annotate each finding with confidence level (high/medium/low) — just like a real SOC analyst flags alerts for review. Materials: [GDoc](https://docs.google.com/document/d/17j4biu8_Pih7I8pZMv9zTLz2LE9wdfOpwgQGMyjc22M/edit).
4. **Exit ticket (5 min):** "What's one detection method that doesn't require any technology?"

---

## P23: Badge Log Analysis Lab (Oct 16, Fri — TECH DAY)

**Period:** 23  |  **LOs:** 3.C, 3.D, 4.D

**Materials:** Simulated badge log CSV, lab worksheet ([GDoc](https://docs.google.com/document/d/1vu1NYhc2rGKvWRYpOK8KILg3dLghV7TgG0JgMw-Bbvc/edit))

**Lab spec:** CSV file with ~500 entries. Python or spreadsheet analysis.

**Activities:**
1. **Setup (5 min):** Explain the log format — timestamp, badge ID, door, granted/denied.
2. **Lab — Analyze badge logs (30 min):** Given the CSV, identify: (a) simultaneous entries at distant doors (shared badge), (b) rapid successive entries (tailgating), (c) failed attempts followed by success (brute-force or found badge), (d) after-hours access with no overtime request. Document findings.
3. **Debrief (10 min):** Compare findings. Did everyone find the same anomalies? What would a false positive look like?

---

## P24: Video & Log Correlation (Oct 19, Mon — TECH DAY)

**Period:** 24  |  **LOs:** 3.D

**Materials:** Incident scenario packet ([GDoc](https://docs.google.com/document/d/1aYIuiU2N_UvsH2AftpngUZTtWr7h9Xp_Tef3YxOsHRg/edit))

**Activities:**
1. **Setup (5 min):** "An alarm went off in the server room at 2 AM. The badge log shows Door C opened. What else do you need to know?"
2. **Investigation — reconstruct the timeline (25 min):** Given badge logs, visitor logs, guard patrol records, and camera footage descriptions, students reconstruct the sequence of events for a simulated physical breach. Determine: what happened, who was involved, which controls failed, which controls worked.
3. **Report writing (15 min):** Write an incident summary: timeline, findings, recommendations (max 1 page).
4. **Exit ticket (5 min):** "What evidence would you collect first after a physical breach?"

---

## P25: Mini-Project — Design (Oct 20, Tue — TECH DAY)

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

## P26: Mini-Project — Peer Review (Oct 21, Wed — TECH DAY)

**Period:** 26  |  **LOs:** 2.B, 4.A, 4.B, 4.D

**Materials:** Scenario packets ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides

**Activities:**
1. **Setup peer review (5 min):** Explain review criteria and expectations.
2. **Work + peer review (25 min):** Draft complete. Swap with another group for a 15-min review. Address feedback in remaining time.
3. **Refinement (10 min):** Iterate based on peer feedback.
4. **Check-in (5 min):** Teacher checks group progress.

---

## P27: Mini-Project — Presentations (Oct 22, Thu — TECH DAY)

**Period:** 27  |  **LOs:** 2.B, 4.A, 4.B, 4.D

**Materials:** Scenario packets ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides

**Activities:**
1. **Setup presentations (5 min):** Presentation order, timing, Q&A expectations.
2. **Presentations (25 min):** 5 min per group + 2 min Q&A.
3. **Judging / feedback (10 min):** Class vote on best plan. Teacher provides rubric-based feedback.
4. **Wrap up (5 min):** Key takeaways, connection to Unit 2 content.

---

## P28: Unit 2 Review (Oct 23, Fri — TECH DAY)

**Period:** 28  |  **LOs:** All Unit 2

**Activities:**
1. **Scenario review (15 min):** "A USB drive found in the parking lot contains malware. Walk through: phase of attack, risk assessment, physical controls that could prevent, detection method."
2. **Sample FRQ (20 min):** Work through an AP-style free-response question for Unit 2. Grade using rubric.
3. **Study guide / Q&A (10 min):** Students review weak areas.

---

## P29: Unit 2 Test (Oct 26, Mon — TEST DAY)

**Period:** 29  |  **LOs:** All Unit 2

**Activities:**
1. **Test (40 min):** 20 MC (2 min each) + 1 FRQ. Covers attack phases, risk assessment, physical attacks, controls, detection methods.
2. **Early finishers:** Read Unit 3 preview.

---

## Unit 2 — Lab Infrastructure Summary

| Lab | Tech Needed | Accounts Required | Setup Time |
|-----|-------------|-------------------|------------|
| Risk register | Google Sheets or paper | None (or school Google) | 5 min template |
| Physical audit | Checklist printout | None | 10 min |
| Badge log analysis | CSV + spreadsheet | None | 10 min |
| Video/log correlation | Printed scenario packet | None | 5 min |
| Mini-project | Google Slides | School Google account | Launch materials |