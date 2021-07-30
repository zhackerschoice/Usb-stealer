import os
from art import *
from colorama import *



os.system("cls")
p = text2art("Usb Telegram stealer", font="speed")
print(Fore.LIGHTGREEN_EX + p)

tprint("Read the txt file carefully!!!")

os.system("notepad Readme.txt")

i = input(Fore.LIGHTGREEN_EX + "Generate the exe file y/n :")

if i == 'y' :
    dir = os.getcwd()
    os.system("rmdir /s /q output")
    os.system("pyinstaller --clean --hidden-import=shutil --hidden-import=os --noconfirm --onefile --windowed Telegrams.py") 
    os.system("del /s /q /f Telegram.spec")
    os.system("rmdir /s /q __pycache__")
    os.system("rmdir /s /q build")
    os.system("ren dist output")
    os.system("cls")
    print(Fore.LIGHTGREEN_EX + p)
    i2 = input(Fore.LIGHTGREEN_EX + "Open the output folder y/n : ")
    if i2 == 'y' :
        os.system("explorer " + dir + "\output")
           
elif i == 'n' :
    print("Good bye !!")
