import sys
import os
import time
import pyautogui
from PIL import Image

def get_Image():
    try:
        im = pyautogui.screenshot()
        a = int(input('Enter 1st position: '))
        b = int(input('Enter 2st position: '))
        c = int(input('Enter 3st position: '))
        d = int(input('Enter 4st position: '))
        om = im.crop((a, b, c, d))
        fileName = input('Enter the fileName: ')
        om.save(fileName)
    except KeyboardInterrupt:
        print('\nDone.')

if __name__ == "__main__":
    #print())
    get_Image()
