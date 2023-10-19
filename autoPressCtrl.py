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

def find_oject(screen, tools, threshold):

    tools_gray = cv2.imread(tools, 0)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screen_gray= cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(tools_gray, screen_gray, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    return loc

while True:
    screen = ImageGrab.grab()
    start_loc = find_oject(screen, start, 0.9)
    if len(start_loc[0]) > 0:
        while True:
            # 截取指定区域的屏幕图像
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            screenshot.save('screenshot.png')
            img = cv2.imread('screenshot.png')

            similarity = np.mean(img == img2) >= 0.077
            if similarity:
                keyboard.send_keys('{VK_CONTROL down}')
                keyboard.send_keys('{VK_CONTROL up}')


