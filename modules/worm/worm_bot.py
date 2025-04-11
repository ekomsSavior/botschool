#!/usr/bin/env python3
import socket
import threading
import random
import time
import os

# Simulated list of IPs to "infect"
NEARBY_DEVICES = [
    "192.168.0.10", "192.168.0.11", "192.168.0.12",
    "192.168.0.13", "192.168.0.14"
]

FAKE_FILES = ["family_photos.txt", "passwords.doc", "notes.md", "finance.csv"]
RANSOM_NOTE = """
🔒 Your files have been encrypted by WormBot!
To decrypt, send 100 XMR to: FAKE-RANSOM-WALLET-666
Team Forever still loves you. 💖
"""

def connect_to_c2():
    SERVER = '127.0.0.1'
    PORT = 4444

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))
    print("[WORMBOT] Connected to Worm C2.")

    def listen():
        while True:
            try:
                cmd = sock.recv(1024).decode().strip()
                if cmd == "encrypt":
                    print("[WORMBOT] Executing encryption payload...")
                    encrypt_files()
                elif cmd == "kill":
                    print("[WORMBOT] Self-destruct initiated.")
                    time.sleep(1)
                    os._exit(0)
            except:
                break

    threading.Thread(target=listen).start()
    spread_to_nearby()

def encrypt_files():
    for file in FAKE_FILES:
        print(f"🔐 Encrypting {file}...")
        time.sleep(0.5)
    print("📝 Dropping ransom note...\n")
    print(RANSOM_NOTE)

def spread_to_nearby():
    print("[WORMBOT] Scanning LAN for vulnerable hosts...")
    for ip in NEARBY_DEVICES:
        print(f"[WORMBOT] Infecting {ip}... [simulated]")
        time.sleep(0.3)
    print("[WORMBOT] Worm spread complete.")

if __name__ == "__main__":
    connect_to_c2()
