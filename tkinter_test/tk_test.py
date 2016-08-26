import tkinter as tk


def say_hi(var):
    tex = var.get()
    var.set("hello" + tex)


root = tk.Tk()
root.title("test tkinter")
root.geometry('300x300')  # 是x 不是*
root.resizable(width=True, height=True)  # 宽不可变, 高可变,默认为T
app = tk.Frame(root)
quitButton = tk.Button(app, text="QUIT", fg="red", command=root.destroy)
hi_there = tk.Button(app)
text = tk.StringVar()
inputButton = tk.Entry(app, width=21)
inputButton['textvariable'] = text
inputButton.pack(side="bottom")

hi_there["text"] = "Hello World\n(click me)"
hi_there["command"] = lambda: say_hi(text)
hi_there.pack(side="left")
quitButton.pack(side="bottom")
app.pack()
app.mainloop()
