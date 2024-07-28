import sys
import os
import time
import pyautogui
import keyboard

LoginLoS = [None, None]
#print("LoginLoS[0] ", LoginLoS[0], LoginLoS[1])
def locateOnScreen(ImgName):
    los = pyautogui.locateOnScreen(ImgName)
    if los:
        return los
    else:
        pyautogui.locateOnScreen(ImgName)
        


def centeredCoords(_coords):
    return _coords[0] + int(_coords[2]/2), _coords[1] + int(_coords[3]/2)

def findCenterOnScreen(ImgName):
    try:
      found = pyautogui.locateOnScreen(ImgName, grayscale=True, confidence=0.5)
      if found:
        cx, cy = centeredCoords(found)
        return cx, cy
      else:
        return None, None
    except TypeError:
        print( 'TypeError')

    
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
        #LoginLoS = locateOnScreen('./img/login.png')
        if LoginLoS[0] == None or LoginLoS[1] == None:
          LoginLoS[0], LoginLoS[1] = findCenterOnScreen('./img/login.png')
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
        else:
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
        
        pyautogui.click()

        #time.sleep(2)
        cx, cy = findCenterOnScreen('./img/Advanced-settings.png')
        #print(cx, cy)
        pyautogui.moveTo(cx, cy, duration=0.25)
        pyautogui.click()

        # Browse
        time.sleep(1)
        cx, cy = findCenterOnScreen('./img/UpdateNormalModeImage.png')
        print(cx, cy)
        #pyautogui.moveTo(cx-82, cy-49, duration=0.25)
        pyautogui.moveTo(1300, 350, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(1300, 145, duration=0.25)
        #pyautogui.moveTo(cx-82, cy-249, duration=0.25)
        pyautogui.click()
        # open
        pyautogui.moveTo(1750, 563, duration=0.25)
        pyautogui.click()
        #
        
        # Yes
        pyautogui.moveTo(1400, 395, duration=0.25)
        pyautogui.click()

        # 
        pyautogui.moveTo(1300, 655, duration=0.25)
        #pyautogui.moveTo(cx-82, cy-49, duration=0.25)
        pyautogui.click()

    def Recovery_Mode_Update(self):
        pyautogui.size()
        width, height = pyautogui.size()
        # login
        if LoginLoS[0] == None or LoginLoS[1] == None:
          LoginLoS[0], LoginLoS[1] = findCenterOnScreen('./img/login.png')
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
          print("if")
        else:
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
          print("else")
        pyautogui.click()

        time.sleep(1.8)
        # Advanced-settings
        AdvancedsettingsLoS = locateOnScreen('./img/Advanced-settings.png')
        pyautogui.moveTo(AdvancedsettingsLoS[0]+AdvancedsettingsLoS[2]/2, AdvancedsettingsLoS[1]+AdvancedsettingsLoS[3]/2, duration=0.25)
        #pyautogui.moveTo(1650, 110, duration=0.25)
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
   