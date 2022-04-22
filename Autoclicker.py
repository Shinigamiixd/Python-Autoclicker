import subprocess
from time import sleep

# THIS IS A FIRST TIME DEPENDANCIES INSTALLATION

keyboard_check = subprocess.run(["pip", "show", "--quiet", "keyboard"])
pywin_check = subprocess.run(["pip", "show", "--quiet", "pywin32"])

if keyboard_check.returncode or pywin_check.returncode != 0:
    subprocess.call("cls", shell=True)
    print("Dependancies not found, installing in 3 seconds")
    sleep(3)
    subprocess.call("cls", shell=True)
    print("Installing keyboard dependancy")
    subprocess.run(["pip", "install", "keyboard"])
    print("Installing pywin32 dependancy")
    subprocess.run(["pip", "install", "pywin32"])
    subprocess.call("cls", shell=True)
    print("Please restart the program")
    sleep(30)
    exit()

import keyboard
import win32api, win32con
from random import uniform, randrange

# KEYBINDS:
Click_Button = "r" # HOLD THIS TO AUTOCLICK
Stop_Script_Button = "Pause" # PRESS THIS TO STOP THE AUTOCLICKER COMPLETELY

def autoclick():
    while keyboard.is_pressed(Click_Button) == True:

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

        if randrange(15) == 0:
            sleep(0.175)
            continue

        randomclicks = uniform(0.025, 0.095)
        sleep(randomclicks)

print(f"""Autoclicker
  ____  _   _ ___ __  __ ___ ____  
 / ___|| | | |_ _|  \/  |_ _/ ___| 
 \___ \| |_| || || |\/| || |\___ \ 
  ___) |  _  || || |  | || | ___) |
 |____/|_| |_|___|_|  |_|___|____/ 

https://github.com/Shinigamiixd

Hold {Click_Button} to autoclick
Press {Stop_Script_Button} to stop the script""")

while keyboard.is_pressed(Stop_Script_Button) == False: 
    if keyboard.is_pressed(Click_Button) == True: 
        autoclick()
