import numpy as np
from PIL import Image
import pytesseract
import pyautogui
import re

# Define the path to the tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r''
# Define the path to the png file where the screenshots will be stored
img_path = r''

def init_grid():
    nums = ['1','2','3','4','5','6','7','8','9']
    vals = []

    for r in range(9):
        for c in range(9):
            pyautogui.screenshot(img_path, (320+(c*62), 308+(r*62), 62, 62))    
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
