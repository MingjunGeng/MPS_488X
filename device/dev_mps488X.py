import sys
import os
import time
import pyautogui
import keyboard
from PIL import ImageGrab, Image
import cv2
import pyscreeze

def findCenter():
    screenScale = 1
    target = cv2.imread('./img/login.png', cv2.IMREAD_GRAYSCALE)
    screenshot = pyscreeze.screenshot('my_screenshot.png')
    temp = cv2.imread('my_screenshot.png', cv2.IMREAD_GRAYSCALE)
    theight, tweigth = target.shape[:2]
    tempheight, tempweigth = temp.shape[:2]
    scaleTemp = cv2.resize(temp, (int(tempweigth/screenScale), int(tempheight/screenScale)) )
    stempheight, stempweigth = scaleTemp.shape[:2]
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 
    if(max_val>=0.9):
        top_left = max_loc
        bottom_right = (top_left[0] + tweigth, top_left[1] + theight)
        tagHalfW = int(tweigth/2)
        tagHalfH = int(theight/2)
        tagCenterX = top_left[0] + tagHalfW
        tagCenterY = top_left[1] + tagHalfH
    else:
        print('no found')
    os.remove('my_screenshot.png')
    return tagCenterX, tagCenterY
    
LoginLoS = [None, None]
AdvancedsettingsLoS = [None, None]
Browse = [None, None]
#print("LoginLoS[0] ", LoginLoS[0], LoginLoS[1])
#print("AdvancedsettingsLoS[0] ", AdvancedsettingsLoS[0], AdvancedsettingsLoS[1])
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
        x, y = findCenter()
        print(x, y)
        if LoginLoS[0] == None or LoginLoS[1] == None:
          LoginLoS[0], LoginLoS[1] = findCenterOnScreen('./img/login.png')
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
        else:
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
        #pyautogui.moveTo(1450, 300, duration=0.25)
        pyautogui.click()

        #time.sleep(2)

        # Advanced-settings
        if AdvancedsettingsLoS[0] == None or AdvancedsettingsLoS[1] == None:
          AdvancedsettingsLoS[0], AdvancedsettingsLoS[1] = findCenterOnScreen('./img/Advanced-settings.png')
          #print("AdvancedsettingsLoS[0] ", AdvancedsettingsLoS[0], AdvancedsettingsLoS[1])
          pyautogui.moveTo(AdvancedsettingsLoS[0], AdvancedsettingsLoS[1], duration=0.25)
        else:
          pyautogui.moveTo(AdvancedsettingsLoS[0], AdvancedsettingsLoS[1], duration=0.25)
        #pyautogui.moveTo(1650, 110, duration=0.25)
        pyautogui.click()

        # Browse Browse.png
        time.sleep(1)
        #if Browse[0] == None or Browse[1] == None:
        Browse[0], Browse[1] = findCenterOnScreen('./img/Browse.png')
        print("Browse = ", Browse[0], Browse[1])
        pyautogui.moveTo(Browse[0], Browse[1], duration=0.25)
        #else:
        #  pyautogui.moveTo(Browse[0], Browse[1], duration=0.25)
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
        #pyautogui.size()
        #width, height = pyautogui.size()
        # login
        #LoginLoS = locateOnScreen('./img/login.png')
        #pyautogui.moveTo(int(LoginLoS[0])+int(LoginLoS[2])/2, int(LoginLoS[1])+int(LoginLoS[3])/2, duration=0.25)

        #pyautogui.moveTo(1450, 300, duration=0.25)
        if LoginLoS[0] == None and LoginLoS[1] == None:
          LoginLoS[0], LoginLoS[1] = findCenterOnScreen('./img/login.png')
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
          print("if")
        else:
          print("LoginLoS[0] ", LoginLoS[0], LoginLoS[1])
          pyautogui.moveTo(LoginLoS[0], LoginLoS[1], duration=0.25)
          print("else")
        pyautogui.click()

        time.sleep(1)
        # Advanced-settings
        AdvancedsettingsLoS = locateOnScreen('./img/Advanced-settings.png')
        #pyautogui.moveTo(AdvancedsettingsLoS[0]+AdvancedsettingsLoS[2]/2, AdvancedsettingsLoS[1]+AdvancedsettingsLoS[3]/2, duration=0.25)
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
   