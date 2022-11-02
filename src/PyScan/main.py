import socket
import threading
import time
import os
import platform
from colorama import Fore

pm = platform.system()
if pm == "Windows":
    os.system("cls")
elif pm == "Linux":
    os.system("clear")
elif pm == "Darwin":
    os.system("clear")
banner = Fore.RED + f"""
                      ______          _   _____                            
                      | ___ \        | | /  ___|                                
                      | |_/ /__  _ __| |_\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
                      |  __/ _ \| '__| __|`--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
                      | | | (_) | |  | |_/\__/ / (_| (_| | | | | | | |  __/ |   
                      \_|  \___/|_|   \__\____/ \___\__,_|_| |_|_| |_|\___|_| 

                                Github : https://github.com/TanevAZ
"""

print(banner)

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f"{Fore.RESET}Port {Fore.LIGHTMAGENTA_EX}{port}{Fore.RESET} is {Fore.LIGHTGREEN_EX}open{Fore.RESET} on {ip}")
        s.close()
    except:
        print(f"{Fore.RESET}Port {Fore.LIGHTMAGENTA_EX}{port}{Fore.RESET} is {Fore.LIGHTRED_EX}closed{Fore.RESET} on {ip}")

def main():
    ip = input(f"{Fore.WHITE}Enter IP Address : {Fore.BLUE}")
    for port in [21, 22, 23, 25, 80, 8080, 110, 143, 443, 445, 3389, 1433, 3306, 3389, 5900, 19132, 19133, 27015, 30110, 30120]: # add more port if you want
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()
        time.sleep(0.1) # to prevent error but you can delete this line
        if port == 30120:
            t.join()
            input(f"\n{Fore.LIGHTGREEN_EX}Scan Terminated. {Fore.WHITE}Press Enter to Exit...")
            exit()

main()