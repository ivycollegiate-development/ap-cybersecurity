# U2 L11 — Worksheet: Badge Log Analysis

**Name:** ___________________________   **Date:** Oct 14, 2026   **Period:** _____

---

## Exercise B: A Week of Badge Swipes

Open `U2-L11-Badge-Log-Extract.csv` in Google Sheets. Use **Data → Create a filter** to sort and filter.

---

### 1. Choke Point Check
**Which door generated the most entries?**

| Door | Total Entries | Granted | Denied |
|------|---------------|---------|--------|
|      |               |         |        |
|      |               |         |        |
|      |               |         |        |
|      |               |         |        |
|      |               |         |        |

**Does your camera plan from the direct instruction cover this door?**
- Yes / No — If no, where would you move a camera?

---

### 2. After-Hours Activity (10 PM – 6 AM)
Filter for entries between **22:00:00** and **05:59:59**.

**How many after-hours entries?** ________

**Who are those people? (Badge IDs and count)**
| Badge ID | Count | Doors Used |
|----------|-------|------------|
|          |       |            |
|          |       |            |
|          |       |            |
|          |       |            |

**What does this pattern suggest?**

---

### 3. Direction Field Analysis
**Does the log record direction — entry, exit, or just "credential presented"?** ________

**What investigation does a missing direction field make impossible?**
_____________________________________________________________________________
_____________________________________________________________________________

---

### 4. Impossible Travel / Badge Sharing
Filter for **badge S0023**. Look at the timestamps.

| Timestamp | Door | Direction | Result |
|-----------|------|-----------|--------|
|           |      |           |        |
|           |      |           |        |
|           |      |           |        |

**What is suspicious about this badge's movement?**
_____________________________________________________________________________
_____________________________________________________________________________

---

### 5. Reconnaissance Attempt
Filter for **badge S9999** at **Server Room** with **result = denied**.

**How many denied attempts?** ________

**What time window?** ________________

**What does this pattern indicate?**
_____________________________________________________________________________

---

### 6. The 3:07 AM Hook
Find the entry for **badge S0017 at East Stairwell at 03:07:00 on 2026-10-10**.

**What does this log entry tell you that a camera would NOT?**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

---

### 7. Structural Point (Debrief)
**A badge log tells you a _______________ was presented, not that a _______________ was there.**

**That gap is where _______________ anomalies live.**

---

## Exit Ticket (submit before leaving)

**One question I have about analyzing a log I have not seen:**
_____________________________________________________________________________
_____________________________________________________________________________