# Lab 5.3 Capstone Extension — Authenticated Encryption Toolkit

**Base Lab**: `ap-cyber-u5-l3-symmetric-crypto`  
**Core Skills**: 5.3.A, 5.3.B, 5.4.A, 5.4.B, 5.4.C

---

## Extension Requirements (TODO)

Implement **at least 3** of the following:

- [ ] **AEAD Implementation**: AES-GCM or ChaCha20-Poly1305 with proper nonce management
- [ ] **Key Derivation**: PBKDF2, Argon2, or HKDF for password-to-key and key separation
- [ ] **File Encryption CLI**: Encrypt/decrypt files with streaming (large file support)
- [ ] **Key Rotation System**: Automated re-encryption with versioned keys, metadata
- [ ] **Secure Key Storage**: Integration with OS keychain / hardware token / HSM simulator
- [ ] **Authenticated Key Exchange**: Implement a simple PAKE (e.g., SRP) or use Noise protocol
- [ ] **Side-Channel Resistant**: Constant-time comparisons, timing-safe implementations

**Minimum Viable Extension**: AEAD file encryption CLI + key derivation + key rotation + tests

---

## Suggested Architecture

```
capstone/
├── crypto/
│   ├── __init__.py
│   ├── aead.py           # AES-GCM, ChaCha20-Poly1305 wrappers
│   ├── kdf.py            # PBKDF2, Argon2, HKDF
│   ├── file_crypto.py    # Streaming file encrypt/decrypt
│   ├── key_manager.py    # Key generation, rotation, versioning
│   ├── storage.py        # Keychain/HSM interface
│   └── cli.py            # Click/Typer CLI
├── tests/
│   ├── test_aead.py
│   ├── test_kdf.py
│   ├── test_file_crypto.py
│   └── test_key_manager.py
├── .github/
│   └── workflows/
│       └── capstone-ci.yml
└── requirements.txt
```

---

## Starter Stubs (in `src/stubs/`)

```python
# aead.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import os

class AEADCipher:
    """Authenticated Encryption with Associated Data."""
    
    def __init__(self, algorithm: str = "AES-256-GCM"):
        self.algorithm = algorithm
        if algorithm == "AES-256-GCM":
            self.key_size = 32
            self.nonce_size = 12
        elif algorithm == "ChaCha20-Poly1305":
            self.key_size = 32
            self.nonce_size = 12
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    def generate_key(self) -> bytes:
        return os.urandom(self.key_size)
    
    def encrypt(self, key: bytes, plaintext: bytes, associated_data: bytes = None) -> dict:
        """
        Encrypt plaintext.
        Returns: {"nonce": bytes, "ciphertext": bytes, "tag": bytes}
        """
        # TODO: Generate random nonce, encrypt, return all components
        # CRITICAL: Never reuse nonce with same key!
        raise NotImplementedError
    
    def decrypt(self, key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes, 
                associated_data: bytes = None) -> bytes:
        """Decrypt and verify. Raises on authentication failure."""
        # TODO: Verify tag, decrypt, return plaintext
        raise NotImplementedError
    
    def encrypt_stream(self, key: bytes, infile, outfile, chunk_size: int = 64*1024):
        """Encrypt large file in chunks (streaming)."""
        # TODO: Use streaming AEAD or chunked encryption with proper framing
        raise NotImplementedError
    
    def decrypt_stream(self, key: bytes, infile, outfile, chunk_size: int = 64*1024):
        """Decrypt streaming file."""
        raise NotImplementedError


class KeyDerivation:
    @staticmethod
    def pbkdf2(password: bytes, salt: bytes, iterations: int = 600000, key_len: int = 32) -> bytes:
        # TODO: Use cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC
        raise NotImplementedError
    
    @staticmethod
    def argon2id(password: bytes, salt: bytes, time_cost: int = 3, memory_cost: int = 65536, 
                 parallelism: int = 4, key_len: int = 32) -> bytes:
        # TODO: Use argon2-cffi
        raise NotImplementedError
    
    @staticmethod
    def hkdf(master_key: bytes, salt: bytes, info: bytes, key_len: int = 32) -> bytes:
        # TODO: Use HKDF for key separation (encryption key, auth key, etc.)
        raise NotImplementedError
```

```python
# file_crypto.py
import struct
from pathlib import Path
from .aead import AEADCipher, KeyDerivation

MAGIC_HEADER = b"CRYPTOv1"
VERSION = 1

class FileEncryptor:
    def __init__(self, cipher: AEADCipher = None):
        self.cipher = cipher or AEADCipher("AES-256-GCM")
    
    def encrypt_file(self, password: str, in_path: Path, out_path: Path) -> dict:
        """
        Encrypt file with password.
        File format:
        [MAGIC][VERSION][SALT][NONCE][CHUNK_COUNT][CHUNK_SIZE][CHUNK1_TAG][CHUNK1_CT]...
        """
        # TODO: 
        # 1. Generate salt, derive key via Argon2id
        # 2. Generate nonce per file (or per chunk)
        # 3. Stream encrypt in chunks
        # 4. Write header + chunks
        raise NotImplementedError
    
    def decrypt_file(self, password: str, in_path: Path, out_path: Path) -> bool:
        """Decrypt file. Returns True on success, raises on auth failure."""
        # TODO: Verify header, derive key, stream decrypt, verify each chunk
        raise NotImplementedError
    
    def rotate_key(self, old_password: str, new_password: str, in_path: Path, out_path: Path):
        """Decrypt with old password, re-encrypt with new password."""
        # TODO: Stream decrypt + encrypt without full file in memory
        raise NotImplementedError
```

```python
# key_manager.py
from dataclasses import dataclass, asdict
from typing import Dict, Optional
import json
import time

@dataclass
class KeyMetadata:
    key_id: str
    algorithm: str
    created_at: float
    rotated_at: Optional[float]
    version: int
    purpose: str  # "file-encryption", "api-signing", etc.
    salt: bytes  # For key derivation
    nonce: bytes  # For encryption

class KeyManager:
    def __init__(self, storage_backend):
        self.storage = storage_backend
    
    def generate_key(self, purpose: str, algorithm: str = "AES-256-GCM") -> KeyMetadata:
        """Generate new key, store metadata, return metadata."""
        # TODO: Generate key, encrypt with master key, store
        raise NotImplementedError
    
    def get_key(self, key_id: str) -> bytes:
        """Retrieve and decrypt key."""
        raise NotImplementedError
    
    def rotate_key(self, key_id: str) -> KeyMetadata:
        """Generate new version of key, re-encrypt data."""
        # TODO: Create new key version, update metadata, trigger re-encryption
        raise NotImplementedError
    
    def list_keys(self, purpose: str = None) -> List[KeyMetadata]:
        raise NotImplementedError
```

---

## Test Scaffolding

```python
# test_aead.py
import pytest
from capstone.crypto.aead import AEADCipher, KeyDerivation

class TestAEADCipher:
    def test_aes_gcm_roundtrip(self):
        cipher = AEADCipher("AES-256-GCM")
        key = cipher.generate_key()
        plaintext = b"Secret message"
        aad = b"associated data"
        
        encrypted = cipher.encrypt(key, plaintext, aad)
        decrypted = cipher.decrypt(key, encrypted["nonce"], encrypted["ciphertext"], 
                                   encrypted["tag"], aad)
        assert decrypted == plaintext
    
    def test_chacha20_roundtrip(self):
        cipher = AEADCipher("ChaCha20-Poly1305")
        key = cipher.generate_key()
        plaintext = b"Another secret"
        encrypted = cipher.encrypt(key, plaintext)
        decrypted = cipher.decrypt(key, encrypted["nonce"], encrypted["ciphertext"], encrypted["tag"])
        assert decrypted == plaintext
    
    def test_wrong_tag_fails(self):
        cipher = AEADCipher("AES-256-GCM")
        key = cipher.generate_key()
        encrypted = cipher.encrypt(key, b"data")
        # Corrupt tag
        with pytest.raises(Exception):
            cipher.decrypt(key, encrypted["nonce"], encrypted["ciphertext"], 
                          bytes([b ^ 0xFF for b in encrypted["tag"]]))
    
    def test_nonce_reuse_detected(self):
        """Same nonce + key should be detectable/rejected."""
        cipher = AEADCipher("AES-256-GCM")
        key = cipher.generate_key()
        nonce = os.urandom(12)
        ct1 = cipher.encrypt(key, b"msg1", nonce=nonce)
        ct2 = cipher.encrypt(key, b"msg2", nonce=nonce)  # REUSE!
        # This should either fail or be flagged
        # Implementation should prevent nonce reuse
    
    def test_argon2id_deterministic(self):
        pwd = b"password123"
        salt = b"salt1234"
        key1 = KeyDerivation.argon2id(pwd, salt)
        key2 = KeyDerivation.argon2id(pwd, salt)
        assert key1 == key2
        assert len(key1) == 32

# test_file_crypto.py
import pytest
import tempfile
from pathlib import Path
from capstone.crypto.file_crypto import FileEncryptor

class TestFileEncryptor:
    @pytest.fixture
    def encryptor(self):
        return FileEncryptor()
    
    def test_encrypt_decrypt_small_file(self, encryptor):
        with tempfile.TemporaryDirectory() as tmp:
            in_file = Path(tmp) / "plaintext.txt"
            out_file = Path(tmp) / "encrypted.bin"
            dec_file = Path(tmp) / "decrypted.txt"
            
            in_file.write_bytes(b"Hello, World! " * 100)
            
            encryptor.encrypt_file("password123", in_file, out_file)
            assert out_file.exists()
            
            encryptor.decrypt_file("password123", out_file, dec_file)
            assert dec_file.read_bytes() == in_file.read_bytes()
    
    def test_encrypt_decrypt_large_file(self, encryptor):
        with tempfile.TemporaryDirectory() as tmp:
            in_file = Path(tmp) / "large.bin"
            out_file = Path(tmp) / "encrypted.bin"
            dec_file = Path(tmp) / "decrypted.bin"
            
            # 10 MB file
            in_file.write_bytes(os.urandom(10 * 1024 * 1024))
            
            encryptor.encrypt_file("password123", in_file, out_file)
            encryptor.decrypt_file("password123", out_file, dec_file)
            assert dec_file.read_bytes() == in_file.read_bytes()
    
    def test_wrong_password_fails(self, encryptor):
        with tempfile.TemporaryDirectory() as tmp:
            in_file = Path(tmp) / "plaintext.txt"
            out_file = Path(tmp) / "encrypted.bin"
            dec_file = Path(tmp) / "decrypted.txt"
            
            in_file.write_bytes(b"data")
            encryptor.encrypt_file("correct", in_file, out_file)
            
            with pytest.raises(Exception):
                encryptor.decrypt_file("wrong", out_file, dec_file)
```

---

## CI Workflow

```yaml
# .github/workflows/capstone-ci.yml
name: Capstone CI

on:
  push:
    branches: [capstone]
  pull_request:
    branches: [main, capstone]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8 bandit cryptography argon2-cffi
      - name: Lint
        run: flake8 capstone/
      - name: Security scan
        run: bandit -r capstone/ || true
      - name: Tests
        run: pytest tests/ -v --cov=capstone --cov-report=term-missing --cov-fail-under=80
```

---

## Requirements

```
cryptography>=41.0.0
argon2-cffi>=23.1.0
click>=8.1.0
pytest>=7.4.0
pytest-cov>=4.1.0
flake8>=6.0.0
bandit>=1.7.0
```

---

## Grading Notes

| Feature | Points (of 40) |
|---------|----------------|
| AEAD implementation (AES-GCM + ChaCha20) | 12 |
| Key derivation (Argon2id + HKDF) | 8 |
| Streaming file encryption/decryption | 10 |
| Key rotation + versioned metadata | 5 |
| Code quality, tests (80%+), CI, side-channel awareness | 5 |

**Bonus**: PAKE/Noise implementation, HSM integration, constant-time proofs