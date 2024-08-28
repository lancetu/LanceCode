# -*- coding: utf-8 -*-
'''
Description:    This is the main function of the TCA program.
Author:         Du Ning
Date:           2024.08.28
'''

# Import the libs and modules
import    time
import    os
import    wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # 创建一个面板
        pnl = wx.Panel(self)

        # 创建一个静态文本（标签）
        st = wx.StaticText(pnl, label="Hello, wxPython!", pos=(10, 10))

        # 创建一个文本框
        tc = wx.TextCtrl(pnl, value="默认文本", pos=(10, 30))

        # 创建一个按钮
        btn = wx.Button(pnl, label="点击我", pos=(10, 60))

        # 绑定按钮点击事件
        btn.Bind(wx.EVT_BUTTON, self.on_button_click)

        # 创建一个复选框
        cb = wx.CheckBox(pnl, label="选择我", pos=(10, 90))

        # 创建一个单选按钮
        rb = wx.RadioButton(pnl, label="选项1", pos=(10, 120))

        # Set the title of the window to "Test Code Adapter"
        # Set the size of the window to 1600x1200
        # Set the position of the window to the center of the screen
        # Set the window back ground color to white
        self.SetTitle("Test Code Adapter")
        self.SetSize((1920, 1080))
        self.Centre()
        self.SetBackgroundColour(wx.WHITE)

    def on_button_click(self, event):
        wx.MessageBox("按钮被点击了！", "提示")

def main():
    print("Start the TCA main window...")
    # Construct the GUI of a separate window for the TCA program
    app = wx.App(False)
    frame = MyFrame(None)

    # Show the window
    frame.Show()
    # Start the event loop
    app.MainLoop()





if __name__ == '__main__':
    main()