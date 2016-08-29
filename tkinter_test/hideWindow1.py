from pub import *
import tkinter as tk

########################################################################
from pubsub import pub


class OtherFrame(tk.Toplevel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("otherFrame")

        # create the button
        btn = tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    # ----------------------------------------------------------------------
    def onClose(self):
        """
        closes the frame and sends a message to the main frame
        """
        self.destroy()
        pub.sendMessage("otherFrameClosed", arg1="data")


########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        btn = tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

        pub.subscribe(self.listener, "otherFrameClosed")

    # ----------------------------------------------------------------------
    def listener(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------------
    def hide(self):
        """
        hides main frame
        """
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """
        opens other frame and hides main frame
        """
        self.hide()
        subFrame = OtherFrame()

    # ----------------------------------------------------------------------
    def show(self):
        """
        shows main frame
        """
        self.root.update()
        self.root.deiconify()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
