# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:35:25 2021
@author: GO-MCF
"""

import hashlib
import os
import sys

os.system('cls')
os.system('color 4')
os.system('cls')

RED   = "\033[31m"  
GREEN = "\033[92m"
YELLOW = "\033[33m"
RESET = "\033[0m"

print(GREEN)
print("                _ _____                     ")
print("               | | ____|                    ")
print("  _ __ ___   __| | |__  ___ _   _ _ __ ___  ")
print(" | '_ ` _ \ / _` |___ \/ __| | | | '_ ` _ \ ")
print(" | | | | | | (_| |___) \__ \ |_| | | | | | |")
print(" |_| |_| |_|\__,_|____/|___/\__,_|_| |_| |_|")
print("")
print("Version 1.0 - 2021-11-19 - GO-MCF")
print(RESET)

def md5Sum(filename):
 print(GREEN+"md5sum for file {} : ".format(filename),YELLOW,hashlib.md5(open(filename,'rb').read()).hexdigest(),RESET)

def main(argv):
    md5Sum(sys.argv[1])
    
if __name__ == "__main__":
    if not sys.argv[1:]:
        print(RED+"No input file"+RESET)
        sys.exit(0)
    main(sys.argv[1:])