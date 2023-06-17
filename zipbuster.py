#!/usr/bin/env python3
# Author - cyberxaman

import os
import sys
import zipfile

# clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Check if py7zr module is installed, if not, install it
try:
    import py7zr
except ImportError:
    print("Installing requirements")
    os.system('pip3 install py7zr')

# Check if tqdm module is installed, if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("Installing requirements")
    os.system('pip3 install tqdm')

# clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print("""\033[1;96m

  _______       ____            _            
 |___  (_)     |  _ \          | |           
    / / _ _ __ | |_) |_   _ ___| |_ ___ _ __ 
   / / | | '_ \|  _ <| | | / __| __/ _ \ '__|
  / /__| | |_) | |_) | |_| \__ \ ||  __/ |   
 /_____|_| .__/|____/ \__,_|___/\__\___|_|   
         | |                                 
         |_|                                 

------------created by cyberxaman------------
 \033[0;0m""")

zip_file = input("Enter the full path of the zip or 7zip file: ")
dictionary_file = input("Enter the full path of the custom wordlist (press Enter for default: wordlist.txt): ")

if dictionary_file == "":
    dictionary_file = "wordlist.txt"

with open(dictionary_file, 'r') as f:
    passwords = f.readlines()

try:
    for password in tqdm(passwords, desc="Cracking password"):
        password = password.strip('\n')
        try:
            with zipfile.ZipFile(zip_file) as zf:
                zf.extractall(pwd=password.encode())
                print(f" Password found: {password}")
                break
        except Exception:
            try:
                with py7zr.SevenZipFile(zip_file, mode='r', password=password) as szf:
                    szf.extractall()
                    print(f"Password found: {password}")
                    break
            except Exception:
                pass
except KeyboardInterrupt:
    print("\nGoodbye! 👋")

print("Happy Hacking! 😃")
