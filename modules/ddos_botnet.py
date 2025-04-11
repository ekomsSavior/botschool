#!/usr/bin/env python3
import os
import subprocess
import time

def show_menu():
    print("""
[💥] Welcome to the DDoS Botnet Simulation Module
    This module teaches basic C2 and zombie flood logic.

[1] View Explanation
[2] Run Local C2 Server
[3] Run Simulated Bot Client
[0] Return to BotSchool
""")

def run():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("""
[+] This simulation shows how a C2 server controls bots for a DDoS attack.
[+] The server sends commands like 'attack 127.0.0.1 8080'.
[+] Bots simulate a UDP flood locally — no real packets are sent.
[+] This is a safe, visual way to understand DDoS logic 💥
""")
            input("Press ENTER to return.")
        elif choice == "2":
            print("[+] Launching DDoS C2 in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/ddos/ddos_c2.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "3":
            print("[+] Launching DDoS Bot in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/ddos/ddos_bot.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

run()
