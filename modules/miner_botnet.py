#!/usr/bin/env python3
import os
import subprocess
import time

def show_menu():
    print("""
[🪙] Welcome to the Crypto Miner Botnet Simulation
    Simulates a botnet mining fake cryptocurrency for a fake wallet.

[1] View Explanation
[2] Run Mining C2 Controller
[3] Launch Miner Bot
[0] Return to BotSchool
""")

def run():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("""
[+] This simulation shows how botnets hijack compute power for profit.
[+] The C2 controller sends start/stop commands to bot clients.
[+] Miner bots simulate mining and show fake crypto earnings.
[+] Nothing real is mined. It's all educational + cute output 💖
""")
            input("Press ENTER to return.")
        elif choice == "2":
            print("[+] Launching Miner C2 in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/miner/miner_c2.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "3":
            print("[+] Launching Miner Bot in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/miner/miner_bot.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

run()
