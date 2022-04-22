from time import sleep
import keyboard
import win32api, win32con
from random import uniform, randrange

# Dependancies to install (cmd):
# pip install keyboard
# pip install pywin32

# KEYBINDS:
Click_Button = 'r' # HOLD THIS TO AUTOCLICK
Stop_Script_Button = 'Pause' # PRESS THIS TO STOP THE AUTOCLICKER COMPLETELY

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

print(f'''Autoclicker
  ____  _   _ ___ __  __ ___ ____  
 / ___|| | | |_ _|  \/  |_ _/ ___| 
 \___ \| |_| || || |\/| || |\___ \ 
  ___) |  _  || || |  | || | ___) |
 |____/|_| |_|___|_|  |_|___|____/ 

https://github.com/Shinigamiixd

Hold {Click_Button} to autoclick
Press {Stop_Script_Button} to stop the script''')

while keyboard.is_pressed(Stop_Script_Button) == False: 
    if keyboard.is_pressed(Click_Button) == True: 
        autoclick()