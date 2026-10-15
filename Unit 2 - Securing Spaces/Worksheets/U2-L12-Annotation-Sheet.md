# U2 L12: Detecting Physical Attacks — Log Analysis and Alerting (Paper Day)
## Annotation Sheet

**Name:** ___________________________    **Date:** October 15, 2026    **Period:** 13

---

## Instructions
You have 5 log sources covering the same night (October 10–11, 2026). For each source:
1. **Mark the anomalous line(s)** with a highlighter
2. **Write:** What is normal here? What is not? What would it mean?
3. **Answer the correlation question** at the bottom of each source section

---

## SOURCE 1: Badge / Access Log
**Fields:** timestamp, badge_id, door, direction, result (granted/denied)
**Records a credential presentation. Does NOT prove a person was there.**

| # | Anomaly Found? | What is Normal | What is Not Normal | What It Could Mean |
|---|----------------|----------------|---------------------|---------------------|
|   | ☐ Yes ☐ No     |                |                     |                     |

**Correlation:** This badge appears at a different building entrance 3 hours earlier. What does the denied-then-granted pattern at the same reader suggest?

---

## SOURCE 2: CCTV Exception Report
**Fields:** timestamp, camera_id, event_type, location, details
**Records a rule trigger (motion, line-crossing, door-open). Does NOT identify who.**

| # | Anomaly Found? | What is Normal | What is Not Normal | What It Could Mean |
|---|----------------|----------------|---------------------|---------------------|
|   | ☐ Yes ☐ No     |                |                     |                     |

**Correlation:** Line-crossing trigger on loading dock camera at a time with NO scheduled deliveries. What does this prove vs. not prove?

---

## SOURCE 3: Sensor Alert Log
**Fields:** timestamp, sensor_id, sensor_type, location, reading, status
**Records a physical state change. Very hard to interpret alone.**

| # | Anomaly Found? | What is Normal | What is Not Normal | What It Could Mean |
|---|----------------|----------------|---------------------|---------------------|
|   | ☐ Yes ☐ No     |                |                     |                     |

**Correlation:** Door-open contact on a stairwell door that is MECHANICALLY HELD OPEN during operating hours by policy. Is this a true alarm? Does it mean anything?

---

## SOURCE 4: Guard Patrol Report
**Fields:** timestamp, guard_id, checkpoint, location, observation, reason
**Human observation — highest value per line, lowest coverage. Gaps in schedule are findings.**

| # | Anomaly Found? | What is Normal | What is Not Normal | What It Could Mean |
|---|----------------|----------------|---------------------|---------------------|
|   | ☐ Yes ☐ No     |                |                     |                     |

**Correlation:** A patrol entry that SKIPS the west corridor with reason field LEFT BLANK. What does a missing patrol checkpoint indicate?

---

## SOURCE 5: Visitor Log
**Fields:** timestamp, visitor_name, visitor_badge_id, host_name, host_badge_id, purpose, escort_required, escort_name, escort_badge_id, sign_in_time, sign_out_time
**Reconciles against badge records. Visitor with no escort + no badge entries = attack path.**

| # | Anomaly Found? | What is Normal | What is Not Normal | What It Could Mean |
|---|----------------|----------------|---------------------|---------------------|
|   | ☐ Yes ☐ No     |                |                     |                     |

**Correlation:** A signed-in visitor with an escort listed, but NO matching badge or camera activity in the escort's name. What does this quiet anomaly tell you?

---

## CROSS-SOURCE CORRELATION (Pair Discussion — 5 min)

**Time window to correlate:** 22:00 Oct 10 – 03:30 Oct 11

| Question | Notes |
|----------|-------|
| Which anomalies from different sources align in TIME? | |
| Which anomalies align in LOCATION? | |
| What SINGLE narrative explains multiple sources? | |
| Which anomaly is the "boring true alarm" (sensor) vs. the "quiet big one" (visitor log)? | |

---

## ALERT DESIGN (2.4.C)

**Good Alert Characteristics (Left Column)          | Noise Characteristics (Right Column)**
|--------------------------------------------------|--------------------------------------|
| Specific time                                    | Every door-open where doors are propped |
| Specific door                                    | Every motion trigger on a walkway    |
| Specific credential                              | Any alert when nobody is on duty     |
| Deviation from known pattern                     |                                      |
| Human can act within minutes                     |                                      |

**Who receives the 3 AM alert, and what are they doing at 3 AM?**

---

## EXIT TICKET (3 min — submit before leaving)

**One sentence:** "An alert is useful only if ________________________________________."

________________________________________________________________________________

________________________________________________________________________________