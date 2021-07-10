import os
from art import *
from colorama import *
import time

os.system("cls")

p = text2art("Usb Stealer", font="Epic")
print(Fore.LIGHTGREEN_EX + p)

print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "1. Telegram Data stealer")
print(Fore.LIGHTGREEN_EX + "2. Browser Data stealer")
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
time.sleep(0.1)
print(Fore.LIGHTGREEN_EX + "------")
inp = input(Fore.LIGHTGREEN_EX + 'Choose :')
if inp == "1" :
    os.chdir("Usb")
    os.chdir("Tele")
    os.system("python tele.py")
elif inp == "2" :
    os.chdir("Usb")
    os.chdir("Browser")
    os.system("python browser.py")
else :
    print(Fore.RED + "Please enter a valid option!")
    os.system("color 7")

