AP Cybersecurity — Unit 5 · Lesson 5.8 (Period 82)   Name: ______________   Date: ______________

# Case Study: The Cold Card Hardware Wallet Hack (2026)

## 1: Before You Watch — Vocabulary (5 min)

Fill in the definitions as you watch. Use your own words.

| Term | Definition (your words) |
|------|------------------------|
| Hardware wallet | ___________________________ |
| Seed phrase | ___________________________ |
| Entropy (in cryptography) | ___________________________ |
| RNG / PRNG (software random) | ___________________________ |
| TRNG (hardware random) | ___________________________ |
| Private key | ___________________________ |
| Mempool | ___________________________ |

## 2: Comprehension — What Happened? (10 min)

Answer in complete sentences.

1. What is a Cold Card, and what was it designed to do?

   ______________________________________________________________________

2. The video's title says the "safest" way to store Bitcoin was hacked — no malware, no phishing, no physical access. What was actually broken?

   ______________________________________________________________________

3. A one-line firmware bug made the wallet generate its seed phrase using the wrong random number source. Name the two RNG sources the bug mixed up.

   ______________________________________________________________________

4. Why did a weak RNG let attackers guess wallet keys? (Think: what was predictable?)

   ______________________________________________________________________

5. About how many Bitcoin wallets were drained, and roughly how much was it worth?

   ______________________________________________________________________

6. **Exit question:** The victims' "rescue" was a race — they moved their money before the attacker could. Why couldn't they just patch the wallet and keep the same keys?

   ______________________________________________________________________

## 3: Discussion — The Mempool Rescue (10 min)

In the video, victims raced attackers to move their Bitcoin first, and some paid a mining pool to include their transactions directly. Discuss with your group:

- **"Trustless" money needed trust in a single miner.** What does that tell us about risk?
- Could a bank customer recover stolen money this way? What does that comparison say about cryptography vs. institutions?
- After an attack like this, what is the ONLY real fix for the victims?

Group answer (2-3 sentences):

   ______________________________________________________________________

   ______________________________________________________________________

## 4: Exit Ticket

1. One sentence: why does random-number quality matter for encryption?

   ______________________________________________________________________

2. Circle one: I understand why a weak RNG = weak keys — YES / MOSTLY / NOT YET

**Bonus (early finishers):** An attacker brute-forced seed phrases offline. Roughly how many guesses per second would an attacker need to try 7,000+ wallet addresses in days, not years? Write your reasoning in one or two lines.

   ______________________________________________________________________

---

## Teacher Notes & Instructions

**Setup checklist:**
- Projector + speakers; video link: https://youtu.be/2X2V3xv_jik (Fireship, 5:10)
- Skip the sponsor segment: last ~60 seconds (Lovable ad) — stop the video around 4:10 or after the rescue segment
- Printed worksheet, 1 per student (pencil fill-in)
- No student computers needed — this is a viewing + discussion period

**Pacing:** Vocab (5) → Comprehension (10) → Video in two passes: full 5:10 once, then replay 0:00–2:00 (root cause) if students missed it → Discussion (10) → Exit ticket (5) ≈ 45 min.

**Video accuracy note (numbers):** Video says 1,600 BTC / 7,000 wallets; independent reporting (Halborn, BlockSec, BleepingComputer, Coinkite advisory) says ~1,300–1,800 BTC across waves, ~7,300 addresses, ~$130M. Numbers are close enough — if a student asks, both figures are correct within reporting range.

**Key teaching points:**
- Root cause: firmware used MicroPython's deterministic PRNG (Yasmarang) instead of the STM32 hardware TRNG — a `MICROPY_HW_ENABLE_RNG` macro defined-as-zero passed a "defined" check. Small code bug, catastrophic effect.
- Seeds became predictable from chip serial + timer values → offline brute-force → match against blockchain addresses.
- **The irreversibility lesson:** a firmware patch cannot fix already-compromised keys. The only fix was migration to new keys — and the race in the mempool was the visible consequence. Ties to 5.9's "what if you lose the key" discussion.
- Bridges to: CED 5.1 (data vulnerabilities — weak key generation is a data vulnerability), CED 5.3 (cryptography — entropy, RNG, key management). Revisit in Unit 4.1 device vulnerabilities if desired ("remember the Cold Card?").

**Follow-up:** Homework due 20:30 — write 2 questions about key management you'd want answered before the OpenSSL lab (Lesson 5.9).
