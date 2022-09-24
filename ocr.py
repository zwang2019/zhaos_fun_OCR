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

card_no = (550, 570, 888, 592)
pin_no = (1024, 526, 1115, 560)

debug = True

def grab_no(num):
    shot = ImageGrab.grab(bbox=num)

    '''
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
    newshot.save('1.png')
    '''
    str1 = pytesseract.image_to_string(shot)
    return str1


# logic part
loop_flag = True

while loop_flag:
    time.sleep(0.5)
    # capturing the card number
    card_no_flag = True
    while card_no_flag:
        time.sleep(0.75)
        captured_card_no = grab_no(card_no)
        captured_card_no = captured_card_no.strip()
        if debug is True:
            print(captured_card_no)
            print(captured_card_no[:4])
            print(len(captured_card_no))
        if captured_card_no[:4] == '5021' and len(captured_card_no) == 19:
            user_res = pyautogui.confirm(text='Captured card number is ' + captured_card_no, title='Confirmation', buttons=['YES', 'NO'])
            if user_res == 'YES':
                card_no_flag = False
    # end loop for capturing the card number

    # capturing the pin number
    pin_no_flag = True
    while pin_no_flag:
        time.sleep(0.75)
        captured_pin_no = grab_no(pin_no)
        captured_pin_no = captured_pin_no.strip()
        if debug is True:
            print(captured_pin_no)
        if captured_pin_no.isdigit() and len(captured_pin_no) == 4:
            user_res_2 = pyautogui.confirm(text='Captured pin number is ' + captured_pin_no, title='Confirmation', buttons=['YES', 'NO'])
            if user_res_2 == 'YES':
                pin_no_flag = False
    # end loop for capturing the pin number

    # sorting the data
    f = open('log.txt', 'r+')
    f.read()
    f.write('\n' + 'CARD No: ' + captured_card_no + '    Pin: ' + captured_pin_no)
    f.close()

    # query user exit or not
    user_res_3 = pyautogui.confirm(text='Continue Scanning? ' + captured_pin_no, title='Confirmation', buttons=['Continue', 'Exit'])
    if user_res_3 == 'Exit':
        loop_flag = False


pyautogui.alert(text='Mission Complete!', title='Congratulations', button='OK')