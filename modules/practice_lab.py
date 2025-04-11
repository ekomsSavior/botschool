#!/usr/bin/env python3
import os
import time
import subprocess

def launch_in_terminal(script_path):
    terminals = [
        ["xfce4-terminal", "--hold", "--command", f"python3 {script_path}"],
        ["gnome-terminal", "--", "bash", "-c", f"python3 {script_path}; exec bash"],
        ["xterm", "-hold", "-e", "python3", script_path]
    ]

    for term_cmd in terminals:
        try:
            subprocess.Popen(term_cmd)
            return
        except FileNotFoundError:
            continue

    # If no terminals found
    print(f"\n[!] Could not find a compatible terminal to launch {script_path}")
    print("[?] Would you like to install xterm now to enable auto-launch?")
    user_input = input("Type 'y' to install xterm, or press ENTER to skip: ").strip().lower()

    if user_input == "y":
        print("[+] Installing xterm...")
        os.system("sudo apt update && sudo apt install -y xterm")
        print("[+] Installed! Please try launching the lab again 💖")
    else:
        print(f"\n📝 To launch manually, open a new terminal and run:\n$ python3 {script_path}\n")

def launch_practice_lab():
    os.system("clear")
    print("""
🧪 Welcome to the Practice C2 Lab
Build your own mini botnet lab by selecting the modules to include!
""")

    print("[1] Include DDoS Botnet")
    print("[2] Include Wormable Ransom Botnet")
    print("[3] Include ALL (DDoS + Worm)")
    print("[0] Return to BotSchool")
    choice = input("Choose an option: ")

    if choice == "1":
        print("\n[+] Launching DDoS C2 and Bot in new terminals...")
        time.sleep(1)
        launch_in_terminal("modules/ddos/ddos_c2.py")
        time.sleep(1)
        launch_in_terminal("modules/ddos/ddos_bot.py")
    elif choice == "2":
        print("\n[+] Launching Worm C2 and Bot in new terminals...")
        time.sleep(1)
        launch_in_terminal("modules/worm/worm_c2.py")
        time.sleep(1)
        launch_in_terminal("modules/worm/worm_bot.py")
    elif choice == "3":
        print("\n[+] Launching full DDoS + Worm lab...")
        time.sleep(1)
        launch_in_terminal("modules/ddos/ddos_c2.py")
        time.sleep(1)  # Add delay
        launch_in_terminal("modules/ddos/ddos_bot.py")
        time.sleep(1)
        launch_in_terminal("modules/worm/worm_c2.py")
        time.sleep(1)
        launch_in_terminal("modules/worm/worm_bot.py")
    elif choice == "0":
        return
    else:
        print("Invalid choice.")
        time.sleep(1)
        launch_practice_lab()

launch_practice_lab()
