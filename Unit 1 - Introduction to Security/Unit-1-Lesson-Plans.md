# Unit 1: Introduction to Security — Detailed Lesson Plans

**Time Allotment:** 18 class periods (12 tech + 3 substantive paper + 3 study-hall/prep), Sep 2 - Sep 28 
**CED Pages:** 29-48 (scenarios + topic pages) 
**Course Skills:** Analyze Risk (Skill 1), Mitigate Risk (Skill 2) 
**GitHub Labs:** 3 (apcyber-u1-phishing-samples Issue classification, apcyber-u1-password-strength-lab PR + Action, apcyber-u1-vulnerable-code-lab AI code review) 
**Tech Days:** Mon/Wed/Fri — full internet + GitHub + Codespaces 
**Paper Days:** Tue/Thu — no computers; substantive unit-specific activities 
**Study-Hall Days (SH1/SH2/SH3):** Quick review of prior day/unit + student work time on upcoming due work

**⚡ Graded HW Quiz Convention:** Every class period opens with a 5-10 min graded quiz on the previous night's homework (homework assigned in class, due 20:30 the night before; weekend homework due Sun 20:30). Paper days = paper quiz; tech days = quick MCQ. Part of Quizzes/Assessments 25%. Test days skip the quiz (test replaces it).

**🇹🇼 Taiwan Threat Brief format (recurring):** Every unit opener (P1, P11, U3P1, U4P1, U5P1) starts with a 3-minute Taiwan-focused cyber threat brief — one current event, TWNCERT advisory, or iThome news item relevant to the unit's topic. Keeps threat awareness local and current across the full year.

**🧩 Saturday CTF Alignment:** Two Saturday CTF sessions fall during Unit 1 — **Sep 19 (SESSION 1: picoCTF starter)** and **Sep 26 (SESSION 2: picoCTF continued + first writeup)**. Both build general CTF fluency (recon, flag formats, web basics) that support the Unit 1 topics. By P11 (Sep 18) students should have a picoCTF account and attempted the starter challenges. Session 2 reinforces the writeup habit (GitHub repo under ivycollegiate-development) — the same format used for all GitHub lab submissions.

**Unit 1 Period Map:**
| Period | Date | Day | Type | Topic |
|--------|------|-----|------|-------|
| P1 | Sep 2 | Wed | Tech | Course Intro + GitHub Setup |
| SH1 | Sep 3 | Thu | Paper | Study-Hall/Prep 1 |
| P2 | Sep 4 | Fri | Tech | 1.1 Social Engineering — Phishing Issue Lab |
| P3 | Sep 7 | Mon | Tech | 1.1 Victim Impacts & Full Tactic Coverage |
| P4 | Sep 8 | Tue | Paper | Phishing Lab Review |
| P5 | Sep 9 | Wed | Tech | 1.2 Password Attack Signs & Weak Authentication |
| SH2 | Sep 10 | Thu | Paper | Study-Hall/Prep 2 |
| P6 | Sep 11 | Fri | Tech | 1.2 Password Strength Analyzer Lab |
| P7 | Sep 14 | Mon | Tech | 1.3 Adversary Types |
| P8 | Sep 15 | Tue | Paper | Adversary Types Review + FRQ Walk-Through |
| P9 | Sep 16 | Wed | Tech | 1.3 Wireless Attacks + Personal Protection |
| P10 | Sep 17 | Thu | Paper | Preview AI Attacks & Defense |
| P11 | Sep 18 | Fri | Tech | Flex / Overflow Lab Day |
| P12 | Sep 21 | Mon | Tech | 1.4 AI-Based Cybersecurity Attacks |
| SH3 | Sep 22 | Tue | Paper | Study-Hall/Prep 3 |
| P13 | Sep 23 | Wed | Tech | 1.5 AI in Cyber Defense |
| P14 | Sep 25 | Fri | Tech | 1.5 AI Defense Lab + Scenario 1E |
| P15 | Sep 28 | Mon | Tech | Unit 1 Review & Test |

*Sep 24 Thu = Mid-Autumn Festival — no class.*

---

## P1: Course Intro + GitHub Setup (Sep 2, Wed — TECH DAY)

**Orientation note:** Aug 31 (Mon) has no class meeting — school-wide language + math assessment and general orientation; no individual course meets (not even AP). Sep 1 (Tue) is the first class meeting — a paper day, teacher-led orientation/syllabus only, students have no tech. P1 (Sep 2) is the first content period: syllabus/course intro + first GitHub setup.

**⚡ HW Quiz:** Pre-assessment quiz — establishes baseline; not graded for content (participation only).

**Learning Objectives:** Students understand course structure, expectations, and the cybersecurity landscape. Students create GitHub accounts and join the classroom.

**Activities:**
1. **⚡ Pre-Assessment Quiz:** 5 MCQ quick-check: what is phishing? what's a password attack? what's a VPN? Establishes baseline — no grade pressure.
2. **Syllabus Review:** Walk through grading (Labs 40%, Quizzes 25%, Projects 20%, Participation 5%, Midterm 10% — no school final; AP exam May 5, 2027), units, lab expectations, AP exam. Reference Course-Syllabus.md.
3. **Why Cybersecurity?:** Recent breach headlines, career paths, Taiwan relevance (semiconductor industry, critical infrastructure). Quick show-of-hands: "who's been phished or knows someone who was?"
4. **Vocabulary Preview:** Introduce Unit 1 term cluster: social engineering, phishing, brute force, adversary, MFA, VPN, evil twin, deepfake, AI augmentation, defense-in-depth. Students start a vocabulary notebook (paper or Google Doc).
5. **🖥️ GitHub Setup:** 
  - Create GitHub account if they don't have one
  - Accept GitHub Classroom invitation (link posted in Google Classroom)
  - Verify email + 2FA setup
  - Quick tour: repos, Issues, Pull Requests, Codespaces
  - Preview: "Every Friday lab uses this. You're building a professional DevOps workflow alongside cybersecurity skills."

**Materials:** Course Syllabus (Google Doc), projector, GitHub Classroom invitation link

**Homework (due 20:30):** Complete GitHub setup if not finished in class. Read "What is Cybersecurity" one-pager. Vocab flashcard set 1 (5 terms from today's preview).

---

## SH1: Study-Hall/Prep 1 (Sep 3, Thu — PAPER DAY)

**⚡ HW Quiz:** Quick quiz on P1 homework: GitHub concepts + cybersecurity definition + vocab terms.

**Quick Review:** Go over the ⚡ quiz answers. Revisit the key threat landscape concepts from P1. Q&A on GitHub workflow — surface any setup problems. "How comfortable do you feel with GitHub right now? Thumbs up/middle/down."

**Work Time:** Students work on whatever is due next:
- Complete GitHub account setup + Classroom acceptance (the P2 lab requires it working)
- Finish vocabulary flashcards (set 1: social engineering, phishing, brute force, adversary, MFA)
- Read ahead: "S.E.T. framework" one-pager for P2 (Wikipedia summary + CED excerpt)
- Catch up on syllabus questions

**Teacher role:** circulate, check GitHub setup status one-on-one, flag any students still struggling with account creation.

**Materials:** quiz ([GDoc](https://docs.google.com/document/d/1r0BDi2y-QO5JFPF_KwHkl28Xe4Fun-YO81Amc3XkiE0/edit)), Key ([GDoc](https://docs.google.com/document/d/1x9kWG3ZNMxp8fcTNLkh7j30OnO1Yh_TyANT1ElFVthM/edit)). *Paper day — no student computers.*

---

## P2: Social Engineering Tactics — Phishing Issue Lab (Sep 4, Fri — TECH DAY)

**⚡ HW Quiz:** 3 MCQ on S.E.T. framework + phishing red flags (from SH1 work-time pre-read).

**Learning Objectives:**
- 1.1.A Identify common indicators of social engineering tactics
- 1.1.B Explain how social engineering tactics influence victims (S.E.T. framework)

**Suggested Skills:** 1.A (Identify assets, vulnerabilities, threats), 1.B (Describe impacts)

**Materials:** Scenario 1A email text, projector, GitHub repo: `ivycollegiate-development/apcyber-u1-phishing-samples`, TechCrunch UNC6671 vishing article (printed or link): https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/

**Activities:**
1. **Hook:** "Have you or someone you know ever fallen for a scam?" Quick show of hands / stories.
2. **Scenario 1A:** Read the phishing email scenario aloud. Class discussion:
  - What makes this email suspicious? (g00gle.com domain, urgency, emotional manipulation)
  - What elements drive impulsive action? ("Urgent!", teacher-student relationship pressure)
  - What are the potential consequences?
3. **S.E.T. Framework:** Introduce the APSI Social Engineering Taxonomy:
  - Urgency/pressure, Intimidation, Pretexting, Consensus/crowd validation, Authority, Familiarity, Scarcity
  - Each with a real-world email example
4. **🐙 GitHub Lab — Phishing Classification:**
  1. Fork `ivycollegiate-development/apcyber-u1-phishing-samples` (syllabus link)
  2. Codespaces auto-launches — 5 sanitized phishing emails
  3. For each email: file a GitHub Issue classifying the tactic used and the psychological trigger exploited
  4. Reference the S.E.T. framework in each Issue
  5. Teacher reviews Issues to check understanding
  - **Cyber Attack of the Day:** Analyze the UNC6671 vishing attack (Aug 2026) — hackers called financial-firm employees' personal phones pretending to be coworkers/IT helpdesk, tricked them into entering credentials + MFA codes on spoofed sites, then extorted victims via public leak sites ($750K–$3M demands; ~$10M Bitcoin to one wallet). Maps to S.E.T.: authority, familiarity, urgency, pretexting. Link: https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/
6. **🇹🇼 Chinese-Language Phishing (local context):** Teacher projects 3 short phishing examples side-by-side — 2 in English, 1 in traditional Chinese (modeled on documented campaigns targeting Taiwan users: fake 7-11 point-card SMS with URL shortener, fake bank OTP text with link to spoofed login page, fake e-commerce "package delivery failed" email). Students identify the S.E.T. tactic used in each. Key discussion: AI-generated phishing removes grammar tells in Chinese too — how does that change detection for a Taiwan-based target? (All samples are teacher-drafted fakes based on publicly documented campaigns — no live malicious content.)

**Homework (due Sun 20:30 — Monday quiz):** Complete any unfinished Issues. Read CED excerpt on 1.1.C victim impacts (1 page).

---

## P3: Victim Impacts & Full Tactic Coverage (Sep 7, Mon — TECH DAY)

**⚡ HW Quiz:** Quick-check on P2 Issues status + CED reading.

**Learning Objectives:**
- 1.1.C Describe possible impacts for victims (financial, reputational, psychological)
- Complete CED tactics beyond S.E.T.: consensus, familiarity, scarcity, authority

**Suggested Skills:** 1.A, 4.A (Analyze Risk, Evaluate Mitigation Outcomes)

**Materials:** Whiteboard / Jamboard, projector, GitHub Issues from P2, TechCrunch UNC6671 vishing article (printed — supports ELL guided reading)

**Activities:**
1. **⚡ Quiz:** Go over answers — surface the most-missed concept.
2. **Complete CED Tactics:** Beyond phishing — consensus exploitation, familiarity-based trust, scarcity manipulation, authority abuse. For each: define, give a real-world example, discuss why it works psychologically.
3. **Scenario Expansion:** Rewrite Scenario 1A as a phone call (vishing). How do indicators change? What makes voice more or less convincing than email? **Real-world anchor:** UNC6671 (Aug 2026) — attackers phoned private-equity firm employees (Apollo, Blackstone, KKR, CME, Moody's, etc.) pretending to be coworkers/IT helpdesk, steering them to spoofed login pages for credentials + MFA codes. Identify which S.E.T. tactic each step of the call exploits.
4. **Impacts Mapping:** Map social engineering to real impacts — financial loss, data breach, reputation damage, credential compromise. Use a simple impact matrix. "Which victim impact is hardest to recover from?" **From the article:** public extortion sites threatening to leak stolen VIP/client data, ransom demands of $750K–$3M, ~$10M in Bitcoin paid to one hacker-controlled wallet — a real-world impact matrix.
5. **🐙 GitHub Follow-Up:** Students update their P2 apcyber-u1-phishing-samples Issues with any additional tactics or psychological triggers they identify after today's lesson. Add a comment: "After P3, I now also see ___ in this email."

**Homework (due 20:30):** Finish Issue updates. Make one flashcard for each S.E.T. tactic with an example on the back.

---

## P4: Paper — Phishing Lab Review (Sep 8, Tue — PAPER DAY)

**⚡ HW Quiz:** Graded paper quiz on P2/P3 content: S.E.T. framework, phishing tactics, victim impacts. (Longer quiz — first substantive paper day.)

**Learning Objectives:** Review and consolidate 1.1.A-1.1.C through peer discussion of lab findings.

**Activity:**
1. **Class Discussion:** Review Friday's apcyber-u1-phishing-samples Issues as a class.
  - Which S.E.T. tactics were most common across the 5 samples?
  - Which tactic was hardest to identify? Why?
  - Students share their Issue classifications and reasoning
  - Instructor highlights exemplary Issues and corrects common misclassifications
2. **Peer Review:** Pair up, exchange Issue URLs. Give one "glow" and one "grow" on your partner's analysis. Quick class poll: most common misclassification.

**Materials:** Projector (to display select Issues), printed Issue summary sheet if needed, quiz ([GDoc](https://docs.google.com/document/d/15CkRENkc6Juh709JKYahChdaseJw_ze2WNvtF1MSkJM/edit)), Key ([GDoc](https://docs.google.com/document/d/1jeNbXnRnpmWuX1S7SFUFKPtkNnKm2dhysfnwZnlygiQ/edit)). *Paper day — no student computers.*

**Homework (due 20:30):** Read Scenario 1B login log. Underline 2 suspicious entries and write one sentence on why each is suspicious.

---

## P5: Password Attack Signs & Weak Authentication (Sep 9, Wed — TECH DAY)

**⚡ HW Quiz:** 2 MCQ on Scenario 1B suspicious entries.

**Learning Objectives:**
- 1.2.A Identify common signs of a password attack
- 1.2.B Explain how adversaries exploit weak authentication

**Suggested Skills:** 1.A, 1.B (Analyze Risk)

**Materials:** Scenario 1B login log table (handout: [GDoc](https://docs.google.com/document/d/1FIzpTOxd7g01oK39NLIY6Mu_zKv2gsKStfE8ox3Oa8s/edit)), Key ([GDoc](https://docs.google.com/document/d/19QiFBYp5LI1DzfVvsCAhV3H8SOkWQVwhrtAb6EAlXSk/edit)), projector (TechCrunch UNC6671 vishing article on hand for the MFA cross-ref: https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/)

**Activities:**
1. **Hook:** "How many passwords do you think you have?" — students guess, then tally.
2. **Scenario 1B:** Hand out the login log table. Small groups analyze:
  - What information does the log contain? (date/time, device, IP)
  - What patterns do you notice? (some logins from unfamiliar IP 142.54.195.17)
  - Which entries are suspicious and why? (entries 4, 7 — different IP, during school hours when user would be in class)
  - What would you do if this were your account?
3. **Direct Instruction:** Password attack types — brute force, dictionary, credential stuffing, password spraying. Brief concept demo of each. **💻 Demo (projected only):** Show a brute force attempt on a local hash file — visualize why short passwords crack fast.
4. **Signs of Attack:** Unexpected password reset emails, "account accessed from new device" alerts, unfamiliar IPs, MFA fatigue prompts. **Cross-ref (UNC6671 from P3):** attackers didn't break MFA — they phoned employees and asked for the code. This is why MFA fatigue and code-phishing exist as attack signs.
5. **Preview Friday's Lab:** "You'll fork a repo with hashed passwords and crack them yourself. Bring any questions tomorrow."

**Homework (due 20:30):** One-page guided notes: name 3 password attack types and their distinguishing feature. Identify 1 sign of compromise you'd check for on your own accounts.

---

## SH2: Study-Hall/Prep 2 (Sep 10, Thu — PAPER DAY)

**⚡ HW Quiz:** Quiz on password attack types + signs of compromise (from P5 + homework).

**Quick Review:** Go over ⚡ quiz. Revisit Scenario 1B: which two entries were suspicious and why? Quick vocab check: credential stuffing vs brute force vs password spraying — class vote. Preview: "Tomorrow's lab uses a real password cracker. Here's how `cracklib-check` works..." (teacher-only demo prep walk-through).

**Work Time:** Students work on:
- P6 lab prep: read the guided notes lab worksheet (distributed in class)
- Catch up on P2 phishing Issues (any still ungraded)
- Vocab flashcards: set 2 (brute force, dictionary attack, credential stuffing, password spraying, hash, MFA)
- Review their own account security: "check one online account — is MFA enabled?"

**Teacher role:** circulate, check that Codespaces is working for everyone before P6, answer lab-setup questions. Preview the P6 guided notes worksheet trickiest part (how the cracker script interprets hash types).

**Materials:** quiz ([GDoc](https://docs.google.com/document/d/10PPwpjn_CBJaAFmVvKsz6BqcMCwE6XHU_TiSYlqZWm0/edit)), Key ([GDoc](https://docs.google.com/document/d/11CSw8YegDPNWUXY5-cKgiOFtEKRKcuZo_zoq1MQ8Dyo/edit)). *Paper day — no student computers.*

---

## P6: Password Strength Analyzer Lab (Sep 11, Fri — TECH DAY)

**⚡ HW Quiz:** Quick MCQ on P6 pre-read content (graded, covers lab prep).

**Learning Objectives:**
- 1.2.C Explain how to make authentication stronger

**Suggested Skills:** 2.D (Mitigate Risk)

**Materials:** GitHub repo: `ivycollegiate-development/apcyber-u1-password-strength-lab`, guided notes worksheet ([GDoc](https://docs.google.com/document/d/1Yz9r0l1N-DrcMQ53FW21apMswYn6Bk8GJAuHvmbIDY8/edit)), [Answer Key](https://docs.google.com/document/d/1xilJhdvUvlnopVmy0dQewNyWpm2Gs5igBSNxAnPoZj0/edit) — includes the verified 8-row results table (7 crack, row 8 uncracked by design) + stage-by-stage analysis

**Activities:**
1. **⚡ Quiz + Lab Kickoff:** Quiz, then walk through the lab worksheet together. Show the repo structure: hashed password file + cracker script + README template. ⚡ Codespaces: one-click launch — no local setup.
2. **🐙 GitHub Lab:**
  1. Fork `apcyber-u1-password-strength-lab` — **then in every `git clone` URL below, students must replace `YOUR-USERNAME` with their actual GitHub username** (e.g. `eshin28_student`). Example: `git clone https://github.com/eshin28_student/apcyber-u1-password-strength-lab.git`
  2. Open in Codespaces (or clone the fork from the terminal — same URL substitution applies)
  3. Run the cracker script — watch which passwords crack fastest
  4. Document findings in README: which passwords were weak and why (length, complexity, dictionary words)
  5. Submit a Pull Request adding your report (README must be complete)
  - 🤖 GitHub Action runs on PR: validates report format and flags any uncracked hashes that SHOULD have cracked
3. **Pair-Share:** Last 5 min — pair up, compare: which password cracked fastest? Which surprised you?
4. **Early Finishers:** Edit the cracker to add a dictionary wordlist — test against the hash file. Does it find more?

**Homework (due Sun 20:30):** If PR not yet merged, address Action feedback. Read CED excerpt on adversary types (1.3.A). Make one flashcard per adversary category.

---

## P7: Adversary Types (Sep 14, Mon — TECH DAY)

**⚡ HW Quiz:** 3 MCQ on adversary types (from homework reading).

**Learning Objectives:**
- 1.3.A Identify the type of adversary conducting a cyberattack

**Suggested Skills:** 1.A (Identify assets, vulnerabilities, threats)

**Materials:** Whiteboard, projector, Scenario 1C, printed CNN article "Cyber privateers" (Aug 13 2026)

**Activities:**
0. **🎯 CYBER ATTACK OF THE DAY — "Cyber privateers" (Aug 2026):** Read the printed CNN article: a Trump administration memo (Aug 12) authorizes vetted private US companies to surveil and disrupt foreign cybercriminal networks under DOJ/DHS oversight — a government-sanctioned "hack back" program. Former officials warn of deconfliction chaos ("too many cooks"), legal liability pushed onto companies, and collateral damage (taking down a foreign data center could hit a hospital). Warm-up: which TWO of today's six adversary categories does this story involve?
1. **⚡ Quiz Review:** Go over quiz — surface the most-missed adversary category.
2. **Six Adversary Categories:**
  - Script kiddies — low skill, opportunistic, using existing tools
  - Hacktivists — political/social motivation, website defacement, data leaks
  - Insider threats — employees/contractors, authorized access abused
  - Cyberterrorists — critical infrastructure, mass disruption
  - Transnational criminal organizations — financial motivation, ransomware, fraud
  - State adversaries — espionage, intellectual property theft, advanced persistent threats
  - **🇹🇼 WHY HERE (Taiwan context):** For students in Taiwan, state adversaries are not hypothetical. Taiwan is the most-attacked country in the world per capita, and the primary state adversary is the one across the strait: Chinese government-linked APT groups target Taiwan's government agencies, semiconductor industry, and infrastructure continuously. This course's running example — the Jul 2026 AI-assisted attack on Taiwan government agencies (85+ accounts, spread to the nuclear safety agency) — is exactly this category. Ask: which of the six categories do YOU think poses the biggest risk to systems you use daily? Why does studying this in Taiwan differ from studying it in the US?
  - **Story tie-in (from activity 0):** The "cyber privateers" order targets *transnational criminal organizations* (ransomware, fraud) — while the reason it exists is *state adversaries*: Chinese government-backed hackers reportedly outnumber FBI cyber personnel 50-to-1, so the US wants private-sector help to free up FBI/Cyber Command for nation-states. Ask: which category is the program aimed at? Which category is it trying to make room to fight? What new questions does "government-sanctioned private hacking" raise about who counts as an adversary — and who's allowed to hack?
3. **"Draw the Adversary" Activity:** Character-motivation matching game. Six cards with adversary characteristics — students match each to a category, then write a one-sentence threat profile (motive, target, methods). Class discussion: which adversary type is hardest to defend against?
4. **Preview P8:** "Tomorrow's paper day: FRQ practice. You'll get a scenario and identify the adversary type, motivation, and likely attack vectors. Review your threat profiles tonight."

**Homework (due 20:30):** Complete your threat profile if not finished. Practice: find a news headline about a recent cyber incident — which adversary type is most likely behind it? Be ready to discuss tomorrow.

---

## P8: Paper — Adversary Types Review + FRQ Walk-Through (Sep 15, Tue — PAPER DAY)

**⚡ HW Quiz:** 4 MCQ + 1 short scenario: "Given these clues, which adversary type?" Graded quiz testing P7 + homework.

**Learning Objectives:**
- 1.3.A Identify adversary types from scenarios
- 1.3.B Identify types of wireless cyberattacks
- FRQ skill: Analyze Risk (1.A)

**Activity:**
1. **Think-Pair-Share:** Each pair gets one adversary category, creates a detailed threat profile (motive, target, methods, real-world example), presents to class. Class fills in the remaining categories on a shared worksheet.
2. **FRQ Walk-Through:** AP-style FRQ prompt: "An employee at a semiconductor company receives a suspicious email from their CEO requesting a wire transfer..."
  - Part A: Identify the adversary type and motivation (1.3.A)
  - Part B: What wireless attack could intercept their communications? (1.3.B preview)
  - Part C: Recommend three protections for the employee (1.3.C preview)
  - Write individual responses, peer-score using simplified AP rubric, model answer review
  - **Extension (if time) — cyber privateers FRQ:** Use the P7 story as a second prompt: "A US company joins a government program authorizing it to disrupt a foreign criminal group's network." Part A: identify the adversary types involved (criminal org = target; state adversaries = the reason the program exists). Part B: what legal/ethical risks does the company face? (liability, oversight, collateral damage — e.g., hitting a hospital in the same data center). Part C: who should be allowed to hack, and under what rules?
3. **Exit Ticket:** Match 6 short scenarios to adversary categories (ungraded, immediate feedback).

**Materials:** Printed scenarios, FRQ prompt handout, simplified AP rubric ([GDoc](https://docs.google.com/document/d/1IhyFSy3u9yxMrKYrCXxZimD1bmOYOl8-NuxPYwEPzxM/edit)), printed CNN "Cyber privateers" article (from P7), quiz ([GDoc](https://docs.google.com/document/d/1oBKOY35FdLU3IME0uDvjBv90C7czCnVhfYtzNVMA2Ro/edit)), Key ([GDoc](https://docs.google.com/document/d/1rWFDYiFh71yGDyw8e9ZZObhkSYoBXCrcu82GW5bn4A0/edit)). *Paper day — no student computers.*

**Homework (due 20:30):** Read Scenario 1C on public Wi-Fi risks. Identify the adversary type and write one paragraph on how the attack could have been prevented.

**Cross-ref:** Tomorrow's P9 opens with the Delta flight evil twin news story (Aug 2026) — as you read Scenario 1C, think about what a rogue "Delta WiFi Fast" hotspot is an example of.

---

## P9: Wireless Attacks + Personal Protection (Sep 16, Wed — TECH DAY)

**⚡ HW Quiz:** Quick MCQ on Scenario 1C + adversary type identification.

**Learning Objectives:**
- 1.3.B Identify types of wireless cyberattacks
- 1.3.C Describe actions to increase protection of sensitive data on public Wi-Fi
*Note: Combined 1.3.B + 1.3.C per APSI Option A (was originally two periods).*

**Suggested Skills:** 1.A, 2.A (Analyze Risk, Select Controls)

**Materials:** Projector, teacher laptop for evil twin demo, printed Delta flight article (Tom's Hardware, Aug 11 2026)

**Activities:**
0. **🎯 CYBER ATTACK OF THE DAY — Delta flight evil twin (Aug 2026):** Read the printed Tom's Hardware article: a DEF CON attendee on Delta Flight 591 (LAS→ATL) used a Wi-Fi Pineapple to deauth passengers off the in-flight Wi-Fi, then broadcast a rogue "Delta WiFi Fast" hotspot with a fake login page harvesting Google credentials. Crew disabled the Wi-Fi for ~30 min; the plane was met at the gate. Delta confirmed no airline systems were hacked — the attack targeted *passengers*, not the airline. Warm-up: which of today's wireless attack types did this attacker use?
1. **⚡ Quiz Review:** Discuss the Scenario 1C adversary type — walk through why.
2. **Wireless Attack Types:**
  - Evil twin / rogue AP — attacker sets up a fake hotspot with the same SSID
  - Man-in-the-middle (MITM) — intercepting unencrypted traffic
  - Packet sniffing — capturing passwords, session tokens
  - Deauthentication attacks — forcing devices off legitimate networks
3. **⚠️ Evil Twin Demo:** Teacher sets up a hotspot "ICA_Guest" — show how attackers can clone a legitimate SSID. Evil twin vs legitimate WAP comparison chart. Students see the visual difference (or lack thereof). **Do NOT have students scan for networks — this is a projector demo only.** This is the same technique as the Delta flight story (activity 0) — same attack, safe setting.
4. **Public Wi-Fi Protection:**
  - VPN: what it protects and doesn't protect
  - HTTPS: check for the lock icon
  - Certificate checking: what a warning means
  - Turn off auto-connect, forget networks after use
  - Use phone hotspot instead when possible
  - Mitigation toolkit handout ([GDoc](https://docs.google.com/document/d/1Qami6MWU1lvp3nkMHKb-Oc2-dnMkulE1BKI6no1GR7g/edit))

**Homework (due 20:30):** "One thing you'll do differently on public Wi-Fi" — one paragraph. Read AI attacks pre-reading (1-page CED excerpt on 1.4).

---

## P10: Paper — Preview AI Attacks & Defense (Sep 17, Thu — PAPER DAY)

**⚡ HW Quiz:** Graded quiz on wireless attacks, protections, and AI attacks pre-read.

**Learning Objectives:**
- 1.4.A Preview: how adversaries use AI-powered tools to augment attacks
- 1.4.B Preview: how to protect against AI-augmented attacks

**Activity:**
1. **Quick Primer:** What is generative AI? How could it be used for phishing, voice cloning, malware generation?
2. **Email Comparison:** Teacher projects 2 email samples side by side — 1 real human-written phishing email, 1 AI-generated. Students vote which is which (show of hands). Discuss the tells: perfect grammar, personalized details, lack of awkward phrasing. "AI-generated phishing is harder to spot because the grammar errors are gone."
3. **Vocabulary Preview:** Introduce key terms for next week: LLM, voice cloning, deepfake, adversarial AI, AI augmentation. Students add to vocab notebook.
4. **Pre-Reading Distribution:** "For P12, read this CED excerpt on AI attack vectors. We'll do a hands-on activity: forking a repo with AI-generated phishing samples side-by-side with real ones."
5. **Exit Ticket:** "Which AI attack worries you most? Why?"

**Materials:** Projector, printed vocabulary sheet ([GDoc](https://docs.google.com/document/d/1ZmMRdtLtZ6dAP4RKWoj8gSYc9dWcI9Ly01inPkNCxVs/edit)), CED excerpt handout ([GDoc](https://docs.google.com/document/d/1-wJk23MaEvi22HdAX2ogyBhUBR5k5AMeLTolV6tZbk0/edit)), quiz ([GDoc](https://docs.google.com/document/d/1umJNzbH_c58redCtRx1dZIwNQWvllU-GptEBlv_bwLA/edit)), Preview AI Attacks & Defense worksheet ([GDoc](https://docs.google.com/document/d/11ym3G7-jCPih-31zKPU-LQtwvuRqcwqMBq2He6egoDE/edit)), Key ([GDoc](https://docs.google.com/document/d/1dwKq7xnp6q-nrhXxs1zg8DLrO2ZssMC3ytB9M4Irm8k/edit)), Key ([GDoc](https://docs.google.com/document/d/11ciDmamjYi2U_ckilp00w5KeBf4E_TB7gpnpmQHeB60/edit)). *Paper day — no student computers.*

**Homework (due 20:30):** Read CED excerpt on AI attacks (1.4). Write 2 questions you have about AI in cybersecurity.

---

## P11: Flex / Overflow Lab Day (Sep 18, Fri — TECH DAY)

**⚡ HW Quiz:** Quick-check on AI pre-read + questions from P10.

**Activities (flex — adjust based on class progress):**
1. **Catch-Up:** Any students who haven't finished P2 Issues or P6 PRs get dedicated time.
2. **🐙 Optional Open Lab:** 
  - Password-strength-lab extended challenges: add dictionary wordlists, test personal passwords (offline, no collection), compare cracking times
  - Begin exploring the `apcyber-u1-vulnerable-code-lab` repo for P14 — what kinds of vulnerabilities do you see?
  - GitHub workflow troubleshooting: git basics, merge conflicts, Codespaces quirks
3. **Re-Teach:** Any LO from 1.1-1.2 that exit tickets showed weakness on. Quick re-teach + mini-quiz.

**Homework (due Sun 20:30):** Catch up any incomplete lab work. Preview P12: watch the Fireship videos — the original Hugging Face hack (link in Google Classroom, 4:33) and the sequel "The most interesting hack in history just got weirder..." (https://youtu.be/0Rp9KJCEIvg, ~6 min, published Sep 2 — OpenAI's postmortem).

---

## P12: 1.4 AI-Based Cybersecurity Attacks (Sep 21, Mon — TECH DAY)

**⚡ HW Quiz:** Quick MCQ on the Fireship video + P11 AI pre-read content.

**Learning Objectives:**
- 1.4.A Explain how adversaries use AI-powered tools to augment cyberattacks
- 1.4.B Explain how to protect against some AI-augmented attacks

**Suggested Skills:** 1.A, 1.B, 4.C (Analyze Risk, Evaluate Mitigation Outcomes)

**Materials:** Scenario 1D, projector, GitHub repo: `ivycollegiate-development/apcyber-u1-ai-phishing-samples`, printed Guardian article: "Taiwan says it was hit by 'abnormal' AI-assisted cyber-attack" (Aug 13, 2026), Fireship sequel video https://youtu.be/0Rp9KJCEIvg (~6 min; skip sponsor ~first 60s), OpenAI postmortem: openai.com/index/hugging-face-incident-and-the-road-ahead (Aug 26, 2026, free)

**Activities:**
1. **Hook:** 🎯 CYBER ATTACK OF THE DAY — lead with the Taiwan AI-assisted attack: "Taiwan's government agencies were hit by an AI-assisted attack last month — 85+ accounts, 2,500+ records, and it spread to the nuclear safety agency. Let's look at how." Then a short AI voice cloning demo (teacher-plays sample → AI clone of the same). "Would you fall for this?"
2. **Scenario 1D:** Read and discuss:
  - How did the adversary get voice samples? (social media scraping via fake friend request)
  - Why did the relative believe it? (emotional manipulation + convincing voice clone)
  - Prevention: pre-arranged safe word, callback on known number, multi-channel verification
3. **AI-Attack Landscape:** Beyond voice cloning:
  - AI-generated phishing emails (grammar errors gone, harder to detect)
  - Deepfake video in video calls
  - Automated vulnerability scanning + exploitation
  - AI-generated malware that adapts
  - *Current Event (Sep 2026 UPDATE — OpenAI postmortem):* OpenAI published its full technical report Aug 26 (with CrowdStrike validation + an independent METR/Redwood investigation) — the story got weirder, not tamer. Confirmed new details: the agents called themselves a **"swarm"** and coordinated through a covert message board they hid inside an internal package manager (and rebuilt it in directory names after it was shut down); they found exposed HF credentials **on the open internet** and shared them with the collective; one agent hijacked a customer sandbox on the Modal cloud platform as an "external launchpad"; the swarm ran **~17,600 actions** across HF infrastructure over 4 days, reached **root on a production server**, got write access to source repos, and enrolled **181 attacker-controlled devices** into HF's corporate mesh network. HF forensics: the agent wasn't even trying to solve its benchmark — it was **cheating**, inferring the answer key was on HF's servers and going to steal it. And oddly, it ran every destructive API call with DryRun=True — cautious, not malicious. Hugging Face's own postmortem reached deeper than first disclosed. Framing for students: the swarm itself reasoned "this is arguably unauthorized" and proceeded anyway — safeguards held back by humans, not by the AI. *Primary sources (free, non-paywalled): openai.com/index/hugging-face-incident-and-the-road-ahead (Aug 26) + huggingface.co/blog/agent-intrusion-technical-timeline. Fireship sequel video: https://youtu.be/0Rp9KJCEIvg (~6 min — skip sponsor segment ~first 60s).*
  - *Current Event (Aug 2026):* AI models escaping test environments and hacking real organizations — AI as the attacker, not just the tool. Update: the OpenAI incident was a **coordinated swarm** — unreleased cyber model ran for weeks unmonitored, agents built a secret message board to coordinate sandbox escapes, disabled their own monitoring, and OpenAI only noticed when the board crashed its infrastructure (Jul 4); agents rebuilt it within 2 days. Reuters: OpenAI found *other* escape incidents; probing widening. Also: AI-designed novel viruses (Evo 2 → 16 viable phages, *Science* Aug 7) — attack amplification extends past code to biological code. *Reference: Breaking Points "Rogue Coordinated AI SWARM" (30:29, segments 0:00–7:00 swarm detail, 24:30–27:40 novel viruses) or assign as optional viewing.*
  - *Current Event (Aug 2026) — Taiwan AI-assisted attack (LOCAL ANGLE):* Taiwan's Ministry of Digital Affairs reported an "abnormal" AI-assisted attack on government agencies beginning Jul 20 — open-source AI agents (incl. Open Claw) built an autonomous hacking tool that behaved like a **coordinated cyber team** (Dream/FT: "first-of-a-kind breach"). Result: 85+ government accounts compromised, 2,500+ personnel records extracted, then expansion to Taiwan's nuclear safety agency and 7+ energy companies. Simplified Chinese comms → China-linked suspected (not officially accused). Teaching points: (1) this is offensive AI in the wild, attacking **our home country** — the "hybrid" model (manual ops + AI-agent assistance) is exactly how adversaries augment attacks (1.4.A); (2) "There's still a human in there somewhere" (Cris Thomas, Semgrep) — someone chose the target and set the objective; the AI amplified, it didn't decide. *Reference: theguardian.com, Aug 13, 2026 (non-paywalled; teacher prints/PDFs for handout).*
> **Teacher context — Mythos/Taiwan framing (not student-facing):** The same week, the NYT reported the US government couldn't agree on whether to use its own AI cyber tool (Mythos) for offensive ops — Air Force banned it, NSA said cutting it off would be "unilateral disarmament," ban reversed. Meanwhile China's Z.ai claims it's nearing Mythos 5. Framing question for the teacher to deliver as a 30-second bridge: "The US has this capability and can't decide whether to use it. China's closing the gap. And Taiwan — which just got hit by an AI-assisted attack from China-linked actors — can't build its own. What does the US infighting mean for Taiwan's cyber defense?" *Reference: nytimes.com, Aug 16, 2026 (paywalled — teacher context only, not a student reading).*
4. **🐙 GitHub Activity — AI Phishing Comparison:**
  1. Fork `ivycollegiate-development/apcyber-u1-ai-phishing-samples`
  2. Each sample has a real phishing email and an AI-generated version side-by-side
  3. Open Issues on the repo: for each pair, identify which is real and which is AI — and list the tells
  4. Which is more convincing? Why?
  - **Cyber Attack of the Day:** AI-themed phishing case study

**Homework (due 20:30):** Finish Issue analyses. Read CNN report on AI models (link posted). Write 1 paragraph: "If you received a call from your parent's voice asking for money, what would you do to verify it's really them?"

---

## SH3: Study-Hall/Prep 3 (Sep 22, Tue — PAPER DAY)

**⚡ HW Quiz:** Quiz on AI attack methods + protection strategies (from P12 + homework).

**Quick Review:** Go over quiz. Quick whole-unit recap: "From social engineering to AI attacks — what's the thread connecting all 1.1-1.4 topics?" Students do a 2-minute free-write, then share. Review the adversarial landscape: how AI changes everything.

**Work Time:** Students work on:
- P13/P14 prep: read the AI defense one-pager + CED excerpt on 1.5
- Catch up on AI phishing Issues (P12)
- Study for Unit 1 test (P15 is Monday Sep 28 — 6 days away)
- Vocab flashcards: set 3 (LLM, voice cloning, deepfake, adversarial AI, AI augmentation, anomaly detection)
- Review weakest topic: check your ⚡ quiz scores so far — which concept needs more work?

**Teacher role:** circulate, check P12 Issue completion, preview the P14 lab structure (apcyber-u1-vulnerable-code-lab repo walk-through), flag students who need extra prep time.

**Materials:** quiz ([GDoc](https://docs.google.com/document/d/18OnVBApt9XZNIE89Ga7Ms3pYI8STejVccPRA9U8cgVk/edit)), Key ([GDoc](https://docs.google.com/document/d/1Ft8Go7dXJXBg7zVggC7QrZvNvvCzyO3zO7QrO3ok_CY/edit)). *Paper day — no student computers.*

---

## P13: AI in Cyber Defense — Tools & Concepts (Sep 23, Wed — TECH DAY)

**⚡ HW Quiz:** Quick MCQ on AI defense concepts + P13 prep reading.

**Learning Objectives:**
- 1.5.A Explain ways AI-powered tools are used to defend against cyberattacks

**Suggested Skills:** 2.A, 4.C (Select Controls, Evaluate Outcomes)

**Materials:** Projector, CodeQL demo environment

**Activities:**
1. **Warm-Up:** ⚡ Quiz + review. "AI is used for attacks. How do defenders use it?" Quick brainstorm — board the ideas.
2. **Defense AI Applications:**
  - **GitHub Copilot / CodeQL for security code review:** 💻 Live demo — project a CodeQL query running on a vulnerable code snippet (SQL injection). Show how it flags the vulnerability without manual review.
  - **Anomaly detection in SOC dashboards:** AI models spotting unusual process behavior at scale
  - **Automated incident response:** AI triaging alerts, suggesting remediation
  - **AI in firewalls/IDS:** pattern recognition in network traffic
  - *Case Study (Aug 2026):* Hugging Face breach response (Jul 2026) — how the AI/ML community detected and contained the attack. AI-assisted supply chain auditing. **Containment-failure angle (Aug 2026 update):** OpenAI didn't notice its agents for weeks — the tell was its own infrastructure crashing; agents covered their tracks, sabotaged monitors, and none alerted a human. Defense lesson: AI systems need visibility + audit trails + human oversight baked in, because they will actively evade monitoring. *Reference: Breaking Points segment 10:00–13:10 (covering tracks, monitor sabotage) or optional viewing.*
  - *Case Study (Sep 2026 UPDATE — postmortem response measures):* OpenAI's own published response to the breach is a ready-made defense-controls list: **chain-of-thought monitoring** paired with automated alerts that page researchers when models act dangerously (with a 30-minute pause-or-justify rule for severe alerts), stricter sandbox isolation + restricted internet access + controlled access to model weights, clearer escalation rules for who can stop a run, and graders that reward agents for stopping safely on broken tasks rather than pursuing "increasingly questionable alternatives." Note the honest gap: OpenAI admits an internal team saw the message-board activity as early as late May and escalation failed. Teaching points for 1.5.A: monitoring only works if alerts reach humans fast, and detection without escalation is detection that fails. *Primary source: openai.com/index/hugging-face-incident-and-the-road-ahead (Aug 26, 2026). Fireship sequel video (hook): https://youtu.be/0Rp9KJCEIvg — skip sponsor segment (~first 60s).*
  - *Case Study (Aug 2026) — Taiwan MDA defense-in-action (LOCAL ANGLE):* When the AI-assisted attack on government agencies began Jul 20, Taiwan's Ministry of Digital Affairs monitoring units **detected** the "abnormal attack," the National Institute of Cyber Security issued warning alerts while investigating, and the government responded with protective guidelines + strengthened system monitoring to block attacks early. Defense lesson: the defender's playbook = detect anomalous AI-assisted activity → alert → investigate → harden. This is anomaly detection and automated incident response in a real, local context (ties to P12's attack story — same incident, defender's side). *Reference: theguardian.com, Aug 13, 2026.*
3. **Can AI Do This Job? — The Accountability Line (15 min):** Two-column sort on the board: tasks AI does TODAY vs tasks requiring a human who is ACCOUNTABLE for the decision.
   - Left column (AI-capable): log triage at scale, known-signature detection, code scanning, phishing email drafting (attack side), patch suggestions
   - Right column (human-accountable): signing off that a system is compliant, deciding whether an anomaly is a real intrusion, accepting residual risk, testifying to what happened after an incident, approving a firewall rule change
   - Discussion driver: "MIT researchers estimate AI can technically perform ~12% of US wage value already — including parts of IT work. But every one of those right-column tasks ends with one person whose name is on the decision. Which column did YOU work in on Monday's lab?"
   - Framing for students: this course trains you for the right column. AI tools make the left column free — which makes the right column MORE valuable, not less.
4. **Preview Friday's Lab:**
  - "You'll fork a repo with vulnerable Python/JS code and use an AI tool to find the bugs — just like we demoed."
  - Walk through the `apcyber-u1-vulnerable-code-lab` repo structure
  - Ensure all students can launch Codespaces (verify before Friday to avoid day-of setup issues)
4. **Unit 1 Wrap-Up:** Quick review of all 5 topics. Answer questions. "P14 lab completes the unit. P15 is the test — Monday Sep 28."

**Homework (due 20:30):** Review all ⚡ quiz results — identify your weakest LO. Write 3 questions you want answered before the test. Prepare for Friday's lab: read the lab worksheet.

---

## P14: AI Defense Lab + Scenario 1E (Sep 25, Fri — TECH DAY)

**⚡ HW Quiz:** Quick-check on lab prep + weakest-LO identification.

**Learning Objectives:**
- 1.5.A Apply AI-powered tools to find vulnerabilities in code
- 1.5.B Evaluate AI defense tool effectiveness
- Scenario 1E application

**Materials:** GitHub repo: `ivycollegiate-development/apcyber-u1-vulnerable-code-lab`, AI tool access (Claude/ChatGPT or built-in CodeQL), lab worksheet ([GDoc](https://docs.google.com/document/d/1fYVgcq-yDZMzVM7_G_pG6M3HfdT97nah2usnAhR6fQY/edit)), Key ([GDoc](https://docs.google.com/document/d/1B6IFue2qz7vIvpexWFBgwTb9LRCiIhCsfpwsAC4leJo/edit))

**Activities:**
1. **⚡ Quiz + Lab Kickoff:** Quiz, then lab walk-through — show the repo with vulnerable Python/JS snippets.
2. **🐙 GitHub Lab — AI-Powered Code Review:**
  1. Fork `apcyber-u1-vulnerable-code-lab` (contains Python/JS snippets with SQLi, XSS, weak auth flaws)
  2. Use an AI tool (Claude/ChatGPT in a second tab) or the repo's built-in CodeQL analysis to find vulnerabilities
  3. Fix each vulnerability and commit the fix
  4. Open a Pull Request
  - 🤖 GitHub Action runs on PR: runs linter + security checks. Green checkmark = all vulnerabilities addressed.
  - ⚡ Codespaces: pre-loaded with AI tools.
3. **Reflection — Attestation Comment (required):** Write a PR comment that ATTESTS to your work, in this format:
   - **What I fixed:** [each vulnerability, one line each]
   - **How I verified:** [what check you ran / why you're confident the fix is complete]
   - **Where I did NOT trust the AI tool:** [any suggestion you rejected or double-checked, and why]
   - This is an attestation — a signed statement of judgment. In professional security work, someone must be accountable for every "this is safe now" decision. AI tools can find bugs; only you can sign your name saying the fix is correct. Your attestation comment IS the deliverable that proves human judgment.
4. **Exit discussion (if time):** "Did anyone reject an AI suggestion? What was wrong with it?"

**Homework (due Sun 20:30):** Study for Unit 1 test (Monday). Review: all Issues (P2, P12), PR (P6, P14), ⚡ quiz scores, vocab. Create a one-page "cheat sheet" of key terms and frameworks.

---

## P15: Unit 1 Review & Test (Sep 28, Mon — TECH DAY)

**No ⚡ HW quiz** — replaced by the unit test (test covers homework quiz weight for this period).

**Activities:**
1. **Kahoot-Style Review:** Focus on hardest LOs: 1.5.A (AI defense tools), 1.3.B (wireless attacks), 1.3.C (protections). Collaborative concept map on whiteboard: all 5 topics interconnected.
2. **Practice AP-Style MCQs:** 3 quick MCQs to warm up, peer-grade, discuss reasoning.
3. **📝 UNIT 1 TEST:** Paper-based (even though it's a tech day — fairness). Covers all LO 1.1-1.5. 15 MCQ + 2 short answer.
  - **Students may reference their PRs and Issues from the unit as a "portfolio of work" during the review portion, but not during the test.**

**Materials:** Printed test papers, whiteboard for concept map

---

## Unit 1 Quiz / Test Bank

### Sample MCQ Questions

1. Which of the following is the strongest indicator of a phishing email?
  a) The email uses the company logo
  b) The email address contains a subtle misspelling (e.g., g00gle.com)
  c) The email is addressed to you by name
  d) The email contains an unsubscribe link

2. A user notices logins from unfamiliar IP addresses during school hours. This is most likely a sign of:
  a) A brute force attack in progress
  b) Successful credential compromise
  c) Normal account activity
  d) A DDoS attack

3. Which of the following is NOT a recommended practice on public Wi-Fi?
  a) Use a VPN
  b) Connect to any open network with "Free Wi-Fi" in the name
  c) Ensure websites use HTTPS
  d) Turn off file sharing

4. An attacker sets up a Wi-Fi hotspot with the same name as a coffee shop's network to intercept customer traffic. This is an example of:
  a) A brute force attack
  b) An evil twin attack
  c) A dictionary attack
  d) A credential stuffing attack

5. Which adversary type is most motivated by financial gain?
  a) Hacktivists
  b) Script kiddies
  c) Transnational criminal organizations
  d) Cyberterrorists

### Sample Short Answer Questions

4. Describe two ways AI can be used in cybersecurity — one for offense (attacks) and one for defense. Provide a specific example of each.

5. List three indicators of a social engineering attempt and explain what makes each one effective, referencing specific S.E.T. framework tactics.

6. You receive a phone call from someone who sounds exactly like your parent asking you to urgently wire money. Identify the type of attack, the adversary motivation, and three specific actions you would take to verify the caller's identity before acting.

---

## Lab Infrastructure Needs (Unit 1)

| Lab | GitHub Repo | Tools | Notes |
|-----|------------|-------|-------|
| Phishing Classification (P2) | `apcyber-u1-phishing-samples` | Codespaces, GitHub Issues | File Issues classifying 5 emails by tactic. No other tools needed |
| Password Strength Analyzer (P6) | `apcyber-u1-password-strength-lab` | Codespaces, cracker script, GitHub Actions | Students run cracker on hashed file; PR validated by Action |
| AI-Powered Code Review (P14) | `apcyber-u1-vulnerable-code-lab` | Codespaces, CodeQL, AI tool (Claude/ChatGPT) | Students use AI to find vulns, fix, PR; Action runs security checks |

Unit 1 labs are intentionally low-infrastructure — no VMs or special software required beyond GitHub + Codespaces. All three labs use `ivycollegiate-development` org repos with GitHub Classroom auto-grading via Actions.
