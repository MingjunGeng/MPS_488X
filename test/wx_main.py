import wx
import subprocess

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Panel
        pnl = wx.Panel(self)
        
        # Buttons
        self.btn1 = wx.Button(pnl, label='Run ls', pos=(10, 10))
        self.btn2 = wx.Button(pnl, label='Button 2', pos=(10, 50))
        self.btn3 = wx.Button(pnl, label='Button 3', pos=(10, 90))
        
        # Bind buttons to event handlers
        self.btn1.Bind(wx.EVT_BUTTON, self.on_button1)
        self.btn2.Bind(wx.EVT_BUTTON, self.on_button2)
        self.btn3.Bind(wx.EVT_BUTTON, self.on_button3)
        
        # Set the frame properties
        self.SetSize((300, 200))
        self.SetTitle('wxPython Example')
        self.Centre()

    def on_button1(self, event):
        # Run the ls command and print the output
        result = subprocess.run(['ls'], capture_output=True, text=True)
        wx.MessageBox(result.stdout, 'ls Output', wx.OK | wx.ICON_INFORMATION)
    
    def on_button2(self, event):
        wx.MessageBox('Button 2 pressed', 'Info', wx.OK | wx.ICON_INFORMATION)
    
    def on_button3(self, event):
        wx.MessageBox('Button 3 pressed', 'Info', wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
