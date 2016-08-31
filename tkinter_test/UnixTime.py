import ctypes
import threading
from tkinter import *
from datetime import *
import time
import ctypes.wintypes
import win32con

DEFAULTDATE = "0000-01-01 00:00:00"


class HotKey(threading.Thread):  # 创建一个Thread.threading的扩展类
    def __init__(self, group=None, name=None,
                 args=(), kwargs=None, *, daemon=True):
        super().__init__(group=group, target=self.run, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)

    def run(self):
        user32 = ctypes.windll.user32  # 加载user32.dll
        if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, 65):  # 注册快捷键 alt + a 并判断是否成功。
            exit()
        if not user32.RegisterHotKey(None, 100, win32con.MOD_ALT, 66):  # 注册快捷键 alt + b 并判断是否成功。
            exit()
        # 以下为判断快捷键冲突，释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            # print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        root.withdraw()
                    if msg.wParam == 100:
                        root.update()
                        root.deiconify()
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)


#
# def subscribe(event):
#     if event.Key == 'A' and event.Alt != 0:
#         root.withdraw()
#     if event.Key == 'B' and event.Alt != 0:
#         root.update()
#         root.deiconify()
#     return True


def change_unix_to_date(int_date, view_text):
    int_time = int_date.get()
    value = time.localtime(int_time)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", value)
    view_text.set(dt)


def change_date_to_unix(int_date, view_text):
    time_str = view_text.get()
    time_str += DEFAULTDATE[len(time_str):]
    view_text.set(time_str)
    value = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    value = time.mktime(value)
    int_date.set(int(value))


root = Tk()
root.title("UnixTime")
root.geometry("200x100")
root.wm_attributes('-topmost', 1)
mainFrame = Frame(root)
# mainFrame['bg'] = 'yellow'
# Var
result = StringVar()
result.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
Unix = IntVar()
Unix.set(int(time.time()))
# Entry
view = Entry(mainFrame, textvariable=result)
view.pack(side=TOP)

inputBox = Entry(mainFrame, textvariable=Unix)
inputBox.pack()
# button
change_int = Button(mainFrame, text="时间戳转string", command=lambda: change_unix_to_date(Unix, result))
change_int.pack(side=LEFT)

# hide_btn = Button(mainFrame, text="退出", command=root.quit)
# hide_btn.pack(side=BOTTOM)

change_str = Button(mainFrame, text="string转时间戳", command=lambda: change_date_to_unix(Unix, result))
change_str.pack(side=RIGHT)
mainFrame.pack()
hk = HotKey()
hk.setDaemon(True)
hk.start()
root.mainloop()
