import tkinter as tk


def say_hi(var):
    text = var.get()
    var.set("hello"+text)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master,)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.hi_there = tk.Button(self)
        self.text = tk.StringVar()
        self.input = tk.Entry(self, width=21)
        self.input['textvariable'] = self.text
        self.input.pack(side="bottom")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = lambda : say_hi(self.text)
        self.hi_there.pack(side="top")

        self.quit.pack(side="bottom")


root = tk.Tk()
app = Application(root)

app.mainloop()
