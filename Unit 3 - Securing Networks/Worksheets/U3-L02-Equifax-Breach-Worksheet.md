# U3 L2: Equifax Breach — Network Attack Path Worksheet

**Date:** Nov 17 (Tue) — PAPER DAY
**Unit 3 Topic:** 3.1 Network Vulnerabilities — Case Study

---

## Instructions
Read the Equifax breach summary from **Cyber Case Files** (nascar-paul.github.io/cyber-case-files/). Complete each section below. Submit at end of class.

---

## Section 1: Breach Overview (5 min)

| Question | Your Answer |
|----------|-------------|
| What was the initial vulnerability exploited? (CVE number) | |
| What type of server/application was targeted? | |
| How many records were exfiltrated? | |
| What type of data was stolen? | |

---

## Section 2: Attack Path Trace (15 min)

**Trace the attack from entry to exfiltration. Map each step to a CED 3.1 vulnerability category.**

| Step | What Happened | 3.1 Vulnerability Category (Interception / Disruption / Redirection / Infiltration) | CED LO Reference |
|------|---------------|--------------------------------------------------------------------------------------|------------------|
| 1. Entry Point | | | |
| 2. Lateral Movement | | | |
| 3. Privilege Escalation | | | |
| 4. Data Discovery | | | |
| 5. Exfiltration | | | |

---

## Section 3: Segmentation Analysis (10 min)

**Equifax had no internal network segmentation between the web portal and the consumer dispute database.**

1. **Which 3.3 segmentation control would have contained this breach?**
   - [ ] VLANs separating web tier from data tier
   - [ ] DMZ for public-facing servers
   - [ ] Zero Trust microsegmentation (per-workload isolation)
   - [ ] Firewall rules blocking web→database traffic except via API

2. **Explain your choice in 2–3 sentences. Why would this have stopped the attacker?**

---

## Section 4: CISO Quick-Write (5 min)

> **Prompt:** *If you were Equifax's CISO in 2017, what is the ONE control you would add first? Justify with reference to today's attack path.*

**Your response:**

---

## Section 5: Reflection (Homework)

**Due 20:30 tonight.** Complete any unfinished sections. Read CED excerpt on 3.1 exploitation (1 page — provided separately).

**Vocab Flashcard Set 2 (due Sun 20:30):**
- lateral movement
- privilege escalation
- data exfiltration
- network segmentation
- blast radius
- DMZ
- east-west traffic
- north-south traffic