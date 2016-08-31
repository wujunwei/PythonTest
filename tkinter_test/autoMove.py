from PIL import ImageGrab
from autopy3 import alert


def hello_there_world():
    alert.alert("Hello, world")
# hello_there_world()
try:
    path = "C:\\"
    filename = "YC-" + str(12) + ".jpg"
    im = ImageGrab.grab()
    im.save(path + filename)
except Exception as e:
    print(e)
