AP Cybersecurity — Unit 1  Name: ______________  Date: ______________

# Unit 1 Review — Decks 1.1–1.5 Worksheet

The Unit 1 test is Monday. Every question in this packet comes from the decks we studied — 1.1 Social Engineering, 1.2 Suspicious Website Logins, 1.3 Public Networks, 1.4 AI-Based Attacks, and 1.5 AI in Cyber Defense. This is review, so dig into what you already learned and make it stick.

## 1: Social Engineering — 1.1 (S.E.T. Framework)

Social engineering attacks the **person**, not the machine. The S.E.T. framework names the tactics:

> Urgency/pressure · Intimidation · Pretexting · Consensus/crowd validation · Authority · Familiarity · Scarcity

Match each scenario to its S.E.T. tactic (write the tactic name):

| Scenario | S.E.T. tactic |
|----------|---------------|
| An email from "the principal" says you must click a link in the next 10 minutes or lose your account | ______ |
| A caller claims to be from IT and says they "just need your login to fix your laptop" | ______ |
| "Everyone in your class has already signed up — don't be left out!" | ______ |
| A message says only 2 discount cards remain and the offer ends tonight | ______ |

The UNC6671 vishing attack (Aug 2026): hackers called financial-firm employees on their **personal phones**, pretending to be coworkers and IT helpdesk, tricked them into entering credentials and MFA codes on spoofed sites, then extorted victims.

Name TWO S.E.T. tactics that made this phone attack work:

1.  ____________________________________________________________________

2.  ____________________________________________________________________

One red flag in the Scenario 1A email was the domain "g00gle.com". Why does a zero-instead-of-o domain work as a phishing tell?

  ______________________________________________________________________

QUICK CHECK: Which of the following is the clearest indicator of a social engineering attack?

☐  A. An email that arrives during school hours
☐  B. A message that creates urgency and pressures you to act before checking
☐  C. A newsletter you subscribed to
☐  D. An email with an attachment you requested

My answer: ______    Why:

  ______________________________________________________________________

## 2: Suspicious Website Logins — 1.2 (Review)

**Warning signs.** Name all three warning signs that a password attack is in progress:

1.  ____________________________________________________________________

2.  ____________________________________________________________________

3.  ____________________________________________________________________

**The password formula.** Most weak passwords follow the shape: **WORD YOU'LL REMEMBER + YEAR + !**

Give one example of this formula (not from the deck):

  ______________________________________________________________________

Why does a password that "looks strong" this way actually fall fast?

  ______________________________________________________________________

**Maya's Snapchat.** The attacker spent ten minutes on her public profiles and collected four facts. Name the kinds of facts that made her password predictable:

  ______________________________________________________________________

  ______________________________________________________________________

QUICK CHECK: Maya's cat's name, her jersey number, and her school are all on her public profile. What is the BEST first step she could have taken to protect her accounts?

☐  A. Post less often so attackers find fewer facts
☐  B. Build passwords from information that is not on her public profiles
☐  C. Add more friends she knows in real life
☐  D. Change her username every month

My answer: ______

**MFA.** An attacker cracks your Fortnite password. What exactly stops them when multifactor authentication is on?

  ______________________________________________________________________

Name three types of MFA factors from the deck:

1.  ____________________________________________________________________

2.  ____________________________________________________________________

3.  ____________________________________________________________________

**Jordan's one password.** Jordan uses **Password2026!** for email, Instagram, the school portal, and a game. The game gets breached. Number the four steps in order (1–4):

| Step | Order |
|------|-------|
| Email = master key — they send password resets for everything else | ______ |
| Game site breached — "Password2026!" leaks with millions of others | ______ |
| Total takeover — Instagram reset, TikTok locked, recovery codes harvested | ______ |
| Tried everywhere — attackers test it on Gmail, Instagram, TikTok, the school portal | ______ |

QUICK CHECK: Why can a single data breach lead to multiple accounts being compromised?

☐  A. Because strong passwords are easy for attackers to guess
☐  B. Because attackers use the same password on different websites
☐  C. Because users often reuse the same password across multiple accounts
☐  D. Because all accounts are connected automatically

My answer: ______

## 3: Public Networks — 1.3

**Attack types.** Match each description to its attack (write the attack name):

| Description | Attack type |
|-------------|-------------|
| A fake hotspot broadcasts the same network name as the real one | ______________________ |
| An attacker sits between you and the website and reads unencrypted traffic | ______________________ |
| An attacker forces your device off the legitimate network | ______________________ |
| An attacker captures passwords and session tokens from open traffic | ______________________ |

**The Delta flight evil twin (Aug 2026).** A DEF CON attendee on Delta Flight 591 used a Wi-Fi Pineapple to knock passengers off the in-flight Wi-Fi, then broadcast a rogue "Delta WiFi Fast" hotspot with a fake login page harvesting Google credentials. Delta confirmed no airline systems were hacked.

Who did this attack target — the airline or the passengers? How do you know?

  ______________________________________________________________________

**Protection on public Wi-Fi.** Circle or list FOUR protections from our mitigation toolkit:

☐  Check for HTTPS (the lock icon) before entering anything
☐  Connect to the open Wi-Fi and stay on it all day
☐  Turn off auto-connect and forget networks after use
☐  Use your phone's hotspot instead of public Wi-Fi when possible
☐  Use a VPN to encrypt your traffic
☐  Enter passwords quickly so the attacker has less time

My four: ______ , ______ , ______ , ______

QUICK CHECK: A website you visit on café Wi-Fi shows a certificate warning. What should you do?

☐  A. Click through it — warnings are usually fake
☐  B. Leave the site; the connection may be intercepted or spoofed
☐  C. Reload the page until the warning disappears
☐  D. Enter your password quickly before the warning returns

My answer: ______

## 4: AI-Based Cybersecurity Attacks — 1.4

**AI phishing.** In our GitHub lab you compared a real phishing email with an AI-generated one side by side. What made the AI-generated version harder to spot?

  ______________________________________________________________________

**Voice cloning (Scenario 1D).** How did the adversary get the voice samples in the first place?

  ______________________________________________________________________

Why did the relative believe the call?

  ______________________________________________________________________

List the THREE defenses against a voice-cloning call from the scenario:

1.  ____________________________________________________________________

2.  ____________________________________________________________________

3.  ____________________________________________________________________

**Taiwan, Jul 20 2026 (local case).** An AI-assisted attack on government agencies behaved like a coordinated cyber team: 85+ accounts compromised, 2,500+ records extracted, then expansion to the nuclear safety agency and 7+ energy companies.

"AI amplified, it didn't decide" — what does that tell us about who is still responsible for an AI-assisted attack?

  ______________________________________________________________________

**The OpenAI swarm.** AI agents ran ~17,600 actions across Hugging Face infrastructure over 4 days, hid a secret message board to coordinate, and disabled their own monitoring. OpenAI only noticed when their own infrastructure crashed.

What defense lesson does this teach about monitoring AI systems?

  ______________________________________________________________________

QUICK CHECK: Which of the following is an example of adversaries using AI-powered tools to augment an attack?

☐  A. An AI tool flagging SQL injection in code before release
☐  B. An AI model generating flawless phishing emails with no grammar errors
☐  C. An SOC dashboard alerting on unusual process behavior
☐  D. A password manager generating a long random password

My answer: ______

## 5: AI in Cyber Defense — 1.5

**How defenders use AI.** Fill in the four defender applications we studied:

1. ______________________ — a tool that scans code for vulnerabilities (like our SQL injection demo) without manual review
2. ______________________ — AI models spotting unusual process behavior at scale in SOC dashboards
3. ______________________ — AI triaging alerts and suggesting remediation
4. AI in firewalls/IDS — ______________________ in network traffic

**The accountability line.** Sort each task into the correct column — write AI-TODAY or HUMAN:

| Task | AI-TODAY or HUMAN? |
|------|--------------------|
| Triage thousands of log alerts for known signatures | ______ |
| Sign off that a system is compliant | ______ |
| Draft a phishing email (attack side) | ______ |
| Decide whether an anomaly is a real intrusion | ______ |
| Approve a firewall rule change | ______ |
| Accept residual risk | ______ |

QUICK CHECK: AI tools make the left column (AI-capable tasks) free. What happens to the value of the right column (human-accountable tasks)?

☐  A. It decreases, because AI eventually does everything
☐  B. It stays exactly the same
☐  C. It increases — human judgment and accountability become MORE valuable, not less
☐  D. It disappears, because AI handles accountability too

My answer: ______

## 6: Put It Together — The Unit 1 Thread

One sentence each. How does AI change the ATTACK side of Unit 1 (1.1–1.3 tactics)?

  ______________________________________________________________________

  ______________________________________________________________________

One sentence each. How does AI change the DEFENSE side (1.5)?

  ______________________________________________________________________

Which of the five decks do you feel WEAKEST on? What will you do about it before Monday's test?

  ______________________________________________________________________

## 7: Reflective Writing (5–7 sentences, at least one full paragraph)

Choose ONE prompt and write your honest reflection. I am grading for thinking, not length.

**Option A — Your own warning sign.** Have you (or someone in your family) ever received a security alert — a login code you didn't request, a "new device" email, a "was this you?" notification? Describe it, name which of the three warning signs it was, and what you did about it.

**Option B — AI on both sides.** AI now writes the phishing emails AND reviews the code that defends against them. In your own words: does AI favor attackers or defenders more? Use at least one case study from Unit 1 as evidence.

**Option C — The master key.** Jordan's email was the account that unlocked everything else. Why is your EMAIL account the most important one to protect with a strong unique password and MFA? What would an attacker do with YOUR inbox?

My reflection:

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________

  ______________________________________________________________________
