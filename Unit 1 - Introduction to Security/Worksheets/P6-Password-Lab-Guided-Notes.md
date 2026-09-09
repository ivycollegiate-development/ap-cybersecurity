AP Cybersecurity — Unit 1 · Period 6 (Fri, Sep 11)  Name: ______________  Date: ______________

# Password Strength Lab — Guided Notes

**GitHub repo:** `ivycollegiate-development/apcyber-u1-password-strength-lab`

Follow along as the teacher walks through the lab structure, then complete the lab independently.

## 1: Lab Structure Overview

The repo contains three main parts:

| File / Folder | What it is |
|---------------|------------|
| `hashed_passwords.txt` | A file containing hashed passwords from a simulated breach |
| `crack.py` | A Python script that attempts to crack the hashed passwords |
| `README.md` | Your lab report template — fill this in as you work |

## 2: How Hash Cracking Works — Quick Reference

```
Password → [Hash Function] → Hash Value (looks like: 5d41402abc4b2a76b9719d911017c592)

Crack script reads: hashed_passwords.txt
          ↓
    Compares each hash against: dictionary words → common patterns → brute force
          ↓
    Outputs: password + hash + time-to-crack
```

**Key terms:**
- **Hash:** A one-way mathematical transformation of data. You can't reverse it — you can only guess inputs and compare.
- **Dictionary attack:** Tries common words, passwords from known breaches, and patterns.
- **Brute force:** Tries every possible character combination (slow for long passwords).
- **Salt:** Random data added to a password before hashing — prevents identical passwords from producing identical hashes.

## 3: Guided Activities

**A) Inspect `hashed_passwords.txt`**

Open the file. How many hashes are in the file? ________

What format are they in? __________________________________________________

**B) The cracker script — how hash types work**

The script detects the hash type (MD5, SHA-1, SHA-256) automatically. It uses the hash length and format to decide which algorithm to try.

| Hash Algorithm | Output Length (hex) | Example |
|----------------|:-------------------:|---------|
| MD5 | 32 chars | `5d41402abc4b2a76b9719d911017c592` |
| SHA-1 | 40 chars | |
| SHA-256 | 64 chars | |

Run the script with: `python3 crack.py`

**C) Results table**

As the script runs, record what it finds:

| Hash # | Cracked? (Y/N) | Password Found | Time to Crack | Algorithm |
|--------|:--------------:|----------------|:-------------:|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

## 4: Analysis

1. Which password cracked fastest? Why?

  ______________________________________________________________________

2. Which password took the longest (or didn't crack at all)? What made it stronger?

  ______________________________________________________________________

3. How does hash length affect cracking difficulty?

  ______________________________________________________________________

4. None of these hashes are salted. How would salt change the cracking process?

  ______________________________________________________________________

## 5: Lab Deliverable

Complete the `README.md` in your fork with:
- Your results table (from section 3 above)
- Your answers to questions 1–4
- A one-paragraph recommendation: *"What minimum password policy would you recommend for a school and why?"*

Create a PR with your completed README before the next class.