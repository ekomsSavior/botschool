#!/usr/bin/env python3
import socket
import threading
import random
import time

# Generate a cute fake BLE MAC address
def generate_fake_mac():
    return "FA:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(
        random.randint(0, 255), random.randint(0, 255),
        random.randint(0, 255), random.randint(0, 255),
        random.randint(0, 255)
    )

MAC = generate_fake_mac()

def connect_to_mesh():
    SERVER = '127.0.0.1'
    PORT = 6666

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))
    print(f"[BOT 📡] {MAC} connected to Bluetooth mesh...")

    def listen_for_commands():
        while True:
            try:
                cmd = sock.recv(1024).decode().strip()
                if cmd == "ping":
                    print(f"[{MAC}] Received PING → Broadcasting to nearby nodes...")
                elif cmd == "sync":
                    print(f"[{MAC}] Syncing mesh data across virtual links...")
                else:
                    print(f"[{MAC}] Unknown mesh command: {cmd}")
            except:
                print(f"[{MAC}] Disconnected from mesh.")
                break

    threading.Thread(target=listen_for_commands).start()

if __name__ == "__main__":
    connect_to_mesh()
