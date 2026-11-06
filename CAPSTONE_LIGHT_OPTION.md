# Capstone Light Option — Threat Model + Pseudocode + Test Plan

**For students who cannot complete implementation due to lab readiness issues**  
**Maximum Score**: 60/100 pts  
**Declaration Deadline**: Mar 26, 2027 (notify teacher via email)

---

## When to Use Light Option

- Your chosen lab fails the Mar 24 Codespaces readiness check
- You encounter blocking technical issues that cannot be resolved in time
- You declare intent by **Mar 26** (cannot switch after this date)

---

## Light Option Deliverables (Due Mar 31, 8:00 AM)

### 1. Threat Model Document — 25 pts (same as full)
- Complete `THREAT_MODEL.md` using provided template
- STRIDE analysis with all required sections
- Risk prioritization with mitigations

### 2. Pseudocode Design Document — 20 pts
**File**: `PSEUDOCODE.md`

| Section | Requirements | Points |
|---------|--------------|--------|
| **Algorithm Overview** | High-level description of core algorithms (encryption, rule evaluation, policy decision, anomaly detection) | 5 |
| **Data Structures** | Define all key data structures (structs/classes, fields, invariants) | 5 |
| **Core Functions** | Pseudocode for 3–5 critical functions with pre/post conditions | 8 |
| **Error Handling** | How failures are detected, logged, recovered | 2 |

**Pseudocode Style Guide**:
```
FUNCTION encrypt_file(password, input_path, output_path):
    // Pre: password is non-empty string, input_path exists and readable
    // Post: output_path contains encrypted file, or exception raised
    
    salt ← generate_random_bytes(32)
    key ← argon2id(password, salt, time=3, memory=64MB, parallelism=4)
    
    nonce ← generate_random_bytes(12)
    cipher ← AES-GCM(key)
    
    TRY:
        OPEN input_path FOR READING
        OPEN output_path FOR WRITING
        WRITE header: MAGIC + VERSION + salt + nonce
        
        WHILE not EOF(input_path):
            chunk ← READ 64KB
            ciphertext, tag ← cipher.encrypt(chunk, nonce)
            WRITE chunk_length + tag + ciphertext
            nonce ← increment(nonce)  // Critical: never reuse!
        
        WRITE trailer: final_auth_tag
    CATCH IOError:
        DELETE output_path if partial
        RAISE EncryptionError("Failed to read/write file")
    END TRY
    
    RETURN success
```

### 3. Test Plan — 15 pts
**File**: `TEST_PLAN.md`

| Section | Requirements | Points |
|---------|--------------|--------|
| **Test Strategy** | Unit, integration, security, property-based testing approach | 3 |
| **Test Cases** | Minimum 15 test cases covering: happy path, edge cases, security properties, error conditions | 8 |
| **Security Test Cases** | At least 5 tests specifically for security properties (e.g., "nonce reuse fails", "wrong password fails", "tampered ciphertext rejected") | 4 |

**Test Case Format**:
| ID | Category | Description | Input | Expected Output | Security Property |
|----|----------|-------------|-------|-----------------|-------------------|
| TC-01 | Happy Path | Encrypt/decrypt small file | password="test", 1KB file | Decrypted == original | Confidentiality |
| TC-02 | Security | Wrong password fails | Encrypt with "A", decrypt with "B" | Exception raised | Key separation |
| TC-03 | Security | Tampered ciphertext rejected | Flip 1 bit in ciphertext | Auth tag verification fails | Integrity |
| TC-04 | Edge | Empty file | password="test", 0 byte file | Valid encrypted file | Robustness |
| TC-05 | Edge | Large file (1GB) | password="test", 1GB file | Decrypted == original | Streaming works |

---

## Demo Adjustment (35 pts → same weight)

**Instead of live demo**: 3-minute **Design Walkthrough**
- Present threat model highlights (2 risks + mitigations) — 30 sec
- Walk through pseudocode for core algorithm — 90 sec
- Explain test plan security cases — 30 sec
- Q&A — 1 min

---

## Grading Summary (Light Option)

| Component | Full Option | Light Option |
|-----------|-------------|--------------|
| Threat Model | 25 | 25 |
| Implementation | 40 | — |
| Pseudocode | — | 20 |
| Test Plan | — | 15 |
| Demo / Walkthrough | 35 | 35 |
| **Total** | **100** | **60 (max)** |

**Course Grade Impact**: 60 pts → 12% of 500 pts (vs 20% for full)

---

## Important Notes

- Light Option **cannot** be upgraded to full option after Mar 26
- You still present on Mar 31 (design walkthrough)
- Pseudocode must be detailed enough for a competent developer to implement
- Test plan must be executable (not just "test encryption")
- All three documents submitted via `capstone/` branch

---

## Declaration Process

1. Email teacher by **Mar 26, 23:59** with subject: `Capstone Light Option — [Your Name] — [Lab Number]`
2. Teacher confirms eligibility (lab failed readiness OR documented blocker)
3. Teacher replies with approval
4. Proceed with Light Option deliverables

---

*If all 5 labs fail readiness by Mar 24, teacher activates Mini-Juice-Shop backup for entire class.*