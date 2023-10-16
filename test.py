from PIL import ImageGrab
import cv2
import numpy as np
from pywinauto import keyboard


perfect = 'key/perfect4.png'

i = 0
while True:
    screen = ImageGrab.grab()
    perfect_gray = cv2.imread(perfect, 0)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(perfect_gray, screen_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.905)

    if len(loc[0]) > 0 :
        keyboard.send_keys('{VK_CONTROL down}')
        keyboard.send_keys('{VK_CONTROL up}')
        print("press" + str(i))
        i = i+1