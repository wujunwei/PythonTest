from tkinter import *
from datetime import *
import time


def change_unix_to_date(int_date, view_text):
    int_time = int_date.get()
    value = time.localtime(int_time)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", value)
    view_text.set(dt)


def change_date_to_unix(int_date, view_text):
    time_str = view_text.get()
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

change_str = Button(mainFrame, text="string转时间戳", command=lambda: change_date_to_unix(Unix, result))
change_str.pack(side=RIGHT)

mainFrame.pack()
root.mainloop()
