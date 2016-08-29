from tkinter import *

root = Tk()
root.wm_attributes('-topmost', 1)


def printCoords(event):
    print('event.char = ', event.char)
    print('event.keycode = ', event.keycode)


# 创建第一个   Button,并将它与Key键绑定
bt1 = Button(root, text='Press BackSpace')
bt1.bind('<Control-Alt-b>', printCoords)
# 将焦点设置到第   1个  Button上
bt1.focus_set()
bt1.grid()
root.mainloop()
