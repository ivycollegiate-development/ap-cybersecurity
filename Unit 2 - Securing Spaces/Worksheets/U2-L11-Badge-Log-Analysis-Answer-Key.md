# U2 L11 — Worksheet: Badge Log Analysis — ANSWER KEY

**Name:** ___________________________   **Date:** ___________________   **Period:** _____

---

## Exercise B: A Week of Badge Swipes

Open `U2-L11-Badge-Log-Extract.csv` in Google Sheets. Use **Data → Create a filter** to sort and filter.

---

### 1. Choke Point Check
**Which door generated the most entries?**

| Door | Total Entries | Granted | Denied |
|------|---------------|---------|--------|
| Loading Dock | 23 | 22 | 1 |
| East Stairwell | 18 | 17 | 1 |
| Server Room | 17 | 14 | 3 |
| Cafeteria | 17 | 15 | 2 |
| Main Entrance | 15 | 14 | 1 |

**Does your camera plan from the direct instruction cover this door?**
- **Yes** — Loading Dock is a primary choke point (deliveries, after-hours access, staff entry) and should be covered by Camera 1 (Loading Dock, inside facing out) per the direct instruction floor plan.

---

### 2. After-Hours Activity (10 PM – 6 AM)
Filter for entries between **22:00:00** and **05:59:59**.

**How many after-hours entries?** **60**

**Who are those people? (Badge IDs and count)**

| Badge ID | Count | Doors Used |
|----------|-------|------------|
| S0023 | 6 | East Stairwell, Main Entrance, Loading Dock, Server Room, Cafeteria |
| S0029 | 5 | West Stairwell, Loading Dock, Main Entrance, East Stairwell, Admin Office |
| S9999 | 5 | Server Room (all denied) |
| S0017 | 4 | West Stairwell, Loading Dock, Main Entrance, East Stairwell |
| S0003 | 4 | Library Entrance, West Stairwell, Bike Storage, Main Entrance |
| S0005 | 4 | Library Entrance, Loading Dock, Main Entrance |
| S0012 | 3 | Loading Dock, West Stairwell |
| S0022 | 2 | Server Room, Admin Office |
| S0001 | 2 | Library Entrance, Loading Dock |
| S0015 | 2 | Cafeteria, Server Room, Main Entrance |
| S0014 | 2 | Gym Entrance, Library Entrance, Loading Dock |
| S0008 | 2 | Cafeteria, Admin Office, East Stairwell, Main Entrance, Bike Storage, Gym Entrance |
| S0026 | 2 | Bike Storage, Admin Office, West Stairwell |
| S0009 | 2 | Library Entrance, Loading Dock |
| S0006 | 2 | Gym Entrance, Library Entrance, Cafeteria, Loading Dock |
| S0011 | 2 | Loading Dock, Admin Office, Cafeteria |
| S0004 | 2 | East Stairwell, Loading Dock |
| S0013 | 2 | Loading Dock, Library Entrance, Cafeteria |
| S0007 | 1 | Gym Entrance |
| S0020 | 1 | Server Room |
| S0025 | 1 | Loading Dock |
| S0016 | 1 | Main Entrance |
| S0002 | 1 | Main Entrance |
| S0018 | 1 | Admin Office |
| S0027 | 1 | Cafeteria |

**What does this pattern suggest?**
Multiple staff badges show legitimate after-hours movement (S0023, S0029, S0017, S0003, S0005, etc.) — likely night custodial, IT, or security staff. **S9999** stands out: 5 consecutive denied attempts at Server Room in a 12-minute window (22:15–22:27 on 2026-10-09), indicating a reconnaissance or brute-force attempt against a high-value target.

---

### 3. Direction Field Analysis
**Does the log record direction — entry, exit, or just "credential presented"?**
**Yes, the log records both `entry` and `exit` directions.**

**What investigation does a missing direction field make impossible?**
Without direction, you cannot determine whether a person was **entering or leaving** a space. This makes it impossible to:
- Reconstruct occupancy (who is currently inside a room)
- Detect tailgating (someone entering behind an authorized exit)
- Identify impossible travel (same badge exiting one door and entering another too quickly)
- Establish time-of-presence for alibi or timeline investigations

---

### 4. Impossible Travel / Badge Sharing
Filter for **badge S0023**. Look at the timestamps.

| Timestamp | Door | Direction | Result |
|-----------|------|-----------|--------|
| 2026-10-06 05:36:00 | East Stairwell | exit | granted |
| 2026-10-06 22:22:00 | East Stairwell | entry | granted |
| 2026-10-07 01:23:00 | Main Entrance | entry | granted |
| 2026-10-07 03:09:00 | Loading Dock | entry | granted |
| 2026-10-07 22:12:00 | Main Entrance | entry | granted |
| 2026-10-08 10:30:00 | East Stairwell | entry | denied |
| 2026-10-08 12:17:00 | Cafeteria | exit | granted |
| 2026-10-08 14:30:00 | Server Room | entry | granted |
| 2026-10-08 14:32:00 | Loading Dock | exit | granted |
| 2026-10-09 06:54:00 | East Stairwell | entry | granted |
| 2026-10-11 01:30:00 | Cafeteria | exit | granted |

**What is suspicious about this badge's movement?**
**S0023 appears in widely separated locations within implausible time windows:**
- 2026-10-07: Main Entrance entry at 01:23 → Loading Dock entry at 03:09 (1h 46m gap, plausible)
- 2026-10-08: **East Stairwell denied at 10:30 → Cafeteria exit at 12:17 → Server Room entry at 14:30 → Loading Dock exit at 14:32**. The Server Room → Loading Dock transition in **2 minutes** is physically implausible for a human (different building wings, secured doors between). This suggests **badge sharing** (multiple people using S0023) or a **cloned credential**.

---

### 5. Reconnaissance Attempt
Filter for **badge S9999** at **Server Room** with **result = denied**.

**How many denied attempts?** **5**

**What time window?** **2026-10-09 22:15:00 – 22:27:00** (12-minute window)

**What does this pattern indicate?**
**Targeted reconnaissance / credential stuffing against the Server Room.** Five rapid, evenly spaced (≈3 min apart) denied entry attempts on a non-existent badge (S9999) at the highest-value door indicates an attacker testing whether the Server Room reader accepts unknown credentials, probing for a misconfigured "fail-open" state, or attempting to brute-force a valid badge ID. The regularity suggests automation or scripted attempts.

---

### 6. The 3:07 AM Hook
Find the entry for **badge S0017 at East Stairwell at 03:07:00 on 2026-10-10**.

**What does this log entry tell you that a camera would NOT?**
The log confirms **S0017's credential was presented and granted entry at East Stairwell at 03:07:00**. A camera at that door would show **a person entering** — but **cannot confirm it was the person assigned to S0017**. The log ties the event to a specific credential; the camera only ties it to a face/body. If S0017 was cloned or shared, the log still shows S0017; the camera shows the impostor. The log provides **credential-level attribution**; the camera provides **physical presence**. Both are needed for a complete picture.

---

### 7. Structural Point (Debrief)
**A badge log tells you a _credential_ was presented, not that a _person_ was there.**

**That gap is where _identity_ anomalies live.**

---

## Exit Ticket (submit before leaving)

**One question I have about analyzing a log I have not seen:**
_____________________________________________________________________________
_____________________________________________________________________________