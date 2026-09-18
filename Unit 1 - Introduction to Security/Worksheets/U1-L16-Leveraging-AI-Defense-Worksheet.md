AP Cybersecurity — Unit 1  Name: ______________  Date: ______________

# Leveraging AI in Cyber Defense — Worksheet (Decks 1.5 + 1.2)

Today AI is the shield. This worksheet pairs Unit 1.5 (AI defense) with Unit 1.2 (suspicious logins), because the defender's AI watches for exactly the signs you studied in 1.2. Heads up: we are going back over deck 1.2 as part of this — Sections 3 and 4 lean on it, so treat those questions as review, not new material.

## 1: The Haystack Math (Deck 1.5, Cold Open)

One network logs **5,000,000** events today. Ten analysts could carefully review about **50,000** of them.

Fill in the numbers:

- Events analyzed by AI before human review: ______________
- Events a human team can realistically review: ______________
- Events nobody would ever look at without AI: ______________

In your own words, why can't human analysts do this alone? (Hint: it is NOT an intelligence problem.)

  ______________________________________________________________________

  ______________________________________________________________________

## 2: What the AI Defender Does (Deck 1.5, Lessons 1.5.1–1.5.2)

Match each AI defense job to what it actually does — write the letter:

| AI defense job | What it does |
|----------------|--------------|
| Configuration audit | ______ |
| Code vulnerability scan | ______ |
| Threat detection / filtering | ______ |
| Automated response | ______ |

A. Reads the whole codebase and flags patterns like SQL injection, XSS, and hardcoded credentials before attackers find them
B. Locks an account, blocks an IP, or quarantines a file in seconds — before a human is even awake
C. Reviews thousands of firewall rules and login settings against best practices, like a settings checkup for the whole company
D. Sorts millions of digital events against known attack fingerprints and surfaces the suspicious few

Vocabulary check — define in your own words:

| Term | Definition (your words) |
|------|-------------------------|
| Digital event | ___________________________ |
| Configuration audit | ___________________________ |
| False positive | ___________________________ |
| False negative | ___________________________ |
| Human oversight | ___________________________ |

## 3: The Warning Signs, Now Automated (Deck 1.2 review)

In 1.2 you learned the three warning signs of a password attack. Name all three:

1.  ____________________________________________________________________

2.  ____________________________________________________________________

3.  ____________________________________________________________________

Now the connection: an AI detection tool "knows" these signs automatically. Draw the line from each 1.2 warning sign to what the defender's AI does with it (write 1, 2, or 3):

| What the AI detection system does | Which 1.2 warning sign? |
|-----------------------------------|--------------------------|
| Flags a login from a country and device that don't match your history | ______ |
| Count dozens of failed logins in one minute as an attack pattern, not a typo | ______ |
| Treats 3:14 AM activity on a student account as a time-based anomaly | ______ |

QUICK CHECK (from deck 1.2, re-answer with 1.5 in mind): Which of the following is the clearest sign of a password attack in progress?

☐  A. Logging in successfully on the first try
☐  B. Receiving multiple failed login attempt alerts in a short period
☐  C. Updating your password regularly
☐  D. Logging in from your usual device

My answer: ______    Why:

  ______________________________________________________________________

## 4: When the AI Gets It Wrong (Deck 1.5, Part 3)

Classify each scenario — write **false positive**, **false negative**, or **correct call**:

1. Wi-Fi flags Mom's new tablet as an "unknown intruder." → ______________
2. The phishing filter passes a flawless AI-written phishing email. → ______________
3. The game locks an account after a login from another continent — and it WAS a hacker. → ______________
4. A Monday-morning flood of failed logins (hundreds of students fat-fingering passwords after a weekend) is flagged as an attack. → ______________

Which type of error do you think is more dangerous for a school network, and why?

  ______________________________________________________________________

  ______________________________________________________________________

## 5: Autopilot — or Ask a Human First? (Deck 1.5, Class Challenge)

The golden rule: **AI supports human decisions. It does not replace human judgment.** But some actions are safe to automate. For each, check ☐ Autopilot or ☐ Ask first, and write ONE reason (think: certainty of the threat, blast radius, reversibility):

| Action | ☐ Autopilot | ☐ Ask first | My reason |
|--------|-------------|-------------|-----------|
| Quarantine an email attachment matching known malware | ☐  | ☐  | |
| Lock a student account after a login from another continent | ☐  | ☐  | |
| Shut down the school's entire Wi-Fi network | ☐  | ☐  | |
| Block a website students keep visiting during class | ☐  | ☐  | |
| Push the AI's code fix to the live grade portal | ☐  | ☐  | |

What three criteria did the class keep using to decide?

  ______________________________________________________________________

## 6: Reflective Writing (5–7 sentences, at least one full paragraph)

Choose ONE prompt and write your honest reflection. I am grading for thinking, not length.

**Option A — The human in the loop.** The 1.5 deck says "AI brings speed and scale, humans bring context and judgment." Describe one moment from YOUR life when you were the human in the loop — an Instagram or bank security alert, a game account lock, a "was this you?" email — and explain whether the AI's call was right, wrong, or needed your context to decide.

**Option B — Two decks, one arms race.** In 1.2, attackers use automated tools to grind through password guesses; in 1.5, defenders use AI to grind through five million events. Both sides automated the same job. Does automation favor the attacker or the defender — and does the answer change if BOTH sides use AI?

**Option C — Trust.** An AI defender flags your account and locks it automatically, but it can't explain WHY, and sometimes it's a false positive. How much control over your own accounts should you hand to a system you can't inspect? Would your answer change for a school network? A hospital?

My reflection:

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

---

## Teacher Notes & Instructions

**Setup checklist:**
- ☑ Print one copy per student — paper day, no computers needed
- Decks: 1.5_Leveraging_AI_in_Cyber_Defense (slides 1–21) + 1.2_Suspicious_Website_Logins (25 slides) projected while students work
- Section 3 requires students to remember 1.2's three warning signs — allow peeking at the 1.2 deck's slides 5–7 if it was taught weeks ago
- Section 5 works best after a whole-class vote on each row; demand reasons for split votes
- Section 6: choose ONE prompt; share the sentence starter "The AI flagged... and I..."

**Answer key (quick reference):**
- §1: 5,000,000 / 50,000 / 4,950,000; volume + endurance problem, not intelligence
- §2: C, A, D, B
- §3: burst of failed logins; logins at times you'd never log in; unknown devices. Table: 3, 1, 2. Quick check: B
- §4: false positive / false negative / correct call / false positive; either answer defensible (FNs cause breaches; FPs cause alarm fatigue)
- §5: quarantine = autopilot (high certainty, reversible); lock account = autopilot (reversible); shut down Wi-Fi = ask first (huge collateral); block website = ask first (may block teacher sites); push code fix = ask first (could break live features). Criteria: certainty × blast radius × reversibility
- §6: grade for thinking — rubric: does the student connect AI's speed/scale to a human's context/judgment (A), reason about symmetry of automation (B), or stake a defensible position on trust with a real trade-off (C)
