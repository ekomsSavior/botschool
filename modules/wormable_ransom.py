#!/usr/bin/env python3
import os
import subprocess
import time

def show_menu():
    print("""
[🧟♀] Welcome to the Wormable Ransom Botnet Simulation
    Simulates a worm that spreads and 'encrypts' fake files.

[1] View Explanation
[2] Run Worm C2 Controller
[3] Launch Worm Bot
[0] Return to BotSchool
""")

def run():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("""
[+] This simulation demonstrates a worm-like botnet behavior.
[+] A central C2 server sends commands to connected bots.
[+] Bots can simulate spreading to fake LAN IPs and encrypting fake files.
[+] A cute ransom note is dropped for realism — totally harmless and local.
""")
            input("Press ENTER to return.")
        elif choice == "2":
            print("[+] Launching Worm C2 in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/worm/worm_c2.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "3":
            print("[+] Launching Worm Bot in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/worm/worm_bot.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

run()
