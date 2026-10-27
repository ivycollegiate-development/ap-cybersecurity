# U3 L17: Peer Review — Firewall Config Findings Rubric

**Date:** Dec 8 (Tue) — PAPER DAY
**Reviews:** U3 L15 GitHub Lab: Firewall Config Lab (Dec 4) + U3 L16 ACL Ordering & Misconfig Hunt (Dec 7)

---

## Instructions
Swap your firewall config report (lab + findings) with a partner. Evaluate using this rubric. Write one "glow" and one "grow." Submit completed rubric with both names.

---

## Reviewer Info

| Field | Your Info |
|-------|-----------|
| **Your Name** | |
| **Partner's Name** | |
| **Date** | Dec 8 |

---

## Rubric: Firewall Config Report Evaluation

### Section 1: Evidence Quality (Rule Snapshots + Logs)

| Criterion | Yes / Partial / No | Notes |
|-----------|---------------------|-------|
| Screenshots show each firewall rule created | | |
| Screenshots show test traffic results (allowed/blocked) | | |
| Logs show blocked/allowed as expected for each rule | | |
| Each rule has a clear purpose statement | | |
| Rule order is visible and matches the lab requirements | | |

**Evidence Score: ____ / 5**

---

### Section 2: Correctness (Rules Do What Was Claimed)

| Lab Requirement | Correct / Partial / Incorrect | Evidence |
|-----------------|-------------------------------|----------|
| (a) Block all traffic from specific compromised PC IP | | |
| (b) Allow inbound SSH (22) from specific admin IP only | | |
| (c) Block outbound to known malicious domains (alias) | | |
| (d) Allow web (80/443) from LAN to DMZ web server only | | |
| (e) Allow DNS (UDP 53) to specific servers only | | |

**Correctness Score: ____ / 5**

---

### Section 3: Security Soundness

| Principle | Yes / Partial / No | Explanation |
|-----------|---------------------|-------------|
| Default-deny posture (implicit deny at end) | | |
| Least privilege (each rule allows minimum necessary) | | |
| Logging enabled on all rules (especially denies) | | |
| No insecure services allowed (Telnet, FTP, SMB to WAN) | | |
| Rules ordered correctly (specific before general) | | |
| No dead rules (rules never matched due to ordering) | | |

**Security Score: ____ / 6**

---

### Section 4: U3 L16 Misconfiguration Hunt Findings

**Did the partner identify the same issues from Monday's activity?**

| Misconfiguration Type | Partner Found It? | Your Finding (if different) |
|-----------------------|-------------------|----------------------------|
| Overly permissive rule (e.g., allow any→any) | | |
| Rule out of order (dead rule) | | |
| Missing logging on critical rule | | |
| Insecure service exposed to WAN (Telnet/FTP/SMB) | | |
| Default-allow violation | | |
| Other: _______________ | | |

**Alignment Score: ____ / 6** (6 = perfect match, 0 = completely different findings)

---

### Section 5: Synthesis Quick-Write

**Partner's answer to:** *"What's the single most dangerous firewall misconfiguration you can make?"*

**Your assessment of their answer:**
- [ ] Identifies a real, high-impact misconfiguration
- [ ] Explains *why* it's dangerous (attack scenario)
- [ ] References a principle (default-deny, least privilege, logging)
- [ ] Concise and clear

---

## Glow & Grow (Required)

### Glow (What they did well — be specific):

### Grow (One concrete improvement — be specific):

---

## Class Discussion Notes

**Most commonly missed misconfiguration (from class poll):**

**Any false positives — rules that looked wrong but are actually needed?**

---

## Overall Assessment

**Total Score: ____ / 22**

**Would this firewall config effectively protect the network?**
- [ ] Yes, with minor tweaks
- [ ] Mostly, but has significant gaps
- [ ] No, major redesign needed

**Reviewer Signature:** _________________________

**Partner Signature (acknowledging feedback):** _________________________

---

## Homework (Due 20:30)

**Study for tomorrow's test (Dec 9).** Bring a one-page handwritten study sheet (allowed on test).

**Focus areas based on today's review:**
1. _________________________________
2. _________________________________
3. _________________________________