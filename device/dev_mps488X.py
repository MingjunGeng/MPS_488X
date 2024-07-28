import pyautogui
import keyboard
import sys
import os

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
    def exit(self):
        sys.exit(1)
   