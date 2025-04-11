# 🧠 BotSchool v1.0 – Rise of the Swarm  
*An open-source ethical red team botnet learning lab – by ekoms savior 🫂*

---

## 🚀 What is BotSchool?

**BotSchool** is a modular red team simulation lab that lets users explore how botnets are created, controlled, and stopped — all in a safe and fully educational virtual environment.

Perfect for:
- 🧠 Ethical hackers
- 🧃 Cybersecurity students
- 🐣 Total beginners who want to learn red team tactics the right way

---

## 📦 What's Inside?

BotSchool includes **6 modular learning labs**:

| Module | What It Teaches |
|--------|------------------|
| [1] DDoS Botnet | Simulates a simple C2-to-bot UDP flood |
| [2] Crypto Miner Botnet | Simulates mining bots & fake earnings |
| [3] Bluetooth Mesh Botnet | Simulates BLE relay-style zombie logic |
| [4] Wormable Ransom Botnet | Simulates self-spreading encryption & ransom drops |
| [5] Zombie Army Builder | Clone, customize, and launch a swarm of bots |
| [6] Guidelines & About | Ethical use rules + credits 💖 |

---

## 🖥 How to Use It

### 🔧 Step 1: Clone the repo


git clone https://github.com/ekomsSavior/botschool.git
cd botschool

📦 Step 2: Install xterm for terminal simulation


sudo apt update && sudo apt install xterm

▶️ Step 3: Launch BotSchool


python3 botschool.py


Choose any module and follow the in-app prompts.

🔍 What's Happening Behind the Scenes?
🤖 What Is a C2 Server?

A C2 (Command & Control) server is the brain of a botnet. It tells bots what to do: attack, mine, scan, spread, etc.

In BotSchool, each C2:

    Is written in Python

    Uses socket to listen for connections

    Sends simple text-based commands to bots

🧟‍♀️ What Is a Bot?

A bot:

    Connects back to the C2

    Waits for commands like attack 127.0.0.1 8080

    Simulates actions (e.g., floods, mining, BLE pings, fake encryption)

All actions are harmless and occur only on your machine.
🧠 How Do Devices Get Infected in Real Life?

In real-world botnets:

    Malware spreads via phishing, exploits, open ports, etc.

    Devices are silently infected and added to a C2

    C2s may control millions of bots (a “botnet”) for attacks or profit

BotSchool replicates these concepts safely and visually.
📜 Disclaimer

    BotSchool is for educational and ethical red team training only.

    ❌ Do not deploy or modify these tools for use outside your own machines.

    ❌ Do not attack, scan, or connect to anything you do not own or have explicit permission for.

    ✅ Learn how these systems work so you can detect, prevent, and defend.

Use this knowledge responsibly. You're the future of cybersecurity. 🫂
✨ By ekoms savior 🤍

Made with love for Team Forever.
Instagram: @ekomsSavior
GitHub: ekomsSavior
Medium: ekomsSavior

