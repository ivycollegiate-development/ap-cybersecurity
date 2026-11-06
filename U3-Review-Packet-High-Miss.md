# Unit 3 Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: 3 — Cryptography  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6 Questions)

### HM-013 | LO 3.1.C | Miss Rate: 76%
**Question**: Which property describes a hash function where finding **any input** that produces a given output is computationally infeasible?

A) Collision resistance  
B) Preimage resistance  
C) Second preimage resistance  
D) Avalanche effect  

**Correct Answer**: B  
**Distractor Analysis**:  
- A: Collision resistance = hard to find ANY two inputs with same hash  
- C: Second preimage = given input x, hard to find y ≠ x with H(y) = H(x)  
- D: Avalanche = small input change → large output change  
**Key Concept**: Preimage resistance = one-wayness. Given hash h, can't find input m where H(m) = h.

---

### HM-014 | LO 3.2.B | Miss Rate: 73%
**Question**: In **AES-256**, what is the block size and key size?

A) 128-bit block, 128-bit key  
B) 128-bit block, 256-bit key  
C) 256-bit block, 128-bit key  
D) 256-bit block, 256-bit key  

**Correct Answer**: B  
**Distractor Analysis**:  
- AES block size is ALWAYS 128 bits (regardless of key size)  
- Key sizes: 128, 192, or 256 bits  
- AES-256 = 256-bit key, 128-bit block, 14 rounds  
**Key Concept**: Block size fixed at 128 bits. Key size varies. Rounds: 10/12/14 for 128/192/256-bit keys.

---

### HM-015 | LO 3.3.A | Miss Rate: 81%
**Question**: **Diffie-Hellman key exchange** allows two parties to establish a shared secret over an insecure channel. What mathematical problem provides its security?

A) Integer factorization  
B) Discrete logarithm problem  
C) Elliptic curve discrete logarithm  
D) RSA problem  

**Correct Answer**: B  
**Distractor Analysis**:  
- Classic DH (modular exponentiation) = Discrete Logarithm Problem (DLP) in multiplicative group  
- A: RSA security = integer factorization  
- C: ECDH = Elliptic Curve DLP (variant, not classic DH)  
- D: RSA problem = recovering plaintext from ciphertext without private key  
**Key Concept**: DH security = given g^a mod p and g^b mod p, hard to compute g^(ab) mod p without a or b.

---

### HM-016 | LO 3.4.C | Miss Rate: 67%
**Question**: Which **digital signature scheme** provides **non-repudiation** and is based on **elliptic curve cryptography**?

A) RSA-PSS  
B) DSA  
C) ECDSA  
D) EdDSA  

**Correct Answer**: C (or D — both are ECC-based; ECDSA is NIST standard)  
**Distractor Analysis**:  
- A: RSA-based (factorization)  
- B: DSA = Discrete Log (modular), not ECC  
- C: ECDSA = Elliptic Curve DSA (widely used)  
- D: EdDSA = Edwards-curve DSA (modern, deterministic, also ECC)  
**Key Concept**: Both ECDSA and EdDSA are ECC-based. ECDSA is the traditional answer; EdDSA is modern improvement.

---

### HM-017 | LO 3.5.B | Miss Rate: 63%
**Question**: A **digital certificate** (X.509) contains a public key and identity information. Who signs the certificate to vouch for its authenticity?

A) The subject (owner of the key)  
B) The Certificate Authority (CA)  
C) The Registration Authority (RA)  
D) The Certificate Transparency Log  

**Correct Answer**: B  
**Distractor Analysis**:  
- CA = trusted third party that verifies identity and signs certificate  
- A: Self-signed = no third-party trust  
- C: RA = validates identity for CA, doesn't sign certs  
- D: CT Log = public audit log, doesn't sign  
**Key Concept**: PKI trust chain: Root CA → Intermediate CA → Leaf Certificate. Each signed by parent.

---

### HM-018 | LO 3.6.A | Miss Rate: 58%
**Question**: **Perfect Forward Secrecy (PFS)** in TLS ensures that:

A) Session keys are never reused  
B) Compromise of long-term private key doesn't reveal past session keys  
C) All traffic is encrypted with AES-256  
D) Certificates are automatically rotated  

**Correct Answer**: B  
**Distractor Analysis**:  
- PFS = ephemeral key exchange (DHE/ECDHE). Each session has unique key.  
- Long-term key (certificate private key) only used for authentication, not key derivation.  
- A: Partially true but not the definition  
- C: Cipher suite choice, not PFS  
- D: Certificate management, not PFS  
**Key Concept**: PFS requires ephemeral Diffie-Hellman (DHE or ECDHE). Static RSA key exchange does NOT provide PFS.

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-013 | 3.1.C | Unit 3 Topic 1.C | Hash Functions / Preimage Resistance |
| HM-014 | 3.2.B | Unit 3 Topic 2.B | AES / Block & Key Size |
| HM-015 | 3.3.A | Unit 3 Topic 3.A | Diffie-Hellman / Discrete Log |
| HM-016 | 3.4.C | Unit 3 Topic 4.C | Digital Signatures / ECC |
| HM-017 | 3.5.B | Unit 3 Topic 5.B | PKI / Certificate Signing |
| HM-018 | 3.6.A | Unit 3 Topic 6.A | TLS / Perfect Forward Secrecy |

---

## Mini-Lesson: Top 2 Missed LOs

### LO 3.3.A — Diffie-Hellman & Discrete Logarithm (Miss Rate 81%)

**Classic Diffie-Hellman**:
```
Public Parameters: Prime p, Generator g
Alice: Private a → Public A = g^a mod p
Bob:   Private b → Public B = g^b mod p

Shared Secret: Alice computes B^a mod p = g^(ab) mod p
               Bob computes A^b mod p = g^(ab) mod p
```

**Security**: Discrete Logarithm Problem (DLP)
- Given g, p, and g^x mod p, finding x is hard
- Best algorithms: Index Calculus, Number Field Sieve (sub-exponential)
- Key size: 2048-bit p minimum (3072 recommended)

**Elliptic Curve Diffie-Hellman (ECDH)**:
- Same protocol, but operations on elliptic curve group
- Security = Elliptic Curve Discrete Log Problem (ECDLP)
- Much smaller keys for equivalent security: 256-bit ECDH ≈ 3072-bit DH

**Key Sizes Comparison**:
| Security Level | DH (mod p) | ECDH | RSA |
|----------------|------------|------|-----|
| 128-bit | 3072-bit | 256-bit | 3072-bit |
| 192-bit | 7680-bit | 384-bit | 7680-bit |
| 256-bit | 15360-bit | 521-bit | 15360-bit |

**Common Pitfalls**:
- Static DH (same a,b reused) = no forward secrecy
- Must use ephemeral (DHE/ECDHE) for PFS
- Man-in-the-middle without authentication (need signatures/certs)

---

### LO 3.1.C — Hash Function Properties (Miss Rate 76%)

**Three Core Properties**:

| Property | Definition | Attack Goal |
|----------|------------|-------------|
| **Preimage Resistance** | Given h, hard to find m: H(m) = h | Reverse the hash |
| **Second Preimage Resistance** | Given m1, hard to find m2 ≠ m1: H(m2) = H(m1) | Find different input with same hash |
| **Collision Resistance** | Hard to find ANY m1 ≠ m2: H(m1) = H(m2) | Find any collision |

**Relationship**: Collision Resistance ⇒ Second Preimage Resistance ⇒ Preimage Resistance
- Collision resistance is strongest (hardest to achieve)
- Birthday attack: collision in ~2^(n/2) operations (n = output bits)
- Preimage attack: ~2^n operations

**SHA-256 Example**:
- Output: 256 bits
- Preimage resistance: ~2^256 operations
- Collision resistance: ~2^128 operations (birthday bound)

**Common Confusions**:
- "One-way" = Preimage resistance
- "Collision-free" = Collision resistance (impossible; just hard)
- MD5/SHA-1 broken for collisions, but preimage still hard

---

## Practice Set (5 New Items)

### P11 | LO 3.1.A
**Question**: The **avalanche effect** in a cryptographic hash function means:

A) Output length is double input length  
B) A 1-bit input change flips ~50% of output bits  
C) Hash computation time increases exponentially  
D) Collisions are impossible  
**Answer**: B — Avalanche = small change → large, unpredictable output change. Desirable property.

### P12 | LO 3.2.A
**Question**: **AES** is a:

A) Stream cipher  
B) Asymmetric cipher  
C) Block cipher  
D) Hash function  
**Answer**: C — AES = Advanced Encryption Standard, symmetric block cipher (128-bit blocks).

### P13 | LO 3.4.A
**Question**: **RSA signatures** use the private key for:

A) Encryption  
B) Decryption  
C) Signing  
D) Key exchange  
**Answer**: C — Signing = private key operation. Verification = public key. (Mathematically similar to decrypt, but purpose is signing).

### P14 | LO 3.5.A
**Question**: In **PKI**, a **Certificate Revocation List (CRL)** contains:

A) All valid certificates  
B) Serial numbers of revoked certificates  
C) Public keys of all CAs  
D) Hashes of root certificates  
**Answer**: B — CRL = list of revoked cert serial numbers, signed by CA, published periodically.

### P15 | LO 3.6.B
**Question**: **TLS 1.3** removed support for which key exchange mechanism?

A) ECDHE  
B) DHE  
C) Static RSA  
D) PSK  
**Answer**: C — TLS 1.3 only supports ephemeral key exchange (DHE/ECDHE) for PFS. Static RSA removed.

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-013 | B | 3.1.C | Preimage = one-way |
| HM-014 | B | 3.2.B | AES block=128, key=256 |
| HM-015 | B | 3.3.A | DH = Discrete Log |
| HM-016 | C | 3.4.C | ECDSA = ECC signature |
| HM-017 | B | 3.5.B | CA signs certificates |
| HM-018 | B | 3.6.A | PFS = ephemeral keys |
| P11 | B | 3.1.A | Avalanche = 1 bit → 50% flip |
| P12 | C | 3.2.A | AES = block cipher |
| P13 | C | 3.4.A | Private key = sign |
| P14 | B | 3.5.A | CRL = revoked serials |
| P15 | C | 3.6.B | TLS 1.3 = ephemeral only |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| 3.3.A | Diffie-Hellman / DLP | ___ | Mini-lesson, key size table | Apr 20 |
| 3.1.C | Hash Properties | ___ | Mini-lesson, 3 properties | Apr 20 |
| 3.2.B | AES Parameters | ___ | Memorize block/key/rounds | Apr 21 |
| 3.6.A | PFS / TLS | ___ | TLS 1.2 vs 1.3 comparison | Apr 21 |
| 3.4.C | ECC Signatures | ___ | ECDSA vs EdDSA | Apr 22 |
| 3.5.B | CA Role | ___ | PKI trust chain diagram | Apr 22 |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*