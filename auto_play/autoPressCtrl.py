# 1076 0.77 107BPM

from pywinauto import keyboard
import cv2
import numpy as np
from PIL import ImageGrab

start = 'key/start.png'
img2 = cv2.imread('key/perfect5.png')
x = 1076
y = 663
width = 15
height = 12

while True:
        while True:
            # 截取指定区域的屏幕图像
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            screenshot.save('screenshot.png')
            img = cv2.imread('screenshot.png')

            similarity = np.mean(img == img2) >= 0.077
            if similarity:
                keyboard.send_keys('{VK_CONTROL down}')
                keyboard.send_keys('{VK_CONTROL up}')
                print("Press")


