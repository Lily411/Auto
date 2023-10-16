import time

import cv2
import numpy as np
import pyautogui as py
#(121, 114, 3)

def resize_template(template_path, scale_percent):
    # 读取模板图像
    template = cv2.imread(template_path,0)

    # 计算调整后的尺寸
    width = int(template.shape[1] * scale_percent / 100)
    height = int(template.shape[0] * scale_percent / 100)
    dim = (width, height)

    # 调整模板图像尺寸
    resized_template = cv2.resize(template, dim, interpolation=cv2.INTER_AREA)

    return resized_template

def find_image_in_another(img, temp):

    img = cv2.imread(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w,h = temp.shape

    res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] +w, pt[1] +h),(25,255,0),1)

    cv2.imshow('img', img)
    cv2.waitKey(0)


img = 'temp4.png'
temp = 'clear1.png'

for i in range(10, 1200, 10):
    find_image_in_another(img, resize_template(temp, i))
