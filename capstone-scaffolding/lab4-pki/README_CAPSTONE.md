# Lab 5.4 Capstone Extension — Mini Certificate Authority

**Base Lab**: `ap-cyber-u5-l4-pki-simulation`  
**Core Skills**: 5.4.A, 5.4.B, 5.4.C, 5.5.A, 5.5.B

---

## Extension Requirements (TODO)

Implement **at least 3** of the following:

- [ ] **CA Hierarchy**: Root CA → Intermediate CA → Leaf certs with proper constraints
- [ ] **Certificate Lifecycle**: Issue, renew, revoke (CRL/OCSP), expire automation
- [ ] **OCSP Responder**: Real-time revocation status with caching
- [ ] **CRL Generator**: Periodic CRL publication with delta CRL support
- [ ] **ACME Client**: Automate cert issuance via ACME (Let's Encrypt compatible)
- [ ] **CT Log Submission**: Submit pre-certificates to Certificate Transparency logs
- [ ] **PKI Health Dashboard**: Expiry monitoring, revocation stats, compliance checks

**Minimum Viable Extension**: CA hierarchy + issue/renew/revoke + OCSP responder + dashboard

---

## Suggested Architecture

```
capstone/
├── pki/
│   ├── __init__.py
│   ├── ca.py               # Certificate Authority core
│   ├── cert_manager.py     # Issue, renew, revoke, store
│   ├── ocsp_responder.py   # RFC 6960 OCSP responder
│   ├── crl_generator.py    # CRL + Delta CRL
│   ├── acme_client.py      # ACME protocol client
│   ├── ct_submitter.py     # Certificate Transparency
│   ├── dashboard.py        # Health monitoring
│   └── cli.py              # Management CLI
├── tests/
│   ├── test_ca.py
│   ├── test_ocsp.py
│   ├── test_crl.py
│   └── test_lifecycle.py
├── .github/
│   └── workflows/
│       └── capstone-ci.yml
└── requirements.txt
```

---

## Starter Stubs (in `src/stubs/`)

```python
# ca.py
from cryptography import x509
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from dataclasses import dataclass
from datetime import datetime, timedelta
import uuid

@dataclass
class CAConfig:
    name: str
    key_type: str = "RSA"  # or "EC"
    key_size: int = 4096
    hash_algorithm: str = "SHA256"
    valid_days: int = 3650  # 10 years for root
    path_length: int = 1    # For intermediate CAs

class CertificateAuthority:
    def __init__(self, config: CAConfig, parent_ca: 'CertificateAuthority' = None):
        self.config = config
        self.parent_ca = parent_ca
        self.private_key = None
        self.certificate = None
        self.issued_certs = {}  # serial -> cert
        self.revoked_certs = {} # serial -> revocation_info
    
    def initialize(self):
        """Generate root or intermediate CA key and self-signed/parent-signed cert."""
        # TODO: Generate key pair, build CSR, sign (self or by parent)
        # Set BasicConstraints: CA=True, path_length
        # Set KeyUsage: keyCertSign, cRLSign
        # Set SubjectKeyIdentifier, AuthorityKeyIdentifier
        raise NotImplementedError
    
    def issue_certificate(self, subject: x509.Name, public_key, 
                         valid_days: int = 365, 
                         extensions: list = None,
                         is_ca: bool = False) -> x509.Certificate:
        """Issue leaf or intermediate certificate."""
        # TODO: Build certificate with:
        # - Serial number (RFC 5280: positive, unique, unpredictable)
        # - Validity period
        # - Subject, Issuer
        # - Public key
        # - Extensions: BasicConstraints, KeyUsage, ExtendedKeyUsage
        # - SAN if provided
        # - Sign with CA private key
        raise NotImplementedError
    
    def revoke_certificate(self, serial: int, reason: x509.ReasonFlags = x509.ReasonFlags.unspecified):
        """Mark certificate as revoked."""
        # TODO: Add to revoked list with timestamp and reason
        raise NotImplementedError
    
    def get_certificate(self, serial: int) -> x509.Certificate:
        raise NotImplementedError
```

```python
# ocsp_responder.py
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import ocsp  # pyocsp or custom implementation

class OCSPResponder:
    def __init__(self, ca: CertificateAuthority, responder_key, responder_cert):
        self.ca = ca
        self.responder_key = responder_key
        self.responder_cert = responder_cert
    
    def create_response(self, request: ocsp.OCSPRequest) -> ocsp.OCSPResponse:
        """Generate OCSP response for requested certificate serial."""
        # TODO: 
        # 1. Parse request (serial, issuer)
        # 2. Check revocation status
        # 3. Build response: Good / Revoked / Unknown
        # 4. Sign with responder key (must be authorized by CA)
        # 5. Include nonce if requested
        # 6. Set thisUpdate, nextUpdate, producedAt
        raise NotImplementedError
    
    def start_server(self, host: str = "0.0.0.0", port: int = 8080):
        """Run HTTP OCSP responder."""
        # TODO: Simple HTTP server handling POST / with Content-Type: application/ocsp-request
        raise NotImplementedError
```

```python
# cert_manager.py
class CertificateManager:
    def __init__(self, ca: CertificateAuthority, storage_path: str):
        self.ca = ca
        self.storage_path = storage_path
    
    def request_certificate(self, csr_pem: bytes, profile: str = "server") -> x509.Certificate:
        """Process CSR, apply profile, issue cert."""
        # TODO: Validate CSR, apply profile (SAN, EKU, validity), issue
        raise NotImplementedError
    
    def renew_certificate(self, cert_pem: bytes) -> x509.Certificate:
        """Renew expiring certificate (same key or new key)."""
        # TODO: Verify cert not revoked, issued by this CA, near expiry
        raise NotImplementedError
    
    def get_revocation_list(self) -> x509.CertificateRevocationList:
        """Generate CRL."""
        # TODO: Build CRL with all revoked certs, sign, set nextUpdate
        raise NotImplementedError
```

```python
# dashboard.py
class PKIHealthDashboard:
    def __init__(self, ca: CertificateAuthority):
        self.ca = ca
    
    def generate_report(self) -> dict:
        """Return health metrics."""
        return {
            "total_issued": len(self.ca.issued_certs),
            "total_revoked": len(self.ca.revoked_certs),
            "expiring_soon": self._count_expiring(days=30),
            "expired": self._count_expired(),
            "by_profile": self._count_by_profile(),
            "crl_size": len(self.ca.revoked_certs),
            "ocsp_status": "operational" if self.ca.ocsp_responder else "not configured",
        }
    
    def _count_expiring(self, days: int) -> int:
        raise NotImplementedError
    
    def _count_expired(self) -> int:
        raise NotImplementedError
    
    def _count_by_profile(self) -> dict:
        raise NotImplementedError
```

---

## Test Scaffolding

```python
# test_ca.py
import pytest
from datetime import datetime, timedelta
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from capstone.pki.ca import CertificateAuthority, CAConfig

class TestCertificateAuthority:
    @pytest.fixture
    def root_ca(self):
        config = CAConfig(name="Test Root CA", valid_days=3650)
        ca = CertificateAuthority(config)
        ca.initialize()
        return ca
    
    def test_root_ca_initialized(self, root_ca):
        assert root_ca.private_key is not None
        assert root_ca.certificate is not None
        assert root_ca.certificate.subject == root_ca.certificate.issuer  # Self-signed
        assert root_ca.certificate.extensions.get_extension_for_class(x509.BasicConstraints).value.ca
    
    def test_issue_leaf_certificate(self, root_ca):
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "test.example.com")])
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        
        cert = root_ca.issue_certificate(subject, key.public_key(), valid_days=90)
        
        assert cert.subject == subject
        assert cert.issuer == root_ca.certificate.subject
        assert cert.public_key() == key.public_key()
        assert cert.not_valid_after > datetime.utcnow()
        assert not cert.extensions.get_extension_for_class(x509.BasicConstraints).value.ca
    
    def test_revoke_certificate(self, root_ca):
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "revoke.example.com")])
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        cert = root_ca.issue_certificate(subject, key.public_key())
        
        root_ca.revoke_certificate(cert.serial_number, x509.ReasonFlags.keyCompromise)
        
        assert cert.serial_number in root_ca.revoked_certs
        assert root_ca.revoked_certs[cert.serial_number].reason == x509.ReasonFlags.keyCompromise

# test_ocsp.py
import pytest
from capstone.pki.ocsp_responder import OCSPResponder

class TestOCSPResponder:
    @pytest.fixture
    def responder(self, root_ca):
        # Create responder cert signed by root_ca
        return OCSPResponder(root_ca, responder_key, responder_cert)
    
    def test_good_response(self, responder, root_ca):
        cert = root_ca.issue_certificate(...)
        request = create_ocsp_request(cert.serial_number, root_ca.certificate)
        response = responder.create_response(request)
        assert response.certificate_status == ocsp.OCSPCertStatus.GOOD
    
    def test_revoked_response(self, responder, root_ca):
        cert = root_ca.issue_certificate(...)
        root_ca.revoke_certificate(cert.serial_number)
        request = create_ocsp_request(cert.serial_number, root_ca.certificate)
        response = responder.create_response(request)
        assert response.certificate_status == ocsp.OCSPCertStatus.REVOKED
        assert response.revocation_reason == x509.ReasonFlags.keyCompromise
    
    def test_unknown_response(self, responder):
        request = create_ocsp_request(999999, root_ca.certificate)  # Non-existent
        response = responder.create_response(request)
        assert response.certificate_status == ocsp.OCSPCertStatus.UNKNOWN
```

---

## CI Workflow

```yaml
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
          pip install pytest pytest-cov flake8 bandit cryptography pyocsp
      - name: Lint
        run: flake8 capstone/
      - name: Security scan
        run: bandit -r capstone/ || true
      - name: Tests
        run: pytest tests/ -v --cov=capstone --cov-report=term-missing
```

---

## Requirements

```
cryptography>=41.0.0
pyocsp>=1.0.0
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
| CA hierarchy (root → intermediate → leaf) | 10 |
| Issue/renew/revoke with proper extensions | 10 |
| OCSP responder (RFC 6960 compliant) | 10 |
| CRL generation + dashboard | 5 |
| Code quality, tests, CI | 5 |

**Bonus**: ACME client, CT log submission, delta CRL, HSM integration