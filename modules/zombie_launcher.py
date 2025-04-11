#!/usr/bin/env python3
import modules.zombie_simulator as zb
import subprocess
import time

ROLE_TO_MODULE = {
    "DDoS Attacker": ("modules/ddos/ddos_c2.py", "modules/ddos/ddos_bot.py"),
    "Miner": ("modules/miner/miner_c2.py", "modules/miner/miner_bot.py"),
    "BLE Relay": ("modules/bluetooth/bluetooth_c2.py", "modules/bluetooth/bluetooth_bot.py"),
    "Worm Spreader": ("modules/worm/worm_c2.py", "modules/worm/worm_bot.py"),
}

def launch_with_xterm(script_path):
    subprocess.Popen(["xterm", "-hold", "-e", "python3", script_path])

def launch_zombie_network():
    army = zb.run_zombie_builder()

    if not army:
        print("⚠️ No zombies were activated.")
        return

    launched_c2s = set()

    for zombie in army:
        role = zombie["role"]
        if role in ROLE_TO_MODULE:
            c2, bot = ROLE_TO_MODULE[role]

            # Only launch the C2 for each role once
            if role not in launched_c2s:
                print(f"[+] Launching C2 for role: {role}")
                launch_with_xterm(c2)
                time.sleep(1)
                launched_c2s.add(role)

            print(f"[+] Launching bot for: {zombie['name']} → {role}")
            launch_with_xterm(bot)
            time.sleep(0.5)

    print("\n✅ All bots launched! Your zombie army is operational.")
    input("Press ENTER to return to BotSchool.")
