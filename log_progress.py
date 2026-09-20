import os
import subprocess
from datetime import datetime

# ─────────────────────────────────────────────
#  DOMAIN CONFIGURATION
#  Add or remove domains here freely.
# ─────────────────────────────────────────────
DOMAINS = {

    "1": {
        "name":   "Frontend Development",
        "folder": "Frontend",
        "emoji":  "🌐",
        "color":  "HTML → CSS → JavaScript → DOM → APIs → React → Git/GitHub → Next.js"
    },

    "2": {
        "name":   "IoT (Internet of Things)",
        "folder": "Iot",
        "emoji":  "📡",
        "color":  "IoT Fundamentals → Electronics → Arduino → Sensors/Actuators → Embedded Systems → ESP32 → Wi-Fi → HTTP/MQTT → IoT Projects"
    },

    "3": {
        "name":   "SQL & Databases",
        "folder": "SQL",
        "emoji":  "🗄️",
        "color":  "SQL Basics → SELECT/Filtering → GROUP BY → JOINs → Subqueries → CASE → CTEs → Window Functions → Indexes → PostgreSQL/MySQL"
    },

    "4": {
        "name":   "Computer Networks (CN)",
        "folder": "CN",
        "emoji":  "🔗",
        "color":  "Networking Basics → OSI/TCP-IP → Ethernet → IP → TCP/UDP → DNS → HTTP/HTTPS → Routing → Ports/Sockets → Network Security Basics"
    },

    "5": {
        "name":   "Operating Systems (OS)",
        "folder": "OS",
        "emoji":  "⚙️",
        "color":  "OS Fundamentals → Processes → Threads → CPU Scheduling → Synchronization → Deadlocks → Memory Management → Paging → Virtual Memory → File Systems"
    },

    "6": {
        "name":   "AI & Machine Learning (AIML)",
        "folder": "AIML",
        "emoji":  "🤖",
        "color":  "AI/ML Basics → Data & Features → Supervised Learning → Unsupervised Learning → Regression → Classification → Model Training → Evaluation → Overfitting → Neural Networks → Deep Learning Basics"
    },

    "7": {
        "name":   "UI/UX Design",
        "folder": "UIUX",
        "emoji":  "🎨",
        "color":  "Figma Basics → Layout → Typography → Color → Spacing → Wireframes → UI Patterns → Components → Auto Layout → Prototyping → Design Systems → UX Fundamentals"
    },

    "8": {
        "name":   "Coursera (General)",
        "folder": "Coursera",
        "emoji":  "📘",
        "color":  "Frontend → IoT → SQL → UX/Design → CS Fundamentals → Certifications & Supporting Courses"
    },

    "9": {
    "name":   "DSA (Data Structures & Algorithms)",
    "folder": "dsa",
    "emoji":  "💻",
    "color":  "Arrays → Strings → Hashing → Two Pointers → Sliding Window → Linked Lists → Stacks → Queues → Binary Search → Trees → Heaps → Graphs → Dynamic Programming"
},

}

# ─────────────────────────────────────────────
#  HELPER: Run shell commands with error handling
# ─────────────────────────────────────────────
def run_command(command: list) -> bool:
    print(f"\n  ⏳ {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ❌ Failed: {result.stderr.strip()}")
        return False
    print(f"  ✅ OK")
    if result.stdout.strip():
        print(f"     {result.stdout.strip()}")
    return True

# ─────────────────────────────────────────────
#  HELPER: Ensure a domain's README exists
# ─────────────────────────────────────────────
def ensure_domain_readme(domain: dict, base_dir: str):
    folder_path = os.path.join(base_dir, domain["folder"])
    readme_path = os.path.join(folder_path, "README.md")

    os.makedirs(folder_path, exist_ok=True)

    if not os.path.exists(readme_path):
        header = (
            f"# {domain['emoji']} {domain['name']} — Learning Log\n\n"
            f"_Topics: {domain['color']}_\n\n"
            f"Tracking daily progress and notes in this domain.\n"
            f"Each entry is pushed automatically via `log_progress.py`.\n"
        )
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(header)
        print(f"\n  📄 Created: {domain['folder']}/README.md")

    return readme_path

# ─────────────────────────────────────────────
#  HELPER: Update root README dashboard
# ─────────────────────────────────────────────
def update_root_dashboard(base_dir: str):
    root_readme = os.path.join(base_dir, "README.md")

    lines = [
        "# 📚 Learning Progress Dashboard\n\n",
        "_Auto-updated daily log across multiple tech domains._\n\n",
        "---\n\n",
        "## 🗂️ Domains\n\n",
        "| # | Domain | Topics | Log |\n",
        "|---|--------|--------|-----|\n",
    ]

    for key, domain in DOMAINS.items():
        readme_link = f"[View Log](./{domain['folder']}/README.md)"
        lines.append(
            f"| {domain['emoji']} | **{domain['name']}** "
            f"| {domain['color']} | {readme_link} |\n"
        )

    lines.append("\n---\n\n")
    lines.append("_Run `python log_progress.py` to add a new entry._\n")

    with open(root_readme, "w", encoding="utf-8") as f:
        f.writelines(lines)

# ─────────────────────────────────────────────
#  STEP 1: Show the domain menu
# ─────────────────────────────────────────────
print("\n" + "═" * 58)
print("   📓  Multi-Domain Daily Learning Logger")
print("═" * 58)
print("\n  Select a domain to log your progress:\n")

for key, domain in DOMAINS.items():
    print(f"  [{key}]  {domain['emoji']}  {domain['name']}")
    print(f"        └─ {domain['color']}")
    print()

while True:
    choice = input("  Enter the number of your domain: ").strip()
    if choice in DOMAINS:
        selected = DOMAINS[choice]
        print(f"\n  ✅ Domain selected: {selected['emoji']} {selected['name']}")
        break
    else:
        print(f"  ⚠️  Invalid choice. Please enter a number between 1 and {len(DOMAINS)}.")

# ─────────────────────────────────────────────
#  STEP 2: Collect topic and notes
# ─────────────────────────────────────────────
print()
topic = input(f"  📌 What specific topic or course within {selected['name']}?\n  > ").strip()
if not topic:
    print("  ❌ Topic cannot be empty. Exiting.")
    exit(1)

print()
notes = input(f"  ✏️  What did you learn or complete today?\n  > ").strip()
if not notes:
    print("  ❌ Notes cannot be empty. Exiting.")
    exit(1)

# Optional: resources or links
print()
resources = input("  🔗 Any resources / links to note? (press Enter to skip)\n  > ").strip()

# ─────────────────────────────────────────────
#  STEP 3: Build the Markdown entry
# ─────────────────────────────────────────────
today        = datetime.now()
date_str     = today.strftime("%B %d, %Y")
weekday_str  = today.strftime("%A")
timestamp    = today.strftime("%Y-%m-%d %H:%M")

resource_line = (
    f"\n**🔗 Resources:**\n\n{resources}\n"
    if resources else ""
)

entry = f"""
---

### {selected['emoji']} {date_str} ({weekday_str})

| Field         | Details                          |
|---------------|----------------------------------|
| **Domain**    | {selected['name']}               |
| **Topic**     | {topic}                          |
| **Logged at** | {timestamp}                      |

**📝 What I learned / completed today:**

> {notes}
{resource_line}
"""

# ─────────────────────────────────────────────
#  STEP 4: Write to the domain's README.md
# ─────────────────────────────────────────────
base_dir    = os.path.dirname(os.path.abspath(__file__))
readme_path = ensure_domain_readme(selected, base_dir)

with open(readme_path, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"\n  ✅ Entry appended → {selected['folder']}/README.md")

# Update root dashboard with domain table
update_root_dashboard(base_dir)
print("  ✅ Root README.md dashboard updated")

# ─────────────────────────────────────────────
#  STEP 5: Git — add, commit, push
# ─────────────────────────────────────────────
print("\n" + "═" * 58)
print("  🚀 Pushing to GitHub...")
print("═" * 58)

commit_msg = f"[{selected['name']}] {topic} — {date_str}"

os.chdir(base_dir)

steps = [
    ["git", "add", "."],
    ["git", "commit", "-m", commit_msg],
    ["git", "push", "-u", "origin", "main", "--force"],
]

all_ok = True
for cmd in steps:
    if not run_command(cmd):
        all_ok = False
        print(f"\n  ⚠️  Stopped at: {' '.join(cmd)}")
        print("  Fix the error above and re-run the script.")
        break

# ─────────────────────────────────────────────
#  STEP 6: Final status
# ─────────────────────────────────────────────
print("\n" + "═" * 58)
if all_ok:
    print(f"  🎉 Done! [{selected['name']}] entry is live on GitHub.")
    print(f"  🟩 Contribution square logged for today.")
else:
    print("  ⚠️  Push incomplete — see errors above.")
print("═" * 58)

print("""
  ┌──────────────────────────────────────────────────┐
  │  ⚠️  REMINDER: Green squares need matching email  │
  │                                                  │
  │  Run in terminal:  git config user.email         │
  │  Must match:       github.com → Settings → Email │
  │                                                  │
  │  Fix with:                                       │
  │  git config --global user.email "you@email.com"  │
  └──────────────────────────────────────────────────┘
""")