# Lab 5.1 Capstone Extension — Juice Shop Recon & Vulnerability Automation

**Base Lab**: `ap-cyber-u5-l1-juice-shop-recon`  
**Core Skills**: 1.3.A, 1.3.B, 1.3.C, 5.1.A, 5.1.B, 5.1.C

---

## Extension Requirements (TODO)

Implement **at least 3** of the following (or propose your own):

- [ ] **Automated Recon Pipeline**: Script that discovers endpoints, parameters, tech stack, and maps attack surface
- [ ] **Auth Bypass Testing**: Automated tests for IDOR, broken access control, session fixation
- [ ] **CI/CD Integration**: GitHub Action that runs recon on PR deployments, posts summary as comment
- [ ] **Vulnerability Correlation**: Cross-reference discovered endpoints with known CVE patterns (e.g., OWASP Top 10)
- [ ] **Report Generation**: HTML/PDF report with findings, severity, evidence, remediation
- [ ] **Rate-Limit Bypass Detection**: Test and document rate-limiting effectiveness
- [ ] **Client-Side Analysis**: Static analysis of JS for hardcoded secrets, API keys, debug endpoints

**Minimum Viable Extension**: Automated recon + 1 vulnerability test + CI integration + report

---

## Suggested Architecture

```
capstone/
├── recon/
│   ├── __init__.py
│   ├── scanner.py          # Endpoint discovery, tech fingerprinting
│   ├── auth_tester.py      # Auth bypass test cases
│   ├── correlator.py       # Map findings to CVE/CWE
│   └── reporter.py         # Generate HTML/Markdown report
├── tests/
│   ├── test_scanner.py
│   └── test_auth_tester.py
├── .github/
│   └── workflows/
│       └── capstone-ci.yml # Runs on push/PR
└── requirements.txt
```

---

## Starter Stubs (in `src/stubs/`)

```python
# scanner.py
class ReconScanner:
    def __init__(self, base_url: str, auth_token: str = None):
        self.base_url = base_url
        self.session = requests.Session()
        if auth_token:
            self.session.headers.update({"Authorization": f"Bearer {auth_token}"})
    
    def discover_endpoints(self, wordlist: str = None) -> List[Endpoint]:
        """Crawl and fuzz to discover endpoints. Return list of Endpoint objects."""
        # TODO: Implement directory fuzzing, link extraction, API spec parsing
        raise NotImplementedError
    
    def fingerprint_tech(self) -> TechProfile:
        """Identify framework, server, language, versions."""
        # TODO: Analyze headers, cookies, response patterns, JS files
        raise NotImplementedError
    
    def find_parameters(self, endpoint: Endpoint) -> List[Parameter]:
        """Discover query params, body params, headers for an endpoint."""
        raise NotImplementedError

# auth_tester.py
class AuthBypassTester:
    def __init__(self, scanner: ReconScanner):
        self.scanner = scanner
    
    def test_idor(self, endpoints: List[Endpoint]) -> List[Finding]:
        """Test for Insecure Direct Object References."""
        # TODO: Manipulate object IDs in params/paths; check unauthorized access
        raise NotImplementedError
    
    def test_session_fixation(self) -> Finding:
        """Test if session ID can be set before login and persists after."""
        raise NotImplementedError
    
    def test_broken_access_control(self) -> List[Finding]:
        """Test vertical/horizontal privilege escalation."""
        raise NotImplementedError

# correlator.py
class VulnCorrelator:
    CVE_PATTERNS = {
        "CVE-2021-44228": ["log4j", "jndi"],  # Example
        # TODO: Add relevant patterns for Juice Shop tech stack
    }
    
    def correlate(self, findings: List[Finding], tech_profile: TechProfile) -> List[CorrelatedFinding]:
        """Match findings to known vulnerability patterns."""
        raise NotImplementedError

# reporter.py
class ReportGenerator:
    def generate_html(self, findings: List[Finding], output_path: str):
        """Generate professional HTML report with severity, evidence, remediation."""
        raise NotImplementedError
    
    def generate_markdown(self, findings: List[Finding]) -> str:
        """Generate Markdown for GitHub PR comment."""
        raise NotImplementedError
```

---

## Test Scaffolding (in `tests/`)

```python
# test_scanner.py
import pytest
from capstone.recon.scanner import ReconScanner, Endpoint, TechProfile

class TestReconScanner:
    @pytest.fixture
    def scanner(self):
        return ReconScanner("http://localhost:3000")
    
    def test_discover_endpoints_returns_list(self, scanner):
        endpoints = scanner.discover_endpoints()
        assert isinstance(endpoints, list)
    
    def test_fingerprint_returns_tech_profile(self, scanner):
        profile = scanner.fingerprint_tech()
        assert isinstance(profile, TechProfile)
        assert profile.framework in ["Angular", "React", "Vue", "Unknown"]
    
    def test_endpoint_has_required_fields(self, scanner):
        endpoints = scanner.discover_endpoints()
        for ep in endpoints:
            assert hasattr(ep, 'url')
            assert hasattr(ep, 'method')
            assert hasattr(ep, 'parameters')

# test_auth_tester.py
import pytest
from capstone.recon.auth_tester import AuthBypassTester, Finding

class TestAuthBypassTester:
    @pytest.fixture
    def tester(self, scanner):
        return AuthBypassTester(scanner)
    
    def test_idor_returns_findings(self, tester):
        endpoints = [Endpoint(url="/api/user/1", method="GET")]
        findings = tester.test_idor(endpoints)
        assert isinstance(findings, list)
        for f in findings:
            assert isinstance(f, Finding)
            assert f.severity in ["Critical", "High", "Medium", "Low", "Info"]
```

---

## CI Workflow (`.github/workflows/capstone-ci.yml`)

```yaml
name: Capstone CI

on:
  push:
    branches: [capstone]
  pull_request:
    branches: [main, capstone]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8 bandit
      
      - name: Lint (flake8)
        run: flake8 capstone/ --max-line-length=100 --ignore=E501,W503
      
      - name: Security scan (bandit)
        run: bandit -r capstone/ -f json -o bandit-report.json || true
      
      - name: Run tests with coverage
        run: pytest tests/ -v --cov=capstone --cov-report=xml --cov-report=term-missing
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
      
      - name: Run recon on test target (if configured)
        if: env.JUICE_SHOP_URL != ''
        run: |
          python -m capstone.recon.scanner --url ${{ env.JUICE_SHOP_URL }} --output report.html
      
      - name: Upload report artifact
        uses: actions/upload-artifact@v4
        with:
          name: recon-report
          path: report.html

  # Optional: Deploy to test environment
  # deploy-test:
  #   needs: lint-and-test
  #   if: github.ref == 'refs/heads/capstone'
  #   runs-on: ubuntu-latest
  #   steps:
  #     - uses: actions/checkout@v4
  #     - name: Deploy to Codespaces/Render
  #       run: echo "Deploy stub"
```

---

## Requirements (`requirements.txt`)

```
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
pyyaml>=6.0
jinja2>=3.1.0
pytest>=7.4.0
pytest-cov>=4.1.0
bandit>=1.7.0
flake8>=6.0.0
```

---

## Grading Notes

| Feature | Points (of 40) |
|---------|----------------|
| Endpoint discovery + tech fingerprinting | 10 |
| Auth bypass tests (IDOR, session, access control) | 10 |
| CI integration + automated report | 10 |
| Code quality, tests, security practices | 10 |

**Bonus** (up to +5, max 40): CVE correlation, rate-limit bypass, client-side analysis, exceptional report UX

---

*Copy this folder structure to your lab repo's `capstone-starter/` branch.*