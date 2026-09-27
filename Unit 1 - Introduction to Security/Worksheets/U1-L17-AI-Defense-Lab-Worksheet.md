AP Cybersecurity — Unit 1 · Period 14 (Fri, Sep 25)   Name: ______________   Date: ______________

# AI Defense Lab — Vulnerable Code Review

**GitHub repo:** `ivycollegiate-development/apcyber-u1-vulnerable-code-lab`

You'll fork a repo containing Python and JavaScript code snippets with security vulnerabilities. Your job: use an AI tool (Claude, ChatGPT, or built-in CodeQL) to find and fix each vulnerability.

## 1: Lab Setup

1. Open the repo link in GitHub (in your browser)
2. Fork the repo to your account
3. Open your VS Code workspace (vscode.ivycollegiate.org) and clone your fork:
   `git clone https://github.com/<your-username>/apcyber-u1-vulnerable-code-lab.git`
4. Open the `vulnerabilities/` folder — each file contains at least one security flaw

## 2: Vulnerability Hunt

As you find each vulnerability, record it in the table below.

| File Name | Vulnerability Type | Line(s) | How did you find it? | How would you fix it? |
|-----------|------------------|:-------:|----------------------|-----------------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

**Vulnerability types to look for:**

- SQL Injection (SQLi) — unsanitized user input in database queries
- Cross-Site Scripting (XSS) — user input rendered directly in HTML
- Weak authentication — hardcoded passwords, no rate limiting
- Command injection — user input passed to system commands
- Insecure data storage — passwords stored in plain text

## 3: Fix Each Vulnerability

For each file:
1. Edit the code to fix the vulnerability
2. Commit the change with a message describing what you fixed and why
3. Push to your fork (use your GitHub Personal Access Token when asked for a password)

If the push fails with an authentication error, create a Personal Access Token (PAT):

1. In your browser: GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click Generate new token. Name it: `u1-l17-lab`. Repository access: Only select repositories → `apcyber-u1-vulnerable-code-lab`
3. Under Permissions → Repository permissions, set Contents to *Read and write*
4. Click Generate token and copy the token (you will not see it again)
5. Push again. When asked for a Username, enter your GitHub username. When asked for a Password, paste the PAT

If the push succeeds, you are done — no PAT needed.

## 4: Open a Pull Request

1. Open a PR from your fork to the original repo
2. In the PR description, write a reflection:
   - Which tool(s) did you use to find the vulnerabilities? (AI chat, CodeQL, manual review)
   - Which vulnerability was hardest to spot? Why?
   - Did you trust the AI's suggestions? Why or why not?
   - Would you let AI-generated code go straight to production without review?

3. Wait for the 🤖 GitHub Action to run on your PR
   - Green checkmark = all vulnerabilities addressed
   - Red X = something still needs fixing — check the Action logs

## 5: Reflection

What's one thing this lab made you think differently about AI and security?

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________