# U2 L7: Physical Vulnerabilities and Attacks (Oct 8, Thu — PAPER DAY)

**⚡ HW Quiz (5 min):** 4 MCQ on the risk register columns and residual risk.

**Learning Objectives:**
- 2.2.A Distinguish tailgating from piggybacking and describe how each works
- 2.2.B Describe shoulder surfing and identify what makes a credential easy to capture
- 2.2.C Compare social engineering at the door, card cloning, and lock picking as physical attack methods

**Materials:** Slides, printed school floor plan (one per student, handed out at the door), tailgating security footage on the projector, attack-method reference card

**No computers today.** Paper day — the floor-plan activity is on the printed plan.

---

## Activities

1. **Hook (5 min):** Play security camera footage of a badged office door where a second person walks in behind an employee, both authorized separately, and the door never registers a fault. No alarm. Nothing in the logs. Ask the class what the attacker actually did, and what the badge system reported. The badge system reported nothing wrong, which is the point — this is a *physical* attack that a technical control is blind to.

   Then the framing: **"Everything we have put in the register so far assumes the attacker has to get through a door. What if the door is the weakest part of the whole plan?"**

2. **Direct instruction (15 min):**
   - **Tailgating** — following an authorized person through a door they opened for you, with no interaction. Works on politeness: the person holds the door. Works on a badged door where the second person simply follows through before it re-locks.
   - **Piggybacking** — the same idea, but the attacker is usually socially known to the person, or belongs to a group the reader assumes belongs ("he's with the IT contractor"). Piggybacking is the more dangerous version because the front desk stops noticing.
   - **Shoulder surfing** — reading a PIN or password off a keypad, watching a badge tap, or observing an unlock pattern. The vulnerability is not the password being weak; it is the password being *entered where someone can see it*. ATM PIN pads got shields. Badge readers got anti-shielding designs. Note the tie to the "login" habits we discussed in Unit 1 — the attacker is not brute-forcing, they are transcribing.
   - **Social engineering at the door** — a uniform, a clipboard, a plausible reason, a deadline. "I'm with the vendor, we're supposed to be doing the panel replacement at 2, here's the ticket number." Door staff are the front line and are the easiest target because the job is to be helpful.
   - **Card cloning** — an RFID badge is a passive radio tag with a readable ID. A skimmer within a few centimeters copies the ID in milliseconds. The clone is then a valid card, and the badge log shows the cloned number entering — indistinguishable from the real one. This is the key insight: the log is *right* and the conclusion is still wrong.
   - **Lock picking** — mechanical, patient, needs physical access and time, and is genuinely different from the electronic methods above. Pin tumbler, rake, bump key, and a shim for a padlock or door. A "no unauthorized entry" claim from a pin tumbler lock is a claim about a skilled attacker with time, not about a determined one.

   Common thread to state explicitly: **five of these six are defeating a control by using it correctly.** The lock works. The reader works. The person held the door because that is what people do.

3. **Activity — "How would you get in?" (20 min):** Printed floor plan of this building, one per student. Work in pairs. Trace **three attack vectors** through the plan. For each, mark on the plan:
   - the entry point, marked with an X
   - the path to the target, arrowed
   - the control that should have stopped it at each step along the way, with the specific one you think should be added
   - the last point at which the attack would have been *detected* — and by what

   Good targets on the plan: the server closet, the attendance records room, the front office, the staff workroom door, the dumpster and recycling area, the bike storage, the side emergency exit, the second-floor balcony.

   Then: for each vector, state which attack method it uses. The same route often works two different ways — a side exit might be reached by pulling the door bar (physical) or by holding it open for someone with a badge (tailgating), and those need different controls.

4. **Close (5 min):** Each pair names one control to add and where. Collect the plans. Push on the class as a whole: *which single control, added to this building, breaks the most of the vectors you just drew?*

**Homework (due Fri 20:30 — Monday quiz):** Read the four case study briefs in tomorrow's jigsaw: RSA SecurID, Snowden, Stuxnet, and the Taichung fab incident. Each group will be assigned one. Quiz is on tailgating vs. piggybacking and on why cloned badges are hard to detect.

**Differentiation / ELL support:** The floor plan is pre-labelled with room names and the six control locations marked as blanks, so no time is lost on orientation. A printed attack-method reference card names each method with a one-line description and a sketch, which covers the vocabulary students need for the vocabulary portion of the exit response. Pairs may trace the three vectors in a shared short order (easiest to hardest) if that helps. The common thread — attacks that use a control correctly — is the concept to land; if a student is stuck on mechanics, have them answer only the "which control, and where" part.
