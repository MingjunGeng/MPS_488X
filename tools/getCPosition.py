import sys
import os
import time
import pyautogui
#from PIL import pyautogui

def get_position():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: '+ str(x).rjust(4)+'Y: ' + str(y).rjust(4)
            print(positionStr, end = '')
            print('\b' * len(positionStr), end = '', flush = True)
    except KeyboardInterrupt:
        print('\nDone.')

if __name__ == "__main__":
    #print(locateOnScreen('./img/login.png'))
    get_position()
