#!/usr/bin/env python3
import os
import sys

BANNER = r"""
██████╗  ██████╗ ████████╗███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗         
██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║         
██████╔╝██║   ██║   ██║   ███████╗██║     ███████║██║   ██║██║   ██║██║         
██╔══██╗██║   ██║   ██║   ╚════██║██║     ██╔══██║██║   ██║██║   ██║██║         
██████╔╝╚██████╔╝   ██║   ███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗    
╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    
                                                                               
              Ethical Red Team Botnet Learning Lab – by ekoms savior
"""

MENU = """
[1] Learn DDoS Botnet
[2] Learn Crypto Miner Botnet
[3] Learn Bluetooth Mesh Botnet
[4] Learn Wormable Ransom Botnet
[5] Build & Launch Zombie Botnet 🚀
[6] View Ethical Guidelines
[7] About BotSchool
[0] Exit
"""

def main():
    while True:
        os.system("clear")
        print(BANNER)
        print(MENU)
        
        choice = input("Choose a module: ")

        if choice == "1":
            print("\nLaunching DDoS Botnet module...")
            import modules.ddos_botnet
        elif choice == "2":
            print("\nLaunching Crypto Miner Botnet module...")
            import modules.miner_botnet
        elif choice == "3":
            print("\nLaunching Bluetooth Mesh Botnet module...")
            import modules.bluetooth_mesh
        elif choice == "4":
            print("\nLaunching Wormable Ransom Botnet module...")
            import modules.wormable_ransom
        elif choice == "5":
            print("\n🧠 Launching Custom Zombie Botnet...")
            import modules.zombie_launcher
            modules.zombie_launcher.launch_zombie_network()
        elif choice == "6":
            print("\nReading Guidelines...")
            import modules.guidelines
        elif choice == "7":
            print("""
📚 About BotSchool

An open-source, ethical red team botnet lab designed for learning, building, and play.

Created by: ekoms savior 🤍

🔗 GitHub: https://github.com/ekomsSavior/botschool
📖 Medium: https://medium.com/@ekoms1/botschool-101-understanding-the-botnets-behind-the-mayhem
🛠 Scripts live in /modules — feel free to modify and reuse!

Want to contribute? Fork the repo, add a new module, and open a PR ✨
""")
            input("Press ENTER to return.")
        elif choice == "0":
            print("Goodbye fren")
            sys.exit()
        else:
            print("Invalid choice. Try again.")
            input("Press ENTER to return.")

if __name__ == "__main__":
    main()
