import sys
import os
import time
import pyautogui
import keyboard

class MPS_488X():
    def __init__(self):
        pass
    def test(self):
        print("######")
        return 'TEST'
    def Normal_Mode_Update(self):
        pyautogui.size()
        width, height = pyautogui.size()
        # login
        pyautogui.moveTo(1450, 300, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(1650, 110, duration=0.25)
        pyautogui.click()

        # Browse
        pyautogui.moveTo(1300, 350, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(1300, 145, duration=0.25)
        pyautogui.click()
        # open
        pyautogui.moveTo(1750, 563, duration=0.25)
        pyautogui.click()
        #

        pyautogui.moveTo(1400, 395, duration=0.25)
        pyautogui.click()

        # Yes
        pyautogui.moveTo(1300, 655, duration=0.25)
        pyautogui.click()

    def Recovery_Mode_Update(self):
        pyautogui.size()
        width, height = pyautogui.size()
        pyautogui.moveTo(1450, 300, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(1650, 110, duration=0.25)
        pyautogui.click()
        # Browse
        pyautogui.moveTo(1300, 550, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(1300, 145, duration=0.25)
        pyautogui.click()
        # open
        pyautogui.moveTo(1750, 563, duration=0.25)
        pyautogui.click()
        #
        pyautogui.moveTo(1300, 600, duration=0.25)
        pyautogui.click()

        # Yes
        pyautogui.moveTo(1300, 655, duration=0.25)
        pyautogui.click()

    def Mac_Update(self):
        os.startfile(r"C:\Dell\MAC\MPS-488X.lnk")

        time.sleep(2)
        pyautogui.typewrite("\n")
        pyautogui.typewrite("FIV?\n")
        #time.sleep(10)
        pyautogui.press("enter")
        pyautogui.typewrite("TEST MPSTryToGuess42\n")
        pyautogui.press("enter")
        pyautogui.typewrite("OTP M\n")
        pyautogui.press("enter")
        pyautogui.typewrite("OTP S\n")
        pyautogui.press("enter")

        pyautogui.typewrite("SER ")
        keyboard.wait("enter")
        pyautogui.typewrite("\n")
        pyautogui.typewrite("\n")
        pyautogui.typewrite("SER\n")
        pyautogui.press("enter")
        pyautogui.typewrite("MAC ")
        keyboard.wait("enter")
        pyautogui.typewrite("\n")
        pyautogui.typewrite("\n")
        pyautogui.typewrite("MAC\n")
        keyboard.wait("enter")
        pyautogui.typewrite("OTP O\n")
        keyboard.wait("enter")
        pyautogui.typewrite("RESET_FACTORY\n")
        pyautogui.press("enter")
        pyautogui.typewrite("exit()\n")

    def Mac_Check(self):
        os.startfile(r"C:\Dell\MAC\MPS-488X.lnk")
        time.sleep(2)
        pyautogui.typewrite("\n")
        pyautogui.typewrite("FIV?\n")
        pyautogui.press("enter")

        pyautogui.typewrite("TEST MPSTryToGuess42\n")
        pyautogui.press("enter")

        pyautogui.typewrite("OTP M\n")
        pyautogui.press("enter")

        pyautogui.typewrite("OTP S\n")
        keyboard.wait("enter")

        pyautogui.typewrite("exit()\n")
   
def run_menu(menu, parent=None):
    while True:
        print_menu(menu)

        #if parent:
        #    print("99. go back to parent")
        getin = input("Plase enter you  choice: ")

        #if parent and getin =='99':
        #    return

        if not getin.isnumeric() or  int(getin) >= len(menu['options']):
            print()
            print("Invalid choice, please try again.")
            print()
            continue
            
        menu['options'][int(getin)]['command']()


def print_menu(menu):
    print(menu['title'])
    for i, option in enumerate(menu['options']):
        #print(i, option['text'])
        print(f"{i}. {option['text']}")
    print()
mps_488X = MPS_488X()
#print("test", mps_488X.test())
COMMAND = 'command'
main_menu = {
    'title':  'Main Menu',
    'options': [
        {'type': COMMAND, 'text': ' Update Device Normal Mode Fireware', 'command': mps_488X.Normal_Mode_Update },
        {'type': COMMAND, 'text': ' Update Device Recovery Mode Fireware', 'command': mps_488X.Recovery_Mode_Update},
        {'type': COMMAND, 'text': ' Change Mac Sddress and Serial Number', 'command': mps_488X.Mac_Update},
        {'type': COMMAND, 'text': ' Change Mac Sddress and Serial Number', 'command': mps_488X.Mac_Check},
        #{'type': COMMAND, 'text': ' EXIT', 'command': mps_488X.test},
        ]
    }
run_menu(main_menu)
