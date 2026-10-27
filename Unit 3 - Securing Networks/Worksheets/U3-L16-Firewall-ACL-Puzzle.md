# U3 L16: Firewalls — ACL Ordering Puzzle + Misconfiguration Hunt Worksheet

**Date:** Dec 7 (Mon) — TECH DAY
**Topic:** 3.4 Firewalls — Types, Rule Sets, Configurations

---

## Instructions
Complete both activities. Submit at end of class.

---

## Activity 1: ACL Ordering Puzzle (10 min)

**Scenario:** A firewall processes rules top-down, first-match wins. Reorder these 8 rules into correct priority order (most specific first). Some rules overlap or contradict — resolve conflicts.

### Rules (scrambled):

| Original # | Rule (scrambled order) |
|------------|------------------------|
| A | Allow 10.0.1.0/24 → 10.0.2.10 TCP 80,443 (web to DMZ) |
| B | Allow 192.168.50.5 → 10.0.2.10 TCP 22 (admin SSH) |
| C | Deny 10.0.1.0/24 → 10.0.2.0/24 Any (block staff→internal) |
| D | Allow Any → 10.0.2.10 TCP 22 (SSH from anywhere) |
| E | Deny 10.0.1.50 → Any Any (block compromised PC) |
| F | Allow 10.0.1.0/24 → 203.0.113.0/24 TCP 80,443 (staff web) |
| G | Deny Any → 203.0.113.100 Any (block known malicious IP) |
| H | Allow 10.0.1.0/24 → 10.0.3.0/24 UDP 53 (staff DNS) |

---

### Your Ordered Rules (1 = first match, 8 = last before implicit deny):

| Priority | Rule Letter | Rule Description | Why This Position? |
|----------|-------------|------------------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

**Implicit Rule 9:** Deny Any → Any Any (default deny)

---

### Packet Test Cases (apply your ordered rules):

| Test Packet | Source | Dest | Port/Proto | Your Verdict (Allow/Deny) | Matching Rule # |
|-------------|--------|------|------------|---------------------------|-----------------|
| 1 | 10.0.1.50 | 10.0.2.10 | TCP 80 | | |
| 2 | 10.0.1.50 | 8.8.8.8 | UDP 53 | | |
| 3 | 192.168.50.5 | 10.0.2.10 | TCP 22 | | |
| 4 | 10.0.1.100 | 10.0.2.10 | TCP 22 | | |
| 5 | 10.0.1.25 | 203.0.113.100 | TCP 443 | | |
| 6 | 10.0.1.25 | 10.0.3.10 | UDP 53 | | |

---

## Activity 2: Find the Misconfigurations (5 min)

**Given this firewall ruleset for a small company, identify issues.**

### Ruleset:

| Rule | Action | Source | Destination | Port/Proto | Log |
|------|--------|--------|-------------|------------|-----|
| 1 | Allow | Any | 10.0.1.10 | TCP 80,443 | No |
| 2 | Allow | Any | 10.0.1.10 | TCP 22 | No |
| 3 | Allow | Any | 10.0.1.10 | TCP 21 | No |
| 4 | Allow | Any | 10.0.1.10 | TCP 23 | No |
| 5 | Allow | 10.0.2.0/24 | Any | Any | No |
| 6 | Allow | Any | 10.0.2.0/24 | TCP 445 | No |
| 7 | Deny | Any | Any | Any | Yes |

### Find the Issues:

| Issue # | Rule(s) | Issue Type | Risk Level | Recommended Fix |
|---------|---------|------------|------------|-----------------|
| 1 | | Overly permissive | | |
| 2 | | Rules out of order (dead rule) | | |
| 3 | | Missing logging | | |
| 4 | | Insecure service allowed (WAN) | | |
| 5 | | Default-allow violation | | |
| 6 | | | | |

---

## Homework (Due 20:30)

**Document each finding from Activity 2:**
- Rule number
- Issue
- Risk level (Critical/High/Medium/Low)
- Recommended fix

**Answer:** *"Why is default-deny more secure than default-allow?"*

**Study for tomorrow's peer review (U3 L17).** Bring your lab report + this worksheet.