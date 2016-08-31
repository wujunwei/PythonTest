# _*_ coding:UTF-8 _*_
import win32api
import win32con
from ctypes import *
import threading
import sys
import ctypes.wintypes

EXIT = False


def mouse_click(x=None, y=None):
    pass
    # if not x is None and not y is None:
    #     mouse_move(x, y)
    #     time.sleep(0.05)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_move(x, y):
    windll.user32.SetCursorPos(x, y)


class HotKey(threading.Thread):  # 创建一个Thread.threading的扩展类
    def __init__(self, group=None, name=None,
                 args=(), kwargs=None, *, daemon=True):
        super().__init__(group=group, target=self.run, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)

    def run(self):
        user32 = ctypes.windll.user32  # 加载user32.dll
        if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, win32con.VK_F3):  # 注册快捷键 alt + f3 并判断是否成功。
            exit()
        # 以下为判断快捷键冲突，释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            # print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        print(msg.wParam, msg.message, msg.lParam, msg.hWnd)
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)


if __name__ == "__main__":
    hotKey = HotKey()
    hotKey.setDaemon(True)
    hotKey.start()
    # for event in range(1, 30):
    #     mouse_click(1150, 665)
    #     win32api.keybd_event(17, 0, 0, 0)
    #     win32api.keybd_event(86, 0, 0, 0)
    #     win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    #     win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    #     mouse_click(1272, 669)
    hotKey.join()
    if True:
        sys.exit()
