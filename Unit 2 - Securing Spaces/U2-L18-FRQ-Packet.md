# U2 L18 FRQ Packet — Unit 2 Review: USB in the Parking Lot

**AP Cybersecurity — Unit 2: Securing Spaces**  
**Time: 15 minutes** | **Closed notes** | **Written to CED format**

---

## Scenario

On Monday morning, a USB drive labeled **"ICA Payroll Q4"** is found in the staff parking lot at Ivy Collegiate Academy. A staff member picks it up, plugs it into their classroom workstation, and opens a file named `payroll_bonus.pdf.exe`. The file executes a payload that maps the local network, enumerates Active Directory, and attempts SMB connections to servers in the "Clean Room" OU. The adversary's goal is to access chip design files stored on the clean room file server.

The school's current physical controls: badge readers on all exterior doors, one CCTV camera at the front desk, password-protected Wi-Fi, basic key locks on interior doors. No mantrap, no visitor escort policy, no badge log review process. The server room is on the ground floor in a typhoon-prone zone with a single roof drain and no flood barrier.

---

## FRQ

### Part (a) — Attack Phases (2.1.A, 2.1.B)

**Identify the phase of the cyberattack represented by each of the following actions in the scenario. Choose from: Preparatory/Reconnaissance, Establishing Access, Lateral Movement, Exfiltration.**

1. Placing the USB drive in the parking lot: _________________________________
2. The staff member plugging in the USB and the payload executing: _________________________________
3. The payload querying Active Directory for servers in the "Clean Room" OU: _________________________________
4. Compressing chip design files and uploading them to a cloud storage bucket: _________________________________

---

### Part (b) — Risk Assessment & Treatment (2.1.E, 2.1.F)

The school assesses the risk of **typhoon-induced flooding** to the ground-floor server room.

**Historical data:** 1-in-5-year flood event  
**Equipment replacement cost:** NT$12,000,000  
**Downtime cost:** NT$3,000,000 per day  
**Estimated recovery time:** 3 days

1. Calculate the **Single Loss Expectancy (SLE)**. Show your work.
2. Calculate the **Annualized Rate of Occurrence (ARO)**.
3. Calculate the **Annualized Loss Expectancy (ALE)**.
4. The school installs a flood barrier (cost: NT$800,000) and purchases flood insurance (annual premium: NT$450,000). The residual risk after these controls is **low likelihood, medium impact**. The CISO documents: *"We accept the residual risk of a 1-in-50-year catastrophic flood exceeding the barrier; no further investment is justified."* **Name the risk treatment option represented by the CISO's statement and explain why it is appropriate after avoid, transfer, and mitigate have been applied.**

---

### Part (c) — Physical Vulnerabilities & Controls (2.2.A, 2.2.C, 2.3.A, 2.3.C)

The USB was delivered physically — someone placed it in the parking lot knowing staff would find it.

1. **Tailgating risk:** During evening shift change, four people enter behind one badge swipe at the main entrance. The badge log shows one entry event. **Name the physical attack (2.2.A) and the control that physically prevents it (2.3.A).**
2. **Social engineering at the door:** A person in a reflective vest says, *"I'm here to fix the router,"* and the receptionist holds the door. **Name the attack (2.2.C) and one control that addresses the human element (2.3.A or 2.3.C).**
3. **Typhoon resilience:** The server room has a single roof drain, no flood barrier, and the UPS is on the floor. **Identify two environmental controls (2.3.C) that are missing and would reduce flood impact.**

---

### Part (d) — Detection: Badge Logs, Correlation & Alerting (2.4.A, 2.4.B, 2.4.C)

At 03:12, a cleaning contractor badges into the server room (authorized for night cleaning). The badge log records one entry event. The corridor camera at that time shows **no one at the door**.

1. **Badge log limitation (2.4.A):** What does the badge log record, and what **two things** can it **not** confirm about this entry event?
2. **Video/log correlation (2.4.B):** The badge log shows an entry; the video shows no one. **What is the finding, and what are the two possible explanations?**
3. **Alerting threshold & response (2.4.C):** The school sets this threshold: *"Alert if any badge accesses the server room between 22:00 and 06:00."* The alert emails the facilities manager. At 03:13, the manager sees the contractor's name and takes no action. **Why does this fail 2.4.C? Rewrite the threshold/response pair to satisfy 2.4.C.** (Must include: a chosen threshold value, a named action, a named owner, and a time bound.)

---

## Self-Scoring Rubric

**Total: 12 points** — Score 1 point per correct response unless noted.

| Part | Question | Points | Full-Credit Criteria |
|------|----------|--------|---------------------|
| (a) | 1. USB placement | 1 | "Preparatory/Reconnaissance" |
| (a) | 2. USB execution | 1 | "Establishing Access" |
| (a) | 3. AD query / SMB attempts | 1 | "Lateral Movement" |
| (a) | 4. File upload to cloud | 1 | "Exfiltration" |
| (b) | 1. SLE calculation | 1 | NT$12M + (3 × NT$3M) = **NT$21,000,000** |
| (b) | 2. ARO calculation | 1 | **0.2** (or 1/5, or 20%) |
| (b) | 3. ALE calculation | 1 | **NT$4,200,000** (SLE × ARO = NT$21M × 0.2) |
| (b) | 4. Risk treatment | 1 | **Accept** — deliberate, documented retention of residual risk after avoid (relocation not possible), transfer (insurance), mitigate (barrier) have been applied; reasoning provided |
| (c) | 1. Tailgating attack + control | 1 | Attack: **Tailgating** (or piggybacking). Control: **Mantrap with anti-tailgating sensors** (or single-person interlock, turnstile with anti-tailgating) |
| (c) | 2. Social engineering + control | 1 | Attack: **Social engineering at the door** (or impersonation, pretexting). Control: **Visitor escort policy / mantrap / badge verification procedure / security awareness training** (any one from 2.3.A or 2.3.C) |
| (c) | 3. Two missing environmental controls | 1 | Any two: **Flood barrier / raised equipment / redundant roof drainage / UPS elevated / water leak sensors / backup power for badge readers / sump pump with backup** |
| (d) | 1. Badge log records / cannot confirm | 1 | Records: **credential presentation (who badged, where, when)**. Cannot confirm: **(1) whether the badge holder was the person who entered, (2) whether anyone else entered behind them (tailgating), (3) unbadged entries** (any two) |
| (d) | 2. Correlation finding + explanations | 1 | Finding: **Badge event with no corresponding video presence**. Explanations: **(1) camera angle missed the person, (2) someone else used the badge (cloned/borrowed/stolen)** |
| (d) | 3. Why fails 2.4.C + rewrite | 2 | **Why it fails:** Emailing a manager is a *notification*, not a *named action with an owner and time bound*. **Rewrite example:** *"Alert on server room access 22:00–06:00 → Night-shift security officer verifies identity via camera and confirms valid work order within 10 minutes → If not confirmed, dispatch guard to server room door."* |

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 11–12 | Mastery — ready for Unit 2 test |
| 9–10 | Strong — review the 1–2 missed objectives |
| 7–8 | Partial — re-read rationales for missed items, add to study guide |
| ≤6 | Significant gaps — see teacher for targeted re-teach before Nov 9 review block |

---

## Objective Crosswalk (for study guide filing)

| Question | Learning Objective(s) |
|----------|----------------------|
| (a) 1–4 | 2.1.A, 2.1.B, 2.1.C, 2.1.D |
| (b) 1–3 | 2.1.E |
| (b) 4 | 2.1.F |
| (c) 1 | 2.2.A, 2.3.A |
| (c) 2 | 2.2.C, 2.3.A / 2.3.C |
| (c) 3 | 2.3.C |
| (d) 1 | 2.4.A |
| (d) 2 | 2.4.B |
| (d) 3 | 2.4.C |

---

**Instructions for students:**  
Work in silence for 15 minutes. When time is called, swap papers with a classmate and score using this rubric. For every point lost, write the **objective code**, **your answer**, **correct answer**, and **the rubric sentence that explains the error** in your Unit 2 study guide. This is the assignment — the score is just data.