# Unit 5 — Securing Applications and Data: Lesson Plans

**~30 periods (Periods 77–106) | CED Topics 5.1–5.6 | Skills: Analyze Risk (1.A–1.C) · Mitigate Risk (2.A–2.D) · Detect Attacks (3.A–3.D) · Collaborate (4.A–4.D)**

*Includes Capstone (6 periods) + AP Exam Prep (5 periods)*

**🇹🇼 Taiwan Threat Brief format (recurring):** The unit opener (Lesson 5.1) starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to application/data security. Keeps threat awareness local and current across the unit.

**🧩 Saturday CTF Alignment:** Two Saturday CTF sessions frame the second half of Unit 5 — **Feb 27 (SESSION 11: Capstone challenge build begins)** and **Mar 6 (SESSION 12: Capstone challenge work)** . Students design and build their own CTF challenge, applying SDLC principles (5.5), secure coding (5.5), and the detection/protection patterns studied in 5.6. The capstone challenge is their most portfolio-worthy artifact — it should be a multi-step web or application challenge reflecting OWASP Top 10 concepts from Juice Shop (Sessions 8-9). Deliverable: challenge files + solution writeup, due before AP exam prep begins.

---

## Lesson 5.1 — SQL Injection

**Period:** 75  |  **LOs:** 1.A, 1.B

**Materials:** Slides, whiteboard, SQL injection demo (teacher-led in browser). **Key Vocabulary:** Application vulnerability, SQL injection (SQLi), Input validation, Input sanitization

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A login box accepts ' OR 1=1; -- and suddenly you're the admin. How?" |
| 15 min | **Direct instruction:** What SQLi is, how it exploits unsanitized input. Three types: in-band (error-based, UNION), blind (boolean, time-based), out-of-band. Real cases: Heartland Payment Systems (2008), Taiwan e-commerce breach examples. **Cross-ref (forward):** not all application-data vulnerabilities are injection — Lesson 5.8's Cold Card hack shows a broken RNG = predictable keys (data vulnerability via weak randomness). |
| 15 min | **Demo — live SQLi:** Teacher opens a deliberately vulnerable test page (e.g., DVWA or a local PHP script). Demonstrates: `' OR 1=1 --` to bypass login, `UNION SELECT` to extract data, blind injection via timing. Students watch and predict output. |
| 10 min | **Activity — query reconstruction:** Given a vulnerable SQL query and the resulting output, students reconstruct what input was entered. **🇹🇼 PIPL add-on (3 min):** "Your startup's web app leaks 10K user PII records via SQLi. Taiwan's Personal Data Protection Law (PIPL) requires: (1) notify affected individuals, (2) notify the competent authority within X hours, (3) investigate and report corrective measures. You're the CISO — walk through the 24-hour timeline of what you'd do." Students write a quick 3-bullet response. (Maps to: regulatory requirements, incident response planning — CED Skill 1.C.) |
| 5 min | **Exit ticket:** "What's the difference between in-band and blind SQL injection?" |

---

## Lesson 5.2 — Cross-Site Scripting (XSS) & Buffer Overflow

**Period:** 76  |  **LOs:** 1.A, 1.B

**Materials:** Slides, XSS demo page (teacher-led), buffer overflow animation. **Key Vocabulary:** Cross-site scripting (XSS), Stored/reflected/DOM-based XSS, Cross-site request forgery (CSRF), Buffer overflow, Input validation

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "A comment box on a forum runs JavaScript in your browser. What could the attacker do?" |
| 15 min | **Direct instruction — XSS:** Three types — stored (persistent on server), reflected (in URL/request), DOM-based (client-side only). Attack goals: session hijacking, defacement, credential theft, keylogging. Real examples: Samy worm (MySpace, 2005), British Airways (2018). |
| 10 min | **Direct instruction — CSRF & Buffer overflow:** CSRF — trick an authenticated user into unintended actions (e.g., a hidden form submit that transfers funds or changes email using their existing session cookie); defense = anti-CSRF tokens, SameSite cookies, re-auth for sensitive actions. Buffer overflow — writing past buffer bounds to overwrite return addresses or inject shellcode. Input validation (length checks) as the primary defense. Real examples: Morris Worm (1988), Heartbleed (2014). |
| 15 min | **Activity — XSS payload identification:** Given 5 code snippets, classify as Stored/Reflected/DOM-based XSS or not vulnerable. Identify the vulnerable line. |
| 5 min | **Exit ticket:** "Why is stored XSS considered more dangerous than reflected XSS?" |

---

## Lesson 5.3 — Directory Traversal & File Inclusion

**Period:** 77  |  **LOs:** 1.A, 1.B

**Materials:** Slides, file path diagrams, demo snippets. **Key Vocabulary:** Directory traversal, Local File Inclusion (LFI), Remote File Inclusion (RFI), Input sanitization

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "What happens if a URL contains `../../../../etc/passwd`?" |
| 15 min | **Direct instruction — Directory traversal:** Path traversal basics — `../` sequences, URL encoding bypasses (`%2e%2e%2f`), null byte injection (`file.php%00.txt`). What attackers read: config files, source code, shadow files. |
| 10 min | **Direct instruction — LFI/RFI:** Local File Inclusion (read server files via `include()` with no sanitization) vs Remote File Inclusion (attacker hosts malicious script, included by the server). Conditions for RFI — `allow_url_include=On`. |
| 15 min | **Activity — attack identification:** Given 5 URL examples, identify: directory traversal, LFI, RFI, or benign. For each, describe what the attacker gains. |
| 5 min | **Exit ticket:** "Name two defenses that prevent directory traversal attacks." |

---

## Lesson 5.4 — Lab: OWASP Juice Shop — Exploit SQLi & XSS

**Period:** 78  |  **LOs:** 1.A, 3.D

**Materials:** Chromebooks, OWASP Juice Shop (teacher-hosted on Docker or demo site). **Key Vocabulary:** SQL injection, Stored XSS, Path traversal, Exploit, Payload

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Navigate to Juice Shop URL. Explain: this is a deliberately vulnerable web app — everything you do is legal and contained. Safety rules: no attacking other students or external sites. |
| 20 min | **Guided lab — SQLi:** Walk through the SQL injection challenges: (a) Log in with any SQL injection — `' OR 1=1; --`, (b) Retrieve a list of registered users via UNION injection, (c) Blind SQLi — determine a database name character by character. |
| 15 min | **Guided lab — XSS:** Walk through XSS challenges: (a) Perform a reflected XSS in the search bar, (b) Perform a stored XSS in the product review section, (c) Steal a cookie via XSS (simulated). |
| 5 min | **Exit ticket:** "Which was harder — SQLi or XSS? Why?" |

**Lab spec:** Teacher provides Juice Shop URL (localhost or demo.juice-sh.op). Chromebook-compatible via browser. No local install needed.

---

## Lesson 5.5 — Managerial Controls: Security Policies & Data Classification

**Period:** 79  |  **LOs:** 2.A, 2.C

**Materials:** Slides, policy template handouts, sample data classification labels. **Key Vocabulary:** Data at rest, Data in transit, Data in use, Data classification, PII, PHI, PCI, Public/Internal/Confidential/Restricted, Least privilege

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Your school stores student records, grades, medical info, and CCTV footage. Who can access what — and how do you decide?" |
| 15 min | **Direct instruction:** Managerial controls — policies, procedures, standards, guidelines. Key policies: acceptable use, data classification, incident response, business continuity, disaster recovery. Data classification levels (Public, Internal, Confidential, Restricted / or Taiwan's 3-level system). |
| 15 min | **Activity — data classification:** Given a list of 12 data types (e.g., student transcripts, cafeteria menu, payroll, security camera footage, emergency contacts), classify each and justify. Identify which regulations apply (Taiwan AI Fundamental Act, PIPEDA-style data protection). |
| 10 min | **Activity — policy gap analysis:** Given a school's one-paragraph "security policy," identify what's missing (roles, enforcement, review cycle, exceptions process). |
| 5 min | **Exit ticket:** "What's the difference between a policy and a procedure?" |

---

## Lesson 5.6 — Access Controls: RBAC, DAC, MAC, RuBAC & PoLP

**Period:** 80  |  **LOs:** 2.A, 2.B

**Materials:** Slides, role matrix handouts, scenario cards. **Key Vocabulary:** RBAC, RuBAC, DAC, MAC, ACL, Permissions, Role, Rule

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Should a janitor have access to student grades? Should a teacher have access to payroll?" |
| 15 min | **Direct instruction:** Four access control models — DAC (owner sets permissions, discretionary), MAC (system-enforced labels, mandatory), RBAC (roles inherit permissions), RuBAC (rules/conditions, e.g., time-based or IP-based). Principle of Least Privilege (PoLP). Real examples: DAC = NTFS permissions, MAC = SELinux/classified docs, RBAC = Active Directory groups, RuBAC = firewall ACLs, after-hours payroll access. |
| 15 min | **Activity — RBAC design:** For a school's grade management system, define 5 roles (Student, Teacher, Admin, Counselor, Principal) and assign permissions to: view grades, edit grades, view student profiles, edit profiles, view attendance, run reports. Check for privilege creep. |
| 10 min | **Activity — scenario analysis:** Given 3 breach scenarios caused by misconfigured access controls, identify: which model was misused, what should the permissions have been? |
| 5 min | **Exit ticket:** "Why is RBAC preferred over DAC in most enterprise settings?" |

---

## Lesson 5.7 — Lab: Configure Access Controls — RBAC Matrix & Linux chmod

**Period:** 81  |  **LOs:** 2.D

**Materials:** Chromebooks, RBAC simulation tool (Google Sheets template or simple web app), Linux terminal access (WSL/Docker per student or teacher demo). **Key Vocabulary:** chmod, chown, chgrp, rwx, Numeric mode (750, 640, 755), Symbolic mode (u+x, go-rw), Owner, Group, Others

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Introduce the RBAC matrix tool. Roles, permissions, and user-role mappings are configured in a structured table. |
| 15 min | **Lab — RBAC configuration:** Students given a scenario (healthcare clinic data system). Tasks: (a) Define 6 roles — Doctor, Nurse, Receptionist, Lab Tech, Billing, Administrator. (b) Assign 12 permissions per role (view patient records, edit records, order tests, view billing, edit billing, etc.). (c) Assign 8 users to roles. (d) Test: Can Nurse view billing data? Can Receptionist edit medical records? Identify violations. (e) Demonstrate PoLP — reduce excessive permissions. |
| 20 min | **Lab — Linux access controls (chmod):** **AP Exam FRQ Critical — CED Sample FRQ Part C tests this directly.** Level 1 — Interpret `ls -l` output to octal: rwxr-x--- = 750, rw-r--r-- = 644. Level 2 — Configure: "Owner rwx, group rx, others nothing" → `chmod 750`; "Add execute for owner" → `chmod u+x file`. Level 3 — FRQ-style scenario: web server `/var/www/html` = `chmod 755`, config `/etc/webapp/config.ini` = `chmod 640`. Level 4 — Extension: `chown`, `chgrp`, `getfacl`/`setfacl` for granular permissions. |
| 5 min | **Exit ticket — chmod quiz (3 Qs):** (1) What does `chmod 644` do? (2) rwxr----- in octal? (3) Make a script executable by all. |

**Lab spec:** Google Sheets template with named ranges and data validation, or a simple HTML/JS RBAC simulator. No accounts needed — template is provided as a link (view-only, students make a copy). chmod portion: Linux VM/WSL/Docker per student, or teacher-led demo with shared accounts on the Mac Mini terminal (same setup as Lessons 5.9/5.12).

---

## Lesson 5.8 — Symmetric Cryptography

**Period:** 82  |  **LOs:** 2.A

**Materials:** Slides, whiteboard, encryption visualizer (online or paper cipher wheels), Cold Card hack video (https://youtu.be/2X2V3xv_jik, 5:10), Cold Card Case Study worksheet (GDrive: Unit 5 folder / Worksheets)

| Time | Activity |
|------|----------|
| 5 min | **Hook — current events case study:** Play the Cold Card hardware wallet hack video (Fireship, 5:10; skip last ~60s sponsor ad). "The 'safest' Bitcoin wallet was drained — 1,600+ BTC — with no malware and no phishing. The bug was a broken random number generator." |
| 15 min | **Direct instruction:** Symmetric encryption — same key for encrypt and decrypt. Stream ciphers (RC4, ChaCha20) vs block ciphers (AES, DES/3DES). Modes: ECB (bad — leaks patterns), CBC (IV + chaining), GCM (authenticated encryption). Key length matters: AES-128 vs AES-256. **Bridge to the hook:** every key must be generated from a random source — a weak RNG means predictable keys. Hardware TRNG vs software PRNG. |
| 10 min | **Activity — cipher mode comparison:** Show encrypted images of the same bitmap in ECB mode vs CBC mode. Students observe: ECB leaks the penguin silhouette, CBC looks random. Discuss: why does this matter for real data? |
| 10 min | **Activity — Cold Card case study (worksheet):** Students complete the Cold Card Case Study worksheet — vocabulary (hardware wallet, seed phrase, entropy, RNG/TRNG, mempool), 6 comprehension questions, mempool rescue discussion. Focus: why a weak RNG = weak keys, and why patching can't fix already-compromised keys (migration is the only fix). |
| 5 min | **Exit ticket:** "What's one weakness of symmetric encryption — and how does key length help?" (Optional add: "Why does random-number quality matter for encryption?") |

---

## Lesson 5.9 — Lab: Encrypt & Decrypt Files with OpenSSL

**Period:** 83  |  **LOs:** 2.D

**Materials:** Chromebooks (SSH to teacher's Mac Mini or use a browser-based terminal emulator)

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Teacher demonstrates basic OpenSSL syntax. Students connect to a shared terminal or watch teacher demo and complete a worksheet with expected outputs. |
| 25 min | **Lab — OpenSSL encryption:** Tasks: (a) Create a plaintext file with a secret message. (b) Encrypt with AES-256-CBC: `openssl enc -aes-256-cbc -salt -pbkdf2 -in plain.txt -out cipher.enc`. (c) Decrypt and verify. (d) Change one bit in the ciphertext — what happens? (e) Encrypt with DES and compare output length. (f) Encrypt with no salt — what pattern emerges? (g) Answer questions on worksheet about key derivation, IV, salt, and padding. |
| 10 min | **Discussion:** What happens if you lose the key? What if an attacker gets the encrypted file — what do they still need? Why does macOS use FileVault (AES-XTS) instead of basic AES-CBC? **Tie-in:** what if the key itself was weak because the random generator was broken? (Cold Card hack from Lesson 5.8 — patching the software can't fix keys that were already generated badly; you must migrate to new keys.) |
| 5 min | **Exit ticket:** "What is the purpose of the salt in OpenSSL encryption?" |

**Lab spec:** Teacher's Mac Mini terminal (demo + shared accounts) OR use a browser-based web terminal (e.g., Jupyter terminal). Students submit completed worksheet with command outputs pasted in.

---

## Lesson 5.10 — Asymmetric Cryptography

**Period:** 84  |  **LOs:** 2.A

**Materials:** Slides, whiteboard, Diffie-Hellman color-mixing analogy (visual aid)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Two people who've never met want to share a secret — over a public channel where everyone is listening. How?" |
| 15 min | **Direct instruction:** Asymmetric (public-key) cryptography — public key encrypts, private key decrypts. RSA: based on prime factorization difficulty. ECC: based on elliptic curve discrete logarithm — stronger per bit. Diffie-Hellman key exchange. Key sizes: RSA-2048 vs ECC-256 (equivalent security). |
| 15 min | **Activity — DH color-mixing demo:** Walk through the paint-color analogy for Diffie-Hellman (common color + private color → mixed color → shared secret). Students trace the steps: Alice's private color + Bob's mixed color = Bob's private color + Alice's mixed color = shared secret. |
| 10 min | **Activity — key size comparison:** Given a table of RSA vs ECC key sizes at equivalent security levels, answer: (a) Why does ECC use smaller keys? (b) Why would a mobile device prefer ECC? (c) Which is more quantum-vulnerable? |
| 5 min | **Exit ticket:** "What problem does asymmetric cryptography solve that symmetric cannot?" |

---

## Lesson 5.11 — PKI & Digital Signatures

**Period:** 85  |  **LOs:** 2.A, 2.B

**Materials:** Slides, sample TLS certificate (from any HTTPS site), certificate chain diagram

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "When you visit `https://bankofamerica.com`, how does your browser know it's really them?" |
| 15 min | **Direct instruction:** PKI components — Certificate Authority (CA), registration authority, certificate revocation list (CRL), OCSP. X.509 certificate fields (subject, issuer, validity, public key, signature). Chain of trust — root CA → intermediate CA → server cert. TLS handshake simplified: cert exchange, key exchange (RSA or Diffie-Hellman), session key, encrypted tunnel. |
| 15 min | **Activity — certificate inspection:** Students open Chrome DevTools → Security → View certificate for 3 different sites. Record: issuer, validity period, key algorithm, signature algorithm. Compare: a major bank vs a small blog vs an expired/invalid cert. |
| 10 min | **Activity — digital signature scenario:** "You receive a software update signed by Microsoft. How does your computer verify it? Walk through: hash, encrypt with private key, decrypt with public key, compare hashes." |
| 5 min | **Exit ticket:** "What happens when your browser encounters an untrusted or expired certificate?" |

---

## Lesson 5.12 — Lab: Create & Verify Digital Signatures

**Period:** 86  |  **LOs:** 2.D

**Materials:** Chromebooks (SSH to teacher's Mac Mini or demo terminal)

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Recap: signing is encrypt-with-private-key, verification is decrypt-with-public-key. Commands for today. |
| 25 min | **Lab — Digital signatures with OpenSSL:** Tasks: (a) Generate an RSA key pair: `openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048`. (b) Extract public key: `openssl rsa -pubout -in private.pem -out public.pem`. (c) Create a document and hash it: `openssl dgst -sha256 -sign private.pem -out doc.sig document.txt`. (d) Verify: `openssl dgst -sha256 -verify public.pem -signature doc.sig document.txt`. (e) Tamper with the document — what happens on verification? (f) Generate an ECC key pair and repeat. Compare RSA vs ECC signature sizes. |
| 10 min | **Discussion:** Real applications — code signing (authenticode), document signing (Adobe Sign), software update verification. What if the private key is leaked? |
| 5 min | **Exit ticket:** "Why does a digital signature prove both authenticity AND integrity?" |

**Lab spec:** Teacher's terminal or web terminal session. Students submit screenshots or pasted terminal output.

---

## Lesson 5.13 — Protecting Applications: Secure Coding

**Period:** 87  |  **LOs:** 2.A, 2.D

**Materials:** Slides, intentionally vulnerable code samples (printed or displayed)

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "One line of code — `SELECT * FROM users WHERE id = '` + userInput + `'` — can lose millions of records. What's the fix?" |
| 15 min | **Direct instruction:** Secure coding principles — input validation (allowlist vs denylist, type checking, length limits), output encoding (HTML entity encoding, URL encoding), parameterized queries (prepared statements), proper error handling (don't leak stack traces), defense in depth for code. |
| 20 min | **Lab — vulnerable code review:** Given 5 code snippets (Python/JS/PHP), each containing a vulnerability: (a) Identify the vulnerability type (SQLi, XSS, command injection, path traversal, insecure deserialization). (b) Rewrite the vulnerable line securely. (c) For each, identify which layer should have caught it (WAF, input validation, output encoding, DB layer). |
| 5 min | **Exit ticket:** "Why is input validation alone not enough to prevent XSS?" |

**Lab spec:** Printed or displayed code snippets. No running environment needed.

---

## Lesson 5.14 — WAF & Runtime Protection

**Period:** 88  |  **LOs:** 2.A, 2.B

**Materials:** Slides, WAF rule examples, WAF block page screenshots

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "What if you could put a security guard in front of your web app that watched every request?" |
| 15 min | **Direct instruction:** WAF (Web Application Firewall) — sits between user and app, inspects HTTP traffic. Modes: blocking, detection, learning. Rule types: SQLi patterns, XSS patterns, rate limiting, IP reputation. OWASP ModSecurity Core Rule Set. RASP (Runtime Application Self-Protection) — embedded in the app runtime, understands app logic, can block from inside. WAF vs RASP: network layer vs application layer, signature vs behavior. |
| 15 min | **Activity — WAF rule design:** Given 3 attack patterns (SQLi UNION injection, reflected XSS in search, directory traversal with `../`), write a simple WAF rule (pseudo-code) that detects and blocks each. Consider: what about false positives? |
| 10 min | **Case study — WAF bypass:** Show real examples of WAF bypass techniques (encoding, case variation, comment injection, parameter pollution). Discuss: why defense-in-depth still matters. **🇹🇼 Semiconductor OHT spotlight (3 min):** "A TSMC 300mm fab uses an OHT (overhead hoist transport) system — automated carriers move wafer lots across the fab ceiling on monorails. The OHT control server is a web application: receives move commands, tracks carrier locations, logs every transfer. Without WAF + network segmentation, a SQLi in the OHT management dashboard could let an attacker redirect lots to the wrong tool or halt production. Question: if you're securing the OHT web app, what WAF rules do you write, and what segmentation separates the fab-floor network from the office network?" (Maps to: WAF rule design, defense-in-depth, OT/IT segmentation — CED Skills 2.A, 2.B.) |
| 5 min | **Exit ticket:** "What's one advantage RASP has over WAF?" |

---

## Lesson 5.15 — Lab: Configure WAF Rules

**Period:** 89  |  **LOs:** 2.D

**Materials:** Chromebooks, ModSecurity dashboard screenshots/worksheet, or teacher demo

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Teacher shows the WAF configuration interface (or prepared screenshots). Explain rule structure: SecRule VARIABLES "PATTERN" "ACTION". |
| 25 min | **Lab — WAF rule configuration:** Students complete a worksheet with the following tasks: (a) Given a ModSecurity configuration file, identify 3 existing rules and explain what each blocks. (b) Write a new rule to block requests containing `' OR '1'='1` in the URL query string. (c) Write a rate-limiting rule allowing max 100 requests/min per IP. (d) Write a rule to block requests to `/admin` from non-local IPs. (e) Test given request samples against your rules — would they be blocked or allowed? (f) Identify a false positive scenario for each rule. |
| 10 min | **Discussion:** WAF in the real world — Cloudflare, AWS WAF, Azure WAF, ModSecurity. Challenges: false positives, performance impact, encrypted traffic (TLS inspection). |
| 5 min | **Exit ticket:** "Why might a WAF rule against ' OR 1=1-- be bypassed?" |

**Lab spec:** Screenshot-based or worksheet-based due to Chromebook constraints. Teacher demo of actual rule deployment on Mac Mini. Students submit completed rule sets.

---

## Lesson 5.16 — Detecting Attacks on Data & Applications

**Period:** 90  |  **LOs:** 3.A, 3.B

**Materials:** Slides, sample log entries (printed), anomaly detection scenario cards

| Time | Activity |
|------|----------|
| 5 min | **Hook:** "Every request to a web server leaves a trace. If you know what normal looks like, can you spot the attack?" **🇹🇼 Taiwan context:** The same log analysis techniques caught the 2023 attack on a Taiwan e-commerce platform — attackers probed with SQLi payloads for 2 hours before finding a vulnerable parameter and exfiltrating customer PII. (Source: publicly available breach report / TWNCERT advisory.) |
| 15 min | **Direct instruction:** Web server logs — Apache combined log format, status codes (200, 301, 401, 403, 404, 500), what each reveals. DB audit logs — who queried what, when. Anomaly detection — baseline + deviation (volume spikes, unusual hours, unexpected status code ratios, geolocation mismatches). |
| 20 min | **Activity — log analysis:** Given 50 lines of an Apache access log, find: (a) SQL injection attempts (patterns: `'`, `UNION SELECT`, `--` in URL). (b) Directory traversal attempts (`../`, `%2e%2e`). (c) Brute-force login attempts (many 401s from same IP). (d) Reconnaissance (many 404s probing paths). (e) Unusual user-agent strings. Annotate each finding. |
| 5 min | **Exit ticket:** "What's one indicator of SQL injection you can find in a web server log?" |

---

## Lesson 5.17 — Lab: Analyze Web Server Logs for Attack Patterns

**Period:** 91  |  **LOs:** 3.D, 4.D

**Materials:** Chromebooks, sample access.log CSV (provided by teacher)

| Time | Activity |
|------|----------|
| 5 min | **Setup:** Distribute the log file and explain the format. Demonstrate a few analysis techniques in Google Sheets (filter, sort, COUNTIF, conditional formatting). |
| 30 min | **Lab — log forensics:** Given a 500+ line simulated web server log, identify and document: (a) SQL injection attempts — count them, list the attacker IPs, and identify which URL parameters were targeted. (b) XSS probing — find reflected XSS attempts in search parameters. (c) Directory traversal — trace an attacker's path through your file system. (d) Brute-force timeline — when did the attack start, end, how many attempts, was any successful? (e) Data exfiltration — was large data accessed or transferred? (f) Write a one-paragraph incident summary describing the attack. |
| 10 min | **Debrief:** Compare findings in pairs. Did everyone identify the same attack timeline? What's the difference between a real attack and a false positive? |
| 5 min | **Exit ticket:** "What's the most important log entry you found — and why?" |

**Lab spec:** CSV file with ~500 web server log entries. Students use Google Sheets for analysis. File provided as a Google Sheet or downloadable CSV.

---

## Lessons 5.18-5.22 — Capstone: Taiwan Critical Infrastructure Defense

**Periods:** 92-97  |  **LOs:** 1.B, 1.C, 1.D, 2.B, 2.C, 2.D, 3.B, 4.A, 4.B, 4.C, 4.D

**Materials:** Scenario packets, Google Slides, web research access, Taiwan AI Fundamental Act (summary document)

**Capstone scenario:** "You are a cybersecurity team hired by a Taiwan critical infrastructure operator. Select one sector — semiconductor fab, power grid, water treatment, airport, hospital, or telecom. A state-sponsored APT group (choose from APT40, APT41, or a China-linked group) has been observed conducting reconnaissance against your sector. Your team must: (1) model the threat, (2) assess risk, (3) design a layered defensive architecture, (4) map controls to Taiwan's AI Fundamental Act, and (5) present to the 'board of directors.'"

| Time | Day 1 (Period 92) — Launch & Research | Day 2 (Period 93) — Threat Modeling | Day 3 (Period 94) — Defensive Architecture |
|------|-------|-------|-------|
| 5 min | Launch scenario. Form teams of 3-4. | Quick review: APT group profiles | Recap: defense-in-depth layers |
| 25 min | **Scoping:** Each team selects a sector and APT group. Research: (a) Sector's critical functions, (b) Known attacks against similar sectors, (c) Potential impact of a breach, (d) Regulatory requirements. Begin filling out the threat model template. | **Threat modeling exercise:** Using STRIDE (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege), map threats for their sector. Create an attack tree — what does the APT need to do at each stage? Build a risk register: 10+ assets, threats, likelihood, impact, risk score. | **Design phase:** Draw a network architecture (layered). Must include: (a) Perimeter controls — WAF, firewall, IDS/IPS. (b) Application controls — input validation, RBAC, encryption. (c) Data controls — classification, access policies, encryption at rest. (d) Detection — logging, SIEM, anomaly alerts. Document each control and which threat it mitigates. |
| 10 min | Sector assignment. Team roles defined (lead, researcher, architect, presenter). | Attack tree review with teacher | Architecture check-in — teacher reviews each team's design |
| 5 min | Check-in: sector selected, research started | Exit: one key threat identified | Exit: one control gap you need to address |

| Time | Day 4 (Period 95) — Compliance & Finalization | Day 5 (Period 96) — Work Day | Day 6 (Period 97) — Presentations |
|------|-------|-------|-------|
| 5 min | Recap: Taiwan AI Fundamental Act overview | Work day goals — finalize slides, rehearse | Setup: presentation order |
| 25 min | **Compliance mapping:** Using the Taiwan AI Fundamental Act summary, map each control in your architecture to: (a) relevant articles/requirements, (b) the data classification level it protects, (c) any reporting/audit requirements. Document: is your design fully compliant? What gaps remain? Prepare the compliance section of the presentation. | **Finalization:** Teams finalize slides, complete the architecture diagram, and rehearse their 7-minute presentation. Teacher available for questions. Peer review: swap with another team — review each other's compliance mapping. | **Presentations:** 7 min per team + 3 min Q&A. Cover: (a) Sector + threat profile, (b) Attack tree / threat model, (c) Layered defensive architecture, (d) Compliance with Taiwan AI Fundamental Act, (e) Budget estimates (NT$5M cap). |
| 10 min | Compliance check with teacher | Rehearsals | Peer judging — each team scores others on: threat analysis, defensibility, compliance, presentation quality. |
| 5 min | Exit: one compliance gap you discovered | Exit: one slide you're most proud of | Debrief + awards: most defensible design, best threat analysis, most cost-effective |

**Deliverable:** Google Slides deck (8-10 slides) covering: sector overview, APT profile, attack tree, risk register, network architecture diagram, control selections with costs, compliance mapping, budget summary.

---

## Lesson 5.23 — Unit 5 Review

**Period:** 98  |  **LOs:** All Unit 5

**Materials:** Kahoot / Quizizz, scenario review cards, sample FRQ handouts

| Time | Activity |
|------|----------|
| 15 min | **Kahoot review:** 20 questions covering all six CED topics — SQLi vs XSS identification, access control model scenarios, symmetric vs asymmetric cryptography, PKI chain of trust, WAF vs RASP, log anomaly detection. |
| 15 min | **Scenario FRQ walkthrough:** "A Taiwan e-commerce site was defaced. The web server logs show: (a) `' OR 1=1; --` in the login field, (b) a successful login at 2:03 AM from Russia, (c) `../../etc/passwd` in a URL parameter, (d) a spike in 404s for `/admin` paths. Analyze: what attacks occurred, what was the kill chain, what controls should have prevented each, what detection gaps exist?" |
| 10 min | **Study guide cross-check:** Students compare their notes against a provided Unit 5 study guide. Mark gaps. |
| 5 min | **Q&A:** Open floor for final questions. Review test format. |

---

## Lesson 5.24 — Unit 5 Test

**Period:** 99  |  **LOs:** All Unit 5

**Materials:** Test papers (or Bluebook practice), answer key

| Time | Activity |
|------|----------|
| 40 min | **Test:** 20 multiple-choice (2 min each) + 1 FRQ (10 min). Covers: application vulnerability identification (SQLi, XSS, buffer overflow, directory traversal), access control models (RBAC/DAC/MAC), cryptography concepts (symmetric, asymmetric, hashing), PKI and digital signatures, WAF and secure coding principles, log analysis and anomaly detection. |
| 5 min | Early finishers: Read AP exam overview. |

**Assessment spec:** 20 MC + 1 FRQ = 50 min with buffer.

---

## Lessons 5.25-5.29 — AP Exam Preparation

**Periods:** 100-104  |  **LOs:** All course skills

---

### Lesson 5.25 — AP Exam Prep: MC Strategies

**Period:** 100  |  **LOs:** All

**Materials:** Timed MC practice set (20 questions), Bluebook or printed

| Time | Activity |
|------|----------|
| 5 min | **Strategy overview:** AP Cybersecurity MC format — ~40 questions, ~60 min. Three types: concept recall, scenario analysis, code/log interpretation. Elimination strategy. Pacing: ~1.5 min per question. |
| 25 min | **Timed MC practice:** 20 questions covering all units. Simulated exam conditions — no talking, time limit tracked. |
| 10 min | **Review:** Go over answers. For each missed question: (a) why was the wrong answer appealing? (b) what was the key clue? (c) how could you eliminate distractors? |
| 5 min | **Exit ticket:** "What's your biggest takeaway from the practice set — a pattern, a weakness, a strategy?" |

---

### Lesson 5.26 — AP Exam Prep: FRQ Strategies

**Period:** 101  |  **LOs:** All

**Materials:** Sample FRQs with rubrics, highlighters

| Time | Activity |
|------|----------|
| 5 min | **FRQ overview:** 3-4 free-response questions, ~60 min. Types: scenario analysis, network/log analysis, policy/control design, layered defense diagram. Key to success: address every bullet, use specific terminology, show your reasoning. |
| 20 min | **Sample FRQ walkthrough:** Teacher works through a sample FRQ step by step — reading the prompt, identifying the skill being tested, structuring the response, checking the rubric. Students annotate a model response. |
| 15 min | **Rubric grading exercise:** Students grade 3 anonymized past responses using the official rubric. Discuss: what did the A+ response do that the C response missed? |
| 5 min | **Exit ticket:** "One thing you'll do differently on FRQs after today." |

---

### Lesson 5.27 — Full-Length Practice Test

**Period:** 102  |  **LOs:** All

**Materials:** Bluebook (if available) or printed practice test

| Time | Activity |
|------|----------|
| 50 min | **Full-length practice test:** Simulated AP exam conditions — 40 MC (60 min) + 3 FRQs (40 min). Timed, no notes, no talking. Use the full 45-min period for the first half (MC) and assign the FRQ portion as timed homework if needed. |

**Assessment spec:** Full mock exam. Grade and return before Lesson 5.28.

---

### Lesson 5.28 — AP Exam Prep: Targeted Review

**Period:** 103  |  **LOs:** All (targeted)

**Materials:** Practice test results, personalized review worksheets

| Time | Activity |
|------|----------|
| 5 min | **Review distribution:** Return graded practice tests. Highlight: class strengths, class weaknesses, individual weak areas. |
| 15 min | **Class-wide review:** Go over the 5 most-missed questions across the class. Re-teach the underlying concept. |
| 20 min | **Individualized review:** Students work on their personal weak areas — review sheets, concept cards, or targeted practice questions. Teacher circulates for 1-on-1 help. |
| 5 min | **Exit ticket:** "What's one concept you're still unsure about — and what will you do to fix it?" |

---

### Lesson 5.29 — AP Exam Prep: Final Review / Confidence Builder

**Period:** 104  |  **LOs:** All

**Materials:** Team challenge questions, whiteboard, buzzers (or hand-raising)

| Time | Activity |
|------|----------|
| 5 min | **Pre-game:** "You've prepared for 104 periods. You know this material. Today is about confidence." |
| 30 min | **Cybersecurity Jeopardy / Team challenge:** 4 rounds — (1) Attack Vectors, (2) Controls & Defense, (3) Cryptography, (4) Detection & Response. Teams compete for points. Each round includes one "final Jeopardy"-style large scenario question. |
| 10 min | **Exam logistics:** What to bring, time management, what to do if stuck, where to write the FRQ responses, how Bluebook works. Q&A. |

---

## Unit 5 — Lab Infrastructure Summary

| Lab | Tech Needed | Accounts Required | Setup Time |
|-----|-------------|-------------------|------------|
| OWASP Juice Shop (SQLi & XSS) | Teacher Docker container (or demo.juice-sh.op URL) | None — browser only | 15 min Docker setup |
| RBAC configuration | Google Sheets template | None (view-only link) | 10 min template creation |
| OpenSSL encryption | Terminal access (Mac Mini SSH or web terminal) | Terminal login | 10 min credential setup |
| Digital signatures | Terminal access (same as above) | Terminal login | 5 min |
| WAF rule configuration | ModSecurity screenshots + worksheet | None | 15 min prep |
| Web server log analysis | Sample access.log CSV + Google Sheets | None (view-only link) | 10 min log generation |
| Capstone presentations | Google Slides + web research | School Google account | Scenario packets prepared |
| AP practice test | Bluebook or printed test | AP Classroom (if Bluebook) | 20 min print |

**Notes:**
- All labs work on Chromebooks via browser. No local admin rights needed.
- OWASP Juice Shop can be teacher-hosted on the Mac Mini Docker instance. Alternative: use the public demo site at `https://demo.juice-sh.op` (verify availability).
- OpenSSL labs use a shared terminal (SSH from Chromebook to Mac Mini) OR a worksheet with command outputs for students who can't SSH. Teacher demo with worksheet submission works as a fallback.
- WAF lab is screenshot/worksheet-based due to the complexity of running ModSecurity on Chromebooks.
- Capstone requires 6 periods across a Spring Break boundary (Periods 92-95 before break, Periods 96-97 after). Plan accordingly — research phase before break, presentations after.

## Files to Create for Unit 5 Labs

| File | Description |
|------|-------------|
| `rbac-template.gsheet` | RBAC role/permission matrix — roles as rows, permissions as columns, checkboxes for assignment |
| `sample-access.log` | Simulated web server log (~500 entries with embedded SQLi, XSS, path traversal, brute-force indicators) |
| `waf-rule-worksheet.md` | ModSecurity rule writing exercises with answer key |
| `vulnerable-code-samples.md` | 5 code snippets with SQLi, XSS, command injection, path traversal, insecure deserialization |
| `taiwan-ai-fundamental-act-summary.md` | Student-friendly summary of relevant articles for Capstone compliance mapping |
| `capstone-scenario-packets.md` | Sector descriptions (semiconductor, power grid, water, airport, hospital, telecom) with APT profiles |
| `ap-practice-test-set1.md` | 40 MC questions + 3 FRQs for full-length mock exam |
