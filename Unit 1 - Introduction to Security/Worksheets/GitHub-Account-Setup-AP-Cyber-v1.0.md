GitHub Account Setup — AP Cybersecurity
Name: ______________________   Date: ______________

This term, your cybersecurity work lives on GitHub in the school organization `ivycollegiate-development`. You will keep two kinds of repos: your own workspace repo (`yourusername_student`) and forks of unit repos for graded labs. This worksheet gets both set up.

Check off every step. You are done when all ☐ boxes are ☑.

Part A — Sign in and check (everyone)
☐  Open a browser and go to https://github.com
☐  Check the top-right corner. Are you already signed in (do you see your profile icon)?
☐  If you see a username in the corner, write it below, skip to Part B.
☐  If you are NOT signed in, go to Part C.

MY GITHUB USERNAME IS: ________________________________
(If you're not sure you have an account, go to Part C — creating a new one with your school email is always safe.)

Part B — I already have a GitHub account
☐  Write your username in the field above. Check the spelling letter by letter.
☐  Check your email inbox for a message from GitHub: "Ivy Collegiate Academy invited you to join ivycollegiate-development". Open it and click Accept invitation.
    No email? Go to https://github.com/ivycollegiate-development while signed in — a banner at the top will offer to join. Click it.
☐  Raise your hand and show the green "welcome" banner so it can be marked as joined.

Part C — I need a new account
☐  Go to https://github.com/signup
☐  Email: type your school email: yourusername_student@ivycollegiate.org
☐  Password: create one and WRITE IT DOWN in your planner or notes app. GitHub passwords cannot be recovered by the school.
☐  Username: GitHub will suggest one. You may keep the suggestion or pick your own — but keep it appropriate; this name follows you into your professional life.
☐  Verify your email when the confirmation message arrives (check spam if needed).
☐  After signing in, go to https://github.com/ivycollegiate-development and click Accept invitation if a banner appears. (Your invite is sent right after class.)
☐  Write your new username in the field in Part A.

Part D — Pull YOUR workspace repo (into code-server)
Do this part inside your code-server workspace at vscode.ivycollegiate.org. Open the Terminal (Terminal > New Terminal) and type each command exactly.

Set up your git identity (first time only):
☐  git config --global user.name "Your Name"
☐  git config --global user.email "yourusername_student@ivycollegiate.org"

Clone your workspace repo — it is named after your VPS username:
☐  git clone https://github.com/ivycollegiate-development/yourusername_student.git
☐  cd yourusername_student
☐  You will see README.md, hello.py, and .gitignore — this is your workspace
☐  Change something in hello.py (add a print line with your name), then save
☐  git add . && git commit -m "add name to hello" && git push
☐  When asked for a password, use a Personal Access Token, NOT your GitHub password. If you do not have one: GitHub.com > click your profile icon > Settings > Developer settings > Personal access tokens > Generate new token (classic). Check the repo scope, set an expiration, generate, and copy it — you will not see it again.
☐  Open github.com and find yourusername_student — your change should be there

Part E — Fork your first unit repo
Unit labs use separate repos in the school org — see the Unit 1 labs index: https://github.com/ivycollegiate-development/ap-cybersecurity/blob/main/Unit%201%20-%20Introduction%20to%20Security/Labs.md
For this setup exercise you will fork the unit pilot repo. You do not clone it directly — you fork it (make your own copy on GitHub), then clone your fork.
☐  While signed in on github.com, go to https://github.com/ivycollegiate-development/apcyber-unit1-pilot
☐  Click the Fork button (top-right). If asked where to fork it, choose your own account.
☐  You now have github.com/YOUR-USERNAME/apcyber-unit1-pilot
☐  Back in the code-server terminal: git clone https://github.com/YOUR-USERNAME/apcyber-unit1-pilot.git
☐  cd apcyber-unit1-pilot
☐  Open checkpoint-1.1/CHECKPOINT.md and read the first checkpoint questions
☐  Create your answers file: cp checkpoint-1.1/CHECKPOINT.md answers/checkpoint-1.1.md then open it and answer the questions
☐  git add answers/ && git commit -m "checkpoint 1.1" && git push
☐  On github.com, open the Actions tab of YOUR fork within a minute — look for the green check. If it is red, read the bot comment, fix, and push again.

Commit messages: use present tense ("add answer", not "added answer") — the change is happening now.

What happens next
☐  Every class: write → commit → push. Work is saved, versioned, and visible for grading
☐  Labs are auto-graded by GitHub Actions running on your fork — a green check means the checkpoint passed
☐  The labs index (which repo each lab uses) lives in the course repo: Unit 1 folder → Labs.md
☐  Your workspace repo (yourusername_student) holds notes and small exercises; forks of unit repos hold graded lab work
☐  Losing work becomes impossible once you push

Exit ticket
1. My GitHub username: ________________________________
2. I completed:   ☐ Part A    ☐ Part B (existing account)    ☐ Part C (new account)    ☐ Part D (workspace repo)    ☐ Part E (unit fork)
3. Confidence that I can log into GitHub and push again tomorrow without help:   ☐ sure   ☐ mostly   ☐ need help
