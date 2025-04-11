#!/usr/bin/env python3
import os
import subprocess
import time

def show_menu():
    print("""
[📶] Welcome to the Bluetooth Mesh Botnet Simulation Module
    This simulates a BLE-based mesh botnet with local relay logic.

[1] View Explanation
[2] Run Bluetooth Mesh C2
[3] Run Simulated BLE Bot
[0] Return to BotSchool
""")

def run():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("""
[+] This module demonstrates a simulated BLE-based mesh botnet.
[+] The C2 server sends "mesh" commands like ping or sync.
[+] Bots simulate BLE relay logic and print fake MAC addresses.
[+] A perfect intro to decentralized botnets — no real BLE is used.
""")
            input("Press ENTER to return.")
        elif choice == "2":
            print("[+] Launching Bluetooth Mesh C2 in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/bluetooth/bluetooth_c2.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "3":
            print("[+] Launching BLE Bot in new terminal...")
            try:
                subprocess.Popen(["xterm", "-hold", "-e", "python3", "modules/bluetooth/bluetooth_bot.py"])
            except FileNotFoundError:
                print("❌ xterm not found. Install it with: sudo apt install xterm")
            input("Press ENTER to return.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

run()
