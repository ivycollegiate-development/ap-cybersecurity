AP Cybersecurity — Unit 5  Name: ______________  Date: ______________

# Cracking Enigma: From Rotors to AES

## 1: Warm-Up — Caesar to Enigma

Before we touch AES, we trace the family tree. Fill in as we discuss.

- A Caesar cipher shifts each letter by a **fixed number**. If I know the shift, I can decrypt anything. How many keys exist at most? ____________
- Enigma improved on Caesar by changing the substitution for **every single letter**. It did this with rotating ____________ plus a ____________ board that swapped letter pairs.
- The machine design was public. What actually protected the messages? ____________ (one or two words)

## 2: The 2-Minute Segment — AI Recovers a Lost 1941 Message

Watch the clip (we start it at 23:05 in class): https://www.youtube.com/watch?v=hygMRgnDD7w&t=1385s

- The cracked message was only **82 characters** long. Why did that small size make the job harder, not easier? ______________
- The AI did not just guess. It searched archives, compared unclear handwritten letters, and built its own ____________ ____________ to test settings.
- Roughly how many possible daily configurations did the exhibit estimate? ____________  (write it in plain words too: ____________)
- Was this fully autonomous? Circle one:  YES  /  NO — who chose the target and supplied crucial information? ____________

## 3: Explore the Exhibit — MVUEH

Open: https://mvueh-enigma-solved.carterl.chatgpt.site/ (runs in your browser, nothing to install)

The message reads: "Please specify the route of march. I am in Rosenow, Rosenow. Immediate reply by radio."

Steps (all ☐  boxes are ☑  when done — ☑  means skip):

☐  Read "The recovered message" and the recovered key panel.

☐  Find the settings: rotor order = ______ - ______ - ______,  rings = ______ ______ ______,  body start = ______ ______ ______.

☐  In "Decode the Header", set the windows to GTA and type KCI. What three letters light up? ______ ______ ______

☐  Notice the plugboard pairs (AC, BE, DG, FH, KN, MO, PR, SU, TV, XZ). What does each pair do to a letter before it reaches the rotors? ____________

Questions:

- The team's breakthrough used the repeated phrase "ROSENOWROSENOW" as a **guessed phrase** (a crib). Why does a guessed phrase shrink the search when brute force alone cannot check 159 quintillion settings? ____________________
- The **header** (GTA / KCI) carried the encrypted message start — but never the daily key itself. Both operators already shared the daily key. What modern security lesson is hiding in that design? ____________________
- The two surviving copies of the ciphertext disagreed at 8 positions. What does that tell us about why a cryptanalyst must test evidence, not just run a search? ____________________

## 4: Vocabulary — Write Each in Your Own Words

| Term | Definition (your words) |
|------|------------------------|
| Symmetric encryption | ____________________________ |
| Key management | ____________________________ |
| Key space | ____________________________ |
| Brute force attack | ____________________________ |
| Crib (guessed plaintext) | ____________________________ |
| Rotor machine | ____________________________ |

## 5: Bridge to the Lab — Enigma Lessons in Modern Crypto

Tomorrow's lab encrypts with AES the way the German army encrypted with Enigma: one shared secret key, encrypt and decrypt with the same key. List what modern symmetric crypto learned from Enigma's failures:

- Key length: Enigma's key space was huge for 1941 but searchable today with computers. AES-128 gives about ______ bits of security; AES-256 gives ______.
- Key distribution: the Enigma daily key traveled in codebooks. Today both sides of a TLS connection need a shared key too — but they never ship one in a codebook. Write one word for how they solve this: ____________  (we cover this in 5.4)
- Key reuse: Enigma's rule was "one message key per message, never repeat." What famous rule of symmetric ciphers does that foreshadow? ____________________

## 6: Exit Ticket

1. In one sentence: why did the Enigma daily key distribution — not the machine — turn out to be its weakest link?

  ________________________________________________________________

  ________________________________________________________________

2. Circle one: I can explain how a rotor machine is different from a Caesar cipher —
  YES  /  MOSTLY  /  NOT YET
