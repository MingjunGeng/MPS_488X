import wx
import sys
import os
import time
from device.dev_mps488X import MPS_488X

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        
        self.mps_488X = MPS_488X()
        
        self.init_ui()
        
    def init_ui(self):
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.menu_title = wx.StaticText(panel, label="Main Menu")
        vbox.Add(self.menu_title, flag=wx.CENTER|wx.TOP, border=15)
        
        self.menu_options = [
            {'text': 'Update Device Normal Mode Firmware', 'command': self.mps_488X.Normal_Mode_Update},
            {'text': 'Update Device Recovery Mode Firmware', 'command': self.mps_488X.Recovery_Mode_Update},
            {'text': 'Change Mac Address and Serial Number', 'command': self.mps_488X.Mac_Update},
            {'text': 'Check Mac Address and Serial Number', 'command': self.mps_488X.Mac_Check},
            {'text': 'EXIT', 'command': self.on_exit}
        ]
        
        self.buttons = []
        for option in self.menu_options:
            button = wx.Button(panel, label=option['text'])
            button.Bind(wx.EVT_BUTTON, self.on_button_click)
            vbox.Add(button, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
            self.buttons.append(button)
        
        panel.SetSizer(vbox)
        
        self.SetTitle('Device Menu')
        self.Centre()
        
    def on_button_click(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()
        
        for option in self.menu_options:
            if option['text'] == label:
                option['command']()
                break
                
    def on_exit(self, event=None):
        self.Close(True)

def main():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
