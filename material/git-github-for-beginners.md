# Git & GitHub for Beginners

*A complete 3-hour beginner course for learning Git and GitHub from scratch.*

---

## How to Use This Document

This document is designed for a **live 3-hour instructor-led session**. Each topic follows a simple pattern:

1. **What is it?**
2. **Why do we need it?**
3. **When do we use it?**
4. **How do we use it?**
5. **What happens behind the scenes?**

Look out for these callouts throughout the course:

> **Important:** Key ideas you must understand before moving on.

> **Warning:** Actions that can cause data loss or confusion.

> **Tip:** Shortcuts, good habits, or extra advice.

Instructor-only sections are marked with **Instructor Notes**.

---

## Suggested 3-Hour Schedule

| Time | Topic |
|---|---|
| 0:00 – 0:20 | Introduction to Version Control, Git vs GitHub |
| 0:20 – 0:50 | Installing Git, Configuration, Repositories, Three Main Areas |
| 0:50 – 1:20 | Status, Staging, Commits, Diff, Log, `.gitignore` |
| 1:20 – 1:50 | Branches and Merging (including conflicts) |
| 1:50 – 2:15 | GitHub, Remotes, Push, Clone, Pull/Fetch |
| 2:15 – 2:40 | Collaboration, Forks, Pull Requests, Issues, README |
| 2:40 – 2:55 | Undoing Changes, Stash, Tags, SSH |
| 2:55 – 3:00 | Final Recap and Q&A |

> **Tip for Instructor:** Keep a terminal open the whole session. Every command in this document should be typed live, not just shown on a slide.

---

# 1. Introduction to Version Control

### What is it?
Version control is a system that **records changes** to files over time, so you can look back at older versions, compare changes, or restore something if needed.

### Why do we need it?
Without version control, developers usually end up with folders like this:

```text
project_final.zip
project_final_v2.zip
project_final_v2_REAL.zip
project_final_v2_REAL_fixed.zip
```

This is confusing, error-prone, and impossible to manage in a team.

### Real-World Analogy
Think of version control like **"Track Changes" in Microsoft Word**, but far more powerful. Instead of just seeing edits, you can:
- Go back to any previous version
- See who changed what and when
- Work on different versions at the same time without overwriting each other

### Manual File Versions vs Git

| Manual Versioning | Git |
|---|---|
| Rename files manually (`v1`, `v2`, `final`) | Automatic, precise history |
| No record of *who* changed *what* | Every change is tracked with author and time |
| Hard to combine changes from multiple people | Built-in tools to merge changes |
| Easy to lose work | History is safely stored |

### Centralized vs Distributed Version Control
- **Centralized (old style):** One central server holds the history. If the server goes down, nobody can work.
- **Distributed (Git's style):** Every developer has a **full copy** of the entire project history on their own computer.

> **Important:** This is one of the most important ideas in Git — your local copy is a complete, independent repository, not just a snapshot.

### Why Developers Use Git
- It's fast, free, and works offline
- It's the industry standard
- It supports teams of any size
- It protects your work from being lost or overwritten

**Instructor Notes**
- **Emphasize:** Git works locally first — you don't need internet to commit.
- **Ask students:** "Have you ever lost work because you overwrote a file? How did that feel?"
- **Common confusion:** Students often think Git and GitHub are the same thing. Tell them we'll clarify this in the next section.
- **Live demo idea:** Show a messy folder of "final_v2_real" files as a joke to set the scene.

---

# 2. Git vs GitHub

### What is Git?
Git is a **tool** installed on your computer. It tracks changes in your project's files. Git works **locally** — no internet required.

### What is GitHub?
GitHub is a **website/service** that hosts Git repositories online. It lets you:
- Store your code in the cloud
- Collaborate with other developers
- Use extra tools like Issues, Pull Requests, and project boards

> **Important:** Git is the *technology*. GitHub is a *company/platform* that uses Git. You can use Git without ever using GitHub.

### Local Repository vs Remote Repository
- **Local repository:** Lives on your computer. Created with `git init` or `git clone`.
- **Remote repository:** Lives on a server (like GitHub). You push/pull changes to sync it with your local repository.

### GitHub Alternatives
GitHub is not the only option:
- **GitLab** – similar to GitHub, popular in companies for private DevOps pipelines
- **Bitbucket** – similar service, often used with Atlassian tools (Jira, Trello)

All of them use **Git** underneath. Learning Git means you can use any of these platforms.

### Comparison Table

| Feature | Git | GitHub |
|---|---|---|
| Type | Version control software | Cloud hosting platform |
| Runs | On your computer | On the internet |
| Needs internet? | No | Yes (to access remote data) |
| Stores history | Yes | Yes (hosts your Git history) |
| Has Pull Requests / Issues | No | Yes |
| Alternatives | Mercurial, SVN | GitLab, Bitbucket |

**Instructor Notes**
- **Emphasize:** "You could use Git your whole career without touching GitHub."
- **Ask students:** "If GitHub disappeared tomorrow, would your Git history disappear too?" (Answer: No — it's still on your computer.)
- **Common confusion:** Believing `git push` sends code "to Git" instead of "to GitHub."

---

# 3. Installing Git

### Ubuntu / Linux
```bash
sudo apt update
sudo apt install git
```

### Windows
Download the installer from the official Git website and run it. Keep default options unless you have a specific reason to change them.

### macOS
```bash
brew install git
```
(If you don't have Homebrew, Git also comes bundled with Xcode Command Line Tools.)

### Verify Installation
```bash
git --version
```

**Expected output (version number may differ):**
```text
git version 2.43.0
```

> **Tip:** If you get "command not found," restart your terminal or check your installation steps again.

---

# 4. Git Configuration

Before using Git, tell it who you are. This information is attached to every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Checking your configuration
```bash
git config --list
```

**Expected output (example):**
```text
user.name=Your Name
user.email=you@example.com
core.editor=nano
```

### Why these settings matter
- `user.name` and `user.email` appear on every commit you create
- `--global` means this setting applies to **all** repositories on your computer
- You can override it per-project by running the same command **without** `--global` inside a specific repository

> **Tip:** Use the same email as your GitHub account so your commits are correctly linked to your GitHub profile later.

**Instructor Notes**
- **Live demo:** Run `git config --list` and point out that name/email are just text — Git does not verify identity.
- **Common confusion:** Students think this "creates an account." It doesn't — it's just local labeling.

---

# 5. Git Repository

### What is a repository?
A repository (or "repo") is a project folder that Git is tracking. It contains your files **plus** a hidden folder that stores the entire history.

### `git init`
```bash
mkdir my-project
cd my-project
git init
```

**Expected output:**
```text
Initialized empty Git repository in /path/to/my-project/.git/
```

### What happens after `git init`?
Git creates a hidden `.git` folder inside your project. This folder contains:
- The entire commit history
- Configuration
- References to branches

> **Important:** The `.git` folder **is** the repository. If you delete it, you lose all Git history (but your files remain).

### Working Directory
The **working directory** is simply the normal folder where you edit your files — the ones you see in your file explorer or code editor.

**Instructor Notes**
- **Live demo:** Run `git init`, then `ls -a` to show the `.git` folder appearing.
- **Ask students:** "What do you think would happen if we deleted the `.git` folder?"
- **Common confusion:** Students think `git init` uploads anything anywhere. It does not — everything is 100% local.

---

# 6. Git's Three Main Areas

Git organizes your work into three areas:

```text
Working Directory
        |
        |  git add
        v
   Staging Area
        |
        |  git commit
        v
Repository (Commit History)
```

1. **Working Directory** — where you actually edit files.
2. **Staging Area** — a "waiting room" for changes you plan to commit.
3. **Repository** — the permanent, saved history of committed snapshots.

### Why does Git use a staging area?
The staging area lets you **choose exactly** which changes go into your next commit — even if you changed 10 files, you can commit just 2 of them.

> **Real-world analogy:** Think of staging like a shopping cart. You can put items in the cart (`git add`) and remove them again before "checking out" (`git commit`). Only what's in the cart gets purchased.

**Instructor Notes**
- **Emphasize:** This is the single most important mental model in Git. Draw the diagram on a whiteboard.
- **Ask students:** "Why not just commit everything automatically?"
- **Common confusion:** Students think `git add` saves the file. It only stages it — nothing is permanently recorded until `git commit`.

---

# 7. Checking Repository Status

```bash
git status
```

This command tells you exactly what state your project is in.

### Untracked file example
```text
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        newfile.py
```
Meaning: Git sees the file but is not tracking it yet.

### Modified file example
```text
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   app.py
```
Meaning: The file is tracked, but has changes not yet staged.

### Staged file example
```text
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   app.py
```
Meaning: The file is staged and ready to be committed.

### Clean working tree
```text
On branch main
nothing to commit, working tree clean
```
Meaning: Nothing has changed since the last commit.

> **Tip:** Run `git status` constantly. It's the safest command in Git and never changes anything.

---

# 8. Staging Files

```bash
git add file.py
```
Stages a **specific file**.

```bash
git add .
```
Stages **all changed files** in the current folder and subfolders.

### When to use each
- Use `git add file.py` when you only want to commit specific, related changes.
- Use `git add .` when you're confident every change belongs in the next commit.

> **Warning:** `git add .` can accidentally stage files you didn't mean to commit (like temporary files or secrets). Always run `git status` first.

---

# 9. Commits

### What is a commit?
A commit is a **saved snapshot** of your staged changes, along with a message describing what changed.

### Why commits are important
- They create a permanent point you can return to
- They document the history of *why* changes were made
- They allow teams to understand project evolution

### Good commit messages
- Use present tense: "Add login form" not "Added login form"
- Be specific: "Fix null pointer in payment service" not "fix bug"
- Keep the first line under ~50 characters when possible

### Creating a commit
```bash
git commit -m "Add user authentication"
```

**Expected output (example):**
```text
[main 4a1f9c2] Add user authentication
 1 file changed, 12 insertions(+)
```

### Commit history conceptually
Each commit points to the **previous commit**, forming a chain:

```text
C1 --- C2 --- C3 --- C4 (main)
```

This chain is your project's full history.

**Instructor Notes**
- **Live demo:** Make 2–3 small commits live and show the chain forming with `git log --oneline`.
- **Ask students:** "Why not just save one giant commit at the end of the project?"
- **Common confusion:** Students forget to `git add` before `git commit`, and are confused why nothing happens.

---

# 10. Viewing Changes

```bash
git diff
```
Shows changes in the **working directory** that are **not staged yet**.

```bash
git diff --staged
```
Shows changes that **are staged**, waiting to be committed.

### Difference
| Command | Shows |
|---|---|
| `git diff` | Working directory vs staging area |
| `git diff --staged` | Staging area vs last commit |

> **Tip:** Always run `git diff --staged` right before committing, as a final check.

---

# 11. Viewing Commit History

```bash
git log
```
Shows full commit details: author, date, message, and unique ID (hash).

```bash
git log --oneline
```
Shows a compact, one-line-per-commit summary.

**Example output:**
```text
4a1f9c2 Add user authentication
9d3e21a Set up project structure
```

```bash
git log --graph --oneline --all
```
Shows a visual graph of branches and merges — very useful once branching is introduced.

---

# 12. `.gitignore`

### Why `.gitignore` exists
Some files should **never** be tracked by Git — temporary files, secrets, or generated files. `.gitignore` tells Git to ignore them.

### Files that should usually not be committed
- Environment variable files (`.env`)
- Dependency folders (`node_modules/`)
- Compiled/generated files
- IDE settings folders
- Log files

> **Warning:** Never commit files containing passwords, API keys, or secrets. Once committed, they remain in history even if deleted later.

### Python example
```text
__pycache__/
*.pyc
venv/
.env
```

### Django example
```text
*.sqlite3
media/
staticfiles/
.env
```

### Node.js example
```text
node_modules/
.env
dist/
npm-debug.log
```

### Realistic combined example
```text
# Environment
.env

# Python
__pycache__/
*.pyc
venv/

# Node
node_modules/
dist/

# Editor
.vscode/
.idea/

# OS
.DS_Store
```

> **Tip:** Create your `.gitignore` file **before** your first commit whenever possible.

---

# 13. Branches

### What is a branch?
A branch is an **independent line of development**. It lets you work on new features without affecting the main codebase.

### Why branches are useful
- Multiple people can work on different features at the same time
- You can experiment safely
- `main` stays stable and deployable

### Real-world analogy
Think of a branch like a **parallel universe copy of your document**. You can edit the copy freely, and later decide to bring those changes back into the original.

### Commands
```bash
git branch
```
Lists all branches.

```bash
git switch feature/login
```
Switches to an existing branch.

```bash
git switch -c feature/login
```
Creates **and** switches to a new branch in one step.

### Visual diagram
```text
main:      C1---C2---C3
                  \
feature/login:     C4---C5
```

> **Tip:** `git checkout` was the older command used for switching branches. `git switch` is the modern, clearer replacement. `git checkout` still works and you'll see it in older tutorials, but `git switch` is recommended for beginners.

**Instructor Notes**
- **Emphasize:** Branches are just pointers to commits, not full copies of the project — this is why branching in Git is fast.
- **Ask students:** "What would happen if two people edited `main` directly at the same time?"
- **Live demo:** Create a branch, make a commit, then switch back to `main` and show the file change disappears.

---

# 14. Merging Branches

```bash
git switch main
git merge feature/login
```

### Fast-forward merge
Happens when `main` has **no new commits** since the branch was created. Git simply moves the `main` pointer forward.

```text
Before:
main:      C1---C2
                  \
feature/login:     C3---C4

After (fast-forward):
main:      C1---C2---C3---C4
```

### Three-way merge (beginner-friendly)
Happens when **both** branches have new commits. Git combines them using three points: the common ancestor and the tip of each branch, creating a **new merge commit**.

```text
main:            C1---C2---------C5 (merge commit)
                       \         /
feature/login:          C3---C4
```

### What happens during a merge
1. Git compares the two branches
2. It combines the changes automatically where possible
3. If both branches changed the *same* lines, Git asks you to resolve it manually (a **conflict** — covered next)

**Instructor Notes**
- **Live demo:** Do one fast-forward merge and one three-way merge to show the difference in `git log --graph`.
- **Common confusion:** Students think merging always creates a new commit — clarify that fast-forward merges do not.

---

# 15. Merge Conflicts

### Why conflicts happen
A conflict happens when **two branches change the same lines** of the same file, and Git cannot automatically decide which version to keep.

### Example scenario
**On `main`:**
```python
greeting = "Hello, World!"
```

**On `feature/login`:**
```python
greeting = "Welcome to our app!"
```

Running `git merge feature/login` on `main` produces a conflict.

### How Git marks conflicts
```text
<<<<<<< HEAD
greeting = "Hello, World!"
=======
greeting = "Welcome to our app!"
>>>>>>> feature/login
```

- `<<<<<<< HEAD` — start of your current branch's version
- `=======` — divider
- `>>>>>>> feature/login` — end, showing the incoming branch's version

### How to resolve them
1. Open the file and decide what the final content should be
2. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Keep the correct code (yours, theirs, or a combination)

**Resolved example:**
```python
greeting = "Welcome to our app!"
```

### Stage and finish the merge
```bash
git add file.py
git commit
```

> **Important:** After resolving a conflict, you must `git add` the file to mark it as resolved, then commit to complete the merge.

> **Tip:** Never panic during a conflict — it only means Git needs your judgment, not that anything is broken.

**Instructor Notes**
- **Live demo:** Deliberately create a real conflict live and resolve it step by step. This is one of the most valuable demos in the course.
- **Ask students:** "Why can't Git just guess which version is correct?"

---

# 16. GitHub

### Creating a GitHub account
Go to github.com and sign up with an email address and username.

### Creating a repository
1. Click **New repository**
2. Choose a name
3. Choose Public or Private
4. Optionally add a README
5. Click **Create repository**

### Public vs Private repositories
| Type | Who can see it |
|---|---|
| Public | Anyone on the internet |
| Private | Only you and people you invite |

### README
A `README.md` file is shown automatically on the repository's main page. It should explain what the project is and how to use it.

### Repository settings
Includes options like: default branch name, collaborators, branch protection rules, and visibility.

---

# 17. Connecting Local Git to GitHub

```bash
git remote -v
```
Lists the remote repositories your local repo is connected to (empty at first).

```bash
git remote add origin <repository-url>
```
Connects your local repository to a GitHub repository.

### What does `origin` mean?
`origin` is just a **nickname** for the remote repository's URL. By convention, the first/main remote is called `origin`, but it could technically be named anything.

**Example:**
```bash
git remote add origin https://github.com/yourname/my-project.git
git remote -v
```

**Expected output:**
```text
origin  https://github.com/yourname/my-project.git (fetch)
origin  https://github.com/yourname/my-project.git (push)
```

---

# 18. Push

```bash
git push -u origin main
```
Pushes your local `main` branch to the `origin` remote, and sets up **tracking** (`-u`) so future pushes are simpler.

```bash
git push
```
After tracking is set up, this is enough to push new commits.

### Local branch vs Remote branch
- **Local branch:** exists only on your computer
- **Remote branch:** the matching branch stored on GitHub (referred to as `origin/main`)

### Upstream tracking
Once you use `-u`, Git remembers the connection between your local branch and the remote branch, so it knows exactly where to push/pull by default.

---

# 19. Clone

```bash
git clone <repository-url>
```

**Example:**
```bash
git clone https://github.com/yourname/my-project.git
```

### What happens when cloning
Git:
1. Downloads the entire repository, including full history
2. Creates a local folder with all the files
3. Automatically sets up `origin` to point back to the source repository

> **Tip:** Cloning is usually how you start working on an *existing* project (compared to `git init`, which starts a *new* one).

---

# 20. Pull and Fetch

```bash
git fetch
```
Downloads new commits from the remote **without** merging them into your working files.

```bash
git pull
```
Downloads new commits **and** merges them into your current branch (`fetch` + `merge` combined).

### Diagram
```text
git fetch:
Remote --> Local (.git storage only)

git pull:
Remote --> Local (.git storage) --> merged into your working files
```

### Why the difference matters
`git fetch` lets you **safely review** incoming changes before merging them. `git pull` immediately changes your working files, which can cause conflicts if you're not ready.

> **Tip:** If you're unsure what changed remotely, use `git fetch` followed by `git log origin/main` to inspect before merging.

**Instructor Notes**
- **Ask students:** "Why would a cautious developer prefer `fetch` over `pull`?"
- **Common confusion:** Assuming `pull` is always safe — it can create conflicts just like a local merge.

---

# 21. GitHub Collaboration

### Realistic team workflow
```text
main
  |
  +--- feature branch
  |
  +--- commit
  |
  +--- push
  |
  +--- Pull Request
  |
  +--- Code Review
  |
  +--- Merge
```

### Purpose of Pull Requests
A Pull Request (PR) is a **request to merge** your branch into another branch (usually `main`), combined with:
- A place to discuss the change
- A way for teammates to review code before it becomes part of the project
- Automated checks (tests, linting) that can run before merging

> **Important:** PRs are a GitHub feature, not a Git feature. Git itself has no concept of "Pull Requests."

---

# 22. Forks

### What is a fork?
A fork is your **own copy** of someone else's GitHub repository, under your own account.

### Fork vs Clone
| Fork | Clone |
|---|---|
| Happens on GitHub | Happens on your computer |
| Creates a new repository under your account | Downloads a copy of a repository locally |
| Used to contribute to projects you don't own | Used to get a working copy of any repository |

### When developers use forks
When they want to contribute to a project they don't have write access to (very common in open source).

### Open-source workflow
1. Fork the project on GitHub
2. Clone **your fork** locally
3. Create a branch and make changes
4. Push to your fork
5. Open a Pull Request from your fork back to the original project

---

# 23. Pull Requests

### Creating a Pull Request
On GitHub, after pushing a branch, click **Compare & pull request**.

### Key parts of a Pull Request
- **Title** — short summary of the change
- **Description** — explains *what* changed and *why*
- **Reviewers** — teammates asked to review the code
- **Review comments** — feedback left on specific lines
- **Approving** — reviewer confirms the code is ready
- **Requested changes** — reviewer asks for edits before merging
- **Merging** — combining the PR branch into the target branch

> **Tip:** Small, focused Pull Requests are much easier to review than huge ones.

---

# 24. Undoing Changes

Git offers several ways to undo mistakes. Choosing the right one matters.

```bash
git restore file.py
```
Discards **unstaged** changes in the working directory, restoring the file to its last committed version.

> **Warning:** This permanently deletes your uncommitted edits to that file. There is no undo.

```bash
git restore --staged file.py
```
Removes a file from the staging area **without** deleting your changes — it goes back to "modified but not staged."

```bash
git commit --amend
```
Edits the **most recent** commit (message and/or staged changes).

> **Warning:** Don't amend commits that have already been pushed and shared with others — it rewrites history.

```bash
git revert <commit>
```
Creates a **new commit** that undoes the changes from a specific previous commit, without deleting history. Safe for shared branches.

```bash
git reset
```
Moves the branch pointer to a different commit. Can also unstage or discard changes depending on the flag used.

> **Warning:** `git reset --hard` permanently discards changes in your working directory. Use with extreme caution.

### Restore vs Reset vs Revert (beginner-safe explanation)

| Command | What it affects | Safe for shared history? | Typical use |
|---|---|---|---|
| `git restore` | Working directory / staging area | Yes | Undo local, uncommitted edits |
| `git reset` | Commit history (moves branch pointer) | No (if pushed) | Undo local commits before pushing |
| `git revert` | Adds a new commit that undoes changes | Yes | Undo a commit that's already shared |

> **Important:** If you're unsure, `git revert` is almost always the safest option once something has been pushed to GitHub.

**Instructor Notes**
- **Emphasize:** Spend extra time here — this is the section that causes the most fear and mistakes for beginners.
- **Live demo:** Show `restore`, `reset --soft`, and `revert` on a throwaway test repo, side by side.
- **Ask students:** "If you already pushed a bad commit that a teammate pulled, should you use `reset` or `revert`? Why?"

---

# 25. Git Stash

```bash
git stash
```
Temporarily saves your uncommitted changes and gives you a clean working directory, without committing anything.

```bash
git stash list
```
Shows all stashed changes.

```bash
git stash pop
```
Restores the most recent stashed changes and removes them from the stash list.

### Realistic scenario
You're halfway through a feature when your teammate asks you to urgently fix a bug on `main`. You don't want to commit unfinished work.

```bash
git stash
git switch main
# fix the bug, commit, push
git switch feature/login
git stash pop
```

> **Tip:** Stash is like a clipboard for uncommitted work — quick, temporary, and local only.

---

# 26. Git Tags

```bash
git tag
```
Lists existing tags.

```bash
git tag v1.0.0
```
Creates a tag on the current commit, usually marking a release.

```bash
git push origin v1.0.0
```
Pushes the tag to GitHub so others can see it too.

### Why tags are useful
Tags mark specific, important points in history — typically **releases** (e.g., `v1.0.0`, `v2.1.3`) — so you can always find or return to exactly what was shipped at that time.

---

# 27. SSH Authentication

### HTTPS vs SSH
| Method | How you authenticate |
|---|---|
| HTTPS | Username/password or personal access token |
| SSH | A cryptographic key pair stored on your computer |

### Why developers often use SSH
Once set up, SSH doesn't require typing credentials every time you push or pull.

### Basic SSH key concept
You generate two keys:
- A **private key** — stays secret on your computer
- A **public key** — added to your GitHub account

### How it works at a high level
When you connect to GitHub, your computer proves it holds the private key that matches the public key on your GitHub account — without ever sending the private key over the network.

> **Tip:** Never share your private key with anyone. Only the public key goes on GitHub.

---

# 28. GitHub Issues

### What Issues are
A way to track tasks, bugs, and ideas for a project directly on GitHub.

- **Bug reports** — describe something broken, with steps to reproduce
- **Feature requests** — propose new functionality
- **Assignments** — assign an issue to a specific person
- **Labels** — categorize issues (e.g., `bug`, `enhancement`, `urgent`)
- **Milestones** — group issues under a shared deadline or goal (e.g., "v2.0 release")

> **Tip:** Well-written issues make collaboration far smoother, especially in larger teams.

---

# 29. GitHub README

A good `README.md` should typically contain:

- **Project description** — what the project does and why
- **Installation** — how to set it up locally
- **Usage** — how to run or use it
- **Technologies** — languages/frameworks used
- **Environment variables** — required configuration (never actual secret values)
- **Screenshots** — visuals of the app in action
- **Contributing** — how others can help
- **License** — legal terms for using the code

### Sample README structure
```markdown
# Project Name

Short description of what this project does.

## Installation
Step-by-step setup instructions.

## Usage
How to run the project.

## Technologies
- Language/framework 1
- Language/framework 2

## Environment Variables
Explain required variables (without real secret values).

## Screenshots
Add images here.

## Contributing
Guidelines for contributing.

## License
State the license type.
```

---

# 30. Common Git Mistakes

### 1. Forgot to run `git add`
- **Why it happens:** `git commit` only saves staged changes.
- **Diagnose:** `git status` shows unstaged changes.
- **Solution:** `git add <file>` then `git commit`.

### 2. Committed the wrong file
- **Why it happens:** `git add .` staged more than intended.
- **Diagnose:** `git show --stat HEAD` to see what was in the commit.
- **Solution:** `git restore --staged <file>` before committing, or `git commit --amend` if not yet pushed.

### 3. Wrong commit message
- **Why it happens:** Typo or rushed message.
- **Diagnose:** `git log -1`.
- **Solution:** `git commit --amend -m "Correct message"` (only if not pushed).

### 4. Pushed to the wrong branch
- **Why it happens:** Forgot to check current branch before pushing.
- **Diagnose:** `git branch` to see which branch you're on.
- **Solution:** Coordinate with your team; often solved with `git revert` on the wrong branch, then applying the change correctly.

### 5. Merge conflict
- **Why it happens:** Two branches changed the same lines.
- **Diagnose:** `git status` shows "both modified."
- **Solution:** Open the file, resolve markers, `git add`, then `git commit`.

### 6. Accidentally deleted changes
- **Why it happens:** Used `git restore` or `reset --hard` without checking status first.
- **Diagnose:** Check `git reflog` (a log of where `HEAD` has been) — it can sometimes help recover lost commits.
- **Solution:** Prevention is key — always run `git status`/`git diff` before destructive commands.

### 7. Git says "nothing to commit"
- **Why it happens:** There are simply no changes, or changes weren't saved to the file yet.
- **Diagnose:** Check if you saved the file in your editor.
- **Solution:** Save the file, then check `git status` again.

### 8. Git says the branch has "diverged"
- **Why it happens:** Your local branch and the remote branch each have commits the other doesn't have.
- **Diagnose:** `git status` explains how many commits ahead/behind you are.
- **Solution:** `git pull` to merge (or rebase, for advanced users) the remote changes in.

### 9. Forgot to pull before pushing
- **Why it happens:** Someone else pushed changes first.
- **Diagnose:** Git rejects the push with a "fetch first" message.
- **Solution:** `git pull`, resolve any conflicts, then `git push` again.

### 10. Accidentally committed `.env`
- **Why it happens:** No `.gitignore` was set up in time.
- **Diagnose:** `git log --all --full-history -- .env`.
- **Solution:** Remove it from tracking (`git rm --cached .env`), add it to `.gitignore`, commit, and **rotate any exposed secrets immediately**.

> **Warning:** Simply deleting a secret file in a new commit does NOT remove it from history. Anyone can still find it in old commits. Treat any exposed secret as compromised.

---

# 31. Professional Git Workflow

```text
main
  |
  +--- feature branch
  |
  +--- make changes
  |
  +--- git add
  |
  +--- git commit
  |
  +--- git push
  |
  +--- Pull Request
  |
  +--- Review
  |
  +--- Merge
```

### Why avoid making changes directly on `main`?
- `main` usually represents the **stable, deployable** version of the project
- Direct changes skip code review
- A mistake on `main` immediately affects everyone
- Feature branches let broken or unfinished work stay isolated

> **Important:** "Never commit directly to `main`" is one of the most common rules in professional teams.

---

# 32. Practical Exercises

### Exercise 1: Create a Repository
**Goal:** Practice initializing a Git repository.
**Starting situation:** An empty folder.
**Commands:**
```bash
mkdir practice-repo
cd practice-repo
git init
```
**Expected result:** A `.git` folder is created; `git status` shows a clean, empty repository.
**Challenge:** What file/folder did `git init` create, and where is it?

---

### Exercise 2: Make Commits
**Goal:** Practice staging and committing.
**Starting situation:** The `practice-repo` from Exercise 1.
**Commands:**
```bash
echo "print('Hello Git')" > app.py
git add app.py
git commit -m "Add hello world script"
```
**Expected result:** `git log --oneline` shows one commit.
**Challenge:** Make two more commits with different small changes to `app.py`.

---

### Exercise 3: Use `.gitignore`
**Goal:** Prevent unwanted files from being tracked.
**Starting situation:** `practice-repo` with a fake secrets file.
**Commands:**
```bash
echo "SECRET_KEY=12345" > .env
echo ".env" > .gitignore
git status
```
**Expected result:** `.env` does not appear as untracked in `git status`.
**Challenge:** Try adding `__pycache__/` and `*.log` to `.gitignore` too.

---

### Exercise 4: Create a Branch
**Goal:** Practice isolated development.
**Commands:**
```bash
git switch -c feature/greeting
echo "print('Hi there!')" >> app.py
git add app.py
git commit -m "Add greeting message"
```
**Expected result:** `git branch` shows two branches; changes only exist on `feature/greeting`.
**Challenge:** Switch back to `main` and confirm the greeting line is missing.

---

### Exercise 5: Merge a Branch
**Goal:** Practice a fast-forward merge.
**Commands:**
```bash
git switch main
git merge feature/greeting
```
**Expected result:** `app.py` on `main` now includes the greeting line.
**Challenge:** Run `git log --graph --oneline` and describe what you see.

---

### Exercise 6: Resolve a Merge Conflict
**Goal:** Practice resolving conflicts safely.
**Starting situation:** Create two branches that edit the same line differently, then merge them.
**Commands:**
```bash
git switch -c branch-a
echo "message = 'Version A'" > conflict.py
git add conflict.py
git commit -m "Add version A"

git switch main
git switch -c branch-b
echo "message = 'Version B'" > conflict.py
git add conflict.py
git commit -m "Add version B"

git switch main
git merge branch-a
git merge branch-b
```
**Expected result:** A conflict appears in `conflict.py`.
**Challenge:** Resolve the conflict, keeping only one version, then commit.

---

### Exercise 7: Connect GitHub
**Goal:** Link a local repo to GitHub.
**Starting situation:** A GitHub repository created (empty).
**Commands:**
```bash
git remote add origin <repository-url>
git remote -v
```
**Expected result:** `origin` appears with fetch and push URLs.
**Challenge:** What happens if you run `git remote add origin` twice with different URLs?

---

### Exercise 8: Push and Pull
**Goal:** Sync local and remote repositories.
**Commands:**
```bash
git push -u origin main
git pull
```
**Expected result:** Your commits appear on GitHub; `git pull` reports "Already up to date" if nothing changed remotely.
**Challenge:** Edit a file directly on GitHub, then run `git pull` locally to see it appear.

---

### Exercise 9: Create a Pull Request
**Goal:** Practice the GitHub collaboration flow.
**Commands:**
```bash
git switch -c feature/readme-update
echo "## New Section" >> README.md
git add README.md
git commit -m "Update README with new section"
git push -u origin feature/readme-update
```
**Expected result:** GitHub shows a prompt to open a Pull Request for this branch.
**Challenge:** Open the PR, write a description, and merge it through the GitHub interface.

---

### Exercise 10: Undo a Mistake
**Goal:** Practice safe undo operations.
**Commands:**
```bash
echo "oops" >> app.py
git restore app.py
```
**Expected result:** The "oops" line is removed since it was never staged or committed.
**Challenge:** Repeat the exercise, but this time stage the change first — which command do you need instead of `git restore`?

---

# 33. Final Mini Project

**Project: "My First Team Feature"**

Simulate a small, realistic team workflow from start to finish.

### Requirements
1. Create a new GitHub repository named `my-first-team-feature`
2. Clone it locally
3. Add a `.gitignore` suited for your chosen language
4. Create an initial commit with a basic project file (e.g., `app.py` or `index.js`)
5. Create a feature branch: `feature/add-config`
6. Add a configuration file and commit it
7. Push the feature branch to GitHub
8. Open a Pull Request describing the change
9. Review your own PR (leave at least one comment)
10. Merge the Pull Request into `main`
11. Pull the updated `main` locally
12. Create a release tag: `v1.0.0` and push it

### Deliverable
A GitHub repository showing: multiple commits, a merged Pull Request, a clean `.gitignore`, and a `v1.0.0` tag.

> **Tip for Instructor:** This project touches every major skill from the course — use it as a graded or reviewed final exercise.

---

# 34. Git Command Cheat Sheet

| Command | Purpose | Example |
|---|---|---|
| `git --version` | Check installed Git version | `git --version` |
| `git config --global user.name` | Set your name | `git config --global user.name "Ana"` |
| `git config --global user.email` | Set your email | `git config --global user.email "ana@mail.com"` |
| `git init` | Create a new repository | `git init` |
| `git clone` | Copy an existing repository | `git clone <url>` |
| `git status` | Show current state of repo | `git status` |
| `git add` | Stage changes | `git add file.py` |
| `git commit` | Save staged changes | `git commit -m "message"` |
| `git diff` | Show unstaged changes | `git diff` |
| `git diff --staged` | Show staged changes | `git diff --staged` |
| `git log` | View commit history | `git log --oneline` |
| `git branch` | List/create branches | `git branch` |
| `git switch` | Change branches | `git switch main` |
| `git switch -c` | Create and switch branch | `git switch -c feature/x` |
| `git merge` | Merge a branch into current | `git merge feature/x` |
| `git remote add` | Connect to a remote repo | `git remote add origin <url>` |
| `git push` | Upload commits to remote | `git push -u origin main` |
| `git pull` | Download and merge remote changes | `git pull` |
| `git fetch` | Download remote changes only | `git fetch` |
| `git restore` | Discard unstaged changes | `git restore file.py` |
| `git restore --staged` | Unstage a file | `git restore --staged file.py` |
| `git commit --amend` | Edit last commit | `git commit --amend` |
| `git revert` | Undo a commit safely | `git revert a1b2c3d` |
| `git reset` | Move branch pointer / unstage | `git reset --soft HEAD~1` |
| `git stash` | Temporarily save changes | `git stash` |
| `git stash pop` | Restore stashed changes | `git stash pop` |
| `git tag` | Mark a release point | `git tag v1.0.0` |

---

# 35. Git Terminology (Glossary)

| Term | Meaning |
|---|---|
| **Repository** | A project folder tracked by Git, including its full history |
| **Working tree** | The actual files you see and edit on disk |
| **Staging area** | A holding area for changes about to be committed |
| **Commit** | A saved snapshot of staged changes, with a message |
| **Branch** | An independent line of development |
| **Merge** | Combining changes from one branch into another |
| **Conflict** | When Git can't automatically combine changes to the same lines |
| **Remote** | A version of your repository hosted elsewhere (e.g., GitHub) |
| **Origin** | The default nickname for your main remote repository |
| **Clone** | Downloading a full copy of a remote repository |
| **Fetch** | Downloading remote changes without merging them |
| **Pull** | Fetching and merging remote changes in one step |
| **Push** | Uploading local commits to a remote repository |
| **Pull Request** | A GitHub feature requesting to merge one branch into another, with review |
| **Fork** | Your own copy of someone else's GitHub repository |
| **Tag** | A permanent label marking a specific commit, usually a release |
| **HEAD** | A pointer to your current position (usually the tip of the current branch) |
| **Revert** | Creating a new commit that undoes an earlier commit |
| **Reset** | Moving the branch pointer to a different commit (can discard history) |
| **Stash** | Temporary, uncommitted storage for changes you're not ready to commit |

---

# 36. Final Review

## Part A: Multiple-Choice Questions (20)

1. What does Git primarily track?
   a) File names only
   b) Changes to files over time
   c) Internet connections
   d) Screenshots

2. Which of these is true?
   a) Git and GitHub are the same thing
   b) GitHub is a tool, Git is a website
   c) Git is a tool, GitHub is a website/platform
   d) GitHub replaces Git

3. Which command creates a new local repository?
   a) `git clone`
   b) `git init`
   c) `git start`
   d) `git new`

4. What does `git add` do?
   a) Commits changes permanently
   b) Deletes a file
   c) Stages changes for the next commit
   d) Uploads changes to GitHub

5. What does `git commit -m "message"` do?
   a) Stages a file
   b) Saves staged changes with a message
   c) Deletes commit history
   d) Creates a new branch

6. What does `git status` show?
   a) The current state of tracked/untracked/staged files
   b) The remote repository URL
   c) The list of all commits ever made
   d) Your GitHub username

7. What is the purpose of `.gitignore`?
   a) To delete files permanently
   b) To tell Git which files to skip tracking
   c) To create backups
   d) To rename branches

8. What does `git branch` show?
   a) The commit history
   b) The list of branches
   c) The remote URL
   d) The staged files

9. What is a fast-forward merge?
   a) A merge that creates a new commit
   b) A merge where the branch pointer simply moves forward
   c) A merge that deletes history
   d) A type of conflict

10. What causes a merge conflict?
    a) Two branches changing the same lines differently
    b) Running `git status`
    c) Creating a new branch
    d) Cloning a repository

11. Which symbol marks the start of a conflict block?
    a) `>>>>>>>`
    b) `<<<<<<<`
    c) `=======`
    d) `#####`

12. What is `origin` in Git?
    a) The first commit ever made
    b) A default nickname for a remote repository
    c) A branch name
    d) A type of merge

13. What does `git push -u origin main` do?
    a) Downloads changes
    b) Uploads local commits and sets up tracking
    c) Deletes the remote branch
    d) Creates a new repository

14. What is the difference between `fetch` and `pull`?
    a) They are identical
    b) `fetch` downloads only; `pull` downloads and merges
    c) `pull` downloads only; `fetch` downloads and merges
    d) Neither downloads anything

15. What is a Pull Request?
    a) A Git command
    b) A GitHub feature to propose and review a merge
    c) A way to delete a repository
    d) A type of branch

16. What is a fork?
    a) A local copy created with `git clone`
    b) Your own GitHub copy of someone else's repository
    c) A type of commit
    d) A merge conflict

17. Which command safely undoes an already-pushed commit?
    a) `git reset --hard`
    b) `git revert`
    c) `git restore`
    d) `git delete`

18. What does `git stash` do?
    a) Deletes uncommitted changes
    b) Temporarily saves uncommitted changes
    c) Creates a permanent commit
    d) Pushes changes to GitHub

19. What is the purpose of a Git tag?
    a) To mark a specific point, usually a release
    b) To create a new branch
    c) To delete history
    d) To resolve conflicts

20. Why should you avoid committing `.env` files?
    a) They make the repo run faster
    b) They often contain secrets/passwords
    c) Git doesn't support them
    d) They are always empty

---

## Part B: Practical Questions (10)

1. Write the commands to initialize a repository and make your first commit.
2. How do you check which files are staged versus unstaged?
3. Write the commands to create a new branch called `feature/cart` and switch to it.
4. How would you merge `feature/cart` into `main`?
5. Show the conflict markers Git uses and explain each part.
6. Write the commands to connect a local repo to a GitHub repository and push it for the first time.
7. What command would you use to download remote changes without merging them yet?
8. Write the commands to undo uncommitted changes in `app.py`.
9. How would you safely undo a commit that has already been pushed and pulled by teammates?
10. Write the commands to create a release tag `v2.0.0` and push it to GitHub.

---

## Part C: Interview Questions for Junior Developers (10)

1. Explain the difference between Git and GitHub in your own words.
2. What is the staging area, and why does it exist?
3. Explain the difference between `git merge` and a fast-forward merge.
4. What causes a merge conflict, and how do you resolve one?
5. What's the difference between `git fetch` and `git pull`?
6. Explain the difference between `git restore`, `git reset`, and `git revert`.
7. What is a Pull Request, and why is it important in team workflows?
8. What is the difference between a fork and a clone?
9. Why shouldn't developers commit directly to `main` in a professional workflow?
10. What would you do if you accidentally committed a secret API key?

---

## Answers

### Part A: Multiple-Choice Answers
1. b — 2. c — 3. b — 4. c — 5. b — 6. a — 7. b — 8. b — 9. b — 10. a
11. b — 12. b — 13. b — 14. b — 15. b — 16. b — 17. b — 18. b — 19. a — 20. b

### Part B: Practical Answers
1.
```bash
git init
git add .
git commit -m "Initial commit"
```
2. Run `git status`: unstaged changes appear under "Changes not staged for commit"; staged changes appear under "Changes to be committed."
3.
```bash
git switch -c feature/cart
```
4.
```bash
git switch main
git merge feature/cart
```
5.
```text
<<<<<<< HEAD
(your branch's version)
=======
(incoming branch's version)
>>>>>>> branch-name
```
`<<<<<<< HEAD` marks the start of your current branch's content, `=======` separates the two versions, and `>>>>>>> branch-name` marks the end of the incoming branch's content.
6.
```bash
git remote add origin <repository-url>
git push -u origin main
```
7.
```bash
git fetch
```
8.
```bash
git restore app.py
```
9.
```bash
git revert <commit-hash>
```
10.
```bash
git tag v2.0.0
git push origin v2.0.0
```

### Part C: Interview Answer Guidance
1. Git is the version control tool that runs locally; GitHub is an online platform that hosts Git repositories and adds collaboration features.
2. The staging area is a middle step between editing files and committing, letting developers choose exactly which changes go into the next commit.
3. A regular merge can create a new merge commit combining two diverged histories; a fast-forward merge simply moves the branch pointer forward because there was no divergence.
4. Conflicts happen when two branches change the same lines differently; they're resolved by manually editing the conflicted file, removing conflict markers, staging the file, and committing.
5. `git fetch` only downloads remote changes; `git pull` downloads and immediately merges them into the current branch.
6. `git restore` undoes uncommitted changes; `git reset` moves the branch pointer (and can unstage or discard commits locally); `git revert` creates a new commit that safely undoes a previous commit, ideal for shared history.
7. A Pull Request is a GitHub feature that proposes merging one branch into another, allowing code review and discussion before changes join the main codebase.
8. A clone downloads a copy of a repository you already have access to; a fork creates your own separate copy under your GitHub account, typically used to contribute to projects you don't own.
9. Committing directly to `main` skips code review and can break the stable, deployable version of the project for the whole team.
10. Remove the file from tracking, add it to `.gitignore`, commit the fix, and immediately rotate/replace the exposed secret, since it remains visible in Git history even after removal.

---

# End of Course

Congratulations — you've now covered the essential skills for using Git and GitHub as a beginner developer, from local commits to full team collaboration workflows. Keep practicing with real projects to build confidence.

> **Tip:** The best way to master Git is to use it daily, even for small personal projects.
