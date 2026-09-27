# U6 L02: CTF Session 6 Debrief — Network Forensics from the PCAP (May 7, Fri — P123)

**Date:** Fri May 7, 2027
**Unit:** 6 — Post-Exam and Portfolio
**Period:** P123
**Gradebook category:** Participation
**LOs:** 3.A–3.C (Detect attacks) · 1.A (analyse indicators) · 4.B (document findings for a non-specialist)

**Graded as: Participation.** 🔨 **MACHINE DAY — the first of the post-exam days, and the one that sets the pattern for every debrief in this block.**

**Two days ago the AP exam happened. That part of the year is over.** What is not over is the Saturday work, and this is the first of four debriefs in three weeks.

**Saturday May 8 was CTF Session 6 — Wireshark forensics.** Wait: that is *tomorrow*. Say that again, because it changes today entirely.

**Today is the prep, not the debrief.** The session runs tomorrow. **The artifact — the pcap writeup — is the deliverable, and it is the most directly portable piece of work in your entire portfolio.** A Wireshark analysis is a document an interviewer can read and understand in ninety seconds, and it demonstrates the exact skill the Credential Ladder keeps pointing at: taking raw evidence and producing a defensible narrative.

So today: the method, and the template. Tomorrow you get the capture. The writeup is written **after** the session, and it is written much better if you know now what a strong one contains.

---

## PART 1 — WHY A PCAP WRITEOUT IS THE BEST FIRST PORTFOLIO PIECE (10 min)

**A network capture is the closest thing cybersecurity has to a primary source.** Not a summary, not a report about something, not a claim — the actual bytes, as they crossed the network, unaltered. Every other artifact you have produced this year is an interpretation. This is the thing itself.

**And the professional value of analysing it is that there is exactly one correct procedure, and it is learnable.** Unlike most of security, where judgement is the hard part, network forensics is a discipline: you know what to look for, in what order, and how to prove what you found. **A student who has done this well is doing real work.**

**What the artifact proves to a reader, in order of how much it matters:**
1. **You can find evidence others miss.** The capture contains far more than you will find in the time available. Choosing what matters out of that is the skill.
2. **You can prove a claim.** Every finding in a forensic writeup is anchored to a specific frame, a specific field, a specific time. **No assertion without a citation** — the same rule you have used since the Apr 29 fluency check, and this is where it is most natural.
3. **You can build a timeline.** Reconstructing a sequence from interleaved traffic is the core forensic act, and it is a genuinely impressive thing to be able to do.
4. **You can tell a story to a non-specialist.** Which is the one that gets you the interview.

**The honest caveat, because it is the thing that catches people:** a pcap analysis written as a list of "I saw this packet" is worthless. **The value is entirely in the reasoning between the observations** — why this packet matters, what it implies about what happened before and after it, and what you can and cannot conclude from it. This is the same lesson as the capstone conversion on May 14, applied to a different medium.

## PART 2 — THE METHOD, BUILT FOR THE WRITEUP (18 min)

**This card is the template. Rebuild it cold and write it down — this is what you fill in tomorrow.**

### Phase 0 — Establish what you are working with, before you look at anything

**Never open a capture and start reading packets. Establish the shape first.**

- ☐ **Survey level:** what is here at all? The conversation and protocol layers present, the time range of the capture, the volume. A quick protocol hierarchy read tells you whether this is mostly TCP, mostly DNS, mostly TLS, and that changes everything about your approach.
- ☐ **The endpoints:** the distinct addresses and ports. **Write down the list of who is talking to whom.** This is the cast list, and you cannot understand a story without knowing the characters.
- ☐ **The conversations:** which pairs exchanged the most, which exchanged the most *bytes*, and which exchanged very little. **Asymmetry is a signal** — a host that received a lot and replied with almost nothing is behaving differently from the others.
- ☐ **The baseline:** what does ordinary traffic look like in this capture, and what is the volume and timing pattern? **Same rule as everything else this year: you cannot find a deviation before you know the norm.** A quiet capture and a capture with a burst in it are different investigations.

**Write the Phase 0 output into the writeup as the "data" section.** It is unglamorous and it is the foundation of everything after it, and a reader who skips it cannot follow your findings.

### Phase 1 — Filter, then look at what survives

**Filters are how you make a large capture tractable — and a filter with a wrong assumption loses the finding.** Use them, and record the ones you used, because the writeup's method section is *which filters, in what order, and why.*

- ☐ Conversation filters — the cast list, then focus on the pairs that matter.
- ☐ Protocol and port filters — the traffic type relevant to the hypothesis.
- ☐ **Content filters — used last, and used with suspicion.** A content filter finds what you already thought to look for. **The finding you did not expect will never be found by a content filter, which is exactly why you survey before you filter.**

### Phase 2 — Form hypotheses and test them

**The forensic habit: a hypothesis, a test, and a record of whether it survived.**

- ☐ *"Something is being resolved that a normal client would not resolve."* → look at DNS queries and answers.
- ☐ *"This connection carries more traffic, or more sensitive-looking traffic, than the role of the host suggests."* → look at what protocol and port the payload actually is, not what the label says.
- ☐ *"This host is talking to something it should not be, or at a time it should not be."* → the timeline, and the timing relative to the rest of the capture.
- ☐ *"Someone is authenticating and the pattern is wrong."* → the authentication exchange: how many attempts, from where, how long, and what the responses were.

**Test each one and write down the result, including the ones that failed.** The failed tests are what separate an analysis from a guess, and they are what a reader uses to judge whether your successful finding was method or luck.

### Phase 3 — Cite the frame, every time

**This is the rule that makes the writeup worth reading, and it is the same field-citation discipline from the rest of the year applied to a new medium.**

Not "there was suspicious traffic from an external host." Instead: *the specific frame number, the timestamp, the source and destination as seen in the header fields, the protocol and port, and the field or payload detail that makes it notable.* **A reader should be able to open the capture at exactly the frame you cited and see the thing you are describing, without asking you a question.**

**If you can make the citation exact enough that someone else can find it, you have met the standard. If you cannot, either find a better citation or downgrade the claim from "this is what happened" to "this is consistent with"** — and saying the second thing is more honest and more professional, not weaker.

### Phase 4 — Build the timeline

**Ordered, with each step cited.** Earliest evidence first, then each subsequent step, and each one anchored to a frame or a field. **Where a gap exists, mark the gap.** A forensic timeline that silently bridges an interval it cannot evidence is the most common way a forensic document becomes wrong.

**Then, for each step, ask: what benign explanation could this be?** Health checks, monitoring, software update traffic, a misconfigured client, a proxy, a legitimate administrative tool. **Naming the benign explanations and ruling them out is the mark of an analyst.** Where you cannot rule one out, say so — that is a limit, and limits are honest.

### Phase 5 — Determine what you cannot determine

**The limits section, and it goes in the writeup:**

- ☐ What the capture does not contain. **If the traffic was encrypted, say so plainly** — encrypted payload is opaque to you, full stop, and pretending otherwise is a real failure. What you can still do is analyse the *metadata* of the encrypted conversation: the endpoints, the timing, the volume, the duration, the pattern. **Encrypted traffic is not a dead end for forensics; it is an analysis of a different kind of evidence, and saying that is a more sophisticated answer than complaining about it.**
- ☐ What you did not have time to examine.
- ☐ What would have made the analysis conclusive and was not available.

**This paragraph is the most credibility-building part of the whole document.** Everyone deletes it.

### Phase 6 — Recommend specifically

Three things, and each must be specific enough to act on:
- ☐ **A control that would have prevented this.**
- ☐ **A detection that would have caught it earlier**, and from what source — and be honest if the available telemetry genuinely would not have caught it.
- ☐ **A logging or monitoring improvement** so the next analyst has more to work with. **The third one is what people forget, and it is the one that shows you are thinking about the system rather than the incident.**

## PART 3 — THE WRITEOUT SHAPE (10 min)

**This is the deliverable. One to two pages, the same shape you will use for the log analysis on May 13 and the web assessment on May 19 — learn it once, use it three times.**

**Headings, in order:**

1. **The question.** What you were asked to find, in one or two sentences. *(Nobody writes this and it is what makes a reader able to follow everything after it.)*
2. **The data.** The capture: what produced it, its time range, its volume, the endpoint inventory, the baseline. **And what it cannot show.**
3. **The method.** The phases you worked through, the filters you used and why, in an order someone could reproduce. **Reproducibility is the whole ballgame.**
4. **The findings.** Numbered. Each: what, the cited frame or field as evidence, the confidence, and the impact.
5. **The timeline.** The reconstructed sequence, with the benign explanations you considered and ruled out — or did not.
6. **The failed tests.** What you looked for and did not find, and what you think that means.
7. **The limits.** What the data cannot support, including the encrypted-traffic reality.
8. **The recommendations.** Prevention, earlier detection, better logging.
9. **What I got wrong first.** The wrong turns and what each taught you. **Do not skip this. It is the highest-value section in the document and it is the one every writeup omits.**

**Voice, and it matters more here than anywhere: "I."** You ran the analysis. A forensic document written in the passive voice reads as a report nobody stands behind, and a reader notices.

**Length discipline:** one to two pages. A four-page packet listing is a worse artifact than a two-page document that reasons, because nobody reads past page three and the reasoning is the value.

## PART 4 — SET UP FOR TOMORROW (7 min)

- ☐ **Re-read your own notes from the Unit 5 labs** and list the two or three analysis questions you could not answer then. **Bring those as your first targets tomorrow.** A debrief is worth more when it starts from a real open question.
- ☐ **Write the questions you expect to be able to answer from the capture, and the ones you expect not to.** The second list is as useful as the first — it is the limits section, drafted before you know the answers, which means you will not retrofit it to whatever you happened to find.
- ☐ **Open your portfolio repo and create the folder for this writeup with a stub README**, so tomorrow's output goes straight in.
- ☐ **Confirm the practice environment works.** The capture and the analysis tool need to be available tomorrow morning, and finding that out tonight is far better than finding out at 09:00.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief, and this one is genuinely about the evidence rather than about the job.**

**Question:** *what would a network capture from a Taiwanese organisation show that a US one would not?*

Answer it structurally, not by guessing at content:

- **The endpoints and the DNS.** **The domains, resolvers, and internal naming conventions of an organisation in this region are locally specific**, and a real capture shows them. Internal hostnames, service names, and the domain structure of local businesses and public-sector bodies are all visible in a capture. **That is a real forensic observation, and it is also why capture handling and retention are genuinely sensitive when personal data is involved.**
- **The traffic pattern of local services.** The mix of protocols and destinations in a local organisation's traffic reflects the services it actually uses, and those differ by region.
- **The supply-chain reality.** An organisation that depends on a small number of suppliers, or on a concentrated industry cluster, has a correspondingly narrow and specific network surface. **Concentration that is a national fact is a network fact, and a forensic analyst can see it in the endpoint list** — that is a genuine analytical insight rather than a talking point.
- **The data-protection dimension.** Where personal data appears in the traffic, the legal obligations from your May 18 lesson attach: what may be retained, who may read it, and how long. **Handling a capture is a compliance activity, not only a technical one, and being able to say that puts you ahead.**

**The portfolio line this produces:** *"I know what the evidence will not show before I start looking."* You will be able to say that truthfully, because you have now written the limits section by hand.

## CLOSE (2 min)

Hand in the nine-phase method card and the nine writeup headings.

**Next: Sat May 8 — CTF Session 6, Wireshark forensics.** The capture is yours tomorrow. **Mon May 10, P124 — portfolio assembly**, and today is the direct lead-in to that, because the PCAP writeup is the first thing going into the portfolio structure.

## TURN IN —

1. **The forensic method card**, all nine phases written from memory in your own words, with the **frame-citation rule** stated explicitly under Phase 3 and the **encrypted-traffic honesty rule** under Phase 5.
2. **The nine writeup headings**, with two or three sentences under each on what belongs there. Under "What I got wrong first," state specifically what you will record.
3. **Your two lists** — the questions you expect to answer and the questions you expect not to. The second list is graded harder, because naming what you will not be able to determine is the harder and more valuable skill.
4. **Confirmation that the practice environment works**, tonight, not tomorrow morning.
