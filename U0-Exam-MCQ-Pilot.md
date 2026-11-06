# U0-Exam-MCQ-Pilot.md — Peer-Review Pilot (10 MCQs, 2 per Unit)

**Purpose**: Internal peer-review pilot for AP Cybersecurity practice exam MCQs  
**Reviewer**: Mr. Chen, CS Dept.  
**Review Session**: March 20, 2027  
**Criteria**: LO alignment, distractor plausibility, no duplicates, appropriate difficulty  
**Format**: 2 MCQs per unit (Units 1–5), mix of single-select and multi-select

---

## Unit 1: Introduction to Security (Topics 1.1–1.5)

### Question 1 (LO 1.1.A — Single-Select)
**Topic**: 1.1 Understanding Social Engineering

A cybersecurity analyst receives an email claiming to be from the company's IT department. The email states: "Your account will be deactivated in 2 hours unless you click this link and verify your credentials immediately. Over 90% of employees have already completed this process."

Which social engineering tactic is **most** prominently demonstrated in this email?

A. Pretexting  
B. Urgency and consensus  
C. Authority impersonation  
D. Familiarity exploitation

**Correct Answer**: B  
**LO Tag**: 1.1.A  
**Distractor Analysis**:
- A (Pretexting): Present but not the *most* prominent; the email creates a scenario but urgency/consensus drive action
- C (Authority): IT department impersonation is present but secondary to urgency/consensus pressure
- D (Familiarity): Not demonstrated; no personal relationship claimed

---

### Question 2 (LO 1.4.A — Multi-Select)
**Topic**: 1.4 AI-Based Cybersecurity Attacks

Which of the following are ways adversaries use AI-powered tools to augment cyberattacks? **Select all that apply.**

A. Creating convincing phishing messages in any target language using LLMs  
B. Generating digital avatars from voice/image samples for impersonation  
C. Automating vulnerability scanning across target networks  
D. Crafting prompts to extract sensitive information from LLMs  
E. Encrypting ransomware payloads to evade signature detection

**Correct Answers**: A, B, D  
**LO Tag**: 1.4.A  
**Distractor Analysis**:
- C: Vulnerability scanning automation predates AI; not specific to AI-augmented attacks per CED
- E: Payload encryption is traditional malware technique, not AI-specific

---

## Unit 2: Securing Spaces (Topics 2.1–2.4)

### Question 3 (LO 2.1.D — Single-Select)
**Topic**: 2.1 Cyber Foundations

An organization conducts a risk assessment for a new server deployment. They identify a vulnerability, estimate the likelihood of exploitation as "High," and the potential impact as "Critical." They decide to implement a network segmentation strategy to reduce the attack surface.

Which step of the risk assessment process does the network segmentation decision represent?

A. Identify vulnerabilities  
B. Evaluate likelihood and impact  
C. Determine risk response strategy  
D. Document residual risk

**Correct Answer**: C  
**LO Tag**: 2.1.D  
**Distractor Analysis**:
- A: Occurs before risk evaluation
- B: Describes the assessment step already completed (likelihood/impact estimated)
- D: Occurs after mitigation implementation

---

### Question 4 (LO 2.2.A — Multi-Select)
**Topic**: 2.2 Physical Vulnerabilities and Attacks

Which of the following are examples of physical social engineering attacks? **Select all that apply.**

A. An adversary carries a large box and asks an employee to hold the door to a restricted area  
B. An adversary follows closely behind an authorized employee through a badge-secured door without the employee's awareness  
C. An adversary uses a hidden camera to record a user entering their password at a workstation  
D. An adversary pretends to be a maintenance technician needing access to a server room  
E. An adversary connects a rogue access point to the network via an unsecured Ethernet port

**Correct Answers**: A, B, D  
**LO Tag**: 2.2.A  
**Distractor Analysis**:
- C: Shoulder surfing (physical attack but not social engineering — no manipulation of a person)
- E: Rogue access point (technical attack, not social engineering)

---

## Unit 3: Securing Networks (Topics 3.1–3.5)

### Question 5 (LO 3.1.A — Single-Select)
**Topic**: 3.1 Network Vulnerabilities and Attacks

A network administrator observes that a switch has entered broadcast mode, flooding all ports with traffic. Investigation reveals the switch's MAC address table is full of entries mapping to a single port.

Which attack is **most** likely occurring?

A. ARP poisoning  
B. MAC flooding  
C. DHCP starvation  
D. VLAN hopping

**Correct Answer**: B  
**LO Tag**: 3.1.A  
**Distractor Analysis**:
- A: ARP poisoning targets ARP tables, not switch MAC tables
- C: DHCP starvation exhausts DHCP pool, doesn't fill MAC table
- D: VLAN hopping bypasses VLAN segmentation, doesn't cause broadcast mode

---

### Question 6 (LO 3.4.B — Multi-Select)
**Topic**: 3.4 Protecting Networks: Firewalls

A firewall uses an access control list (ACL) with the following rules (processed top-down):

| Rule | Action | Direction | Protocol | Port | Source |
|------|--------|-----------|----------|------|--------|
| 1 | Allow | Inbound | TCP | 80 | ALL |
| 2 | Deny | Inbound | TCP | 443 | 192.168.10.0/24 |
| 3 | Allow | Inbound | TCP | 443 | ALL |
| 4 | Deny | Inbound | ALL | ALL | ALL |

Which of the following statements about this ACL are correct? **Select all that apply.**

A. Traffic from 192.168.10.50 to port 443 will be denied  
B. Traffic from 192.168.20.50 to port 443 will be allowed  
C. Traffic from 192.168.10.50 to port 80 will be allowed  
D. The implicit deny (Rule 4) is unnecessary because Rule 2 denies all remaining traffic  
E. Swapping Rule 2 and Rule 3 would allow 192.168.10.0/24 to access port 443

**Correct Answers**: A, B, C, E  
**LO Tag**: 3.4.B  
**Distractor Analysis**:
- D: Implicit deny is a best practice; Rule 2 only denies 192.168.10.0/24 on port 443, not all remaining traffic

---

## Unit 4: Securing Devices (Topics 4.1–4.4)

### Question 7 (LO 4.2.A — Single-Select)
**Topic**: 4.2 Authentication

Why are cryptographic hash functions used to store passwords instead of storing plaintext passwords?

A. Hashes are reversible, allowing administrators to recover forgotten passwords  
B. Hashes have fixed-length output regardless of input length, saving database space  
C. Hashes provide pre-image resistance, making it infeasible to determine the input from the hash  
D. Hashes are faster to compute than encryption algorithms

**Correct Answer**: C  
**LO Tag**: 4.2.A  
**Distractor Analysis**:
- A: False; hashes are one-way (pre-image resistant), not reversible
- B: True but not the *security reason* for password storage
- D: Speed is actually a disadvantage for password hashing (slow hashes preferred)

---

### Question 8 (LO 4.4.A — Multi-Select)
**Topic**: 4.4 Detecting Attacks on Devices

Which of the following are indicators of compromise (IoCs) that can be found in authentication logs? **Select all that apply.**

A. Multiple failed login attempts for non-existent usernames (admin, root, test) from the same IP  
B. A successful login followed by immediate sudo command execution  
C. Login attempts at unusual hours from a user's typical geographic location  
D. CRON job sessions opening and closing for root at regular intervals  
E. UFW BLOCK entries showing denied connections to unusual ports (e.g., port 25, 77)

**Correct Answers**: A, C, E  
**LO Tag**: 4.4.A  
**Distractor Analysis**:
- B: Legitimate admin activity (sudo after login is normal)
- D: Normal system behavior (scheduled cron jobs)

---

## Unit 5: Securing Applications & Data (Topics 5.1–5.6)

### Question 9 (LO 5.1.B — Single-Select)
**Topic**: 5.1 Application and Data Vulnerabilities and Attacks

A web application accepts user input from a search form and directly concatenates it into a SQL query without sanitization. An attacker submits: `' OR '1'='1';--`

What type of attack is this?

A. Cross-site scripting (XSS)  
B. SQL injection  
C. Directory traversal  
D. Buffer overflow

**Correct Answer**: B  
**LO Tag**: 5.1.B  
**Distractor Analysis**:
- A: XSS injects scripts executed in browser, not database queries
- C: Directory traversal uses `../` sequences to access files
- D: Buffer overflow exploits memory allocation, not query logic

---

### Question 10 (LO 5.4.A — Multi-Select)
**Topic**: 5.4 Asymmetric Cryptography

Which of the following statements about asymmetric encryption are correct? **Select all that apply.**

A. The public key encrypts data; only the corresponding private key can decrypt it  
B. Either key in a key pair can encrypt, but only the other key can decrypt  
C. Key pairs are generated simultaneously and are mathematical inverses  
D. If a private key is compromised, the key pair must be regenerated  
E. Asymmetric encryption uses the same key for encryption and decryption

**Correct Answers**: A, B, C, D  
**LO Tag**: 5.4.A  
**Distractor Analysis**:
- E: Describes symmetric encryption, not asymmetric

---

## Pilot Review Checklist (for Mr. Chen, Mar 20)

| Criterion | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|-----------|----|----|----|----|----|----|----|----|----|-----|
| LO alignment verified | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Distractors plausible | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| No duplicate LOs | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Appropriate difficulty | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Multi-select format correct | N/A | ☐ | N/A | ☐ | N/A | ☐ | N/A | ☐ | N/A | ☐ |

**Notes**: 
- 6 single-select, 4 multi-select (scaled to 40/20 ratio for full exam)
- All 5 units represented, 2 questions each
- LO codes use exact `Unit.Topic.Letter` format from Course Curriculum Framework

---

*After pilot review approval, proceed to full 60 MCQ development (Task 1.2 Steps 1–4).*