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

file = open("ports.txt", "w")
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f"{Fore.RESET}Port {Fore.LIGHTMAGENTA_EX}{port}{Fore.RESET} is {Fore.LIGHTGREEN_EX}open{Fore.RESET} on {ip}")
        file.write(f"{port} is open on {ip}\n")
        s.close()
    except:
        print(f"{Fore.RESET}Port {Fore.LIGHTMAGENTA_EX}{port}{Fore.RESET} is {Fore.LIGHTRED_EX}closed{Fore.RESET} on {ip}")

def main():
    ip = input(f"{Fore.WHITE}Enter IP Address (1-65535): {Fore.BLUE}")
    port_range = input(f"{Fore.WHITE}Enter Port Range : {Fore.LIGHTMAGENTA_EX}")
    port_range = port_range.split("-")
    port_range = list(range(int(port_range[0]), int(port_range[1]) + 1))
    for port in port_range:
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()
        time.sleep(0.1)
        if port == port_range[-1]:
            t.join()
            input(f"\n{Fore.LIGHTGREEN_EX}Scan Terminated. {Fore.WHITE}Press Enter to Exit...")
            exit()

main()
file.close()
