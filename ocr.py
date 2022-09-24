# pretty dame hard core

import pyautogui

from PIL import Image
from PIL import ImageGrab
import pytesseract

import time

# check realtime postion
# pyautogui.displayMousePosition()

# setting pytesseract
# download tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def grab_card_no():
    shot = ImageGrab.grab(bbox=(512, 534, 888, 560))
    #  Binary
    #  Threshold = 160
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)
    Img = shot.convert('L')
    newshot = Img.point(table,'1')
    str1 = pytesseract.image_to_string(newshot)
    return str1


while True:
    time.sleep(1)
    output = grab_card_no()
    print(output)