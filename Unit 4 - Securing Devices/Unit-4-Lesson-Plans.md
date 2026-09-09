# Unit 4 — Securing Devices: Lesson Plans

**~23 periods (Periods 56–76) | CED Topics 4.1–4.4 | Skills: Analyze (1.A, 1.B) · Mitigate (2.A, 2.B, 2.D) · Detect (3.A–3.D)**

**🇹🇼 Taiwan Threat Brief format (recurring):** The unit opener (Lesson 4.1) starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to device security. Keeps threat awareness local and current across the unit.

**🧩 Saturday CTF Alignment:** Three Saturday CTF sessions land around Unit 4 — **Dec 12 (SESSION 8: OWASP Juice Shop intro)** bridges Unit 3 (network) and Unit 4 (device security) by introducing web app security fundamentals early. **Jan 16 (SESSION 9: Juice Shop continued + writeup catch-up)** falls after midterms and gives students hands-on web vuln experience that connects to device-level attack surfaces (4.1-4.3). **Jan 23 (SESSION 10: MCQ/FRQ midterm drills)** directly supports Unit 4 test prep and midterm readiness. Session 8-9 build a web security foundation that Unit 5 will fully leverage.

---

## Lesson 4.1 — Malware Types

**Period:** 55  |  **LOs:** 1.A, 1.B

**Materials:** Slides, whiteboard, malware fact cards

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Your laptop starts encrypting every file and demands $500 in Bitcoin. What just infected you?" |
| 20 min | **Direct instruction:** Eight malware types — virus, worm, trojan, ransomware, rootkit, RAT (remote access trojan), keylogger, spyware. For each: how it spreads, what it does, classic example. **🇹🇼 Mustang Panda spotlight (2 min, integrated):** When covering trojan/RAT types, mention that Mustang Panda — a China-linked APT group — used malicious Chrome extensions disguised as productivity tools to target Taiwanese users in 2024-2025. The extension phished browser data, credentials, and could force Chrome to visit attacker-controlled sites. This demonstrates both trojan delivery (user installs a 'useful' extension) and RAT-like behavior (persistent remote access to the browser's data). Reference: publicly documented Trend Micro / Recorded Future reports on Mustang Panda's Chrome extension campaigns targeting Taiwan. |
| 15 min | **Activity — malware matching:** Given 8 scenario descriptions (e.g., "logs every keystroke and sends to attacker"), match each to the correct malware type. Then rank by: (a) hardest to detect, (b) most damaging. |
| 5 min | **Exit ticket:** "Which malware type would you least want on your device — and why?" |

---

## Lesson 4.2 — Attack Vectors

**Period:** 56  |  **LOs:** 1.A, 1.B

**Materials:** Slides, vector scenario cards, PBS NewsHour video (6:33, projector — optional re-watch)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A USB stick with a company logo is found in the parking lot. Would you plug it in?" |
| 15 min | **Direct instruction:** Attack vectors — USB drops, drive-by downloads, supply chain attacks, zero-day exploits, watering hole attacks, malicious ads. How each works, who uses them, detection difficulty. |
| 15 min | **Activity — vector identification:** Given 8 real-world incidents (e.g., NotPetya via accounting software update), identify the attack vector used. Discuss: which vectors are hardest to defend against? **Add the Aug 2026 U.S. water-system hack (NYT, Aug 1 2026):** the initial vector wasn't a USB drop or a drive-by — attackers reached internet-connected PLC/SCADA controllers directly (or via the vendor/IT network). Cross-reference Unit 3: this is why CISA told utilities to unplug vulnerable controllers from the internet — segmentation is the device-level defense too. **Optional re-watch:** PBS NewsHour segment (https://youtu.be/4cqSk0EGH10, 6:33) — the interview with former FBI cyber official Cynthia Kaiser reinforces "attribution is a process, not a fact" (FBI: Iran is the *likely* culprit, no formal attribution). |
| 10 min | **Discussion — zero-days:** What makes a zero-day so dangerous? How are they discovered? Who buys them? Ethical implications. |
| 5 min | **Exit ticket:** "What's the difference between a drive-by download and a watering hole attack?" |

---

## Lesson 4.3 — Malware Analysis Demo Lab

**Period:** 57  |  **LOs:** 1.A, 1.B

**Materials:** Projector, ANY.RUN (teacher account), sample malware hash / URL

| Time | Activity |
|------|----------|
| 5 min | **Setup:** "How do we know what malware does without infecting our own computer?" Introduce sandbox analysis — run in isolated environment, watch what it does. |
| 25 min | **Demo — ANY.RUN analysis:** Teacher submits a malware sample (e.g., a known Emotet or AgentTesla sample hash). Walk through: network connections, processes spawned, files written, registry changes, screenshots. Call out indicators of compromise (IoCs). |
| 10 min | **Worksheet — analysis report:** While watching, students fill in a structured observation sheet: malware type, technique used, IoCs found (IPs, domains, file paths, mutexes). |
| 5 min | **Exit ticket:** "What's one IoC you'd put in a detection rule based on today's sample?" |

**Lab spec:** Teacher-led demo via ANY.RUN (browser-based, no install). Students observe and complete worksheet. No student accounts needed.

---

## Lesson 4.4 — Authentication & Password Hashes

**Period:** 58  |  **LOs:** 1.A, 1.B

**Materials:** Slides, whiteboard

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Your password is stored as '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'. What does that mean?" |
| 15 min | **Direct instruction:** Authentication factors (something you know/have/are). Password hashing — why plaintext is bad, hash functions (MD5, SHA-1, SHA-256), what a hash looks like. |
| 15 min | **Activity — hash comparison:** Given 3 different hash values, determine which are the same password and which differ. Discuss: can you reverse a hash? What can you do instead? |
| 10 min | **Concept check:** Why does a website only need to store a hash? How does login work with hashes? |
| 5 min | **Exit ticket:** "Why is storing a hash better than storing an encrypted password?" |

---

## Lesson 4.5 — Salting, Peppering & Password Storage

**Period:** 59  |  **LOs:** 1.A, 1.B, 2.A

**Materials:** Slides, hash calculator (browser-based)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** Show a rainbow table lookup: "hash('password') = 5e884898… — and 5e884898… = 'password'. Uh oh." |
| 15 min | **Direct instruction:** Salt (per-user random value), pepper (application-wide secret), key derivation functions (bcrypt, Argon2, PBKDF2). Why modern systems use slow hash functions. |
| 15 min | **Activity — salted hash demo:** Teacher uses a browser-based hash tool. Show: same password + different salt = different hash. Same password + same salt = same hash (rainbow table vulnerability). |
| 10 min | **Discussion — database breaches:** When a breach happens, what protects users who used the same password everywhere? Why salting matters at scale. |
| 5 min | **Exit ticket:** "Why does bcrypt use a work factor, and what tradeoff does it represent?" |

---

## Lesson 4.6 — MFA, Biometrics & FIDO2

**Period:** 60  |  **LOs:** 1.A, 1.B, 2.A, 2.B

**Materials:** Slides, YubiKey / FIDO2 security key (teacher demo), phone for authenticator app demo

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A hacker has your password. Can they still log in?" |
| 15 min | **Direct instruction:** MFA types — SMS codes (vulnerable to SIM swapping), TOTP authenticator apps, push notifications, hardware security keys (FIDO2/U2F), biometrics (fingerprint, face, iris). Compare security vs convenience. |
| 15 min | **Demo — FIDO2:** Teacher shows a YubiKey in action on a supported site (e.g., GitHub or Google). Explain: public-key cryptography, why phishing can't steal a FIDO2 credential. |
| 10 min | **Activity — MFA scenario ranking:** Given 6 scenarios (bank login, school LMS, personal email, server SSH, crypto exchange, ATM), recommend the appropriate MFA method and justify. |
| 5 min | **Exit ticket:** "Why does SMS-based MFA have a lower security rating than app-based TOTP?" |

---

## Lesson 4.7 — Advanced Authentication Attacks

**Period:** 61  |  **LOs:** 1.A, 1.B, 2.A

**Materials:** Slides, attack diagram handouts

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "You typed your password once. Now the attacker has it everywhere on the network — and they didn't even need your password." |
| 20 min | **Direct instruction:** Pass-the-hash (NTLM relay), golden ticket (Kerberos forgery), Silver Ticket, Kerberoasting, MFA fatigue bombing. How each works, what it exploits, which platform (Windows/Linux/cloud). |
| 15 min | **Activity — attack mapping:** Given 5 authentication attack scenarios, trace the attack path: initial access → credential access → lateral movement. Identify: which control would block it? |
| 5 min | **Exit ticket:** "What makes golden ticket attacks so hard to detect?" |

---

## Lesson 4.8 — Hash Cracking Lab

**Period:** 62  |  **LOs:** 1.A, 2.D

**Materials:** John the Ripper (teacher Mac Mini, projected), sample hash files, wordlists

| Time | Activity |
|------|----------|
| 5 min | **Setup:** "How long does it actually take to crack a hash?" Explain the lab: teacher runs JtR on a set of hashes. Students observe and analyze results. |
| 25 min | **Demo — John the Ripper:** Teacher demonstrates: (a) cracking unsalted MD5 hashes with a wordlist, (b) cracking with rules/mangling, (c) cracking salted hashes (much slower). Show real-time hash rates. Project a pre-cracked set of 20 hashes — students identify which passwords were weak and why. |
| 10 min | **Worksheet — crack time analysis:** Given hash type, algorithm, and hardware specs, estimate crack time for passwords of different lengths and complexity. Compare: MD5 vs SHA-256 vs bcrypt. |
| 5 min | **Exit ticket:** "What's the cheapest way to make hashes 100x harder to crack?" |

**Lab spec:** Teacher demo on Mac Mini (John the Ripper). Students analyze projected results and complete worksheet. No student terminal access needed.

---

## Lesson 4.9 — Antimalware Defenses

**Period:** 63  |  **LOs:** 2.A, 2.D

**Materials:** Slides, whiteboard

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Antivirus found the malware. But how did it know it was bad?" |
| 20 min | **Direct instruction:** Three detection methods — signature-based (hash/pattern match), heuristic-based (looks suspicious), behavioral-based (acts suspicious). Pros and cons of each. Modern EDR vs traditional AV. |
| 15 min | **Activity — detection method matching:** Given 10 detection scenarios (e.g., "file hash matches known malware database", "process modifies system32 while encrypted", "script attempts to download and execute"), label each as signature/heuristic/behavioral. |
| 5 min | **Exit ticket:** "Why can't we rely on signatures alone?" |

---

## Lesson 4.10 — Patch Management & Host Firewalls

**Period:** 64  |  **LOs:** 2.A, 2.B

**Materials:** Slides, timeline poster

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Microsoft released a security patch on Tuesday. By Thursday, it was being exploited. What's your move?" |
| 20 min | **Direct instruction:** Patch management lifecycle — identify, test, deploy, verify. Vulnerability severity scoring (CVSS). Patch Tuesday vs zero-day. Host firewall basics — inbound/outbound rules, allow/deny by port/IP/application. **🇹🇼 CHT spotlight (3 min, integrated):** Chunghwa Telecom (CHT) manages ~4M+ customer-premises equipment devices (home gateways/routers/fiber modems) across Taiwan. Their patch challenge: thousands of device models, limited compute/update windows, and customers who won't reboot their router. CHT has to do staged rollouts — test on 1% of devices first, then 10%, then full fleet — with rollback capability at every stage. Question for students: "How is CHT's patch problem different from patching a corporate laptop fleet? What happens if a CHT router CVE gets exploited while waiting for a patch window?" (Maps to: operational risk, staged deployment, rollback planning — CED Skill 2.A.) |
| 15 min | **Activity — patch prioritization exercise:** Given 5 CVEs with CVSS scores, affected systems, and exploit availability, prioritize patching order. Justify each decision. |
| 5 min | **Exit ticket:** "Why might an organization delay deploying a critical patch?" |

---

## Lesson 4.11 — Disk Encryption & EDR

**Period:** 65  |  **LOs:** 2.A, 2.B

**Materials:** Slides, encryption demo (command-line)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "You smash someone's laptop and take the hard drive. Can you read the data? Only if it wasn't encrypted." |
| 15 min | **Direct instruction:** Full-disk encryption (FileVault, BitLocker), how it protects data at rest. EDR (Endpoint Detection and Response) — continuous monitoring, threat hunting, automated response. EDR vs AV — the key differences. |
| 15 min | **Demo — encryption:** Teacher shows encrypted vs unencrypted USB drive. Show: with encryption, the data is gibberish without the key. Explain where the key lives (TPM, Secure Enclave). |
| 10 min | **Activity — defense layer stacking:** Given an endpoint (laptop), list all available protection layers in order — from outermost (network firewall) to innermost (disk encryption). Mark which layers protect which CIA triad elements. |
| 5 min | **Exit ticket:** "Does disk encryption protect against ransomware while the laptop is on? Why or why not?" |

---

## Lesson 4.12 — Endpoint Hardening Lab

**Period:** 66  |  **LOs:** 2.A, 2.D

**Materials:** Endpoint hardening checklist template (printed), scenario sheet

| Time | Activity |
|------|----------|
| 5 min | **Setup:** "What does a 'hardened' endpoint look like?" Introduce the concept of a security baseline — the minimum acceptable configuration. |
| 30 min | **Lab — Build an endpoint hardening guide:** Given a scenario (onboarding a new employee laptop for a Taiwan semiconductor company), students create a hardening checklist covering all 5 categories: OS hardening, application security, network security, access controls, monitoring. For each item: setting, rationale, priority (P1-P3). |
| 10 min | **Peer review:** Swap hardening guides with another pair. Review: is it complete? Are the priorities reasonable? Could any setting break productivity? |
| 5 min | **Exit ticket:** "What's the hardest balance to strike when hardening an endpoint?" |

**Lab spec:** Browser-accessible checklist template (Google Docs or printed) + scenario sheet. No system access required.

---

## Lesson 4.13 — Event Logs & Sysmon

**Period:** 67  |  **LOs:** 3.A, 3.B

**Materials:** Slides, sample Windows Event Viewer screenshots, Sysmon configuration file (sample)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A process spawned cmd.exe that connected to a suspicious IP. Did Windows notice? Yes — if you know where to look." |
| 20 min | **Direct instruction:** Windows Event Log structure — Application, Security, System, and custom logs. Event IDs (4624=logon, 4688=process creation, 7045=service install). Sysmon — what it adds (ProcessCreate with hash, NetworkConnect, FileCreateTime, RegistryEvent). Sysmon config files (what to log, what to ignore). |
| 15 min | **Activity — event ID bingo:** Given 15 event descriptions, match each to the correct Event ID. Then: given an event log entry, identify: what happened, when, who, what process, suspicious indicators. |
| 5 min | **Exit ticket:** "Why does Sysmon add process hashes when Windows already logs process creation?" |

---

## Lesson 4.14 — EDR Telemetry & File Integrity Monitoring

**Period:** 68  |  **LOs:** 3.A, 3.B, 3.C

**Materials:** Slides, sample EDR telemetry screenshots, file hash database

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A file in C:\Windows\System32 changed. Normal Windows update or malware replacing a system file?" |
| 15 min | **Direct instruction:** EDR telemetry types — process trees, network connections, file operations, registry changes, loaded modules, DNS queries. File Integrity Monitoring (FIM) — baselining file hashes, detecting unauthorized changes. Tripwire / OSSEC concepts. |
| 15 min | **Activity — process tree reconstruction:** Given a sequence of EDR telemetry events (parent PID → child PID → network connection → file write), reconstruct the full attack chain. Identify: initial access, persistence mechanism, C2 communication, data exfiltration. |
| 10 min | **Activity — FIM scenario:** Given a list of system files with current hashes vs baseline, identify which files changed. For each: is this legitimate (Windows Update, application install) or suspicious (possible malware)? |
| 5 min | **Exit ticket:** "Why does FIM need a trusted baseline?" |

---

## Lesson 4.15 — Sysmon Log Analysis Lab

**Period:** 69  |  **LOs:** 3.A, 3.B, 3.C, 3.D

**Materials:** Pre-generated .evtx files (Sysmon logs), analysis worksheet

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Distribute Sysmon log files (as CSV/JSON extracts — .evtx can't open on Chromebooks). Explain the log format — EventID, UtcTime, ProcessGuid, ProcessId, Image, CommandLine, ParentImage, ParentCommandLine, Network connection details. |
| 30 min | **Lab — Analyze Sysmon logs:** Given 3 sets of logs from a simulated infection:
| | **Set A — Initial access:** Find the malicious document and the process it launched. Identify: filename, parent process, command line arguments.
| | **Set B — C2 communication:** Find the outbound network connection. Identify: destination IP and port, process making the connection, DNS query (if present).
| | **Set C — Persistence:** Find the registry run key creation or scheduled task. Identify: what key/value was written, what binary it points to.
| 10 min | **Debrief:** Compare findings. What was the full attack chain? Which single detection rule would have caught the earliest step? |
| 5 min | **Exit ticket:** "What's one Event ID you'd write a detection rule for?" |

**Lab spec:** Pre-generated Sysmon logs as CSV/JSON (compatible with Chromebook browser). Analysis worksheet provided. No .evtx viewer needed.

---

## Lessons 4.16-4.18 — Mini-Project: Device Security Hardening Guide

**Periods:** 70-72  |  **LOs:** 2.B, 2.D, 3.D, 4.A, 4.D

**Materials:** Scenario packet, Google Docs/Slides, reference materials (CIS benchmarks, NIST guidelines — teacher-provided excerpts)

| Time | Day 1 (Period 70) | Day 2 (Period 71) | Day 3 (Period 72) |
|------|--------------------|--------------------|--------------------|
| 5 min | Launch scenario + deliverables | Setup peer review | Setup presentations |
| 25 min | **Research & outline:** Groups receive their scenario (see below). Identify: (a) threat model for the organization, (b) 5 key controls to recommend, (c) detection methods for each. Research provided reference materials and class notes. | **Draft complete + peer review:** Complete first draft of hardening guide. Swap with another group for a structured 15-minute review. Review criteria: completeness, accuracy, feasibility, clarity. Address feedback in remaining time. | **Presentations:** 5 min per group + 2 min Q&A. Audience evaluates: would this guide actually work for that organization? |
| 10 min | Fill in scenario-specific details | Revisions + finalize guide | Peer evaluation forms |
| 5 min | Role assignments + group check-in | Teacher check-in on progress | Wrap up, collect deliverables |

**Scenario options (teacher assigns one per group):**

- **Scenario A — Small business:** A Taichung bubble tea shop with 1 Windows POS terminal, 2 employee laptops, 1 phone for Instagram orders. Budget: minimal. Goal: protect customer payment data.
- **Scenario B — School:** ICA's computer lab with 30 Chromebooks and 1 admin Windows PC. Goal: prevent students from installing malware, protect grading data.
- **Scenario C — Remote worker:** An employee at a Taiwan tech company working from home on a personal laptop that accesses company VPN. Goal: secure the endpoint without full IT control.
- **Scenario D — Server:** A Linux web server hosting a customer portal. Goal: harden OS, detect intrusion attempts, respond to compromise.

**Deliverable:** Hardening guide document (2-3 pages) with:
1. Threat model summary (2-3 highest-priority threats)
2. Hardening checklist (minimum 10 items across OS, apps, network, access, monitoring)
3. Detection rules (2-3 specific rules: e.g., "Alert when Event ID 4688 shows powershell.exe launched from Office app")
4. Incident response flow (what to do if a control detects something)

---

## Lesson 4.19 — Unit 4 Review

**Period:** 73  |  **LOs:** All Unit 4

**Materials:** Kahoot/Quizizz, scenario packet, whiteboard

| Time | Activity |
|------|----------|
| 15 min | **Kahoot review:** 20 questions covering: malware types, attack vectors, authentication (hashes, salting, MFA, pass-the-hash), endpoint protection (AV, patch mgmt, encryption, EDR), detection (event logs, Sysmon, FIM). |
| 20 min | **Scenario — full incident analysis:** "An employee's laptop was infected. Walk through: (1) Which malware? How did it get in? (2) Were passwords compromised? What auth controls would help? (3) What endpoint controls failed? (4) How would you detect it next time?" |
| 10 min | **Study guide review:** Students check notes against provided study guide. Mark gaps. |
| 5 min | **Q&A:** Open floor for questions before tomorrow's test. |

---

## Lesson 4.20 — Unit 4 Test

**Period:** 74  |  **LOs:** All Unit 4

**Materials:** Test papers (or digital form), answer key

| Time | Activity |
|------|----------|
| 40 min | **Test:** 20 MC (2 min each) + 1 FRQ. Covers: malware identification, attack vectors, authentication & MFA, hash concepts, endpoint hardening, log analysis & detection. |
| 5 min | Early finishers: read Unit 5 preview. |

**Assessment spec:** 20 MC + 1 FRQ = 40 min with buffer.

---

## Unit 4 — Lab Infrastructure Summary

| Lab | Tech Needed | Accounts Required | Setup Time |
|-----|-------------|-------------------|------------|
| Malware Analysis Demo | ANY.RUN (teacher browser) | Teacher ANY.RUN account | 5 min |
| Hash Cracking Demo | John the Ripper (teacher Mac Mini) | None | 10 min config |
| Endpoint Hardening | Checklist template (printed or Google Docs) | None (or school Google) | 5 min template |
| Sysmon Log Analysis | Pre-generated CSV/JSON logs + worksheet | None | 15 min log prep |
| Mini-project | Scenario packets + Google Docs/Slides | School Google account | 20 min materials |
| All others | Slides / discussion / printed materials | None | None |

**Unit 4 requires zero student software installs and zero student accounts for labs.** All labs work via teacher demo, printed materials, or browser-accessible documents.
