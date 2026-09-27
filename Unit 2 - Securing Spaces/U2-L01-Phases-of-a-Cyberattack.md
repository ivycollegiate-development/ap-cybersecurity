# U2 L1: Phases of a Cyberattack (Sep 30, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on Unit 1 wrap-up (CIA triad, risk concepts, lessons from U1 labs).

**Learning Objectives:**
- 1.A Explain the six phases of a cyberattack and where defenders can intervene

**Materials:** Unit 2 vocabulary worksheet ([GDoc](https://docs.google.com/document/d/1G9xYu19JC8glSZsN7wcSDHrIOXMo5vQ27mm3yEwAlRU/edit)), slides, whiteboard, attack phase cards (see below), Taiwan threat brief

**🇹🇼 Taiwan Threat Brief (3 min):** Open the unit with one current TWNCERT advisory or iThome item relevant to attack chains. Keep it to three minutes — the point is local, current threat awareness, not deep reading.

---

## Activities

1. **Hook (5 min):** "How does a hacker go from 'I want to break in' to 'I have the data'?" Take three or four guesses before naming the phases. Most students will name steps out of order — that is the point of the sorting activity later.

2. **Direct instruction (20 min):** The six phases, in order:
   - **Reconnaissance** — gathering information about the target (OSINT, port scanning, employee directories, leaked credentials)
   - **Initial Access** — getting in (phishing, stolen password, unpatched service, supply chain)
   - **Persistence** — staying in (backdoor, scheduled task, new admin account, compromised SSH key)
   - **Lateral Movement** — spreading (pivoting to other hosts, credential reuse, trust relationships)
   - **Taking Action** — the objective (exfiltration, ransomware encryption, destructive action)
   - **Evading Detection** — avoiding notice throughout (living off the land, renaming tools, blending into normal traffic)

   Walk one real example end to end. Prefer a **Taiwan-targeted APT** if a current one is available — SolarWinds is the fallback. For each phase, ask: *what would a defender have seen here?* Anchor the phase list to observable evidence, not just attacker intent, because that is the bridge to detection later in the unit.

3. **Activity — attack phase sorting (15 min):** Groups of three or four take a set of action cards and arrange them into the correct phase order, then justify two of the placements. Suggested cards: "scans ports on the target subnet", "opens with a spearphished attachment from a vendor", "installs a scheduled task to re-establish access", "moves to the file server using a cached admin credential", "compresses and uploads the customer database", "renames the tooling to match installed admin software".

   Two cards are deliberately ambiguous — "uses PowerShell to enumerate shares" and "adds a new user to the finance group" — because a single action can serve more than one phase. Groups must decide which phase dominates and defend the call. This is the assessment: the reasoning matters more than the sort order.

4. **Exit ticket (5 min):** "Why does understanding attack phases help defenders?" Collect on paper or paper slips.

**Homework (due Tue 20:30 — Thursday quiz):** Finish the Unit 2 vocabulary worksheet (all four topic sections). Bring your completed risk matrix handout to Thursday's paper day.

**Differentiation / ELL support:** Provide the six phase names on a printed reference card so the sorting activity tests sequencing rather than vocabulary recall. For students who need more structure, pre-sorted example sets are available to compare against after their first attempt.
