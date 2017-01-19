# coding=gbk
import os
import tkinter as tk
from autopy3 import alert
import datetime


def exc(command):
    try:
        os.system(command)
    except:
        alert.alert(msg="δ֪���󣬲���ʧ�ܣ�����Ȩ��!!", title="Alert", default_button="OK")
        return False
    return True


def shutdown(hours, mins, second, is_force):
    # hours = hours.get()
    # mins = mins.get() + 60 * hours
    # second = second.get() + 60 * mins
    now = datetime.datetime.now()
    d1 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    d2 = datetime.datetime(now.year, now.month, now.day, hours.get(), mins.get(), second.get())
    second = (d2 - d1).seconds
    # alert.alert("{0} {1} ��� {2} ��".format(d1, d2, str(second)))
    if is_force.get():
        command = "shutdown -s -f -t " + str(second)
    else:
        command = "shutdown -s -t " + str(second)
    exc(command)

root = tk.Tk()
root.title("�ƻ��ػ�С����")
root.geometry('210x160')  # ��x ����*
root.resizable(width=True, height=True)  # ���ɱ�, �߿ɱ�,Ĭ��ΪT
root.wm_attributes('-topmost', 1)
tk.Label(root, text="����д�ػ�ʱ��").pack(side="top")
Hours = tk.IntVar()
Mins = tk.IntVar()
Seconds = tk.IntVar()
isForce = tk.IntVar()
cb = tk.Checkbutton(root, text="�Ƿ�ǿ�ƹػ�", variable=isForce, onvalue=1)
cb.pack()

app1 = tk.Frame(root)
label = tk.Label(app1, text="Сʱ:")
label.pack(side="left")
inputHour = tk.Entry(app1)
inputHour['textvariable'] = Hours
inputHour.pack(side='right')
app1.pack(side=tk.TOP)

app2 = tk.Frame(root)
label = tk.Label(app2, text="����:")
label.pack(side="left")
inputMin = tk.Entry(app2)
inputMin['textvariable'] = Mins
inputMin.pack()
app2.pack(side=tk.TOP)

app3 = tk.Frame(root)
label = tk.Label(app3, text="  ��:")
label.pack(side="left")
inputSec = tk.Entry(app3)
inputSec['textvariable'] = Seconds
inputSec.pack()
app3.pack()

app4 = tk.Frame(root)
shutdown_btn = tk.Button(app4)
shutdown_btn["text"] = "�ػ�"
shutdown_btn["command"] = lambda: shutdown(Hours, Mins, Seconds, isForce)
shutdown_btn.pack(side="left")
cancel_btn = tk.Button(app4)
cancel_btn["text"] = "ȡ���ػ�"
cancel_btn["command"] = lambda: exc("shutdown -a")
cancel_btn.pack(side="right")
app4.pack(side="bottom")
root.mainloop()
