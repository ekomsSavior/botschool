#!/usr/bin/env python3
import socket
import time
import random
import threading

FAKE_WALLET = "4abcFAKEwALLETxXxFakeMinerYz1123"

def connect_to_c2():
    SERVER = '127.0.0.1'
    PORT = 7777

    print(f"[BOT ⛏️] Connecting to Miner C2 at {SERVER}:{PORT}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))
    print("[BOT] Connected. Awaiting mining commands...")

    def listen():
        while True:
            try:
                cmd = sock.recv(1024).decode().strip()
                if cmd == "mine":
                    print("[BOT] Starting mining loop...")
                    mine_loop()
                elif cmd == "stop":
                    print("[BOT] Mining stopped.")
                    break
            except:
                break

    threading.Thread(target=listen).start()

def mine_loop():
    for i in range(10):  # Simulate mining 10 "blocks"
        time.sleep(random.uniform(0.5, 1.5))
        fake_earnings = round(random.uniform(0.001, 0.01), 5)
        print(f"[BOT ⛏️] Mined {fake_earnings} XMR → Sent to wallet {FAKE_WALLET}")
    print("[BOT] Mining complete.")

if __name__ == "__main__":
    connect_to_c2()
