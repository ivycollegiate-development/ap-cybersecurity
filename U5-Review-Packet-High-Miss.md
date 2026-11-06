# Unit 5 Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: 5 — Application Security  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6 Questions)

### HM-025 | LO 5.1.C | Miss Rate: 79%
**Question**: Which **OWASP Top 10 2021** category includes **SQL Injection, Command Injection, and LDAP Injection**?

A) A01:2021 — Broken Access Control  
B) A03:2021 — Injection  
C) A04:2021 — Insecure Design  
D) A06:2021 — Vulnerable Components  

**Correct Answer**: B  
**Distractor Analysis**:  
- A03: Injection = untrusted data sent to interpreter (SQL, OS, LDAP, XPath, NoSQL)  
- A01: Broken Access Control = authorization failures (IDOR, path traversal)  
- A04: Insecure Design = missing security controls in design phase  
- A06: Vulnerable Components = known vulnerable libraries  
**Key Concept**: Injection = #3 in 2021 (was #1 in 2017). Defense: parameterized queries, input validation, ORM.

---

### HM-026 | LO 5.2.D | Miss Rate: 72%
**Question**: **RBAC (Role-Based Access Control)** assigns permissions to **roles**, not directly to users. Which model assigns permissions based on **attributes** (user, resource, environment)?

A) MAC (Mandatory Access Control)  
B) DAC (Discretionary Access Control)  
C) ABAC (Attribute-Based Access Control)  
D) RuBAC (Rule-Based Access Control)  

**Correct Answer**: C  
**Distractor Analysis**:  
- ABAC = attributes (user.dept, resource.classification, time, location) → policy engine evaluates  
- MAC = system-enforced labels (classification: Top Secret, Secret)  
- DAC = owner discretion (ACLs)  
- RuBAC = rules (if time>9 and time<17 then allow) — subset of ABAC  
**Key Concept**: ABAC = fine-grained, dynamic, policy-based. XACML is standard language.

---

### HM-027 | LO 5.3.B | Miss Rate: 83%
**Question**: In **RSA**, the public key is (n, e) and private key is (n, d). Which value must be kept secret to maintain security?

A) n (modulus)  
B) e (public exponent)  
C) d (private exponent)  
D) φ(n) (Euler's totient)  

**Correct Answer**: C (and D)  
**Distractor Analysis**:  
- Private key = (n, d) — d MUST be secret  
- φ(n) = (p-1)(q-1) — knowing φ(n) allows computing d from e (equivalent to factoring n)  
- n is public (product of p, q)  
- e is public (typically 65537)  
**Key Concept**: Private exponent d and φ(n) are both secrets. Leaking either breaks RSA.

---

### HM-028 | LO 5.4.A | Miss Rate: 68%
**Question**: **OCSP (Online Certificate Status Protocol)** provides real-time certificate revocation checking. What is the **OCSP response** signed by?

A) The certificate subject  
B) The OCSP Responder's certificate  
C) The Root CA  
D) The Certificate Transparency Log  

**Correct Answer**: B  
**Distractor Analysis**:  
- OCSP Responder has its own certificate (signed by CA), signs responses  
- Responder cert must have OCSP Signing EKU (id-kp-ocspSigning)  
- Not signed by subject (they don't have CA key)  
- Not signed by Root CA directly (delegated)  
- CT Logs don't sign OCSP responses  
**Key Concept**: OCSP = real-time alternative to CRL. Responder = trusted by CA. Stapling = server includes OCSP response in TLS handshake.

---

### HM-029 | LO 5.5.B | Miss Rate: 62%
**Question**: A **WAF (Web Application Firewall)** operating in **detection-only mode** (monitor) will:

A) Block malicious requests and log them  
B) Log malicious requests but allow them through  
C) Only log requests matching known CVE signatures  
D) Require manual approval for each request  

**Correct Answer**: B  
**Distractor Analysis**:  
- Detection/Monitor mode = alert/log only, no blocking  
- Prevention/Block mode = block + log  
- Used for tuning rules before enabling blocking  
**Key Concept**: WAF modes: Off → Detection → Prevention. Always test in detection first.

---

### HM-030 | LO 5.6.C | Miss Rate: 56%
**Question**: **Structured logging** (e.g., JSON format) enables which security operations capability?

A) Real-time alerting and automated correlation  
B) Encryption of log data at rest  
C) Compression to save disk space  
D) Tamper-proof log storage  

**Correct Answer**: A  
**Distractor Analysis**:  
- Structured logs = machine-parseable (JSON, key-value) → SIEM can parse, correlate, alert  
- B: Encryption separate from format  
- C: JSON is verbose, not compressed  
- D: Tamper-proof requires signed logs / append-only / blockchain  
**Key Concept**: Structured logging = foundation for SIEM, SOAR, automated detection. Unstructured (syslog) = regex parsing, brittle.

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-025 | 5.1.C | Unit 5 Topic 1.C | OWASP Top 10 / Injection |
| HM-026 | 5.2.D | Unit 5 Topic 2.D | Access Control Models / ABAC |
| HM-027 | 5.3.B | Unit 5 Topic 3.B | RSA / Private Key Components |
| HM-028 | 5.4.A | Unit 5 Topic 4.A | PKI / OCSP |
| HM-029 | 5.5.B | Unit 5 Topic 5.B | WAF / Operating Modes |
| HM-030 | 5.6.C | Unit 5 Topic 6.C | Logging / Structured Logs |

---

## Mini-Lesson: Top 2 Missed LOs

### LO 5.3.B — RSA Private Key Components (Miss Rate 83%)

**RSA Key Generation**:
```
1. Choose large primes p, q
2. n = p × q                    → Public modulus
3. φ(n) = (p-1)(q-1)            → SECRET (equivalent to factoring n)
4. Choose e (e.g., 65537)       → Public exponent (gcd(e, φ(n)) = 1)
5. Compute d = e^(-1) mod φ(n)  → Private exponent (SECRET)
```

**Public Key**: (n, e)
**Private Key**: (n, d)  — **d is THE secret**

**Why φ(n) is also secret**:
- If attacker knows φ(n) and n: can factor n (solve p+q = n - φ(n) + 1)
- If attacker knows φ(n) and e: can compute d = e^(-1) mod φ(n)
- φ(n) leakage = full key compromise

**Key Storage (PKCS#8)**:
```pem
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQD...
-----END PRIVATE KEY-----
```
Contains: n, e, d, p, q, dP, dQ, qInv (CRT parameters for speed)

**CRT Parameters** (Chinese Remainder Theorem optimization):
- dP = d mod (p-1)
- dQ = d mod (q-1)
- qInv = q^(-1) mod p
- These also allow full key recovery if leaked

**Exam Tip**: "Which value must be kept secret?" → d (private exponent). φ(n) is also correct but rarely listed as option.

---

### LO 5.1.C — OWASP Top 10: Injection (Miss Rate 79%)

**A03:2021 — Injection** (was A01:2017)

**Definition**: Untrusted data sent to interpreter as part of command/query. Interpreter executes unintended commands.

**Types of Injection**:
| Type | Interpreter | Example Payload |
|------|-------------|-----------------|
| **SQLi** | SQL Database | `' OR '1'='1` |
| **Command Injection** | OS Shell | `; cat /etc/passwd` |
| **LDAP Injection** | LDAP Directory | `*)(&(userPassword=*))` |
| **XPath Injection** | XML XPath | `'] | //user[position()=1] | ['` |
| **NoSQL Injection** | MongoDB | `{"$ne": null}` |
| **ORM Injection** | Hibernate/JPA | `from User where name='` |
| **Template Injection** | Jinja2/Twig | `{{7*7}}` → 49 |

**Impact**: Data loss, authentication bypass, RCE, full server compromise

**Defense in Depth**:
1. **Primary**: Parameterized Queries / Prepared Statements
   ```python
   # GOOD
   cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
   
   # BAD
   cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
   ```
2. **Input Validation**: Allowlist (not denylist)
3. **ORM**: Use safely (avoid raw SQL)
4. **Least Privilege**: DB user with minimal permissions
5. **WAF**: Detection layer (not primary defense)

**Detection**:
- SAST: taint analysis (user input → sink)
- DAST: automated scanning (SQLMap, OWASP ZAP)
- Runtime: WAF alerts, error monitoring

**Exam Tip**: "Injection" = interpreter executes attacker-controlled data. Parameterized queries = #1 defense. NOT input validation alone.

---

## Practice Set (5 New Items)

### P21 | LO 5.1.A
**Question**: **Broken Access Control (A01:2021)** is the #1 OWASP risk. Which scenario demonstrates **IDOR (Insecure Direct Object Reference)**?

A) User accesses `/api/user/123/profile` by changing ID to 124  
B) SQL injection via login form  
C) XSS via comment field  
D) Weak password policy  
**Answer**: A — IDOR = direct reference to object (ID, filename) without authorization check.

### P22 | LO 5.2.A
**Question**: **DAC (Discretionary Access Control)** means:

A) System enforces labels (Top Secret, Secret)  
B) Owner decides who can access their resources  
C) Access based on attributes (time, location, role)  
D) Central policy engine decides all access  
**Answer**: B — DAC = owner discretion (ACLs, chmod). MAC = labels. ABAC = attributes.

### P23 | LO 5.4.B
**Question**: **Certificate Transparency (CT)** logs provide:

A) Real-time revocation checking  
B) Public audit trail of all issued certificates  
C) Automated certificate renewal  
D) Private key escrow  
**Answer**: B — CT = public, append-only logs of all certificates. Detects mis-issuance.

### P24 | LO 5.5.A
**Question**: **ModSecurity** is an example of:

A) Network firewall  
B) Host-based IDS  
C) Web Application Firewall (WAF)  
D) Database firewall  
**Answer**: C — ModSecurity = open-source WAF (Apache, Nginx, IIS). Rule language = SecRule.

### P25 | LO 5.6.A
**Question**: **Syslog severity levels** (RFC 5424). Which level indicates **immediate action required**?

A) Info (6)  
B) Warning (4)  
C) Critical (2)  
D) Debug (7)  
**Answer**: C — Severity 0=Emergency, 1=Alert, 2=Critical (immediate action). 3=Error, 4=Warning, 5=Notice, 6=Info, 7=Debug.

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-025 | B | 5.1.C | Injection = SQLi, CMDi, LDAPi |
| HM-026 | C | 5.2.D | ABAC = attribute-based |
| HM-027 | C | 5.3.B | d = private exponent (secret) |
| HM-028 | B | 5.4.A | OCSP response signed by Responder |
| HM-029 | B | 5.5.B | Detection mode = log only |
| HM-030 | A | 5.6.C | Structured logs = SIEM correlation |
| P21 | A | 5.1.A | IDOR = direct object reference |
| P22 | B | 5.2.A | DAC = owner discretion |
| P23 | B | 5.4.B | CT = public audit trail |
| P24 | C | 5.5.A | ModSecurity = WAF |
| P25 | C | 5.6.A | Critical (2) = immediate action |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| 5.3.B | RSA Key Components | ___ | Mini-lesson, d & φ(n) secret | Apr 20 |
| 5.1.C | OWASP Injection | ___ | Mini-lesson, parameterized queries | Apr 20 |
| 5.2.D | ABAC vs RBAC | ___ | Comparison table | Apr 21 |
| 5.4.A | OCSP / Stapling | ___ | TLS handshake with OCSP staple | Apr 21 |
| 5.5.B | WAF Modes | ___ | Detection vs Prevention | Apr 22 |
| 5.6.C | Structured Logging | ___ | JSON log example, SIEM query | Apr 22 |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*