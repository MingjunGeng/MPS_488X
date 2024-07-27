import sys
import os
import time
import pyautogui
import keyboard

#os.system("telnet 192.168.0.120 2501")
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
keyboard.wait("enter")
pyautogui.typewrite("exit()\n")
