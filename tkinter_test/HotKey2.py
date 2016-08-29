# coding=utf-8
"""
Created on 2010-10-12
@author: lxd
"""
import wx
import win32con
import time
import threading


class WorkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear()

    def stop(self):
        self.timeToQuit.set()

    def run(self):
        while True:
            if not self.timeToQuit.isSet():
                print('work')
                time.sleep(1)
            else:
                break


def OnHotKeyQuit(evt):
    exit()


class FrameWithHotKey(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.hotKeyId_quit = 102
        self.hotKeyId_end = 101
        self.hotKeyId_start = 100
        self.regHotKey()
        self.Bind(wx.EVT_HOTKEY, self.OnHotKeyStart, id=self.hotKeyId_start)
        self.Bind(wx.EVT_HOTKEY, self.OnHotKeyEnd, id=self.hotKeyId_end)
        self.Bind(wx.EVT_HOTKEY, OnHotKeyQuit, id=self.hotKeyId_quit)
        self.work = None

    def regHotKey(self):
        self.RegisterHotKey(self.hotKeyId_start, win32con.MOD_ALT, win32con.VK_F1)
        self.RegisterHotKey(self.hotKeyId_end, win32con.MOD_ALT, win32con.VK_F2)
        self.RegisterHotKey(self.hotKeyId_quit, win32con.MOD_ALT, win32con.VK_F3)

    def OnHotKeyStart(self, evt):
        if not self.work:
            self.work = WorkThread()
            self.work.setDaemon(True)
            self.work.start()

    def OnHotKeyEnd(self, evt):
        if self.work:
            self.work.stop()
            self.work = None


app = wx.App()
FrameWithHotKey(None)
app.MainLoop()
