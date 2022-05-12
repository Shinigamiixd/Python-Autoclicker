import subprocess
from time import sleep
from random import uniform, randrange
try:
    import win32api, win32con
    import keyboard
except ImportError:
    print("Certain dependancies not found, installing in 3 seconds")
    sleep(3)
    subprocess.run(["pip", "install", "pywin32"])
    subprocess.run(["pip", "install", "keyboard"])
    print("Please restart the script! Closing in 30 seconds...")
    sleep(30)
    exit()

    
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

subprocess.call("cls", shell=True)
print(f"""Autoclicker
  ____  _   _ ___ __  __ ___ ____  
 / ___|| | | |_ _|  \/  |_ _/ ___| 
 \___ \| |_| || || |\/| || |\___ \ 
  ___) |  _  || || |  | || | ___) |
 |____/|_| |_|___|_|  |_|___|____/ 

https://github.com/Shinigamiixd

Hold "{Click_Button}" to autoclick
Press "{Stop_Script_Button}" to stop the script""")

while keyboard.is_pressed(Stop_Script_Button) == False: 
    if keyboard.is_pressed(Click_Button) == True: 
        autoclick()
