import sys
import os
import time
import pyautogui
import keyboard

#os.system("telnet 192.168.0.120 2501")
#pyautogui.typewrite("FIV")
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

#print("test")
#pyautogui.position()

keyboard.wait("enter")
#pyautogui.typewrite("exit()\n")



