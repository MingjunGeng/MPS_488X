import wx
import sys
import os
import time
from gui.mainFrame import MainFrame
# from device.dev_mps488X import MPS_488X


def main():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
