from PIL import Image, ImageGrab
import cv2
import numpy as np
from pywinauto import keyboard


start = 'key/start.png'
key_up = 'key/up.png'
key_down = 'key/down.png'
key_left = 'key/left.png'
key_right = 'key/right.png'
perfect = 'key/perfect.png'
img = cv2.imread(key_up)
w, h = img.shape[0], img.shape[1]
all_key = [key_up, key_down, key_left, key_right]

def presskey(i):
    if i == 0:
        keyboard.send_keys('{VK_UP down}')
        keyboard.send_keys('{VK_UP up}')
    elif i == 1:
        keyboard.send_keys('{VK_DOWN down}')
        keyboard.send_keys('{VK_DOWN up}')
    elif i == 2:
        keyboard.send_keys('{VK_LEFT down}')
        keyboard.send_keys('{VK_LEFT up}')
    else:
        keyboard.send_keys('{VK_RIGHT down}')
        keyboard.send_keys('{VK_RIGHT up}')

def find_oject(screen, tools, threshold):

    tools_gray = cv2.imread(tools, 0)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screen_gray= cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(tools_gray, screen_gray, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    return loc

def autoplay():
    while True:
        screen = ImageGrab.grab()
        result = []
        click = []
        start_loc = find_oject(screen, start, 0.97)
        if len(start_loc[0]) > 0 :
            for i, key in enumerate(all_key):
                loc = find_oject(screen, key, 0.95)
                for pt in zip(*loc[::-1]):
                    result.append(pt[0])
                    click.append(i)

            sorted_key = sorted(zip(result,click))
            print(sorted_key)
            if len(sorted_key) > 0 :
                for key in sorted_key:
                    presskey(key[1])


if __name__ == '__main__':
    autoplay()

