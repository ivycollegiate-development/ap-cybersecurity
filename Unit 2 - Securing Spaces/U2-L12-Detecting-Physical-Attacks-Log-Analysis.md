# U2 L12: Detecting Physical Attacks — Log Analysis and Alerting (Oct 15, Thu — PAPER DAY)

**⚡ HW Quiz (10 min):** Written quiz on camera placement principles and badge log fields, from Wednesday's slides.

**Learning Objectives:**
- 2.4.A Read badge and CCTV logs and identify the anomaly present in each record type
- 2.4.B Explain why no single log source is sufficient and what correlation adds
- 2.4.C Set alerting thresholds and justify them against false positive volume

**Materials:** Printed sample log set (ICA building doors — badge extract, CCTV exception report, sensor alert log, guard patrol report, visitor log), annotation sheet, highlighters, no computers

**No computers today.** Paper day — every log source is on the printed packet and the analysis is done with pen on paper.

---

## Activities

1. **Hook (5 min):** Put the server room door-open event on the board with a time stamp: **02:14, server room, door opened, alarm acknowledged, no response for 9 minutes.** Ask what happened in those 9 minutes that nobody wrote down. Then: the record exists, the alarm fired, and it is still in a queue three days later. The failure is rarely the sensor. It is the triage.

2. **Direct instruction — the five sources (12 min):**
   - **Badge / access log** — timestamp, badge ID, door, direction, result (granted/denied), reader health. Proves a credential was presented. Does not prove a person.
   - **CCTV exception report** — camera triggered an event: motion, line-crossing, door-open, loitering. Proves *something* happened in a field of view. Does not identify who, and the trigger is a rule, not an eye.
   - **Sensor alerts** — door-open-while-shut, motion in an unoccupied zone, glass break, temperature or power anomaly. Proves a physical state changed. Very hard to interpret alone.
   - **Guard patrol report** — time-stamped human observation, often narrative. Highest value per line and the lowest coverage. Gaps in a patrol schedule are themselves a finding.
   - **Visitor log** — who was signed in, by whom, for what purpose, and whether they were escorted. Reconciles against badge records: a visitor with no escort and no badge entries is a whole attack path.
   - **Entry/exit reconciliation** — comparing the set of people who entered against the set who left. A missing exit is a person still inside, which is either a much smaller incident or a much larger one.

   The principle: **each source is high-precision and low-recall on its own. Detection depends on reading several of them against each other over the same window of time.** That is 2.4.B, and it is exactly what next Monday's capstone asks students to do.

   Thresholds (2.4.C): a threshold is a *decision* to look, not a detection of fact. Denied-then-granted within N minutes, a badge on a door it never uses, any entry in an unstaffed-hours zone, motion in a zone with no scheduled activity. The tuning problem is not "how do we catch everything" — it is "how do we catch it without a queue nobody reads."

3. **Log annotation — find the anomaly (20 min):** Printed packet, five sources covering the same night. Individually first, 8 minutes, then in pairs. For each source, mark the anomalous line and write: what is normal here, what is not, and what it would mean.

   There is one planted anomaly per source, and they are not all the same type of event. For each, the question to answer is *what does this prove and what does it not prove*:
   - Badge log: a denied swipe followed by a granted swipe 40 seconds later at the same reader, and the same badge appearing at a different building entrance three hours earlier.
   - CCTV exception report: a line-crossing trigger on the loading dock camera at a time with no scheduled deliveries.
   - Sensor log: a door-open contact on a stairwell door that is mechanically held open during operating hours by policy.
   - Guard patrol: a patrol entry that skips the west corridor, with a reason field left blank.
   - Visitor log: a signed-in visitor, an escort listed, and no matching badge or camera activity in the escort's name.

   Push students past the first anomaly: the door-open contact is a *true* alarm that means nothing, and the missing escort line is *quiet* and means a great deal. A good analyst is suspicious of the boring one.

4. **Pair discussion — good alert vs. noise (5 min):** Two columns on the board. Left: what makes an alert *good* — specific time, specific door, specific credential, a deviation from a known pattern, something a human can act on within minutes. Right: what generates noise — every door-open in a building where doors are propped, every motion trigger on a walkway, any alert during a period when nobody is on duty to receive it.

   Then the real question: **who receives the 3 AM alert, and what are they doing at 3 AM?** This is the bridge to the badge lab tomorrow and to the correlation capstone.

   Tie to alert fatigue: an analyst who receives 40 low-value alerts a night stops reading by the 41st. The threshold that catches the one real event is worthless if it arrives buried. Note the Taichung fab context — night-shift security operations centres are staffed, but a small subcontractor office building is not, and the design has to assume that.

5. **Exit ticket (3 min):** One sentence — "An alert is useful only if ________." Collect on paper.

**Homework (due Fri 20:30 — Friday quiz):** Read the badge log lab handout. Confirm you can reach the VS Code server and open the lab folder before class. Tomorrow is a full technical lab on a ~500-entry badge log.

**Differentiation / ELL support:** The packet is sectioned by source with the field definitions printed in a margin key, so the work is the inference rather than the format. Students who need the task narrowed get a 2-source packet (badge log + sensor log) instead of all five, which is still a complete correlation argument. Provide a plain-language header row for each source naming what it records and what it cannot record. The good-alert discussion works orally first — pairs talk it through before anyone writes on the board.