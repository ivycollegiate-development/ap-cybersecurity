# U3 L14: Mock MCQ Sprint — Unit 3 Review

**Date:** Dec 3 (Thu) — PAPER DAY
**Purpose:** Self-assess Unit 3 knowledge ahead of Dec 9 test.

---

## Instructions
1. **Timed Sprint (7 min):** Complete 5 AP-style MCQs covering 3.1–3.5.
2. **Peer-Grade (10 min):** Exchange, grade, discuss each answer's reasoning.
3. **Identify Gaps (10 min):** Which 2 questions were most missed? Re-teach on whiteboard.
4. **Self-Assessment (8 min):** Mark weak areas on study guide.
5. **Study Strategy (5 min):** Plan review before Wed Dec 9 test.

---

## Sprint: 5 MCQs (7 min — start timer now)

### Question 1 (3.1 — Network Vulnerabilities)
**An attacker sends forged ARP replies mapping their MAC address to the default gateway's IP. All traffic from the victim to the internet now passes through the attacker's machine. This attack is best classified as:**

A. MAC flooding
B. ARP poisoning
C. DNS cache poisoning
D. SYN flood

**Your answer:** ____
**Confidence (1–5):** ____

---

### Question 2 (3.2 — Wireless Security)
**A school uses WPA2-Personal with a shared passphrase for all staff devices. An attacker captures the 4-way handshake when a device reconnects and runs an offline dictionary attack. Which upgrade would BEST mitigate this specific attack?**

A. Disable SSID broadcast
B. Enable MAC address filtering
C. Upgrade to WPA3-Enterprise with 802.1X/EAP-TLS
D. Reduce transmit power to limit parking-lot range

**Your answer:** ____
**Confidence (1–5):** ____

---

### Question 3 (3.3 — Network Segmentation)
**A company places its web server, email server, and internal database server all on the same flat network. An attacker compromises the web server via a vulnerability and pivots to the database. Which segmentation design would have PREVENTED this lateral movement?**

A. Single VLAN with port security on all switch ports
B. DMZ for web/email servers; internal VLAN for database; firewall blocking DMZ→internal except API ports
C. Two VLANs: one for servers, one for clients; no firewall between them
D. All servers in a DMZ with no internal network

**Your answer:** ____
**Confidence (1–5):** ____

---

### Question 4 (3.4 — Firewalls)
**A stateful firewall has the following rules (processed top-down, first-match wins):**

| Rule | Action | Source | Destination | Port/Protocol |
|------|--------|--------|-------------|---------------|
| 1 | Allow | 10.0.1.0/24 | 10.0.2.10 | TCP 80, 443 |
| 2 | Deny | 10.0.1.0/24 | 10.0.2.0/24 | Any |
| 3 | Allow | Any | 10.0.2.10 | TCP 22 |
| 4 | Deny | Any | Any | Any (implicit) |

**A packet from 10.0.1.50 to 10.0.2.10 on TCP port 22 arrives. What happens?**

A. Allowed by Rule 1
B. Denied by Rule 2
C. Allowed by Rule 3
D. Denied by implicit Rule 4

**Your answer:** ____
**Confidence (1–5):** ____

---

### Question 5 (3.5 — Detecting Network Attacks)
**A SIEM correlates three log sources: (1) firewall shows 500 SYN packets from 203.0.113.45 to 10.0.1.10:22 in 60 seconds; (2) SSH server logs show 500 failed login attempts for root from same IP; (3) IDS alerts "SSH brute force" on same flow. This is an example of which correlation type?**

A. Time-based correlation
B. Pattern-based correlation
C. Threshold-based correlation
D. All of the above

**Your answer:** ____
**Confidence (1–5):** ____

---

## Peer-Grade & Discussion (10 min)

| Q | Correct Answer | Your Answer | ✓/✗ | Reasoning (why correct/incorrect) |
|---|----------------|-------------|-----|-----------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Total Correct: ____ / 5**

---

## Gap Identification (10 min)

**Which 2 questions were most missed by the class?**

1. Q____ — Concept: _________________________________
2. Q____ — Concept: _________________________________

**Re-teach notes (whiteboard):**

---

## Self-Assessment & Study Guide Check (8 min)

**Mark your weakest Unit 3 topics:**

| Topic | Confidence (1–5) | Study Guide Section | Flashcard Set |
|-------|------------------|---------------------|---------------|
| 3.1 Network Vulnerabilities (ARP, MAC, DNS, DoS) | | | Set 1 |
| 3.1 Risk Assessment (likelihood × impact, risk register) | | | Set 3 |
| 3.2 Wireless Security (WPA3, 802.1X, evil twin) | | | Set 2 |
| 3.2 Managerial Controls (AUA, guest policy) | | | Set 2 |
| 3.3 Segmentation (VLAN, DMZ, zero trust) | | | — |
| 3.4 Firewalls (types, ACL ordering, default-deny) | | | — |
| 3.5 Detection (NIDS/NIPS, SIEM, correlation) | | | — |

**My TOP 3 weakest topics to review before Dec 9 test:**

1. _________________________________
2. _________________________________
3. _________________________________

---

## Study Strategy (5 min)

**How I'll use the study guide + flashcards between now and the test (Dec 9):**

| Day | Action | Resources |
|-----|--------|-----------|
| Fri Dec 4 | | |
| Mon Dec 7 | | |
| Tue Dec 8 | | |

---

## Homework (Due Sun 20:30 — Monday Quiz)

**Study guide section for your weakest topic.** Test is **Wed Dec 9**.

**Bring a one-page handwritten study sheet** (allowed on test) — start drafting this weekend.