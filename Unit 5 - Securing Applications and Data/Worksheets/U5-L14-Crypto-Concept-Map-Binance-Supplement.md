# Crypto Concept Map — "Crypto in the Wild" Supplement
## Binance Hack (Oct 2026) — Applied Crypto Primitives

**Time:** 10–15 minutes (after main concept map + notecard drill)
**Unit:** 5 | **Topic:** 5.3 Symmetric / 5.4 Asymmetric Cryptography
**CED Mapping:** 5.3.A, 5.3.B, 5.4.A, 5.4.B, 5.4.C, 5.5.A, 5.6.A

---

### Setup (Teacher)
- Project the three transaction screenshots (see Teacher Reference below)
- Students work in pairs with their completed concept maps

---

### Activity

#### 1. Transaction 1 — USDC Freeze (800M USDC)
```
Tx: 0x1a2b... → Circle/USDC contract → freeze(address, amount)
Function: `freeze(address account, uint256 amount)` — only callable by `blacklister` role
```
**Question:** Which crypto primitive enables this?
- ☐ Symmetric encryption (AES)
- ☐ Asymmetric encryption (RSA/ECC)
- ☐ Digital signature (ECDSA)
- ☐ **Access control / role-based authorization (smart contract logic)**
- ☐ Hash function (SHA-256)

**Discussion (1 min):** The freeze isn't cryptography — it's *authorization logic* in the contract. The cryptography (ECDSA) only verifies *who* signed the tx. The *decision* to freeze is a managerial control (5.2) implemented in code.

---

#### 2. Transaction 2 — Tornado Cash Deposit (Attacker)
```
Tx: 0xdead... → Tornado Cash contract → deposit(bytes32 commitment)
Commitment = hash(secret || nullifier)  [Poseidon hash, zk-SNARK friendly]
```
**Question:** Which crypto primitives are at play? (Select all)
- ☐ **Hash function (Poseidon, ZK-friendly)**
- ☐ **Zero-knowledge proof (zk-SNARK — proves knowledge of secret without revealing it)**
- ☐ Symmetric encryption
- ☐ Asymmetric encryption
- ☐ Digital signature

**Discussion (1 min):** Tornado Cash uses ZK proofs (5.4.C — advanced crypto) + hash commitments. The *anonymity set* is the cryptographic guarantee. Volume limit: $5B breaks the anonymity set (5.6.A — detection via on-chain analysis).

---

#### 3. Transaction 3 — On-Chain Loan (Aave v3)
```
Tx: 0xhack... → Aave Pool → supply(stolen USDC) → borrow(WETH)
Collateral factor: 80% → $1M USDC → borrow $800k WETH (unfreezable-ish)
```
**Question:** What crypto primitives secure this?
- ☐ **Digital signature (ECDSA — tx authorization)**
- ☐ **Hash function (Keccak-256 — state roots, Merkle proofs for reserves)**
- ☐ **Elliptic curve (secp256k1 — Ethereum address derivation)**
- ☐ Symmetric encryption
- ☐ Zero-knowledge proof

**Discussion (1 min):** DeFi lending uses *no encryption*. It uses signatures (auth), hashes (integrity), and elliptic curves (identity). The "unfreezable" asset (WETH) is just an ERC-20 without a freeze role — a *design choice*, not a cryptographic property.

---

#### 4. Rapid Classification — "Crypto or Not?" (Binance Edition)
| Item | Crypto Primitive? | Which One? |
|------|-------------------|------------|
| ECDSA signature on withdrawal tx | ☐ Yes / ☐ No | _______________ |
| Tornado Cash zk-SNARK circuit | ☐ Yes / ☐ No | _______________ |
| USDC `freeze()` function | ☐ Yes / ☐ No | _______________ |
| Aave interest rate curve | ☐ Yes / ☐ No | _______________ |
| Binance SAFU fund multisig (3-of-5) | ☐ Yes / ☐ No | _______________ |
| Attacker's BTC → XMR swap (CEX) | ☐ Yes / ☐ No | _______________ |
| Merkle proof of reserves | ☐ Yes / ☐ No | _______________ |
| DevOps laptop → container escape | ☐ Yes / ☐ No | _______________ |

**Answers:** 1) Yes — ECDSA | 2) Yes — ZK-SNARK | 3) No — contract logic (5.2) | 4) No — math formula | 5) Yes — threshold ECDSA (5.4.C) | 6) No — CEX custody (5.2) | 7) Yes — Merkle tree + Keccak | 8) No — OS/exploit chain (4.1)

---

### Teacher Reference — Transaction Screenshots (Project These)

**Tx 1 — USDC Freeze** (Arkham label: "Circle/USDC Freeze")
- Contract: `0xA0b86a33E6441...` (USDC)
- Method: `freeze(address,uint256)` — selector `0x6d8c...`
- Event: `Frozen(address,uint256)` — 800,000,000 USDC

**Tx 2 — Tornado Cash Deposit** (Arkham label: "Attacker Tornado Deposit")
- Contract: `0x722122dF12D4e...` (Tornado Cash 100 ETH pool)
- Method: `deposit(bytes32)` — selector `0x1a2b...`
- Commitment: `0xabc...` (Poseidon hash of secret || nullifier)

**Tx 3 — Aave Supply + Borrow** (Arkham label: "Attacker Aave Leverage")
- Supply: `supply(USDC, amount, onBehalfOf, referralCode)` — Pool contract
- Borrow: `borrow(WETH, amount, interestRateMode, referralCode, onBehalfOf)`
- Health factor calculation: off-chain (Aave UI), on-chain (liquidation threshold)

---

### Exit Ticket (2 min, written on back of concept map)
1. The Binance hacker moved $3.2B into **BTC/ETH** (unfreezable). What *cryptographic property* makes BTC/ETH unfreezable?
   - Answer: _______________________________________________________
   - (Key: No central `freeze` role in protocol — UTXO/account model has no authorization hook. It's a *protocol design* choice, not a crypto primitive.)

2. One crypto primitive from today's concept map that **failed to prevent** this hack:
   - Answer: _______________________________________________________
   - (Any valid: ECDSA didn't stop signed malicious tx; hash didn't stop stolen funds moving; ZK didn't stop volume analysis)

3. One crypto primitive that **helped defenders**:
   - Answer: _______________________________________________________
   - (ECDSA — Arkham traced 71 addresses via signature linkage; Keccak — Merkle proofs of reserves; threshold sig — SAFU multisig)

---

### CED Mapping Quick Reference (for teacher)
| Activity Segment | CED LO |
|------------------|--------|
| Notecard drill / concept map | 5.3.A, 5.3.B, 5.4.A, 5.4.B, 5.4.C |
| Tx 1 (USDC freeze) | 5.2.A (managerial controls), 5.5.A (secure SDLC — role design) |
| Tx 2 (Tornado Cash) | 5.4.C (advanced crypto — ZK), 5.6.A (detection — volume analysis) |
| Tx 3 (Aave loan) | 5.1.A (app vuln — DeFi logic), 5.3.A (hash/integrity), 5.4.A (ECDSA) |
| Rapid classification | 5.3.A, 5.4.A, 5.4.B, 5.4.C, 5.5.A, 5.6.A |
| Exit ticket Q1 | 5.1.A, 5.2.A (protocol design vs crypto) |
| Exit ticket Q2-3 | 5.6.A (detection), 5.5.A (protection) |