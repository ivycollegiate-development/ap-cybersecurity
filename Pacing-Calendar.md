# AP Cybersecurity — Pacing Calendar (2026-2027)

Based on ICA 2026-27 Calendar (v1). 45-min class periods, 5 days/week.
*Taiwan Context: All units integrate Taiwan-specific scenarios (threat landscape, semiconductor industry, local regulations, critical infrastructure). See unit lesson plans for details.*
*🧩 Saturday CTF Track: See Saturday-CTF-Sessions.md for the full Saturday schedule (~15 sessions across the year). Each unit's lesson plan cross-references the relevant CTF sessions in its **🧩 Saturday CTF Alignment** section.*

## Course Model & Conventions

- **Tech days = Mon/Wed/Fri** — direct instruction, GitHub labs, computer work.
- **Paper days = Tue/Thu** — no computers; case studies, peer review, FRQ walk-throughs, pre-lab prep, sprints, synthesis.
- **⚡ Graded HW Quiz** — every class period opens with a 5-10 min graded quiz on the previous night's homework (homework due 20:30 the night before; weekend homework due Sun 20:30). Paper days = paper quiz; tech days = quick MCQ. This is the "quiz tests prev night HW" rhythm — gives a nuanced signal of what students got and didn't get.
- **📝 Unit Test** — one explicit paper-based test period per unit (Units 1-5).
- **📄 Paper day** — substantive, unit-specific activity (never generic).
- **🧘 Study-Hall/Prep Day** (Unit 1 only) — quick review of the previous day or unit + student work time on whatever is due next for that unit/time frame. Not a content delivery day.
- **🔄 Flex Day** — catch-up buffer, review weak LOs, extend labs. Not content delivery.
- **Break assignments** are assigned in the last class before each break and collected the first class back (⚡ quiz covers them).

**Key School Dates (Instructional):**
- Term 1: Aug 31 - Oct 30 (Fall Break dismiss @12:30 Oct 30)
- Term 2: Nov 9 - Dec 18 (Winter Break dismiss @12:30 Dec 18)
- Term 3: Jan 4 - Feb 3 (CNY Break dismiss @12:30 Feb 3)
- Term 3 cont: Feb 14 - Apr 2 (Spring Break dismiss @12:30 Apr 2)
- Term 4: Apr 12 - Late May (AP exam window ~1st-2nd week May)
- Finals: May 31 - Jun 3

**Grading weights (Course-Syllabus.md):** Labs 40% | Quizzes/Assessments 25% | Projects 20% | Participation 5% | Midterm 10% — no school final exam (AP Cybersecurity Exam May 5, 2027 is the culminating assessment).

---

## Unit 1: Introduction to Security (18 periods — 12 tech + 3 paper + 3 study-hall)

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| — | Sep 1 | Tue | Orientation / syllabus day (teacher presents — students no tech) | No content period. Aug 31 = no class (school-wide assessment) |
| P1 | Sep 2 | Wed | Course Intro: Why Cybersecurity Matters + GitHub Setup | Syllabus, threat landscape, pre-assessment, vocab preview. GitHub account + Classroom setup |
| **SH1** | **Sep 3** | **Thu** | **🧘 Study-Hall/Prep 1** | ⚡ Quiz on P1 HW. Quick review: course structure, threat landscape, GitHub basics. Work time: finish GitHub setup, vocab flashcards, prep for P2 |
| P2 | Sep 4 | Fri | Social Engineering Tactics & Human Instincts (S.E.T.) | 🐙 GITHUB ACTIVITY: fork apcyber-u1-phishing-samples, file Issue classifying 5 emails. Cyber Attack of the Day |
| P3 | Sep 7 | Mon | Victim Impacts & Full Tactic Coverage | Complete CED tactics (consensus, familiarity, scarcity, authority). Roleplay attacker/victim. Update P2 Issues |
| P4 | Sep 8 | Tue | 📄 Paper: Phishing Lab Review | Class discussion + peer review of P2 Issue classifications vs S.E.T. framework. Exemplary Issues highlighted |
| P5 | Sep 9 | Wed | Password Attack Signs & Weak Authentication | Scenario 1B login analysis. Credential stuffing, brute force, password spraying. 💻 demo (projected) |
| **SH2** | **Sep 10** | **Thu** | **🧘 Study-Hall/Prep 2** | ⚡ Quiz on P5 HW. Quick review: password attacks, Scenario 1B. Work time: P6 guided notes, catch up on P2 Issues, vocab |
| P6 | Sep 11 | Fri | Strengthening Authentication — Lab | 🐙 GITHUB LAB: Password Strength Analyzer (fork, run cracker, PR findings, Action validates) |
| P7 | Sep 14 | Mon | Adversary Types | Six adversary categories. "Draw the Adversary" matching game |
| P8 | Sep 15 | Tue | 📄 Paper: Adversary Types Review + FRQ Walk-Through | Threat profiles per adversary (motive, target, methods). FRQ practice. Exit ticket: match 6 scenarios |
| P9 | Sep 16 | Wed | Wireless Attacks + Personal Protection (Combined 1.3.B + 1.3.C) | ⚠️ Evil twin demo (teacher-only). Public Wi-Fi protections: VPN, HTTPS, cert checking |
| P10 | Sep 17 | Thu | 📄 Paper: Preview AI Attacks & Defense | Real phishing vs AI-generated email vote. Pre-reading CED excerpt. Vocab: LLM, voice cloning, deepfake, adversarial AI |
| P11 | Sep 18 | Fri | 🔄 Flex / Overflow Lab Day | Optional open lab in apcyber-u1-password-strength-lab; explore apcyber-u1-vulnerable-code-lab repo for P14. GitHub workflow troubleshooting |
| P12 | Sep 21 | Mon | 1.4: AI-Based Cybersecurity Attacks | Voice cloning demo. 🐙 GITHUB ACTIVITY: fork apcyber-u1-ai-phishing-samples, Issue with analysis |
| **SH3** | **Sep 22** | **Tue** | **🧘 Study-Hall/Prep 3** | ⚡ Quiz on P12 HW. Quick review: AI attacks, whole-unit recap. Work time: P13/P14 prep, study for Unit 1 test, catch up on labs |
| P13 | Sep 23 | Wed | AI in Cyber Defense — Tools & Concepts | Copilot/CodeQL, anomaly detection, automated IR. 💻 Live CodeQL demo. Preview P14 lab |
| — | Sep 24 | Thu | **No class — Mid-Autumn Festival** | |
| P14 | Sep 25 | Fri | 1.5 cont.: AI Defense Lab + Scenario 1E | 🐙 GITHUB LAB: AI-Powered Code Review (fork vulnerable-code repo, AI analysis, fix via PR, Action runs checks) |
| P15 | Sep 28 | Mon | Unit 1 Review & Test | Kahoot-style review (hardest LOs: 1.5.A, 1.3.B, 1.3.C), concept map, practice MCQs. **📝 UNIT 1 TEST (paper-based)** |

**Unit 1 GitHub labs (3):** P2 apcyber-u1-phishing-samples (Issue classification) · P6 apcyber-u1-password-strength-lab (PR + Action) · P14 apcyber-u1-vulnerable-code-lab (AI code review + CodeQL).
**Break assignment:** none (unit completes before any break).

---

## Unit 2: Securing Spaces (23 periods + test week)

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| P1 | Sep 29 | Tue | 📄 Case Study: Colonial Pipeline Physical Breach | Read case, map vulnerability→exploit→impact, pair discussion |
| P2 | Sep 30 | Wed | 2.1 Cyber Foundations — Phases, Risk, Defense in Depth | Direct instruction + guided notes. ⚡ HW quiz opens |
| P3 | Oct 1 | Thu | 📄 Pre-Lab: Physical Security Audit Prep | Pre-lab worksheet, predict flagged access points, vocab drill |
| P4 | Oct 2 | Fri | 🐙 GITHUB LAB: Physical Security Audit Lab | fork → Codespaces → submit → pair-share |
| P5 | Oct 5 | Mon | 2.1 Cyber Foundations — Attack Phases Deep Dive | Direct instruction + guided notes |
| P6 | Oct 6 | Tue | 📄 Peer Review: Physical Security Audit Findings | Rubric exchange, one glow + one grow, common misses |
| P7 | Oct 7 | Wed | 2.1 Cyber Foundations — Risk Management Strategies | Direct instruction + guided notes |
| P8 | Oct 8 | Thu | 📄 Pre-Lab: Surveillance Detection Prep | Camera blind-spot diagram, sensor types, placement discussion |
| P9 | Oct 9 | Fri | 🐙 GITHUB LAB: Surveillance Detection Lab | fork → Codespaces → submit → pair-share |
| P10 | Oct 12 | Mon | 2.1 Cyber Foundations — Defense in Depth Layers | Direct instruction + guided notes |
| P11 | Oct 13 | Tue | 📄 FRQ Walk-Through: Physical Security Scenario | Deconstruct prompt, write (10 min), peer-score, model answer |
| P12 | Oct 14 | Wed | 2.2 Physical Vulnerabilities — Access Points & Surveillance | Direct instruction + guided notes |
| P13 | Oct 15 | Thu | 📄 PSAT G11 (paper day — light) | Reflection / discussion only |
| P14 | Oct 19 | Mon | 2.2 Physical Vulnerabilities — Social Engineering at the Door | Direct instruction + guided notes |
| P15 | Oct 20 | Tue | 📄 Threat Modeling: STRIDE on a Data Center | STRIDE mini-lesson, groups apply to data center, present |
| P16 | Oct 21 | Wed | 2.3 Protecting Physical Spaces — Locks, Badges, Biometrics | Direct instruction + guided notes |
| P17 | Oct 22 | Thu | 📄 Current Event: Recent Physical Breach Analysis | CED framework analysis + CSO quick-write |
| P18 | Oct 23 | Fri | 🔄 Flex / Catch-Up Day | Buffer |
| P19 | Oct 26 | Mon | 2.3 Protecting Physical Spaces — Environmental Controls | Direct instruction + guided notes |
| P20 | Oct 27 | Tue | 📄 Mock MCQ Sprint: Unit 2 Review | 5 timed MCQs, peer-grade, re-teach misses, self-assessment |
| P21 | Oct 28 | Wed | 2.4 Detecting Physical Attacks — Sensors, Logs, Alarms | Direct instruction + guided notes |
| P22 | Oct 29 | Thu | 📄 Break Prep + Unit Review: Physical Security Audit Preview | Distribute Fall Break assignment (audit of home), walk through checklist, unit recap |
| P23 | Oct 30 | Fri | 🔄 Flex / Catch-Up Day [HALF-DAY] | Fall Break dismissal @12:30 |

**🍂 Fall Break: Oct 31 - Nov 8.** Assignment: Physical security audit of home (notebook exercise, no tech). **🇹🇼 Taiwan context (approved Aug 26):** the audit includes local-risk questions — shared building network infrastructure common in Taiwanese apartments/communities, and physical resilience for typhoon/flood events. Students note 1 shared-infrastructure risk + 1 weather-resilience gap alongside their standard findings.

### Unit 2 Test Week (Nov 9-13)

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| R1 | Nov 9 | Mon | Unit 2 Review Day 1 | ⚡ Quiz on Fall Break audit assignment. First day back — review 2.1-2.2, collect/discuss audits |
| R2 | Nov 10 | Tue | Unit 2 Review Day 2 | ⚡ HW quiz. FRQ practice + targeted re-teach of weak LOs |
| R3 | Nov 11 | Wed | 📄 Mock MCQ Sprint: Unit 2 | 5 timed MCQs, peer-grade, re-teach most-missed |
| R4 | Nov 12 | Thu | Unit 2 Review Day 4 | ⚡ HW quiz. Targeted weak-area review, open Q&A, study guide |
| **T** | **Nov 13** | **Fri** | **📝 UNIT 2 TEST** | Paper-based, all 2.1-2.4 LOs |

---

## Unit 3: Securing Networks (20 periods — compressed, 0 flex)

*Starts Nov 16 (Unit 2 test consumed Nov 9-13). Compressed from APSI 25 → 20 periods: 3 flex days cut (Dec 7, 9, 11), vocab drill merged into FRQ day, current event merged into synthesis day. 4 GitHub labs retained.*

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| P1 | Nov 16 | Mon | 3.1 Network Vulnerabilities — Identifying Common Attack Vectors | Direct instruction + guided notes. ⚡ HW quiz opens |
| P2 | Nov 17 | Tue | 📄 Case Study: Equifax Breach — Network Attack Path | Trace entry→lateral→exfil; which 3.1 vulns; segmentation fix |
| P3 | Nov 18 | Wed | 3.1 Network Vulnerabilities — How Adversaries Exploit Networks | Direct instruction + guided notes |
| P4 | Nov 19 | Thu | 📄 Pre-Lab: Wireless Security Audit Prep | Wi-Fi attack types, predict misconfig, key terms (WPA3, 802.1X) |
| P5 | Nov 20 | Fri | 🐙 GITHUB LAB: Wireless Security Audit Lab | fork → Codespaces → submit → pair-share |
| P6 | Nov 23 | Mon | 3.1 Network Vulnerabilities — Risk Assessment Framework | Direct instruction + guided notes |
| P7 | Nov 24 | Tue | 📄 FRQ Walk-Through: Network Intrusion Scenario + Vocabulary Drill (merged) | 3-part FRQ (3.1/3.2/3.3), peer-score. Vocab chain game folded in |
| P8 | Nov 25 | Wed | 3.2 Managerial Controls & Wireless — Policies, Acceptable Use | Direct instruction + guided notes |
| P9 | Nov 26 | Thu | 🦃 Thanksgiving Formal Dinner (regular class day) | Light discussion / reflection activity |
| P10 | Nov 27 | Fri | 🐙 GITHUB LAB: Network Segmentation Sim | fork → Codespaces → submit → pair-share |
| P11 | Nov 30 | Mon | 3.3 Network Segmentation — VLANs, Subnets, DMZs | Direct instruction + guided notes |
| P12 | Dec 1 | Tue | 📄 Peer Review: Segmentation Findings | Rubric exchange, compare findings, executive summary |
| P13 | Dec 2 | Wed | 3.3 Network Segmentation — Zero Trust Architecture | Direct instruction + guided notes |
| P14 | Dec 3 | Thu | 📄 Mock MCQ Sprint: Unit 3 Review | 5 timed MCQs, peer-grade, self-assessment |
| P15 | Dec 4 | Fri | 🐙 GITHUB LAB: Firewall Config Lab | fork → Codespaces → submit → pair-share |
| P16 | Dec 7 | Mon | 3.4 Firewalls — Types, Rule Sets, Configurations | Direct instruction + guided notes (converted from flex) |
| P17 | Dec 8 | Tue | 📄 Peer Review: Firewall Config Findings | Rubric exchange, compare rules, class discussion |
| **P18** | **Dec 9** | **Wed** | **📝 UNIT 3 TEST** | Paper-based, all 3.1-3.5 LOs (converted from flex) |
| P19 | Dec 10 | Thu | 📄 Synthesis + Current Event (merged): Build Your Own Network Defense Plan | Design VLAN/firewall/IDS for 50-person business, justify vs CED LOs, pair-critique. Current event analysis folded in |
| P20 | Dec 11 | Fri | 🐙 GITHUB LAB: Network Scanning Detection Lab | fork → Codespaces → submit (converted from flex; applies 3.5) |

**Unit 3 GitHub labs (4):** P5 wireless-security-audit · P10 network-segmentation-sim · P15 firewall-config · P20 network-scanning-detection.
**Winter Break assignment (assigned in P19/P20, collected Jan 4):** Unit 4 device inventory + pre-read of 4.1-4.2 CED excerpt (changed from old "network mapping + review packet" — bridges the Dec 14-17 Unit 4 start so pre-break content isn't forgotten).

---

## Unit 4: Securing Devices (23 periods)

*Starts Dec 14 (4 pre-break days) to keep Unit 4 at CED after midterms eat Jan 18-21. Winter Break: Dec 18 - Jan 3.*

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| P1 | Dec 14 | Mon | 4.1 Device Vulnerabilities — What Counts as a Computing Device? | Direct instruction + guided notes. ⚡ HW quiz opens |
| P2 | Dec 15 | Tue | 📄 Case Study: Stuxnet — Device-Level Attack | Map attack chain, device vulns, consumer device discussion |
| P3 | Dec 16 | Wed | 4.1 Device Vulnerabilities — Types of Malware | Direct instruction + guided notes |
| P4 | Dec 17 | Thu | 📄 Threat Modeling: Personal Device Attack Surface | List own devices, attack surface, risk ranking, pair-share |
| P5 | Jan 4 | Mon | 4.1 Device Vulnerabilities — How Adversaries Exploit Devices | ⚡ Quiz on Winter Break assignment. Direct instruction + guided notes |
| P6 | Jan 5 | Tue | 📄 Pre-Lab: Authentication Bypass Lab Prep | Auth factors, predict weakest methods, key terms (MFA, OAuth) |
| P7 | Jan 6 | Wed | 4.2 Authentication — Passwords, MFA, Biometrics | Direct instruction + guided notes |
| P8 | Jan 7 | Thu | 📄 Vocabulary Drill + Concept Map: 4.1-4.2 Terms | Notecard drill + malware taxonomy whiteboard *(fixed: APSI had peer review here before its lab ran)* |
| P9 | Jan 8 | Fri | 🐙 GITHUB LAB: Auth Bypass Lab | fork → Codespaces → submit → pair-share (peer review of findings in pair-share) |
| P10 | Jan 11 | Mon | 4.2 Authentication — Certificate-Based & Token Auth | Direct instruction + guided notes |
| P11 | Jan 12 | Tue | 📄 Pre-Lab: Device Hardening Workshop Prep | Hardening techniques, predict biggest impact, key terms |
| P12 | Jan 13 | Wed | 4.3 Protecting Devices — Hardening, Patching, Encryption | Direct instruction + guided notes |
| P13 | Jan 14 | Thu | 📄 FRQ Walk-Through: Stolen Laptop Scenario | 3-part FRQ (4.1/4.2/4.3), peer-score |
| P14 | Jan 15 | Fri | 🐙 GITHUB LAB: Device Hardening Workshop | fork → Codespaces → submit → pair-share |
| — | Jan 18-21 | Mon-Thu | **Midterm Exams — no AP Cyber class** | |
| P15 | Jan 22 | Fri | 🐙 GITHUB LAB: Host IDS Lab | fork → Codespaces → submit → pair-share |
| P16 | Jan 25 | Mon | 4.4 Detecting Attacks on Devices — Antivirus, EDR, HIDS | Direct instruction + guided notes |
| P17 | Jan 26 | Tue | 📄 Current Event: Recent Ransomware Attack Analysis | CED framework, ransom-payment debate |
| P18 | Jan 27 | Wed | 🔄 Flex / Catch-Up Day | Buffer |
| P19 | Jan 28 | Thu | 📄 Mock MCQ Sprint: Unit 4 Review | 5 timed MCQs, peer-grade, self-assessment, midterm Q&A |
| **P20** | **Jan 29** | **Fri** | **📝 UNIT 4 TEST** | Paper-based, all 4.1-4.4 LOs (converted from flex) |
| P21 | Feb 1 | Mon | 🔄 Flex / Catch-Up Day | Buffer |
| P22 | Feb 2 | Tue | 📄 Vocabulary Drill: Device Security Terms | Notecard drill, term triangle, malware taxonomy |
| P23 | Feb 3 | Wed | 🔄 Flex / Catch-Up Day [HALF-DAY] | CNY dismissal @12:30 |

**🧧 CNY Break: Feb 4-14.** Assignment: Device hardening checklist + Unit 5 pre-read.

---

## Unit 5: Securing Applications and Data (30 periods)

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| P1 | Feb 15 | Mon | 5.1 App/Data Vulnerabilities — SQL Injection, XSS, CSRF | Direct instruction + guided notes. ⚡ HW quiz opens |
| P2 | Feb 16 | Tue | 📄 Case Study: WannaCry — Application-Layer Attack | Vulnerability, spread, impact; EternalBlue timing question |
| P3 | Feb 17 | Wed | 5.2 Managerial & Access Controls — DAC, MAC, RBAC, ABAC | Direct instruction + guided notes |
| P4 | Feb 18 | Thu | 📄 Pre-Lab: Juice Shop Lab Prep | Web vuln list, predictions, OWASP Top 10 reference |
| P5 | Feb 19 | Fri | 🐙 GITHUB LAB: Juice Shop Lab | fork → Codespaces → submit → pair-share |
| P6 | Feb 22 | Mon | 5.3 Symmetric Cryptography — AES, DES, Key Management | Direct instruction + guided notes |
| P7 | Feb 23 | Tue | 📄 Peer Review: Juice Shop Findings | Compare vulns, risk ranking, remediation plan top 3 |
| P8 | Feb 24 | Wed | 5.4 Asymmetric Cryptography — RSA, ECC, PKI | Direct instruction + guided notes |
| P9 | Feb 25 | Thu | 📄 Access Control Deep Dive: DAC, MAC, RBAC, ABAC | 4-scenario exercise, RBAC for ICA, exit ticket |
| P10 | Feb 26 | Fri | 🐙 GITHUB LAB: Access Control Sim | fork → Codespaces → submit → pair-share |
| P11 | Mar 1 | Mon | 5.4 Asymmetric Cryptography — Digital Signatures & Certificates | Direct instruction + guided notes |
| P12 | Mar 2 | Tue | 📄 Pre-Lab: Symmetric Encryption Lab Prep | Caesar cipher warmup, AES vs Caesar, key terms |
| P13 | Mar 3 | Wed | 5.5 Protecting Applications — Secure SDLC, Code Review, SAST/DAST | Direct instruction + guided notes |
| P14 | Mar 4 | Thu | 📄 Crypto Concept Map: Symmetric vs Asymmetric | Notecard drill, TLS whiteboard, "Crypto or not?" game |
| P15 | Mar 5 | Fri | 🐙 GITHUB LAB: Symmetric Encryption Lab | fork → Codespaces → submit → pair-share |
| P16 | Mar 8 | Mon | 5.6 Detecting Attacks on Data/Apps — WAF, DLP, Audit Logs | Direct instruction + guided notes |
| P17 | Mar 9 | Tue | 📄 Pre-Lab: PKI Simulation Lab Prep | Trace cert chain, compromised-CA prediction, key terms |
| P18 | Mar 10 | Wed | 🔄 Flex / Catch-Up Day | Buffer |
| P19 | Mar 11 | Thu | 📄 FRQ Walk-Through: E-Commerce Data Breach Scenario | 4-part FRQ (5.1/5.2/5.3-4/5.6), peer-score |
| P20 | Mar 12 | Fri | 🐙 GITHUB LAB: PKI Simulation Lab | fork → Codespaces → submit → pair-share |
| P21 | Mar 15 | Mon | 🔄 Flex / Catch-Up Day | Buffer |
| P22 | Mar 16 | Tue | 📄 Current Event: Software Supply Chain Attack + 🇹🇼 Semiconductor Case Study | SolarWinds-style analysis, SDLC + detection synthesis; second half: TSMC/supply-chain threat FRQ-style exercise (approved Aug 26) — students map a hypothetical semiconductor supply-chain attack scenario to CED topics and draft an FRQ response |
| P23 | Mar 17 | Wed | 🔄 Flex / Catch-Up Day | Buffer |
| P24 | Mar 18 | Thu | 📄 Mock MCQ Sprint + Final Review: Units 1-5 | 5 timed MCQs (8 min), "one thing from each unit", AP strategy |
| P25 | Mar 19 | Fri | 🐙 GITHUB LAB: Secure Code Review Lab | fork → Codespaces → submit → pair-share |
| **P26** | **Mar 22** | **Mon** | **📝 UNIT 5 TEST** | Paper-based, all 5.1-5.6 LOs (converted from flex) |
| P27 | Mar 23 | Tue | 📄 Attack Tree Exercise: E-Commerce Platform | Build attack tree, label CED topics, gallery walk |
| P28 | Mar 24 | Wed | 🔄 Flex / Catch-Up Day | Buffer |
| P29 | Mar 25 | Thu | 📄 Secure SDLC Workshop: Design Review Simulation | Feature spec walk-through, security requirements, peer review |
| P30 | Mar 26 | Fri | 🔄 Flex / Catch-Up Day | Buffer |

**Unit 5 GitHub labs (5):** P5 juice-shop · P10 access-control-sim · P15 symmetric-encryption · P20 pki-simulation · P25 secure-code-review.

---

## Capstone & Practice Exam (Mar 29 - Apr 1)

| Period | Date | Day | Topic | Activity |
|--------|------|-----|-------|----------|
| C1 | Mar 29 | Mon | Capstone work day | Project work |
| C2 | Mar 30 | Tue | Capstone work day | Project work |
| C3 | Mar 31 | Wed | Capstone presentations | Presentations |
| **C4** | **Apr 1** | **Thu** | **📝 FULL PRACTICE EXAM (all units)** | Timed full exam. **Self-keyed over Spring Break** — students score their own work using the key, identify weak units. No new content begins pre-break |
| — | Apr 2 | Fri | Spring Break dismiss @12:30 | Half day |

**🌸 Spring Break: Apr 2-11.** Assignment: self-key practice exam + targeted flashcards for weakest units (deliverable: 3 weak-topic summaries submitted).

---

## AP Exam Preparation (~10 periods)

| Period | Date | Day | Topic |
|--------|------|-----|-------|
| 106 | Apr 12 | Mon | Course-wide review: Units 1-2 (results-driven from practice exam) |
| 107 | Apr 13 | Tue | Course-wide review: Unit 3 |
| 108 | Apr 14 | Wed | Course-wide review: Unit 4 |
| 109 | Apr 15 | Thu | Course-wide review: Unit 5 |
| 110 | Apr 16 | Fri | Practice exam (MC) round 2 |
| — | Apr 17 | Sat | Earth Day Event |
| 111 | Apr 19 | Mon | Practice exam review |
| 112 | Apr 20 | Tue | FRQ / performance task practice |
| — | Apr 21 | Wed | PSAT G10 |
| 113 | Apr 22 | Thu | Targeted review (weak areas) |
| — | Apr 24 | Sat | Common Good Day |
| 114 | Apr 26 | Mon | Final prep + study strategies |

*AP Exam: Wednesday, May 5, 2027 (8:00 AM local).*

---

## Post-AP Activities (~10 periods)

| Period | Date | Day | Activity |
|--------|------|-----|----------|
| 115+ | May (post-exam) | | Cybersecurity career exploration |
| | | | Capture the Flag (CTF) competition |
| | | | Guest speaker / industry panel |
| | | | Final projects / presentations |
| — | May 20-25 | | Thesis Week |
| — | May 29 | | Celebrate Seniors |
| — | May 30 | | Commencement |
| — | May 31 - Jun 3 | | No school final exam (AP exam was May 5) |
| — | Jun 3 | | Summer Break dismiss @1pm |

---

## Assessment Map (formative & summative)

**Summative (graded, weighted):**
- **Unit tests (📝):** Units 1-5, paper-based, ~45 min. Unit 1 Sep 28 · Unit 2 Nov 13 · Unit 3 Dec 9 · Unit 4 Jan 29 · Unit 5 Mar 22. → Quizzes/Assessments 25%
- **⚡ Graded HW quizzes:** every class period, 5-10 min, previous night's HW (due 20:30). → Quizzes/Assessments 25%
- **Full practice exam:** Apr 1 (all units, self-keyed over Spring Break). → diagnostic for AP review
- **GitHub lab submissions:** auto-graded via GitHub Classroom + Actions (Labs 40%)
- **Capstone project** (Mar 23-31): Projects 20%
- **Midterm (Jan):** 10% | no school final — AP Cybersecurity Exam (May 5, 2027) is the culminating assessment

**Formative (mostly ungraded, feedback only):**
- **Exit tickets:** 2-3 ungraded MCQs on every tech day
- **Mock MCQ Sprints:** pre-test paper days — U2 Nov 11, U3 Dec 3, U4 Jan 28, U5 Mar 18
- **FRQ Walk-Throughs with peer-scoring:** U2 P11, U3 P7, U4 P13, U5 P19
- **Peer review with rubrics** after every GitHub lab (pair-share component)
- **Pre-lab prediction worksheets** on every pre-lab paper day
- **Vocabulary drills, concept maps, current event analyses** throughout
- **Scenario-based activities** (1A-1E, 2A-2C, 3A-3C, 4A-4C, 5A-5C) from CED

*Notes:*
- *Buffer periods marked with *flex* are available for snow days, illness, or extended topics.*
- *All Scenario references (1A, 2A, etc.) refer to the CED's built-in scenarios.*
- *Lab activities use GitHub Classroom + Codespaces + Actions; org: ivycollegiate-development.*
- *Adjust pacing based on actual student progress; Unit 5 has the most flexibility (6 flex days).*
- *Unit 3 is the tightest unit (20 periods, 0 flex) — if fall-back is needed, pull from Unit 5's flex before touching Unit 3 content.*
