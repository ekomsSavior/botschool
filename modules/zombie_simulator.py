#!/usr/bin/env python3
import time
import random

ZOMBIE_NAMES = [
    "infected-host-01", "camera-dvr-666", "fridge-botnet", "windows-xp-zombie",
    "android-victim", "iot-toaster", "printer-from-hell", "game-console", "pos-system"
]

ROLES = {
    "1": "DDoS Attacker",
    "2": "Miner",
    "3": "BLE Relay",
    "4": "Worm Spreader"
}

def simulate_zombies():
    print("\n🧟♂ Simulating zombie client replication...")
    zombies = []

    for _ in range(10):
        name = random.choice(ZOMBIE_NAMES) + "-" + str(random.randint(1000, 9999))
        zombies.append({"name": name, "role": None})
        print(f"[+] New zombie cloned: {name}")
        time.sleep(0.3)

    return zombies

def assign_roles(zombies):
    print("\n🧠 Choose zombies to activate (comma-separated numbers):")
    for idx, zombie in enumerate(zombies):
        print(f"[{idx+1}] {zombie['name']}")

    selected = input("\nSelect zombies: ").strip().split(",")
    selected = [int(s)-1 for s in selected if s.strip().isdigit() and 0 < int(s) <= len(zombies)]

    for idx in selected:
        print(f"\n🧃 Assign role for {zombies[idx]['name']}:")
        print("[1] DDoS Attacker")
        print("[2] Miner")
        print("[3] BLE Relay")
        print("[4] Worm Spreader")
        role = input("Choose role: ").strip()
        zombies[idx]['role'] = ROLES.get(role, "Unassigned")

    return [z for z in zombies if z['role']]

def display_army(zombies):
    print("\n💀 Custom Zombie Army Assembled:")
    for z in zombies:
        print(f" - {z['name']} → {z['role']}")
    print(f"\n🧟‍♀️ Total active zombies: {len(zombies)}")

def run_zombie_builder():
    zombies = simulate_zombies()
    custom_army = assign_roles(zombies)
    display_army(custom_army)
    return custom_army  # ✅ return it

if __name__ == "__main__":
    army = run_zombie_builder()
