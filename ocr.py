# pretty dame hard core

import pyautogui

from PIL import Image
from PIL import ImageGrab
import pytesseract

import time

# check realtime postion
# pyautogui.displayMousePosition()

# setting pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def grabscreen2txt():
    shot = ImageGrab.grab(bbox=(512, 534, 888, 560))
    #  二值化
    #  自定义灰度界限，大于这个值为黑色，小于这个值为白色
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)
    Img = shot.convert('L')
    newshot=Img.point(table,'1')
    newshot.save('1.png')
    str1=pytesseract.image_to_string(newshot)
    return str1


while True:
    time.sleep(1)
    output = grabscreen2txt()
    print(output)