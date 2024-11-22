import numpy as np
from PIL import Image
import pytesseract
import pyautogui
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img_path = r'C:\Users\lowal\PythonProjects\SudokuBot\ImageTest.png'

def init_grid():
    nums = ['1','2','3','4','5','6','7','8','9']
    vals = []

    for r in range(9):
        for c in range(9):
            pyautogui.screenshot('ImageTest.png', (320+(c*62), 308+(r*62), 62, 62))    
            img = Image.open(img_path)
            img = img.crop((5,5,57,57))
            num = pytesseract.image_to_string(img, config='-psm 1000')
            num = re.sub('[^0-9]', '', num)
            if num in nums:
                vals.append(num)
            else:
                vals.append('0')

    gg = np.reshape(vals,(9,9))
    gg = np.astype(gg,int)
    return gg
