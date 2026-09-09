AP Cybersecurity — Unit 1 · Period 14 (Fri, Sep 25)   Name: ______________   Date: ______________

# AI Defense Lab — Vulnerable Code Review

**GitHub repo:** `ivycollegiate-development/vulnerable-code-lab`

You'll fork a repo containing Python and JavaScript code snippets with security vulnerabilities. Your job: use an AI tool (Claude, ChatGPT, or built-in CodeQL) to find and fix each vulnerability.

## 1: Lab Setup

1. Open the repo link in GitHub
2. Fork the repo to your account
3. Launch Codespaces (one click)
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
3. Push to your fork

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