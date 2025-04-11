#!/usr/bin/env python3
import socket
import threading

bots = []

def handle_new_bots(server):
    while True:
        bot, addr = server.accept()
        print(f"[C2] BLE bot joined mesh from {addr}")
        bots.append(bot)

def broadcast(cmd):
    for bot in bots:
        try:
            bot.send(cmd.encode())
        except:
            bots.remove(bot)

def start_bluetooth_c2():
    HOST = '127.0.0.1'
    PORT = 6666

    print(f"[C2 📶] Starting Bluetooth Mesh C2 on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    # Accept BLE bots in a background thread
    threading.Thread(target=handle_new_bots, args=(server,), daemon=True).start()

    while True:
        cmd = input("C2 > Send mesh command (ping / sync / exit): ").strip()
        if cmd == "exit":
            print("[C2] Powering down BLE mesh...")
            break
        broadcast(cmd)

if __name__ == "__main__":
    start_bluetooth_c2()
