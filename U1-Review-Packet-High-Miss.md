# Unit 1 Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: 1 — Foundations of Cybersecurity  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6 Questions)

### HM-001 | LO 1.2.A | Miss Rate: 72%
**Question**: Which of the following best describes the **CIA triad** relationship in a system where availability is prioritized over confidentiality?

A) Encryption is applied to all data at rest and in transit  
B) Redundant systems and failover mechanisms are implemented  
C) Access controls enforce least privilege for all users  
D) Audit logs capture all authentication attempts  

**Correct Answer**: B  
**Distractor Analysis**:  
- A: Describes confidentiality (encryption), not availability priority  
- C: Describes integrity/confidentiality via access control  
- D: Describes accountability/auditing, not availability  
**Key Concept**: Availability = uptime, redundancy, disaster recovery. When prioritized, you invest in failover, not encryption.

---

### HM-002 | LO 1.3.B | Miss Rate: 68%
**Question**: A threat actor uses **reconnaissance** to gather information about a target organization's email format, employee names, and software versions. Which MITRE ATT&CK tactic does this represent?

A) Initial Access  
B) Reconnaissance  
C) Resource Development  
D) Discovery  

**Correct Answer**: B  
**Distractor Analysis**:  
- A: Initial Access = gaining entry (phishing, exploit)  
- C: Resource Development = building infrastructure (buying domains, staging malware)  
- D: Discovery = post-compromise internal enumeration  
**Key Concept**: Reconnaissance is PRE-compromise information gathering (TA0043). Discovery is POST-compromise (TA0007).

---

### HM-003 | LO 1.4.C | Miss Rate: 75%
**Question**: An organization implements a **zero trust architecture**. Which principle is NOT a core tenet of zero trust?

A) Never trust, always verify  
B) Assume breach  
C) Trust but verify internal network traffic  
D) Least privilege access  

**Correct Answer**: C  
**Distractor Analysis**:  
- "Trust but verify" is the OLD perimeter model. Zero trust = "Never trust, always verify" — no implicit trust for ANY traffic, internal or external.  
**Key Concept**: Zero Trust eliminates implicit trust zones. All traffic authenticated, authorized, encrypted.

---

### HM-004 | LO 1.1.A | Miss Rate: 62%
**Question**: Which scenario best illustrates a **threat** (not a vulnerability or risk)?

A) An unpatched server running outdated Apache  
B) A ransomware group targeting healthcare providers  
C) The potential loss of patient data if breached  
D) A firewall misconfiguration allowing port 22 from internet  

**Correct Answer**: B  
**Distractor Analysis**:  
- A: Vulnerability (weakness)  
- C: Risk (impact × likelihood)  
- D: Vulnerability (misconfiguration)  
**Key Concept**: Threat = actor + intent + capability. Vulnerability = weakness. Risk = threat exploiting vulnerability × impact.

---

### HM-005 | LO 1.5.B | Miss Rate: 65%
**Question**: During **incident response**, the team isolates affected systems, collects volatile memory, and creates disk images. Which phase is this?

A) Preparation  
B) Detection & Analysis  
C) Containment, Eradication & Recovery  
D) Post-Incident Activity  

**Correct Answer**: C  
**Distractor Analysis**:  
- Isolation + forensic collection = Containment (stop spread) + Eradication evidence gathering  
- Preparation = before incident (playbooks, tools)  
- Detection = identifying the incident  
- Post-Incident = lessons learned  
**Key Concept**: NIST SP 800-61 phases. Memory capture happens during containment before eradication.

---

### HM-006 | LO 1.3.A | Miss Rate: 58%
**Question**: Which **threat modeling methodology** uses STRIDE categories (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)?

A) PASTA  
B) VAST  
C) Microsoft Threat Modeling  
D) OCTAVE  

**Correct Answer**: C  
**Distractor Analysis**:  
- PASTA: Process for Attack Simulation and Threat Analysis (7 stages)  
- VAST: Visual, Agile, Simple Threat modeling (Scalable)  
- OCTAVE: Operationally Critical Threat, Asset, Vulnerability Evaluation (org-focused)  
**Key Concept**: STRIDE was created by Microsoft for their threat modeling process.

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-001 | 1.2.A | Unit 1 Topic 2.A | CIA Triad / Availability |
| HM-002 | 1.3.B | Unit 1 Topic 3.B | MITRE ATT&CK / Reconnaissance |
| HM-003 | 1.4.C | Unit 1 Topic 4.C | Zero Trust Architecture |
| HM-004 | 1.1.A | Unit 1 Topic 1.A | Threat vs Vuln vs Risk |
| HM-005 | 1.5.B | Unit 1 Topic 5.B | Incident Response Phases |
| HM-006 | 1.3.A | Unit 1 Topic 3.A | Threat Modeling / STRIDE |

---

## Mini-Lesson: Top 2 Missed LOs

### LO 1.4.C — Zero Trust Architecture (Miss Rate 75%)

**Core Principles**:
1. **Never trust, always verify** — Every request authenticated, authorized, encrypted
2. **Assume breach** — Design as if attacker already inside
3. **Least privilege** — Minimum access needed, just-in-time
4. **Micro-segmentation** — Granular per-resource policies, not network zones

**Architecture Components**:
```
┌─────────────────────────────────────────────────────────┐
│                    Policy Engine (PDP)                   │
│  (Decides: allow/deny based on identity, device, context)│
└─────────────────┬───────────────────────────────────────┘
                  │ Policy Decision
┌─────────────────▼───────────────────────────────────────┐
│              Policy Enforcement Points (PEPs)            │
│  (Proxies, gateways, agents enforcing decisions)         │
└─────────────────────────────────────────────────────────┘
```

**Contrast with Perimeter Model**:
| Perimeter (Castle) | Zero Trust |
|-------------------|------------|
| Trust inside, block outside | Trust no one |
| VPN = full network access | Application-level access |
| Implicit trust by network | Explicit trust by identity+context |
| Static rules | Dynamic, context-aware policies |

**Exam Tip**: If question says "zero trust," eliminate any answer implying implicit trust for internal users/devices.

---

### LO 1.3.B — MITRE ATT&CK Reconnaissance (Miss Rate 68%)

**ATT&CK Matrix Position**: **TA0043 — Reconnaissance** (Pre-ATT&CK / PRE phase)

**Key Techniques**:
| Technique ID | Name | Example |
|--------------|------|---------|
| T1590 | Active Scanning | Port scanning, vulnerability scanning |
| T1591 | Gather Victim Org Info | LinkedIn, website, DNS records |
| T1592 | Gather Victim Host Info | Software versions, OS fingerprinting |
| T1598 | Phishing for Information | Spearphishing to elicit info |

**Critical Distinction**: Reconnaissance (TA0043) vs Discovery (TA0007)
- **Reconnaissance**: BEFORE initial access, external, passive/active info gathering
- **Discovery**: AFTER initial access, internal, enumerating compromised environment

**Exam Tip**: "Attacker scans public website for employee emails" = Reconnaissance. "Attacker runs `net user /domain` on compromised host" = Discovery.

---

## Practice Set (5 New Items)

### P1 | LO 1.2.B
**Question**: A system designed for **integrity** over availability would most likely implement:
A) RAID 10 storage array  
B) Digital signatures on all configuration files  
C) Load balancer with health checks  
D) Uninterruptible power supply (UPS)  
**Answer**: B — Integrity = data authenticity/non-repudiation. Digital signatures detect tampering.

### P2 | LO 1.1.B
**Question**: Risk = Threat × Vulnerability × Impact. If a vulnerability exists but no threat actor can exploit it, the risk is:
A) High  
B) Medium  
C) Low  
D) Zero  
**Answer**: C/D — Risk requires all three factors. No threat actor → no exploitation → minimal risk (residual risk from unknown threats).

### P3 | LO 1.5.A
**Question**: Which action occurs during **Preparation** phase of incident response?
A) Analyzing malware in sandbox  
B) Creating incident response playbooks  
C) Notifying law enforcement  
D) Restoring from backup  
**Answer**: B — Preparation = playbooks, tools, training, communication plans BEFORE incident.

### P4 | LO 1.3.C
**Question**: In the **Cyber Kill Chain**, which phase involves the attacker delivering a weaponized payload to the victim?
A) Reconnaissance  
B) Weaponization  
C) Delivery  
D) Exploitation  
**Answer**: C — Delivery = transmitting weapon (phishing email, drive-by download). Weaponization = creating the payload.

### P5 | LO 1.4.A
**Question**: **Defense in Depth** is best described as:
A) A single strong firewall at network perimeter  
B) Multiple overlapping security controls across layers  
C) Encrypting all data with AES-256  
D) Requiring MFA for all users  
**Answer**: B — Defense in depth = layered controls (physical, network, host, application, data). No single point of failure.

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-001 | B | 1.2.A | Availability = redundancy/failover |
| HM-002 | B | 1.3.B | Recon = pre-compromise (TA0043) |
| HM-003 | C | 1.4.C | Zero trust = never trust, always verify |
| HM-004 | B | 1.1.A | Threat = actor with intent/capability |
| HM-005 | C | 1.5.B | Isolation + forensics = containment |
| HM-006 | C | 1.3.A | STRIDE = Microsoft threat modeling |
| P1 | B | 1.2.B | Integrity = digital signatures |
| P2 | C | 1.1.B | Risk needs threat actor |
| P3 | B | 1.5.A | Preparation = playbooks |
| P4 | C | 1.3.C | Delivery = transmit weapon |
| P5 | B | 1.4.A | Defense in depth = layered controls |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| 1.4.C | Zero Trust | ___ | Re-read mini-lesson, do P1-P5 | Apr 20 |
| 1.3.B | MITRE Recon | ___ | Review ATT&CK matrix TA0043 | Apr 20 |
| 1.2.A | CIA Availability | ___ | Practice questions on redundancy | Apr 21 |
| 1.5.B | IR Containment | ___ | NIST SP 800-61 summary | Apr 21 |
| 1.1.A | Threat/Vuln/Risk | ___ | Create comparison table | Apr 22 |
| 1.3.A | STRIDE | ___ | Practice threat model exercise | Apr 22 |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*