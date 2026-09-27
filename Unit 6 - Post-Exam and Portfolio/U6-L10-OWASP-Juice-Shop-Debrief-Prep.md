# U6 L10: CTF Session 8 Debrief Prep — OWASP Juice Shop (May 19, Wed — P131)

**Date:** Wed May 19, 2027
**Unit:** 6 — Post-Exam and Portfolio
**Period:** P131
**Gradebook category:** Participation
**LOs:** 1.A–1.B (analyse application vulnerabilities) · 2.D (mitigate) · 4.B (document for a non-specialist)

**Materials:** Your Unit 5 Juice Shop lab notes, the writeup template from May 13, a clean sheet

**📄 PAPER DAY. Prep day, not the debrief.**

**Saturday May 22 is CTF Session 8 — OWASP Juice Shop.** It runs as scheduled. The debrief *writeup* is part of build day 2 on May 26, and **the template is today.**

**You have done Juice Shop once before, in Unit 5** — SQL injection and XSS against a deliberately vulnerable application, the lab from Lesson 5.4 of the unit plan. **You know more now than you did in February.** That is the entire point of running it again as a CTF session, and it is worth understanding why before Saturday.

---

## PART 1 — WHY THE SAME APP TWICE IS NOT THE SAME LESSON (8 min)

**The first time through Juice Shop, the question was "can I do this?"** You had a walkthrough. Someone showed you the payload. You executed it and saw a result. That is a demonstration, and demonstrations are low-value: you learn the mechanics and little about the method.

**The second time, the question is "can I find this without being told?"** In the Unit 5 lab the category was named for you. Saturday, nobody names the category. You are given a broken application and a list of challenges, and you have to decide where to look, form a hypothesis, test it, and either confirm or abandon.

**The difference between those is the difference between following a recipe and doing engineering**, and it is the single most important thing this session series has been teaching. Say this and let it sit.

**And the professional framing, which is what goes in the portfolio:** every real application assessment is done this way. Nobody hands a pentester a list of the vulnerabilities they will find. **The skill is not exploitation; exploitation is the easy part and it is automatable. The skill is deciding where to look and how to tell a real finding from a false positive** — and that is exactly what the writeup has to demonstrate.

**The safety frame, restated for Saturday, and it is not a formality:** Juice Shop is a deliberately vulnerable application, and the exercise is entirely legal and contained. Nothing outside the provided target. No scanning, no testing against any other system, no external targets, no real credentials anywhere near it. **The only systems in scope are the ones I hand you, and if you are unsure whether something is in scope, the answer is no until you ask.** This matters professionally: the boundary of an engagement is a legal document, not a judgement call.

## PART 2 — THE METHOD, SPECIFIC TO WEB (12 min)

**The general log-analysis method from May 13 applies, with a web-specific spine. Write this card — it is the template you fill on May 26.**

**Step 0 — Map the surface before attacking anything.**
What does the application do? Enumerate the features, the roles, the inputs, the outputs. **An assessment that starts by attacking rather than by understanding will miss things.** The features map is also what makes your writeup readable, because the reader needs to know what the application is before they can follow your findings.

**Step 1 — Establish the baseline.** For a web app: what does a normal request look like? What does the response look like? What is normal behaviour for a low-privilege user versus an anonymous one? Same rule as the logs — **you cannot find a deviation before you know the norm.**

**Step 2 — Form a hypothesis from the application's own logic.** The core offensive web skill. *This input is echoed back — is it being rendered, and how? This form takes an identifier — is the query behind it built safely? This authorization check happens after the action, or before it?* **Hypotheses come from reading the application's behaviour, not from a list of payloads.**

**Step 3 — Test it, and record the request and the response.** **For the writeup, the request and the response are the evidence.** Not "I tried XSS and it worked" — the actual request, the actual response, and what in the response shows the vulnerability rather than the possibility of it. This is the same field-citation rule from the log work: **a finding without a cited artifact is an opinion.**

**Step 4 — Confirm, or abandon, and write down which.** **Record the failed attempts.** What you tried that did not work is a large fraction of the value of the writeup, and it is what a reader uses to judge whether your successful finding was skill or luck. A finding you got on the first try with three failures before it reads as competent; the same finding with no failures reads as a screenshot.

**Step 5 — Assess.** What is the actual impact? Read the data that was accessible; what is the blast radius; is it authenticated or not; can it be automated. **The difference between "there is an XSS here" and "this XSS executes in the session of any logged-in user and can therefore be used to perform actions as them" is the entire difference between a scanner's output and an analyst's finding.**

**Step 6 — Remediate, specifically, per finding.** **The single most valuable sentence in a web writeup is the fix.** Not "sanitise input" — name the control: the specific place in the request path where validation belongs, the parameterisation of the query, the specific header or cookie attribute, the output-encoding context. **A finding without a fix is a complaint. A finding with a specific fix is work someone can merge.**

**Step 7 — State the limits.** What did you not test? What is out of scope? What would you need in order to go further — accounts you did not have, roles you did not hold, features you could not reach. **This paragraph is credibility.**

## PART 3 — THE WRITEUP SHAPE FOR A WEB ASSESSMENT (10 min)

**The eight headings from May 13, adapted. This is the deliverable of the card:**

1. **The target and the authorisation.** What the application is, where it runs, and the explicit statement of scope. **Put the authorisation boundary first, not last** — a professional assessment leads with its scope, and doing so in a student writeup is a strong signal.
2. **The feature map.** What the application does, and what I chose not to look at.
3. **The method.** How I worked, in an order someone else could reproduce.
4. **The findings.** Numbered. Each: what, the request and response as evidence, the confidence, the impact, and **the specific remediation.**
5. **The chain.** **If any findings compose into a path, show the path.** A stored XSS that steals a session combined with a privileged account is a different finding from either alone, and the chain is what an actual incident looks like. This is the highest-value paragraph in the whole document.
6. **The failed attempts.** What did not work and why you think it did not.
7. **The limits.** Untested areas, accounts not held, time constraints, what I would do next.
8. **What I would do differently.** Your process, not just your findings.

**Length: 1,500–2,000 words.** Longer than the capstone piece, because this one has more findings — and **each finding gets roughly equal space, which means a finding with a weak impact and a good writeup will be visibly less impressive than one with real impact.** That is a feature of the format, not a bug.

**Voice, again, and it matters more in this document than any other:** "I". You did the work. Write it as though a reader is going to ask you a hard question about it in a minute, because one day they will.

## PART 4 — PREPARE FOR SATURDAY (5 min)

- ☐ **List the three vulnerability classes you found in the Unit 5 lab.** You will probably find them again. **Knowing what you found before means you can check whether you found it the same way or a different way** — and "I found it differently this time" is a sentence worth having.
- ☐ **List two things you could not figure out in February.** Bring those as your first targets. A debrief is worth more when it starts from a real open question.
- ☐ **Re-read the Unit 5 writeup shape** — the SQLi, XSS, and path traversal remediation specifics from the unit plan — so your fix language is precise from the start rather than improvised under pressure.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief, on web applications and local relevance.**

**The observation worth making out loud:** Taiwanese organisations run a great deal of their customer-facing web surface on common platforms, and their distinctive local exposure is not exotic — it is **ordinary web applications handling ordinary personal data under PIPL.** That means the highest-value skill locally is not a novel exploit; it is correctly identifying and correctly remediating the standard application vulnerability classes on a system that holds regulated personal data.

**The framing for your writeup, and it is a genuinely strong professional sentence:** *the severity of a finding in an application holding personal data is not determined by the vulnerability class alone.* An unremarkable injection vulnerability in an application with no regulated data is a moderate finding. **The same class in an application holding personal data under a notification obligation is a reportable incident with a clock attached.** Write the impact assessment that way, and you will sound like someone who has read more than a vulnerability scanner.

**Second-order, and worth a paragraph in the writeup:** local threat actors routinely target the applications people in a region actually use, and the local regulatory environment shapes who has to be told. **The composition of a good local impact assessment therefore has two parts: what is technically possible, and who is legally owed notice.** Both. That is a candidate who can do the job.

## CLOSE (2 min)

Hand in the seven-step web method card and the eight writeup headings.

**Next: May 20–25 is thesis week. There is no school and nothing is scheduled.** The next class is **Wednesday May 26, P132 — portfolio build day 2: polish, README, screenshots, near-final.**

**Use the week deliberately.** You have the capstone draft from May 14, this template, and one week with no classes in this course. The realistic plan is that you finish the writing during the week and use May 26 for polish — or you write nothing this week and spend May 26 building from near-zero. **Both are legitimate. Only one of them is comfortable, and you know today which one you are choosing.**

## TURN IN —

1. **The seven-step web assessment method card**, written from memory, with the specific-evidence rule stated in step 3 and the specific-fix rule in step 6.
2. **The eight writeup headings** with two or three sentences each on what goes in that section — including what specifically goes in *The chain*, since that is the paragraph people forget.
3. **The three Unit 5 findings and the two open questions from February.** These are your Saturday starting points.
