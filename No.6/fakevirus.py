import os


os.system("shutdown -s -t 30")
while True:
    str = input("what do you want to do")
    if 'shutdown' in str:
        os.system(str)
        exit()
