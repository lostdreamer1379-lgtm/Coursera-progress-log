import os
import subprocess
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────
README_FILE = "README.md"

# ─────────────────────────────────────────────
#  HELPER: Run a shell command with error handling
# ─────────────────────────────────────────────
def run_command(command: list[str]) -> bool:
    """
    Runs a shell command using subprocess.run.
    Returns True on success, False on failure.
    """
    print(f"\n⏳ Running: {' '.join(command)}")
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"❌ Command failed: {' '.join(command)}")
        print(f"   STDERR: {result.stderr.strip()}")
        return False
    print(f"✅ Success: {' '.join(command)}")
    if result.stdout.strip():
        print(f"   OUTPUT: {result.stdout.strip()}")
    return True

# ─────────────────────────────────────────────
#  STEP 1: Collect user input
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("  📘 Coursera Daily Progress Logger")
print("=" * 55)

course_name = input("\n📚 Which Coursera course are you working on?\n> ").strip()
if not course_name:
    print("❌ Course name cannot be empty. Exiting.")
    exit(1)

learning_notes = input("\n✏️  What did you learn or complete today?\n> ").strip()
if not learning_notes:
    print("❌ Learning notes cannot be empty. Exiting.")
    exit(1)

# ─────────────────────────────────────────────
#  STEP 2: Format the Markdown entry
# ─────────────────────────────────────────────
today = datetime.now()
date_str      = today.strftime("%B %d, %Y")          # e.g. September 20, 2026
weekday_str   = today.strftime("%A")                  # e.g. Saturday
timestamp_str = today.strftime("%Y-%m-%d %H:%M")     # e.g. 2026-09-20 14:30

markdown_entry = f"""
---

### 📅 {date_str} ({weekday_str})

| Field         | Details                        |
|---------------|--------------------------------|
| **Course**    | {course_name}                  |
| **Logged at** | {timestamp_str}                |

**📝 What I learned / completed today:**

> {learning_notes}

"""

# ─────────────────────────────────────────────
#  STEP 3: Append the entry to README.md
# ─────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(script_dir, README_FILE)

# Create README.md with a header if it doesn't exist yet
if not os.path.exists(readme_path):
    print(f"\n📄 README.md not found — creating it at: {readme_path}")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# 📖 Coursera Learning Log\n\n")
        f.write("_Automatically tracked daily progress across Coursera courses._\n")

with open(readme_path, "a", encoding="utf-8") as f:
    f.write(markdown_entry)

print(f"\n✅ Entry appended to {README_FILE}")

# ─────────────────────────────────────────────
#  STEP 4: Git — add, commit, push
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("  🚀 Pushing to GitHub...")
print("=" * 55)

commit_message = f"[Coursera] {course_name} — {date_str}"

# Change working directory to the repo root
os.chdir(script_dir)

git_steps = [
    (["git", "add", "."],                             "Staging changes"),
    (["git", "commit", "-m", commit_message],         "Committing"),
    (["git", "push", "origin", "main"],               "Pushing to GitHub"),
]

all_passed = True
for command, label in git_steps:
    print(f"\n📌 {label}...")
    if not run_command(command):
        all_passed = False
        print(f"\n⚠️  Stopped at: {label}. Fix the error above and try again.")
        break

# ─────────────────────────────────────────────
#  STEP 5: Final status
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
if all_passed:
    print("  🎉 Done! Your progress is live on GitHub.")
    print(f"  🟩 A green square will appear on your profile today.")
else:
    print("  ⚠️  Push incomplete. See errors above.")
print("=" * 55)

# ─────────────────────────────────────────────
#  ⚠️  CRITICAL WARNING — READ THIS
# ─────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GitHub Contribution Graph Warning     ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  The green squares ONLY appear if your local Git     ║
║  email EXACTLY matches your GitHub account email.    ║
║                                                      ║
║  CHECK your current config with:                     ║
║    git config user.email                             ║
║                                                      ║
║  FIX it (for this repo only) with:                   ║
║    git config user.email "you@example.com"           ║
║                                                      ║
║  FIX it globally (all repos) with:                   ║
║    git config --global user.email "you@example.com"  ║
║                                                      ║
║  Your GitHub email is at:                            ║
║    github.com → Settings → Emails                   ║
║                                                      ║
║  Also ensure your repo is PUBLIC — private repos     ║
║  only count if "Private contributions" is turned on  ║
║  in your GitHub profile settings.                    ║
╚══════════════════════════════════════════════════════╝
""")
