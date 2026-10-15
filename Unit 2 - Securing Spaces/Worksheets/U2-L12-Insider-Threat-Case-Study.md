# U2 L12: Detecting Physical Attacks — Insider Threat Case Study

**Name:** _________________________  **Period:** _____  **Date:** ___________

---

## Case Study: The OpenAI Boardroom Bug

**Source:** Fireship Code Report, "OpenAI's lead engineer was secretly a spy..." (Oct 14, 2026)  
**Video:** https://youtu.be/QZVzuq28eFw (watch 0:00–3:50)

**Summary:** Abdul Raman Alphazan, a 35-year-old engineering lead on OpenAI's Agents platform, planted a $23 Wi-Fi audio recording device (Seed Studio microcontroller + antenna) in the USB port of the TV in the executive conference room. He concealed it with toilet paper. The device operated for ~48 hours before OpenAI's Technical Surveillance Countermeasures (TSCM) team found it during a routine sweep.

---

## Detection Chain Reconstruction

For each detection point below, complete the analysis columns.

| # | Detection Point (What caught it) | Control Type (Preventative / Detective / Corrective) | Confidence (High / Medium / Low) | What Would Have Caught It **Sooner**? |
|---|----------------------------------|------------------------------------------------------|-----------------------------------|----------------------------------------|
| 1 | **TSCM sweep** (routine physical sweep found the device) | | | |
| 2 | **MAC address in network logs** (device's MAC appeared in DHCP/wireless logs) | | | |
| 3 | **Wife's ChatGPT history** (same MAC address pasted into ChatGPT two days earlier) | | | |
| 4 | **Security footage** (suspect at executive room door 6× on separate days) | | | |
| 5 | **Covert camera** (installed behind TV after device found; caught him returning Oct 5) | | | |

---

## Analysis Questions

**1.** The bug was physically crude — a $23 microcontroller wrapped in toilet paper. Why did it still take 48 hours and a *routine* sweep to find it?  
*Answer in 2–3 sentences:*

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

**2.** Name **one** control that would have detected this device on **Day 1** (the day it was planted), and explain why it would have worked.  
*Answer in 2–3 sentences:*

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

**3.** The criminal complaint charges *wiretapping* (secretly recording), not *espionage* (acting for a foreign power). In your own words, what is the difference in what the prosecution must prove for each charge?

________________________________________________________________________________
________________________________________________________________________________

**4.** The suspect was an engineering lead who *builds AI agents*. The detection chain relied heavily on AI/ML analysis (OpenAI "used their models to understand the device"). What does this case illustrate about the **dual-use nature of AI in cybersecurity**?  
*Answer in 3–4 sentences:*

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

---

## Exit Ticket (complete before leaving)

**The bug was physically obvious (toilet paper on a microcontroller). Why did it still take 48 hours and a routine sweep to find it? Name one control that would have detected it on Day 1.**

________________________________________________________________________________
________________________________________________________________________________