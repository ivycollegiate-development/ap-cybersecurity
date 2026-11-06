# AP Review Sprint — Slide Deck Outlines

**AP Cybersecurity — ICA 2026-27**  
**Review Period**: Apr 12 – May 4, 2027 (3 weeks before AP Exam May 5)  
**Target**: 5 Unit Review Packets + 3 FRQ Practice Sets + CLI Fluency + Mock Exam

---

## Deck 1: Course Overview & Exam Strategy (1 session)

**Slides**: 15 | **Time**: 50 min | **Date**: Apr 12

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Title | AP Cybersecurity Exam Review — ICA 2026-27 |
| 2 | Exam Format | 60 MCQ (80 min) + 1 FRQ Device Security Analysis (50 min) = 130 min |
| 3 | Scoring | MCQ 70% (42 pts raw) + FRQ 30% (18 pts raw) → Composite 1-5 |
| 4 | Unit Weighting | U1: 18% | U2: 29% | U3: 20% | U4: 24% | U5: 9% (per CED) |
| 5 | Question Types | Single-select MCQ | Multi-select MCQ (5 options, variable correct) | FRQ: 5 parts (A-E) |
| 6 | Time Management | MCQ: 1.3 min/q | FRQ: 10 min/part | Flag & return strategy |
| 7 | Multi-Select Strategy | "Select all that apply" — treat each option as T/F | No penalty for guessing |
| 8 | FRQ Rubric | 14 pts across 5 parts | Partial credit | Key terms = points |
| 9 | High-Miss Bank | 30 items from unit tests + practice exam | Focus review here |
| 10 | Review Schedule | Apr 12-19: Unit packets | Apr 20/22/27: FRQ practice | Apr 28: CLI Fluency |
| 11 | Resources | Course Curriculum Framework LO map | College Board CED | Unit review packets |
| 12 | Practice Exam | Self-scored Apr 2-11 | Error analysis due Apr 11 | Informs high-miss bank |
| 13 | CLI Fluency | 10 tasks Apr 28 | Codespaces environment | Practical skills for FRQ |
| 14 | Test Day Logistics | May 5, 8:00 AM | Bring: pencils, calculator (provided), water | No devices |
| 15 | Q&A / Next Steps | Distribute U1 Review Packet | Homework: Complete U1 packet by Apr 14 |

---

## Deck 2: Unit 1 — Foundations of Cybersecurity (1 session)

**Slides**: 20 | **Time**: 50 min | **Date**: Apr 13

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Unit 1 Overview | 18% of exam | CIA Triad | Threat Actors | Risk Management |
| 2 | LO 1.1.A | Threat vs Vulnerability vs Risk | Definitions | Examples | Risk = T × V × I |
| 3 | LO 1.2.A-C | CIA Triad Deep Dive | Confidentiality (encryption, access control) | Integrity (hashes, signatures) | Availability (redundancy, backups) |
| 4 | LO 1.3.A-B | Threat Modeling | STRIDE | MITRE ATT&CK (Recon TA0043 vs Discovery TA0007) | Attack Trees |
| 5 | LO 1.4.A-C | Security Architecture | Defense in Depth | Zero Trust (never trust, always verify) | Perimeter vs Zero Trust |
| 6 | LO 1.5.A-B | Incident Response | NIST SP 800-61: Prep → Detect → Contain → Recover → Lessons Learned |
| 7 | High-Miss Items (6) | HM-001 to HM-006 from packet | Walk through each with distractor analysis |
| 8 | Mini-Lesson: Zero Trust | Architecture diagram | PDP/PEP | Micro-segmentation | Exam tips |
| 9 | Mini-Lesson: MITRE Recon | TA0043 techniques | Recon vs Discovery distinction | Exam traps |
| 10 | Practice Questions | 5 new items from packet | Think-pair-share | Immediate feedback |
| 11 | Common Pitfalls | Confusing threat/vuln/risk | Mixing up Recon/Discovery | Zero Trust = "trust but verify" (WRONG) |
| 12 | Study Resources | U1 Review Packet | NIST CSF | MITRE ATT&CK Navigator |
| 13 | Homework | Complete U1 packet | Flashcards: STRIDE, CIA, IR phases |

---

## Deck 3: Unit 2 — Network Security (1 session)

**Slides**: 20 | **Time**: 50 min | **Date**: Apr 14

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Unit 2 Overview | 29% of exam (largest unit) | TCP/IP | Firewalls | DNS | Wireless | VPN |
| 2 | LO 2.1.A-C | TCP/IP & Scanning | 3-way handshake | SYN/NULL/FIN/XMAS/ACK scans | RFC 793 responses |
| 3 | LO 2.2.A-B | Firewalls | Stateless vs Stateful | Connection tracking | Default deny vs allow |
| 4 | LO 2.3.A-D | DNS | Record types (A, AAAA, CNAME, NS, MX, TXT) | Delegation | Subdomain takeover | DNSSEC |
| 5 | LO 2.4.A-B | Layer 2 Attacks | ARP poisoning | DHCP snooping | VLAN hopping | MAC flooding |
| 6 | LO 2.5.A-C | Wireless | WPA2-Personal (PSK) vs Enterprise (802.1X) | WPA3 SAE | KRACK |
| 7 | LO 2.6.A-B | VPN & IPsec | Tunnel vs Transport mode | ESP vs AH | SSL/TLS layer |
| 8 | High-Miss Items (6) | HM-007 to HM-012 | Focus: NULL scan, NS records, ARP layer, WPA3 SAE |
| 9 | Mini-Lesson: DNS Delegation | NS records | Subdomain takeover demo | dig +trace |
| 10 | Mini-Lesson: TCP Scan Types | Flag combinations table | Open/Closed/Filtered responses | nmap flags |
| 11 | Practice Questions | 5 new items | nmap output interpretation |
| 12 | Common Pitfalls | Confusing transport/tunnel mode | ARP = Layer 3 (wrong) | WPA2 vs WPA3 auth methods |
| 13 | Study Resources | U2 Review Packet | RFC 793 | nmap cheat sheet |
| 14 | Homework | Complete U2 packet | Practice: nmap scan types |

---

## Deck 4: Unit 3 — Cryptography (1 session)

**Slides**: 20 | **Time**: 50 min | **Date**: Apr 15

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Unit 3 Overview | 20% of exam | Hashes | Symmetric | Asymmetric | PKI | TLS |
| 2 | LO 3.1.A-C | Hash Functions | Properties: Preimage, 2nd Preimage, Collision | Avalanche | SHA-256 | MD5/SHA-1 broken |
| 3 | LO 3.2.A-B | Symmetric Crypto | AES (block=128, keys=128/192/256) | Modes: ECB, CBC, GCM | Stream vs Block |
| 4 | LO 3.3.A | Asymmetric: DH | Discrete Log Problem | Classic DH vs ECDH | Key sizes | PFS |
| 5 | LO 3.4.A-C | Asymmetric: RSA & Signatures | RSA math | Signing = private key | ECDSA/EdDSA | Non-repudiation |
| 6 | LO 3.5.A-B | PKI & Certificates | X.509 structure | CA hierarchy | CRL vs OCSP | CT Logs |
| 7 | LO 3.6.A-B | TLS | Handshake (1.2 vs 1.3) | Cipher suites | PFS = ephemeral DH | Cert pinning |
| 8 | High-Miss Items (6) | HM-013 to HM-018 | Focus: Preimage resistance, AES params, DH=DLP, ECDSA, CA signs, PFS |
| 9 | Mini-Lesson: DH & DLP | Math visualization | Key size comparison table | ECC advantage |
| 10 | Mini-Lesson: Hash Properties | Three properties Venn | Birthday attack | Collision ≠ Preimage |
| 11 | Practice Questions | 5 new items | Certificate chain verification |
| 12 | Common Pitfalls | AES block size = key size (wrong) | DH = factorization (wrong) | PFS = AES-256 (wrong) |
| 13 | Study Resources | U3 Review Packet | Crypto cheat sheet | OpenSSL commands |
| 14 | Homework | Complete U3 packet | OpenSSL practice: gen key, CSR, verify |

---

## Deck 5: Unit 4 — System Security (1 session)

**Slides**: 20 | **Time**: 50 min | **Date**: Apr 16

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Unit 4 Overview | 24% of exam | Windows | Linux | Memory | Malware | SELinux/AppArmor |
| 2 | LO 4.1.A-B | Windows Security | UAC | Credential Guard (VBS) | HVCI | AppLocker | Event logs |
| 3 | LO 4.2.A-C | Linux Security | /etc/passwd vs /etc/shadow | Capabilities (CAP_DAC_OVERRIDE) | SUID/SGID | Auditd |
| 4 | LO 4.3.A-B | Memory Protection | ASLR (entropy 32/64-bit) | DEP/NX | Stack Canaries | CFG/CET | ROP/JOP |
| 5 | LO 4.4.A-B | Buffer Overflows | Stack smashing | Format string | Heap overflow | Mitigations combined |
| 6 | LO 4.5.A-C | Malware Analysis | Static vs Dynamic | Packers | C2 | Persistence | YARA |
| 7 | LO 4.6.A-B | MAC Systems | SELinux modes (Enforcing/Permissive/Disabled) | AppArmor (path-based) | Targeted vs MLS |
| 8 | High-Miss Items (6) | HM-019 to HM-024 | Focus: Credential Guard, /etc/shadow, ASLR scope, ASLR vs Canary, CAP_DAC_OVERRIDE, SELinux Permissive |
| 9 | Mini-Lesson: ASLR + DEP + Canaries | Combined defense table | Bypass techniques | ROP chain concept |
| 10 | Mini-Lesson: Windows VBS | Credential Guard architecture | VSM | Trustlets | Requirements |
| 11 | Practice Questions | 5 new items | Audit log analysis |
| 12 | Common Pitfalls | ASLR = prevents overflow (wrong) | Canary = prevents ROP (wrong) | CAP_SYS_ADMIN = DAC override (wrong) |
| 13 | Study Resources | U4 Review Packet | Mitigation comparison table |
| 14 | Homework | Complete U4 packet | Memory protection diagram |

---

## Deck 6: Unit 5 — Application Security (1 session)

**Slides**: 20 | **Time**: 50 min | **Date**: Apr 17

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Unit 5 Overview | 9% of exam | OWASP Top 10 | Access Control | Crypto in Apps | PKI | WAF | Logging |
| 2 | LO 5.1.A-C | OWASP Top 10 2021 | A01 Broken Access Control | A03 Injection | A04 Insecure Design | A06 Vulnerable Components |
| 3 | LO 5.2.A-D | Access Control Models | DAC | MAC | RBAC | ABAC (attributes) | RuBAC |
| 4 | LO 5.3.A-B | Applied Crypto | RSA key components (d, φ(n) secret) | Key storage | JWT | Key rotation |
| 5 | LO 5.4.A-B | PKI in Applications | OCSP (responder signs) | Stapling | CT Logs | Pinning |
| 6 | LO 5.5.A-B | WAF & Secure Coding | Detection vs Prevention mode | ModSecurity | SAST/DAST | Input validation |
| 7 | LO 5.6.A-C | Logging & Monitoring | Structured logs (JSON) | SIEM correlation | Syslog severity | Alerting |
| 8 | High-Miss Items (6) | HM-025 to HM-030 | Focus: Injection category, ABAC, RSA d secret, OCSP responder, WAF monitor mode, JSON logs |
| 9 | Mini-Lesson: Injection Defense | Parameterized queries #1 | Allowlist validation | ORM safety | WAF = layer 2 |
| 10 | Mini-Lesson: ABAC vs RBAC | Attribute evaluation | XACML | Dynamic vs Static |
| 11 | Practice Questions | 5 new items | Log parsing with jq |
| 12 | Common Pitfalls | Input validation = primary injection defense (wrong) | WAF blocks all attacks (wrong) | OCSP signed by CA (wrong) |
| 13 | Study Resources | U5 Review Packet | OWASP cheat sheet | ModSecurity rules |
| 14 | Homework | Complete U5 packet | Write parameterized query examples |

---

## Deck 7: FRQ Practice — Device Security Analysis (3 sessions)

**Slides**: 15 each | **Time**: 50 min each | **Dates**: Apr 20, 22, 27

### Session 1 (Apr 20) — FRQ Set A: Linux Web Server
| Slide | Title | Content |
|-------|-------|---------|
| 1 | FRQ Format Review | 5 parts (A-E), 14 pts, 50 min | Source documents | Annotation strategy |
| 2 | Set A Scenario | Compromised web server | 5 sources: firewall, netstat, ps, auth.log, audit.rules |
| 3 | Part A Walkthrough | Suspicious connection ID | Netstat reading | Firewall policy violation |
| 4 | Part B Walkthrough | Process IOCs | /tmp hidden dir | Root process | Beaconing |
| 5 | Part C Walkthrough | Auth log correlation | Sudo escalation | MITRE T1548.003 |
| 6 | Part D Walkthrough | Firewall fixes | OUTPUT DROP + allowlist | RFC1918 block | Trade-offs |
| 7 | Part E Walkthrough | Audit rule trigger | execve uid=0 | Would it fire? |
| 8 | Scoring Demo | Annotated sample response | Point mapping | Partial credit examples |
| 9 | Student Practice | 15 min: Write Part A-B | Peer review with rubric |
| 10 | Debrief | Common misses | Time management | Key terms for points |

### Session 2 (Apr 22) — FRQ Set B: Windows Workstation
| Slide | Title | Content |
|-------|-------|---------|
| 1 | Set B Scenario | PowerShell encoded command | 5 sources: firewall, netstat, tasklist, security log, AppLocker |
| 2-8 | Parts A-E Walkthrough | Netstat anomalies | Base64 PowerShell | AppLocker gap | Firewall mods | SeDebugPrivilege |
| 9 | Student Practice | Write Part C-D | Peer review |
| 10 | Debrief | PowerShell obfuscation | AppLocker script vs binary rules |

### Session 3 (Apr 27) — FRQ Set C: Kubernetes Node
| Slide | Title | Content |
|-------|-------|---------|
| 1 | Set C Scenario | Privileged pod escape | 5 sources: NetworkPolicy, crictl, pod YAML, audit.log, RBAC |
| 2-8 | Parts A-E Walkthrough | Pod misconfigs | NetworkPolicy egress | nsenter escape | RBAC escalation | PSA replacement |
| 9 | Student Practice | Write Part A, E | Full timed practice (25 min) |
| 10 | Debrief | Kubernetes security | PSA vs PSP | Least privilege SA |

---

## Deck 8: CLI Fluency Check (1 session)

**Slides**: 10 | **Time**: 50 min | **Date**: Apr 28

| Slide | Title | Content |
|-------|-------|---------|
| 1 | CLI Fluency Overview | 10 tasks, 50 min | Codespaces | Automated grader | Practical skills for FRQ |
| 2 | Environment Setup | Codespaces (primary) | Replit/Gitpod (fallback) | Docker-in-Docker | Pre-installed tools |
| 3 | Task Categories | Network | Traffic | Logs | Forensics | Crypto | Hash | Process | Script | Container | Git |
| 4 | Task 1-2 Demo | nmap + tshark | Live demo in Codespace |
| 5 | Task 3-4 Demo | jq log parsing + find/file forensics |
| 6 | Task 5-6 Demo | openssl keys + gpg signatures |
| 7 | Task 7-8 Demo | ss/lsof processes + bash one-liner |
| 8 | Task 9-10 Demo | crictl containers + trufflehog secrets |
| 9 | Grader Walkthrough | CLI-Check-Grader.py | CSV output | Classroom submission |
| 10 | Live Assessment | Students run grader | Teacher monitors | Results auto-submitted |

---

## Deck 9: Full Mock Exam & Final Tips (1 session)

**Slides**: 15 | **Time**: 50 min | **Date**: May 2

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Mock Exam | 30 MCQ (40 min) + 1 FRQ (25 min) | Simulated conditions |
| 2 | MCQ Review | Top 10 missed | Distractor analysis | LO mapping |
| 3 | FRQ Review | Sample response scoring | Peer grading with rubric |
| 4 | Final Week Plan | Mon: Weak unit review | Tue: FRQ re-practice | Wed: Rest/mental prep |
| 5 | Test Day Checklist | Sleep | Breakfast | Pencils | Calculator | ID | Water |
| 6 | Mental Game | Anxiety management | Time boxing | Flag & return | Educated guessing |
| 7 | Multi-Select Reminder | Treat each option independently | No "all of above" | Usually 2-3 correct |
| 8 | FRQ Key Terms | "Identify" = name it | "Explain" = why/how | "Describe" = details | "Propose" = solution |
| 9 | Common FRQ Errors | Vague answers | Missing source citation | Wrong MITRE ID | No trade-off |
| 10 | Score Prediction | Raw → Composite → 1-5 | Historical curves | Target: 5 |
| 11 | Post-Exam | Portfolio Unit 6 starts May 6 | Capstone presentations Mar 31 | Celebrate! |
| 12 | Q&A | Last questions | Logistics confirmation |
| 13 | Encouragement | You've prepared | Trust your training | Good luck! |
| 14 | Contact Info | Office hours | Email | Discord/Slack |
| 15 | Class Photo / Tradition | ICA Cybersecurity Class of 2027 |

---

## Slide Deck Production Notes

| Deck | File Name | Format | Location |
|------|-----------|--------|----------|
| 1 | `00-Course-Overview-Exam-Strategy` | Google Slides | qsec_ap_review/slide-decks/ |
| 2 | `01-Unit1-Foundations` | Google Slides | qsec_ap_review/slide-decks/ |
| 3 | `02-Unit2-Network` | Google Slides | qsec_ap_review/slide-decks/ |
| 4 | `03-Unit3-Crypto` | Google Slides | qsec_ap_review/slide-decks/ |
| 5 | `04-Unit4-System` | Google Slides | qsec_ap_review/slide-decks/ |
| 6 | `05-Unit5-Application` | Google Slides | qsec_ap_review/slide-decks/ |
| 7 | `06-FRQ-Practice-SetA` | Google Slides | qsec_ap_review/slide-decks/ |
| 8 | `06-FRQ-Practice-SetB` | Google Slides | qsec_ap_review/slide-decks/ |
| 9 | `06-FRQ-Practice-SetC` | Google Slides | qsec_ap_review/slide-decks/ |
| 10 | `07-CLI-Fluency` | Google Slides | qsec_ap_review/slide-decks/ |
| 11 | `08-Mock-Exam-Final-Tips` | Google Slides | qsec_ap_review/slide-decks/ |

**Template**: ICA branded (navy + gold, red CTA) — use `ivy_collegiate_webapplication` theme
**Speaker Notes**: Detailed scripts in each slide for substitute teacher coverage
**Accessibility**: Alt text for diagrams, high contrast, screen reader tested

---

*Slide Deck Outlines — Upload to qsec_ap_review/slide-decks/*