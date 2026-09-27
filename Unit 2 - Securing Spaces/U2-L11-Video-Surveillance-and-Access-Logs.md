# U2 L11: Video Surveillance and Access Logs (Oct 14, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ from CED 2.3–2.4: preventive vs. detective controls, and what a badge log records that a camera does not.

**Learning Objectives:**
- 2.3.B Apply camera placement principles — choke points, overlap, coverage vs. cost — to a real floor plan
- 2.4.A Interpret access log fields (timestamp, badge ID, door, direction, result) and state what each does and does not prove
- 2.4.C Evaluate retention and storage policy as a security control with a legal and privacy cost

**Materials:** Slides, printed floor plan (ICA main building, one per group), camera markers and tape, badge log extract (one week, 120 entries) in the `unit2-labs` Google Drive folder, projector

---

## Activities

1. **Hook (6 min):** **"A badge was used at the east stairwell at 3:07 AM. The badge belongs to a senior who was at home. Does anyone notice?"**

   Poll the room: who finds out, and how fast? Most students say "the cameras" — then make them say what the camera operator is doing at 3 AM, and what a 3 AM clip actually shows (a shape, a jacket, a partial face). Then: the log is unambiguous and searchable, and nobody looked at it for three weeks.

   Frame the lesson: **prevention fails sometimes — every layer does. Detection is the layer that tells you prevention failed, and the question is always what is watching what, and for how long.**

2. **Direct instruction — camera placement (14 min):**
   - **Choke points.** Put cameras where people *must* pass. A camera covering an open hallway is a recording of nothing. Every door into a server room, every stairwell, the loading dock, the one gate that is the only way in.
   - **Overlap.** No single camera should be the only thing covering a critical area. One camera is a target — obscure it, spray it, power it, and that space is now unmonitored. Two cameras with overlapping fields is a design decision about *evidentiary redundancy*, not about count.
   - **Field of view vs. identification.** A wide lens sees more area and produces a face you cannot identify. A tight lens identifies and sees nothing else. Know which one you need before you mount it.
   - **Height and angle.** Above head height, angled down — for the reason you want full body and face, not for neatness. Backlit entrances produce silhouettes; the entrance needs fill light or the camera is decorative.
   - **Coverage vs. cost.** This is a budget argument, not a quality argument. Twenty cameras is not twice as good as ten if the ten were placed on the choke points. Justify every position in terms of *what it is for*.
   - **Retention.** Short retention (7 days) means the footage is gone before the investigation starts. Long retention (90 days) is a real cost — storage, and a larger privacy liability and breach target. Note the tension, and note that retention is a policy decision someone must own.

   Add the Taiwan context: apartment buildings in Taichung share a network cabinet, a bike area, and often a single guard post. The choke points are the elevator lobby, the cabinet room, and the bike storage — and cameras in a shared building must survive tenants who do not control them.

3. **Exercise A — place 8 cameras (15 min):** Each group gets the printed floor plan, a sheet of 8 numbered camera stickers, and 8 blank justification lines. Place all 8, then write one sentence per camera: **what it is for, and what would go undetected without it.**

   Rules: no camera may be justified as "general coverage" or "deterrence" alone. If a group cannot name the specific event it prevents the investigator from never learning about, it is in the wrong place. Two groups swap floor plans and check the worst-positioned camera — the question is whether the justification survives someone else reading it.

4. **Exercise B — a week of badge swipes (10 min):** Groups open the badge log extract in Sheets (or read the printed copy). Sort and filter to answer:
   - Which door generated the most entries? (choke point check — does the camera plan cover it?)
   - How many entries are between 10 PM and 6 AM, and who are those people?
   - Does the log record *direction* — entry, exit, or just "credential presented"? What investigation does that missing field make impossible?
   - Is there a badge that appears at two distant doors within a suspiciously short time?

   Debrief the structural point: a badge log tells you a **credential** was presented, not that a **person** was there. That gap is where Friday's anomalies live.

**Homework (due Fri 20:30 — Friday quiz):** Read the 2.4 lab handout for tomorrow. Bring one question about how you would analyze a log you have not seen.

**Differentiation / ELL support:** The floor plan is pre-numbered with the building's real zones (main hall, east wing, server closet, bike area, loading dock) so the argument is about placement, not about interpreting an unlabeled diagram. Camera marker and justification sheet are pre-structured one-per-line. Students who need a narrower task can be assigned the justification sentences for a group's already-placed cameras rather than placing all 8. Provide the log extract with a "sorted by time" default view so the analysis starts from organized data.