# Unit 3 — Securing Networks: Lesson Plans

**Time Allotment:** 20 class periods (compressed — 0 flex), Nov 16 – Dec 11
**CED Pages:** 55-82 (scenarios + topic pages)
**CED Topics:** 3.1 Network Vulnerabilities · 3.2 Managerial Controls & Wireless · 3.3 Network Segmentation · 3.4 Firewalls · 3.5 Detecting Network Attacks
**Course Skills:** Analyze Risk (Skill 1) · Mitigate Risk (Skill 2) · Detect Attacks (Skill 3)
**GitHub Labs:** 4 (wireless-security-audit, network-segmentation-sim, firewall-config, network-scanning-detection)
**Tech Days:** Mon/Wed/Fri — full internet + GitHub + Codespaces
**Paper Days:** Tue/Thu — no computers; substantive unit-specific activities

**Compression note:** Unit 2's test (Nov 13) consumed the week of Nov 9-13, so Unit 3 starts Nov 16. Compressed from the APSI 25-period plan to 20: 3 flex days cut (Dec 7, 9, 11), vocabulary drill merged into the FRQ day (P7), current event merged into the synthesis day (P19). Unit 3 test lands Wed Dec 9 (converted from flex). 4 GitHub labs retained.

**⚡ Graded HW Quiz Convention:** Every class period opens with a 5-10 min graded quiz on the previous night's homework (homework assigned in class, due 20:30 the night before; weekend homework due Sun 20:30). Paper days = paper quiz; tech days = quick MCQ. Part of Quizzes/Assessments 25%. Test days skip the quiz (test replaces it).

**🇹🇼 Taiwan Threat Brief format (recurring):** Every unit opener (P1) starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to the unit's topic. Keeps threat awareness local and current across the full year.

**🧩 Saturday CTF Alignment:** Two Saturday CTF sessions fall during Unit 3 — **Nov 21 (SESSION 6: Wireshark pcap challenge)** directly supports network attack detection (3.5) and aligns with P5-P7 where students analyze wireless scans and network traffic. **Nov 28 (SESSION 7: Log analysis sprint)** reinforces the firewall log and IDS/IPS monitoring from P15-P20. By Session 6 students should have pcap basics; Session 7 connects to the Unit 3 synthesis day (P19) where they design a network defense plan. Keep writeups current — the log analysis session is strong portfolio material.

**Unit 3 Period Map:**

| Period | Date | Day | Type | Topic |
|--------|------|-----|------|-------|
| P1 | Nov 16 | Mon | Tech | 3.1 Network Vulnerabilities — Identifying Common Attack Vectors |
| P2 | Nov 17 | Tue | Paper | Case Study: Equifax Breach — Network Attack Path |
| P3 | Nov 18 | Wed | Tech | 3.1 How Adversaries Exploit Networks (ARP, MAC Flooding, DNS, DoS) |
| P4 | Nov 19 | Thu | Paper | Pre-Lab: Wireless Security Audit Prep |
| P5 | Nov 20 | Fri | Tech | 🐙 GITHUB LAB: Wireless Security Audit |
| P6 | Nov 23 | Mon | Tech | 3.1 Network Vulnerabilities — Risk Assessment Framework |
| P7 | Nov 24 | Tue | Paper | FRQ Walk-Through: Network Intrusion Scenario + Vocabulary Drill |
| P8 | Nov 25 | Wed | Tech | 3.2 Managerial Controls & Wireless — Policies, Acceptable Use |
| P9 | Nov 26 | Thu | Paper | 🦃 Thanksgiving Formal Dinner (regular class day) |
| P10 | Nov 27 | Fri | Tech | 🐙 GITHUB LAB: Network Segmentation Sim |
| P11 | Nov 30 | Mon | Tech | 3.3 Network Segmentation — VLANs, Subnets, DMZs |
| P12 | Dec 1 | Tue | Paper | Peer Review: Segmentation Findings |
| P13 | Dec 2 | Wed | Tech | 3.3 Network Segmentation — Zero Trust Architecture |
| P14 | Dec 3 | Thu | Paper | Mock MCQ Sprint: Unit 3 Review |
| P15 | Dec 4 | Fri | Tech | 🐙 GITHUB LAB: Firewall Config Lab |
| P16 | Dec 7 | Mon | Tech | 3.4 Firewalls — Types, Rule Sets, Configurations (converted from flex) |
| P17 | Dec 8 | Tue | Paper | Peer Review: Firewall Config Findings |
| P18 | Dec 9 | Wed | Tech | 📝 UNIT 3 TEST (converted from flex) |
| P19 | Dec 10 | Thu | Paper | Synthesis + Current Event (merged): Build Your Own Network Defense Plan |
| P20 | Dec 11 | Fri | Tech | 🐙 GITHUB LAB: Network Scanning Detection Lab (converted from flex) |

**Winter Break assignment (assigned in P20, collected Jan 4):** Unit 4 device inventory + pre-read of 4.1-4.2 CED excerpt. (Changed from the old "network mapping + review packet" — bridges the Dec 14-17 Unit 4 pre-break start so that content isn't forgotten over break.)

---

## P1: 3.1 Network Vulnerabilities — Identifying Common Attack Vectors (Nov 16, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on Unit 2 test corrections + the Unit 2 → Unit 3 pivot (what's a network vulnerability?).

**Learning Objectives:**
- 3.1.A Identify common network vulnerabilities and attack vectors
- 3.1.B Explain how adversaries exploit network weaknesses

**Suggested Skills:** 1.A (Identify assets, vulnerabilities, threats), 1.B (Describe impacts)

**Materials:** Slides, whiteboard, OSI model diagram, PBS NewsHour video (6:33, projector), NYT article (Aug 1, 2026) print/PDF

**Activities:**
1. **Hook (5 min):** "How many ways can someone attack a network they've never physically touched?" Brainstorm on whiteboard. Then connect to current events: **"In August 2026, hackers linked to Iran hit water systems in at least 7 U.S. states — chemical-treatment controllers, water pressure monitors — by finding internet-connected operational computers. No water was made unsafe, but utilities had to run manual operations. The FBI/EPA advisory: unplug vulnerable controllers from the internet."** Play **PBS NewsHour — "What we know about the cyberattacks on water systems in 7 states"** (https://youtu.be/4cqSk0EGH10, 6:33) — FBI confirms the 7 states and Iran as likely culprit. Then ask: what kind of network did they attack? (NYT, Aug 1 2026 — teacher prints/PDFs the article; students may be paywalled.)
2. **Direct instruction (20 min):** OSI model recap focusing on Layers 2–4 (Data Link, Network, Transport). Attack surface: every protocol is an attack vector. Introduce the four categories of network attacks covered in this unit — interception (sniffing/ARP), disruption (DoS/DDoS), redirection (DNS poisoning), and infiltration (MAC flooding).
3. **Activity — attack surface mapping (10 min):** Given a simple network diagram (router, switch, AP, 3 PCs, printer, server), students mark each attack vector opportunity at each layer.
4. **Preview the unit (5 min):** Quick walkthrough of the 5 CED topics, the 4 labs they'll do (wireless audit, segmentation sim, firewall config, scanning detection), and the synthesis day. Connect to the Term 2 timeline (Unit 3 test Dec 9).
5. **🇹🇼 Taiwan context — APT41 case study (3 min):** Show 3-slide mini-case: APT41 (China-based threat group) targeted at least 7 Taiwan tech companies in 2023-2024 using unpatched VPN appliances, weak SNMP community strings, and lack of network segmentation. Key point: these are the exact CED 3.1 attack vectors, deployed against companies within 50 km of this classroom. Question: "If you were the CISO of a Taiwan IC design firm, which attack vector from today keeps you up at night?" (Maps to: vulnerability, attack vector, threat actor targeting — CED Skills 1.A, 1.B.)

**Homework (due 20:30):** Guided notes: list 3 network vulnerabilities from today + one from the water-system story. Vocab flashcard set 1: vulnerability, attack vector, OSI layers 2-4, interception, disruption, redirection, infiltration.

---

## P2: Case Study: Equifax Breach — Network Attack Path (Nov 17, Tue — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 quick questions on attack vectors + vocab.

**Learning Objectives:**
- 3.1.A Identify network vulnerabilities exploited in a real breach
- 3.3.A Explain how segmentation contains lateral movement

**Materials:** Cyber Case Files — Equifax case (printed), worksheet

**Activities:**
1. **Read (10 min):** Read the Equifax breach summary from Cyber Case Files (nascar-paul.github.io/cyber-case-files/).
2. **Trace the attack path (15 min):** On the worksheet, trace: entry point (Apache Struts CVE-2017-5638) → lateral movement → data exfiltration (143M records). Map each step to a 3.1 vulnerability.
3. **Segmentation discussion (10 min):** "Which 3.3 segmentation would have contained the breach?" Pair discussion — why didn't Equifax's network stop the attacker from reaching consumer dispute data?
4. **Quick-write (5 min):** "If you were Equifax's CISO in 2017, what's the ONE control you'd add first?"

**Homework (due 20:30):** Finish worksheet. Read CED excerpt on 3.1 exploitation (1 page).

---

## P3: 3.1 How Adversaries Exploit Networks (Nov 18, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on Equifax case + attack vectors.

**Learning Objectives:**
- 3.1.B Explain how ARP poisoning, MAC flooding, DNS poisoning, and DoS/DDoS work

**Materials:** Slides, ARP diagram handout, switch CAM table diagram, DNS flow chart, video clip

**Activities:**
1. **Hook (3 min):** "You ask 'who has the printer?' and a stranger answers with a fake address — what happens next?"
2. **Direct instruction — ARP poisoning (12 min):** How ARP works: request, reply, cache. ARP poisoning/spoofing: attacker sends forged replies, maps their MAC to the gateway IP. No authentication means no verification. MITM positioning — intercept, modify, forward. Whiteboard walkthrough: normal exchange vs poisoned exchange; students trace a web request through the poisoned network.
3. **Direct instruction — MAC flooding & DNS poisoning (12 min):** MAC flooding: CAM table overflow — attacker floods fake MACs, switch falls back to hub mode (broadcasts all traffic). Enables sniffing. Limitations: modern switches have port security. DNS poisoning: cache poisoning injects fake DNS records, redirects users. Real example — 2019 Sea Turtle campaign.
4. **Direct instruction — DoS/DDoS (8 min):** DoS vs DDoS. SYN flood, amplification (DNS/NTP/Memcached), application-layer (HTTP flood, slow loris). Botnets: Mirai case study (IoT devices recruited).
5. **Comparison activity (5 min):** T-chart: ARP poisoning vs MAC flooding vs DNS poisoning vs DoS/DDoS — attack vector, attacker goal, layer, detection method, mitigation.

**Homework (due 20:30):** Complete the T-chart. Which of the four attacks would be hardest to detect? Write 2-3 sentences defending your choice.

---

## P4: Pre-Lab: Wireless Security Audit Prep (Nov 19, Thu — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 questions on attack types from P3.

**Learning Objectives:**
- 3.2.A Explain wireless security vulnerabilities and protections
- 3.2.B Identify wireless misconfigurations before the Friday lab

**Materials:** Friday's lab handout (wireless-security-audit-lab README), pre-lab worksheet, Delta flight evil twin case study (printed, from Unit 1 P9)

**Activities:**
1. **Read (10 min):** Read Friday's lab handout: Wireless Security Audit (repo: `ivycollegiate-development/wireless-security-audit-lab`).
2. **Pre-lab worksheet (15 min):** List Wi-Fi attack types (evil twin, deauth, KRACK, WPS brute-force, rogue AP). Predict: which wireless security setting is most commonly misconfigured?
3. **Vocabulary drill (10 min):** WPA3, WPA2, 802.1X, RADIUS, EAP, SSID, MAC filtering, evil twin. Notecard speed round.
4. **Discussion (5 min):** "If our school's Wi-Fi is encrypted, can someone in the parking lot still see your traffic?"
5. **Case study (5 min):** Revisit the Delta flight evil twin incident (Unit 1 P9, Aug 2026). Map it onto today's terms: deauth → rogue AP ("Delta WiFi Fast") → fake captive portal → credential harvest. Which audit check in Friday's lab would catch each step?

**Homework (due Sun 20:30 — Monday quiz):** Complete pre-lab predictions. Vocab flashcard set 2 (wireless terms).

---

## P5: GITHUB LAB: Wireless Security Audit (Nov 20, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on wireless terms.

**Lab spec:** `ivycollegiate-development/wireless-security-audit-lab`. Students audit a simulated wireless environment: identify weak encryption (WEP/WPA), rogue APs, open SSIDs, and misconfigurations; classify findings by severity; recommend fixes. Runs in Codespaces (no local install).

**Activities:**
1. **Setup (5 min):** Fork repo → Codespaces auto-launches. Review the audit checklist from P4's pre-lab.
2. **Lab (25 min):** Complete the audit scenarios in the repo: (a) identify which networks are vulnerable and why, (b) detect the evil twin / rogue AP (the same attack pattern as the Delta flight incident from Unit 1 P9), (c) score each finding (likelihood × impact), (d) write remediation for the top 3.
3. **Pair-share (10 min):** Compare findings with a partner — what did they catch that you missed? Submit via GitHub Classroom auto-grading.

**Homework (due Sun 20:30 — Monday quiz):** Finish any incomplete lab steps. Read CED excerpt on 3.1 risk assessment (1 page).

---

## P6: 3.1 Network Vulnerabilities — Risk Assessment Framework (Nov 23, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on wireless audit findings + risk concepts.

**Learning Objectives:**
- 3.1.C Explain how to assess and prioritize network risk

**Suggested Skills:** 1.A, 3.A

**Materials:** Slides, risk matrix handout, sample risk register

**Activities:**
1. **Hook (5 min):** "A school network has a printer exposed to the internet and a server with outdated firmware. Which do you fix first? How do you decide?"
2. **Direct instruction (20 min):** Risk = likelihood × impact. Risk matrix (5×5). Qualitative vs quantitative assessment. Risk register: asset, threat, vulnerability, likelihood, impact, score, mitigation. NIST-style framing. Apply to the water-system story from P1: the controllers were high-impact (public safety) but the fix (unplug from internet) was cheap — why did that take an FBI advisory to trigger?
3. **Activity — risk register (15 min):** Given the ICA network diagram from P1, students build a mini risk register for 5 assets (guest Wi-Fi, admin PCs, server room, Chromebook fleet, printer). Score each, rank, propose one control per asset.

**Homework (due 20:30):** Complete the risk register. Vocab flashcard set 3: likelihood, impact, risk matrix, risk register, mitigation.

---

## P7: FRQ Walk-Through + Vocabulary Drill (merged) (Nov 24, Tue — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 questions on risk assessment.

**Learning Objectives:**
- 1.A Identify the vulnerability in an AP-style scenario
- 2.A Recommend a managerial control
- 2.B Design a segmentation solution

**Materials:** AP-style FRQ prompt (unauthorized device on school network), simplified AP rubric

**Activities:**
1. **FRQ deconstruction (10 min):** Read the prompt: an unauthorized device connected to the school network accessed the admin file server. Part A: Identify the vulnerability (3.1). Part B: Recommend a managerial control (3.2). Part C: Design a segmentation solution (3.3).
2. **Individual response (10 min):** Write responses.
3. **Vocabulary drill (10 min):** Chain game — first student says a term (e.g., VLAN), next says a related term and explains the connection (firewall, DMZ, IDS...). 15 terms from 3.1-3.3.
4. **Peer-score (10 min):** Exchange papers, score with simplified AP rubric. Class discussion of model answer.

**Homework (due 20:30):** Rewrite your weakest FRQ part based on the model answer.

---

## P8: 3.2 Managerial Controls & Wireless — Policies, Acceptable Use (Nov 25, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on FRQ concepts.

**Learning Objectives:**
- 3.2.A Explain managerial controls for network security
- 3.2.C Explain wireless security configurations

**Materials:** Slides, sample policy documents

**Activities:**
1. **Hook (5 min):** **🇹🇼 ICA Chromebook scenario:** "You're at a café near Taichung Station. Your ICA Chromebook auto-connects to the free Wi-Fi — no password, no captive portal. What's the threat model? What's ONE thing ICA could do as a policy that would make this safer?" Brainstorm on whiteboard, then pivot: the café example has no managerial controls — no acceptable use policy, no authentication, no logging. That's the gap between 'the Wi-Fi works' and 'the Wi-Fi is secure.'
2. **Direct instruction — managerial controls (15 min):** SSID naming policy (no org names, no room numbers), acceptable use policy (AUA/P — what's allowed on the network, personal devices, guest access), guest network policy (captive portal, time limits, bandwidth caps, no internal access). Why managerial controls matter even with strong technical controls.
3. **Direct instruction — wireless protections (10 min):** WPA3 (SAE, forward secrecy, no PSK brute-force), EAP framework (EAP-TLS certificate-based, EAP-PEAP tunneled), MAC filtering (allowlist vs blocklist — bypassable but raises the bar), disabling SSID broadcast (hides from casual scanners only), signal control (directional antennas, power adjustment).
4. **Activity — write a guest network policy (10 min):** In groups, outline a one-page guest network policy for ICA: (a) who gets guest access, (b) authentication method, (c) restrictions, (d) acceptable use rules, (e) session time limits, (f) disclaimer/logging notice.
5. **🇹🇼 Taiwan phishing add-on (10 min, approved Aug 26):** Project 2-3 realistic-but-fake Chinese-language phishing samples modeled on documented campaigns targeting Taiwanese users (fake bank/7-11/e-commerce SMS+email, traditional characters) alongside an English sample. Students identify the tells in both languages. Teacher note: samples are teacher-drafted fakes based on publicly documented campaigns (e.g., fake 7-11 point-card SMS waves, bogus bank OTP requests) — no live malicious content. Key discussion: AI-generated phishing removes grammar tells, so language-native scrutiny matters more in Taiwan than anywhere.

**Homework (due 20:30):** Finish the guest policy draft. "Name one technical control and one managerial control that work together to secure a wireless network."

---

## P9: Thanksgiving Formal Dinner (Nov 26, Thu — PAPER DAY, light)

**⚡ HW Quiz (5 min):** Paper quiz — 2 questions on wireless policies.

**Activities:** Light discussion / reflection activity. Connect Thanksgiving to gratitude and reflection: students share one security concept from Unit 3 so far that changed how they see a network they use. No new content. Keep it easy.

**Homework (due 20:30):** None — enjoy the evening. (Reminder: Friday lab tomorrow.)

---

## P10: GITHUB LAB: Network Segmentation Sim (Nov 27, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on segmentation concepts (DMZ, VLAN basics from pre-reading).

**Lab spec:** `ivycollegiate-development/network-segmentation-sim`. Students design and test a segmented network in a browser-based simulator: create VLANs, place servers in a DMZ, add firewall rules between segments, verify traffic flows. Runs in Codespaces.

**Activities:**
1. **Setup (5 min):** Fork repo → Codespaces. Review VLAN concepts — access port vs trunk port, VLAN ID (1-4094), default VLAN (1).
2. **Lab (25 min):** (a) create VLAN 10 (Staff) and VLAN 20 (Students), (b) place web server + email server in a DMZ, (c) verify same-VLAN traffic flows, cross-VLAN blocked, (d) add inter-VLAN routing through the firewall, (e) block guest VLAN from reaching the internal file server. Capture screenshots as evidence.
3. **Pair-share (10 min):** Compare designs. Submit via GitHub Classroom.

**Homework (due Sun 20:30 — Monday quiz):** Finish lab. "What happens to broadcast traffic when you segment? Why protect IoT in their own VLAN?"

---

## P11: 3.3 Network Segmentation — VLANs, Subnets, DMZs (Nov 30, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on the segmentation sim.

**Learning Objectives:**
- 3.3.A Explain segmentation concepts
- 3.3.B Design a segmented network

**Materials:** Slides, network diagram templates

**Activities:**
1. **Hook (5 min):** "Your web server needs to be accessible from the internet. Your database server doesn't. How do you put them in different rooms with a locked door between them?" Then the real-world version: **"CISA's #1 recommendation after the Aug 2026 water-system hacks: unplug the internet-connected controllers from the internet. That's segmentation — isolating the systems that must talk to the outside world from the ones that don't. Why would a water utility have chemical controllers on the internet at all?"** (NYT, Aug 1 2026)
2. **Direct instruction (20 min):** Why segment? (Limit blast radius, isolate untrusted devices, enforce access controls.) DMZ: public-facing servers in a semi-trusted zone. Screened subnet: DMZ with dual firewalls. VLANs: logical segmentation on the same physical switch — different broadcast domains, no Layer 3 routing between them without a router/firewall. Trunk ports vs access ports.
3. **Activity — diagram the segmentation (15 min):** Small business with: web server, email server, internal file server, 20 employee PCs, 10 IoT cameras, guest Wi-Fi. Students draw: (a) DMZ for public servers, (b) screened subnet, (c) VLANs separating staff/IoT/guest, (d) firewalls between segments. **Extension — water utility variant:** add a SCADA controller, chemical dosing pumps, water quality monitor. Where do they go? (Answer: their own OT VLAN with NO internet route — that's the CISA fix.)

**Homework (due 20:30):** Complete the diagram. "How does segmentation limit the damage from a compromised IoT device?"

---

## P12: Peer Review: Segmentation Findings (Dec 1, Tue — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 questions on segmentation.

**Learning Objectives:**
- 3.3.B Evaluate a segmentation design against a rubric

**Materials:** Student P10 lab reports, rubric

**Activities:**
1. **Exchange (5 min):** Swap Friday's segmentation lab reports with a partner.
2. **Evaluate against rubric (15 min):** Completeness (all segments present?), evidence quality (screenshots + reasoning), security soundness (blast radius limited? guest isolated? DMZ correct?). Write one "glow" and one "grow."
3. **Class discussion (10 min):** Which vulnerabilities were most commonly missed? Poll: most common design flaw.
4. **Executive summary (10 min):** Write a 3-sentence executive summary of your combined findings — what would you tell ICA's IT about segmenting the school network?

**Homework (due 20:30):** Revise your lab based on feedback. Read CED excerpt on 3.3 zero trust (1 page).

---

## P13: 3.3 Network Segmentation — Zero Trust Architecture (Dec 2, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on peer review findings + zero trust pre-read.

**Learning Objectives:**
- 3.3.C Explain zero trust architecture principles

**Materials:** Slides, NIST SP 800-207 summary handout

**Activities:**
1. **Hook (5 min):** "Your network is a castle with a moat. Everything inside the walls is trusted... but what if the attacker is already inside?"
2. **Direct instruction (20 min):** Zero trust — "never trust, always verify." Core principles: continuous verification (not just at login), least privilege, microsegmentation (each workload/device isolated), assume breach. Contrast castle-and-moat vs zero trust. NIST SP 800-207 basics. How this reframes the segmentation work from P11: instead of a trusted internal network, every segment is untrusted until proven otherwise.
3. **Activity — zero trust scorecard (15 min):** Given the school network diagram from P11, students identify: which controls are castle-and-moat (perimeter firewall, trusted internal network) vs zero trust (per-device auth, microsegmentation). What would ICA need to move to zero trust?

**Homework (due 20:30):** "Pick one app you use daily (e.g., Google Classroom). What zero-trust-style checks happen behind the scenes?"

---

## P14: Mock MCQ Sprint: Unit 3 Review (Dec 3, Thu — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 questions on zero trust.

**Learning Objectives:**
- Self-assess Unit 3 knowledge ahead of the Dec 9 test

**Materials:** 5 AP-style MCQs, answer key, self-assessment sheet

**Activities:**
1. **Timed sprint (7 min):** 5 timed AP-style MCQs covering 3.1-3.5.
2. **Peer-grade (10 min):** Exchange, grade, discuss each answer's reasoning.
3. **Identify gaps (10 min):** Which 2 questions were most missed? Re-teach those concepts on the spot (whiteboard).
4. **Self-assessment (8 min):** Which 3.1-3.5 topic do you need to review most? Study guide check — mark weak areas.
5. **Study strategy (5 min):** How to use the study guide + flashcards between now and the test.

**Homework (due Sun 20:30 — Monday quiz):** Study guide section for your weakest topic. Test is Wed Dec 9.

---

## P15: GITHUB LAB: Firewall Config Lab (Dec 4, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on firewall pre-reading.

**Lab spec:** `ivycollegiate-development/firewall-config-lab`. Students write and test firewall rules in a browser-based simulator (or pfSense web GUI on the teacher Mac Mini). No client install.

**Activities:**
1. **Setup (5 min):** Fork repo → Codespaces. Overview: firewall menus, default rules (allow LAN→WAN, block WAN→LAN).
2. **Lab (25 min):** (a) block all traffic from a specific PC IP (simulated compromised device), (b) allow inbound SSH (22) from a specific admin IP only, (c) block outbound traffic to known malicious domains (alias with 3 fake domains), (d) allow web traffic (80/443) from LAN to DMZ web server only, (e) allow DNS (UDP 53) to specific servers only, (f) test each rule and verify the log shows blocked/allowed as expected.
3. **Debrief (10 min):** "Which rule took the most thought? How would an attacker try to bypass these rules (e.g., tunneling over allowed ports)?" Submit via GitHub Classroom.

**Homework (due Sun 20:30 — Monday quiz):** Finish lab. Read CED excerpt on 3.4 firewall types (1 page).

---

## P16: 3.4 Firewalls — Types, Rule Sets, Configurations (Dec 7, Mon — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on firewall lab.

**Learning Objectives:**
- 3.4.A Explain firewall types and functions
- 3.4.B Interpret and evaluate firewall rule sets

**Materials:** Slides, firewall rule examples, whiteboard, printed firewall config dumps

**Activities:**
1. **Hook (5 min):** "A firewall is just a list of rules — so why isn't it as simple as 'allow good, block bad'?"
2. **Direct instruction (20 min):** Firewall types — packet-filtering (stateless), stateful (tracks connection state, allows return traffic automatically), NGFW (DPI, application awareness, IPS, TLS decryption). ACLs — permit/deny, source/destination, port/protocol, implicit deny. Rule order matters (first match wins). Default-deny vs default-allow.
3. **Activity — ACL ordering puzzle (10 min):** Given 8 firewall rules (some overlapping, some contradictory), arrange in correct order. Then given a series of packets, determine allowed/denied.
4. **Activity — find the misconfigurations (5 min):** Given a firewall ruleset for a small company, identify: overly permissive rules, rules out of order (dead rules), missing logging, insecure services allowed (Telnet/FTP/SMB exposed to WAN), default-allow violations.

**Homework (due 20:30):** Document each finding: rule number, issue, risk level, recommended fix. "Why is default-deny more secure than default-allow?"

---

## P17: Peer Review: Firewall Config Findings (Dec 8, Tue — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 3 questions on firewall types/rules.

**Learning Objectives:**
- 3.4.C Evaluate firewall configurations against security principles

**Materials:** Student P15 lab reports + P16 findings, rubric

**Activities:**
1. **Exchange (5 min):** Swap firewall config reports with a partner.
2. **Evaluate against rubric (15 min):** Evidence quality (rule snapshots + logs), correctness (would the rules do what was claimed?), security soundness (default-deny? least privilege? logging?). One "glow," one "grow."
3. **Class discussion (10 min):** Compare findings from P16's misconfiguration hunt. Did everyone find the same issues? Any false positives — rules that look wrong but are actually needed?
4. **Synthesis (10 min):** "What's the single most dangerous firewall misconfiguration you can make?" Quick-write + share.

**Homework (due 20:30):** Study for tomorrow's test. Bring a one-page handwritten study sheet (allowed on test).

---

## P18: UNIT 3 TEST (Dec 9, Wed — TECH DAY)

**⚡ No HW quiz — test replaces it.**

**Assessment spec:** Paper-based, ~45 min, all 3.1-3.5 LOs. Structure: 20 MCQs (attack identification — ARP, DNS, MAC flooding, DoS/DDoS; wireless security controls; segmentation benefits; firewall rule interpretation; NIDS vs NIPS; SIEM functions) + 1 FRQ (network breach scenario: identify attack type, explain how it worked, propose mitigations — firewall rules, segmentation changes, NIDS signatures). One-page handwritten study sheet allowed.

**Activities:**
1. **Setup (5 min):** Distribute tests, review format, confirm study-sheet policy.
2. **Test (35 min):** Complete the test.
3. **Early finishers (5 min):** Preview Unit 4 (Securing Devices) one-pager or complete course feedback form.

**Homework (due 20:30):** None (test day). Preview: Unit 4 starts Monday Dec 14 — 4.1 device vulnerabilities.

---

## P19: Synthesis + Current Event (merged): Build Your Own Network Defense Plan (Dec 10, Thu — PAPER DAY)

**⚡ HW Quiz (5 min):** Paper quiz — 2 questions (post-test check-in on test topics).

**Learning Objectives:**
- Synthesize 3.1-3.5 into a complete defense design
- 3.5.C Apply detection concepts (NIDS placement, logging) to a design

**Materials:** Scenario packet, blank network diagram, current event article (printed)

**Activities:**
1. **Scenario launch (5 min):** "You are the IT security team for Ecosoft Electronics, a 50-person company in Hsinchu Science Park (embedded chips). 40 workstations, 1 web server, 1 internal file server (R&D — most sensitive), 1 dev server, 20 IoT sensors on the factory floor, guest Wi-Fi. Budget: one managed switch, one firewall/NGFW, one wireless AP. Design a defense-in-depth network."
2. **Design phase (15 min):** Groups design: VLAN segmentation with justification, firewall ACLs between segments, wireless security configuration, DMZ placement, NIDS placement, managerial controls (acceptable use, guest policy). Document with a network diagram + defense rationale.
3. **Pair-critique (10 min):** Swap with another group — identify at least 3 weaknesses or missing controls.
4. **Current event analysis (folded in, 10 min):** Read the printed current event (teacher-selected — e.g., a recent supply chain or network intrusion incident). Map it to the CED framework: vulnerability → exploit → impact. Which controls from the Ecosoft design would have stopped it?

**Homework (due 20:30):** Revise your design based on peer feedback. Tomorrow: final lab (network scanning detection).

---

## P20: GITHUB LAB: Network Scanning Detection Lab (Dec 11, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on detection concepts (NIDS/NIPS, SIEM).

**Learning Objectives:**
- 3.5.A Explain how NIDS/NIPS detect network attacks
- 3.5.B Explain SIEM functions and log correlation

**Materials:** Repo: `ivycollegiate-development/network-scanning-detection-lab` (pre-captured pcaps + scan artifacts)

**Activities:**
1. **Concept primer (10 min):** NIDS (monitor and alert) vs NIPS (monitor and block inline). Signature-based vs anomaly-based detection. SIEM — collect, normalize, correlate, alert, dashboard. Correlation: time-based, pattern-based, threshold-based. Examples: Snort/Suricata, Splunk, ELK, Wazuh. (Condensed from the original 2-day 3.5 sequence to fit the compressed calendar.)
2. **Lab (25 min):** Given pre-captured scan artifacts (port scan, brute-force, malware C2 beacon), students: (a) identify the scan type (SYN scan, full connect, UDP), (b) trace the attack chain across log sources, (c) write one Snort-style detection rule or SIEM correlation rule that would trigger on the pattern, (d) propose one response per critical finding (block IP, investigate host, patch service).
3. **Wrap-up (5 min):** Submit via GitHub Classroom. **Winter Break assignment assigned:** Unit 4 device inventory (list every device you own + its attack surface) + pre-read of 4.1-4.2 CED excerpt. Collected Jan 4.

**Homework (due Sun 20:30 — Monday Dec 14 quiz):** Finish lab. Start the Winter Break device inventory.

---

## Unit 3 — Lab Infrastructure Summary

| Lab | Tech Needed | Accounts Required | Setup Time |
|-----|-------------|-------------------|------------|
| Wireless Security Audit (P5) | Simulated wireless environment in Codespaces | GitHub Classroom | Repo pre-built |
| Network Segmentation Sim (P10) | Browser-based network simulator in Codespaces | GitHub Classroom | Repo pre-built |
| Firewall Config (P15) | Browser firewall simulator OR pfSense on teacher Mac Mini | None (Chromebook → browser) | 30 min pfSense setup if used |
| Network Scanning Detection (P20) | Pre-captured pcaps + scan artifacts in repo | GitHub Classroom | 15 min prep artifacts |

**Fallback low-infra options:** All labs can run from pre-captured artifacts and printed worksheets if Chromebooks or network access fail — the lab repos should include a `paper-fallback.md` with the equivalent worksheet.
