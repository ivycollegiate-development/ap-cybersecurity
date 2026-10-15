# U2 L12: Detecting Physical Attacks — Log Packet (Print Version)
## ICA Building Security Logs — Night of October 10–11, 2026

**Print double-sided. One packet per student. Highlighters required.**

---

### SOURCE 1: Badge / Access Log (Extract)
*Records credential presentation. Does NOT prove a person was there.*

| Timestamp | Badge ID | Door | Direction | Result |
|-----------|----------|------|-----------|--------|
| 2026-10-10 06:00:00 | S0023 | Main Entrance East | entry | granted |
| 2026-10-10 06:00:40 | S0023 | Main Entrance East | entry | granted |
| 2026-10-10 09:15:00 | S0023 | Loading Dock | entry | granted |
| 2026-10-10 12:30:00 | S0017 | Server Room | entry | granted |
| 2026-10-10 14:22:00 | S0017 | East Stairwell | entry | granted |
| 2026-10-10 15:45:00 | S0029 | Main Entrance West | entry | granted |
| 2026-10-10 16:10:00 | S0005 | Library Entrance | entry | granted |
| 2026-10-10 18:30:00 | S0011 | Science Annex | entry | granted |
| 2026-10-10 22:10:00 | S0012 | Loading Dock | entry | granted |
| 2026-10-10 23:45:00 | S0017 | East Stairwell | entry | granted |
| 2026-10-11 01:22:00 | S0009 | West Stairwell | entry | granted |
| 2026-10-11 02:55:00 | S0004 | Loading Dock | entry | granted |
| 2026-10-11 03:07:00 | S0017 | East Stairwell | entry | granted |

**Field Key:**
- `timestamp` — ISO local time (no timezone)
- `badge_id` — credential identifier (S#### = staff, V#### = visitor)
- `door` — reader location
- `direction` — entry/exit (note: reader logs "credential presented," not confirmed passage)
- `result` — granted / denied

---

### SOURCE 2: CCTV Exception Report
*Records rule triggers (motion, line-crossing, door-open, loitering). Proves something happened in a field of view. Does NOT identify who.*

| Timestamp | Camera ID | Event Type | Location | Details |
|-----------|-----------|------------|----------|---------|
| 2026-10-10 06:15:00 | CAM-MAIN-EAST | motion | Main Entrance East | Person detected in foyer |
| 2026-10-10 06:45:00 | CAM-MAIN-WEST | door_open | Main Entrance West | Door held open >30s |
| 2026-10-10 07:22:00 | CAM-LOADING-DOCK | line_crossing | Loading Dock | Vehicle crossed loading zone line |
| 2026-10-10 07:23:00 | CAM-LOADING-DOCK | line_crossing | Loading Dock | Vehicle crossed loading zone line |
| 2026-10-10 07:24:00 | CAM-LOADING-DOCK | line_crossing | Loading Dock | Vehicle crossed loading zone line |
| 2026-10-10 08:10:00 | CAM-SERVER-RM | motion | Server Room | Motion in secured area |
| 2026-10-10 08:11:00 | CAM-SERVER-RM | door_open | Server Room | Server room door opened |
| 2026-10-10 08:12:00 | CAM-SERVER-RM | motion | Server Room | Person detected at rack 3 |
| 2026-10-10 08:15:00 | CAM-SERVER-RM | door_open | Server Room | Server room door closed |
| 2026-10-10 11:30:00 | CAM-LIB-ENTRY | motion | Library Entrance | Student traffic |
| 2026-10-10 12:00:00 | CAM-CAFETERIA | loitering | Cafeteria | Group >5 persons >10min |
| 2026-10-10 14:45:00 | CAM-SCI-ANNEX | door_open | Science Annex | Door propped open |
| 2026-10-10 15:20:00 | CAM-LOADING-DOCK | line_crossing | Loading Dock | **Person crossed loading zone line (NO SCHEDULED DELIVERY)** |
| 2026-10-10 16:30:00 | CAM-GYM | motion | Gym Entrance | After-hours access |
| 2026-10-10 18:45:00 | CAM-MAIN-EAST | door_open | Main Entrance East | Door held open >30s |
| 2026-10-10 22:10:00 | CAM-LOADING-DOCK | line_crossing | Loading Dock | **Person crossed loading zone line (NO SCHEDULED DELIVERY)** |
| 2026-10-10 23:55:00 | CAM-SERVER-RM | motion | Server Room | **Motion in secured area (after hours)** |
| 2026-10-11 00:30:00 | CAM-STAIRWELL-E | motion | East Stairwell | Motion detected |
| 2026-10-11 01:15:00 | CAM-STAIRWELL-W | motion | West Stairwell | Motion detected |

**Field Key:**
- `event_type` — motion / door_open / line_crossing / loitering
- `details` — free-text description from the analytics rule

---

### SOURCE 3: Sensor Alert Log
*Records physical state changes (door contacts, motion, glass break, environmental). Proves a state changed. Very hard to interpret alone.*

| Timestamp | Sensor ID | Sensor Type | Location | Reading | Status |
|-----------|-----------|-------------|----------|---------|--------|
| 2026-10-10 06:00:00 | SNS-DOOR-MAIN-E | door_contact | Main Entrance East | closed | normal |
| 2026-10-10 06:45:00 | SNS-DOOR-MAIN-E | door_contact | Main Entrance East | open | alert |
| 2026-10-10 06:46:00 | SNS-DOOR-MAIN-E | door_contact | Main Entrance East | closed | normal |
| 2026-10-10 07:15:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | open | alert |
| 2026-10-10 07:16:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | closed | normal |
| 2026-10-10 07:17:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | open | alert |
| 2026-10-10 07:18:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | closed | normal |
| 2026-10-10 08:05:00 | SNS-DOOR-SERVER | door_contact | Server Room | open | alert |
| 2026-10-10 08:06:00 | SNS-DOOR-SERVER | door_contact | Server Room | closed | normal |
| 2026-10-10 08:10:00 | SNS-MOTION-SERVER | motion | Server Room | motion_detected | alert |
| 2026-10-10 08:15:00 | SNS-DOOR-SERVER | door_contact | Server Room | open | alert |
| 2026-10-10 08:16:00 | SNS-DOOR-SERVER | door_contact | Server Room | closed | normal |
| 2026-10-10 11:25:00 | SNS-DOOR-LIB | door_contact | Library Entrance | open | alert |
| 2026-10-10 11:26:00 | SNS-DOOR-LIB | door_contact | Library Entrance | closed | normal |
| 2026-10-10 14:40:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | open | alert |
| 2026-10-10 14:41:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | closed | normal |
| 2026-10-10 14:42:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | open | alert |
| 2026-10-10 14:43:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | closed | normal |
| 2026-10-10 14:44:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | open | alert |
| 2026-10-10 14:45:00 | SNS-DOOR-SCI-ANNEX | door_contact | Science Annex | closed | normal |
| 2026-10-10 15:15:00 | SNS-STAIRWELL-E-DOOR | door_contact | East Stairwell | open | alert |
| 2026-10-10 15:16:00 | SNS-STAIRWELL-E-DOOR | door_contact | East Stairwell | closed | normal |
| ... (repeats every ~1 min until 16:00) | | | | | |
| 2026-10-10 18:30:00 | SNS-DOOR-MAIN-E | door_contact | Main Entrance East | open | alert |
| 2026-10-10 18:31:00 | SNS-DOOR-MAIN-E | door_contact | Main Entrance East | closed | normal |
| 2026-10-10 22:05:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | open | alert |
| 2026-10-10 22:06:00 | SNS-DOOR-LOADING | door_contact | Loading Dock | closed | normal |
| 2026-10-10 23:50:00 | SNS-MOTION-SERVER | motion | Server Room | motion_detected | alert |
| 2026-10-11 00:25:00 | SNS-STAIRWELL-E | door_contact | East Stairwell | open | alert |
| 2026-10-11 00:26:00 | SNS-STAIRWELL-E | door_contact | East Stairwell | closed | normal |
| 2026-10-11 01:10:00 | SNS-STAIRWELL-W | door_contact | West Stairwell | open | alert |
| 2026-10-11 01:11:00 | SNS-STAIRWELL-W | door_contact | West Stairwell | closed | normal |

**Note:** East Stairwell door contact fires every ~1 minute 15:15–16:00. This door is **mechanically held open by policy 07:00–18:00**. Each open/close cycle is a TRUE alarm that means NOTHING.

**Field Key:**
- `sensor_type` — door_contact / motion / glass_break / temp / power
- `status` — normal / alert

---

### SOURCE 4: Guard Patrol Report
*Timestamped human observation. Highest value per line, lowest coverage. Gaps in patrol schedule are themselves findings.*

| Timestamp | Guard ID | Checkpoint | Location | Observation | Reason |
|-----------|----------|------------|----------|-------------|--------|
| 2026-10-10 06:00:00 | G001 | CP-01 | Main Entrance East | Doors secured | Scheduled patrol start |
| 2026-10-10 06:15:00 | G001 | CP-02 | Loading Dock | Area clear | No deliveries scheduled |
| 2026-10-10 06:30:00 | G001 | CP-03 | Server Room | Door secured | Badge access only |
| 2026-10-10 06:45:00 | G001 | CP-04 | Library Entrance | Normal traffic | Students arriving |
| 2026-10-10 07:00:00 | G001 | CP-05 | Science Annex | Doors secured | |
| 2026-10-10 07:15:00 | G001 | CP-06 | Cafeteria | Setup in progress | Kitchen staff present |
| 2026-10-10 07:30:00 | G001 | CP-07 | East Stairwell | Door propped per policy | Held open 07:00-18:00 |
| 2026-10-10 07:45:00 | G001 | CP-08 | West Stairwell | Door secured | |
| 2026-10-10 08:00:00 | G001 | CP-09 | Gym Entrance | Doors secured | |
| 2026-10-10 08:15:00 | G001 | CP-10 | Admin Office | Normal operations | |
| 2026-10-10 08:30:00 | G001 | CP-11 | Main Entrance West | Doors secured | |
| 2026-10-10 08:45:00 | G001 | CP-12 | Bike Storage | Area clear | |
| 2026-10-10 09:00:00 | G002 | CP-01 | Main Entrance East | Doors secured | Shift change |
| ... | ... | ... | ... | ... | ... |
| 2026-10-10 16:30:00 | G001 | CP-07 | East Stairwell | Door propped per policy | Held open 07:00-18:00 |
| 2026-10-10 16:45:00 | G001 | CP-08 | West Stairwell | | **SKIPPED** |
| 2026-10-10 17:00:00 | G001 | CP-09 | Gym Entrance | Doors secured | |
| ... | ... | ... | ... | ... | ... |

**Key Anomaly: 16:45 — CP-08 West Stairwell SKIPPED, reason field LEFT BLANK**

**Field Key:**
- `checkpoint` — predefined patrol point (CP-01 through CP-12)
- `reason` — free-text; blank = no explanation given

---

### SOURCE 5: Visitor Log
*Who was signed in, by whom, for what purpose, and whether escorted. Reconciles against badge records.*

| Timestamp | Visitor Name | Visitor Badge | Host Name | Host Badge | Purpose | Escort Req | Escort Name | Escort Badge | Sign In | Sign Out |
|-----------|--------------|---------------|-----------|------------|---------|------------|-------------|--------------|---------|----------|
| 07:30:00 | CHEN Wei-Lun | V-1001 | WANG Mei-Ling | B-1042 | Parent-teacher conference | Yes | WANG Mei-Ling | B-1042 | 07:30 | 08:45 |
| 08:15:00 | LIN Yu-Chen | V-1002 | HSU Chia-Hao | B-2015 | Vendor - HVAC maintenance | Yes | HSU Chia-Hao | B-2015 | 08:15 | 11:30 |
| 08:45:00 | WU Chien-Hung | V-1003 | CHANG Ya-Ting | B-3008 | Guest speaker - CS class | Yes | CHANG Ya-Ting | B-3008 | 08:45 | 10:15 |
| 09:00:00 | HUANG Po-Chun | V-1004 | LIU Chih-Wei | B-4012 | Alumni visit | Yes | LIU Chih-Wei | B-4012 | 09:00 | 10:30 |
| 09:30:00 | TSAI Hsin-Yi | V-1005 | WANG Mei-Ling | B-1042 | Parent volunteer | Yes | WANG Mei-Ling | B-1042 | 09:30 | 12:00 |
| 10:00:00 | CHEN Wei-Lun | V-1006 | HSU Chia-Hao | B-2015 | Vendor - AV equipment | Yes | HSU Chia-Hao | B-2015 | 10:00 | 12:30 |
| 10:30:00 | LIN Yu-Chen | V-1007 | CHANG Ya-Ting | B-3008 | College fair rep | Yes | CHANG Ya-Ting | B-3008 | 10:30 | 13:00 |
| 11:00:00 | WU Chien-Hung | V-1008 | LIU Chih-Wei | B-4012 | Parent - college counseling | Yes | LIU Chih-Wei | B-4012 | 11:00 | 12:00 |
| 11:30:00 | HUANG Po-Chun | V-1009 | WANG Mei-Ling | B-1042 | Vendor - food service | Yes | WANG Mei-Ling | B-1042 | 11:30 | 13:30 |
| 12:00:00 | TSAI Hsin-Yi | V-1010 | HSU Chia-Hao | B-2015 | Guest lecturer | Yes | HSU Chia-Hao | B-2015 | 12:00 | 13:30 |
| 12:30:00 | CHEN Wei-Lun | V-1011 | CHANG Ya-Ting | B-3008 | Alumni mentor | Yes | CHANG Ya-Ting | B-3008 | 12:30 | 14:00 |
| 13:00:00 | LIN Yu-Chen | V-1012 | LIU Chih-Wei | B-4012 | Parent - PTA meeting | Yes | LIU Chih-Wei | B-4012 | 13:00 | 14:30 |
| 13:30:00 | WU Chien-Hung | V-1013 | WANG Mei-Ling | B-1042 | Vendor - security audit | Yes | WANG Mei-Ling | B-1042 | 13:30 | 15:00 |
| 14:00:00 | HUANG Po-Chun | V-1014 | HSU Chia-Hao | B-2015 | College rep | Yes | HSU Chia-Hao | B-2015 | 14:00 | 15:00 |
| 14:30:00 | TSAI Hsin-Yi | V-1015 | CHANG Ya-Ting | B-3008 | Guest speaker | Yes | CHANG Ya-Ting | B-3008 | 14:30 | 15:30 |
| 15:00:00 | CHEN Wei-Lun | V-1016 | LIU Chih-Wei | B-4012 | Parent pickup | Yes | LIU Chih-Wei | B-4012 | 15:00 | 15:15 |
| 15:30:00 | **SUSPECTED_INTRUDER** | **V-9999** | **UNKNOWN** | **HOST-UNKNOWN** | **UNKNOWN** | **Yes** | **ESCORT_LISTED** | **B-9999** | **15:30** | **** |
| 16:00:00 | LIN Yu-Chen | V-1017 | WANG Mei-Ling | B-1042 | After-school program | Yes | WANG Mei-Ling | B-1042 | 16:00 | 17:30 |
| 16:30:00 | WU Chien-Hung | V-1018 | HSU Chia-Hao | B-2015 | Vendor - IT support | Yes | HSU Chia-Hao | B-2015 | 16:30 | 18:00 |

**Key Anomaly: Row 16 (15:30) — Visitor V-9999, host UNKNOWN, escort listed as "ESCORT_LISTED" with badge B-9999, NO sign-out time. No matching badge or camera activity for escort B-9999.**

**Field Key:**
- `escort_required` — Yes/No per policy
- `escort_badge_id` — badge ID of the assigned escort (should appear in badge log)
- `sign_out_time` — blank = visitor still in building (or never signed out)

---

### PLANTED ANOMALIES SUMMARY (Teacher Reference)

| Source | Anomaly | Type | What It Proves | What It Doesn't Prove |
|--------|---------|------|----------------|----------------------|
| **Badge Log** | S0023: denied then granted 40s later at same reader; same badge at Loading Dock 3h earlier | Credential probing / possible badge sharing | A credential was presented twice in rapid succession; same credential used at distant locations | That a person walked through; that the badge holder is the attacker |
| **CCTV** | 15:20 & 22:10: line_crossing at Loading Dock — NO SCHEDULED DELIVERY | Unauthorized access / recon | Something crossed the loading dock line at unexpected times | Who or what crossed; whether it's a person, vehicle, animal, shadow |
| **Sensor** | East Stairwell door contact firing every ~1 min 15:15–16:00 (door held open by policy) | True alarm, zero signal | The door contact sensor is working correctly | That anything unusual occurred — this is NORMAL operations |
| **Guard Patrol** | 16:45 CP-08 West Stairwell SKIPPED, reason BLANK | Coverage gap / possible insider threat | The guard did not check the west stairwell at the scheduled time | Why it was skipped (fatigue, distraction, complicity, emergency) |
| **Visitor Log** | 15:30 V-9999 "SUSPECTED_INTRUDER", host UNKNOWN, escort B-9999 (ghost), no sign-out | Social engineering / tailgating vector | A visitor was logged with a fabricated escort who has no badge/camera presence | That the visitor actually entered; that the escort exists |

---

### CORRELATION NARRATIVE (What the full picture shows)

**15:20** — CCTV: Person at Loading Dock (no delivery)  
**15:30** — Visitor Log: "SUSPECTED_INTRUDER" signed in with ghost escort B-9999  
**15:30–16:00** — Sensor: East Stairwell door contact firing (normal — door propped)  
**16:45** — Guard: West Stairwell checkpoint SKIPPED (no reason)  
**22:10** — CCTV + Sensor: Loading Dock line crossing + door contact (after hours)  
**23:55** — CCTV + Sensor: Server Room motion + door contact (after hours)  
**03:07** — Badge Log: S0017 at East Stairwell (3 AM entry)  

**Most likely attack path:** Visitor V-9999 enters at 15:30 via Loading Dock (CCTV 15:20), moves through propped East Stairwell (sensor noise masks movement), guard misses West Stairwell check at 16:45 (coverage gap), returns after hours via Loading Dock (22:10), accesses Server Room (23:55), and a staff badge S0017 appears at East Stairwell at 03:07 (possible credential theft or insider).

**The lesson:** The sensor flood (East Stairwell) is the *boring true alarm* that distracts. The visitor log ghost escort is the *quiet anomaly* that matters. Detection depends on reading sources against each other over the same time window.