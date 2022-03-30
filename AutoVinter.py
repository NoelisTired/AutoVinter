import pyautogui
import os
import keyboard
import time
from pystyle import Colors, Colorate, Add, Center, Box, Write

def header():
    os.system('cls')
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[Welcome] to the NoelP X Autofisher made for LongVinter"), 1))
    print(" ")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[INFO] Please enter LongVinter, Fishing rod equipped. and press F6 on the spot of the fish"), 1))
    print(" ")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[CRITICAL] If you wish to halt the script, Please hold F5"), 1))

def autofish():
    global running
    running = True
    if keyboard.is_pressed('F6'):
        pos = pyautogui.position()
        while running:
            header()
            pyautogui.moveTo(pos)
            if keyboard.is_pressed('F5'):
                print('You stopped the script!')
                input("Press ENTER to resume")
                time.sleep(3)
            else:
                print(pyautogui.click())
                pyautogui.press('e')
    else:
        pass

if __name__ == "__main__":
    header()
    while True:
        autofish()