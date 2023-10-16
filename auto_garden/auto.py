from PIL import Image, ImageGrab
import cv2
import numpy as np
import time
import pyautogui as py

big_water = 'water1.png'
img = cv2.imread(big_water)
w, h = img.shape[0] / 2, img.shape[1] / 2
small_water = 'water2.png'
img = cv2.imread(big_water)
w1, h1 = img.shape[0] / 2, img.shape[1] / 2
big_clear = 'clear1.png'
small_clear = 'clear2.png'
big_fertilize = 'fertilize1.png'
small_fertilize = 'fertilize2.png'
big_harvest = 'harvest.png'

seed1 = 'seed1.png'
seed2 = 'seed2.png'
seed3 = 'seed3.png'
shop1 = 'shop.png'

sowing1 = 'sowing1.png'
sowing2 = 'sowing2.png'
sowing3 = 'sowing3.png'

plant1_finish = 'plant1_finish.png'
plant3_finish = 'plant3_finish.png'

def find_oject(screen, tools, threshold):

    tools_gray = cv2.imread(tools, 0)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screen_gray= cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(tools_gray, screen_gray, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    return len(loc[0]), loc,screen

def mouse(x,y,w,h):
    py.moveTo(x + w, y + h, 0.5)
    py.click()
    py.mouseUp()

def shop(seed):
    flag = True
    while flag:
        screen = ImageGrab.grab()
        count_shop, loc_shop, screen = find_oject(screen, shop1, 0.95)
        if count_shop > 0:
            for pt in zip(*loc_shop[::-1]):
                mouse(pt[0], pt[1], w, 0.5*h+h)

        time.sleep(2)
        screen = ImageGrab.grab()
        count_seed1, loc_seed1, screen = find_oject(screen, seed, 0.95)
        if count_seed1 > 0:
            for pt in zip(*loc_seed1[::-1]):
                mouse(pt[0], pt[1], w, h)
            flag = False

def sowing(seed, sown, h1):
    count = 0
    x, y = py.position()
    x1 = x - 80
    y1 = y + h1
    while count < 3:
        py.moveTo( x1+1,  y1)
        screen = ImageGrab.grab()
        count_sowing1, loc_sowing1, screen = find_oject(screen, sown, 0.86)
        if count_sowing1 > 0:
            py.click()
            py.mouseUp()
            count = count + 1
            x1 = py.position()[0]
            shop(seed)
            continue
        x1 = x1 + 1

    return count

def normal_garden():
    while True:
        # 抓取螢幕截圖
        screen = ImageGrab.grab()

        #澆水
        count_water, loc_small_water, screen= find_oject(screen, small_water, 0.75)
        if count_water > 0:
            print("water:" + str(count_water))
            c, loc_big_water, screen = find_oject(screen, big_water, 0.75)
            for pt in zip(*loc_big_water[::-1]):
                mouse(pt[0],pt[1], w,  h)
            for pt in zip(*loc_small_water[::-1]):
                py.moveTo(pt[0] -w, pt[1] + h , 0.5)
                py.mouseDown()
                time.sleep(2)
                py.mouseUp()

        #掃塵
        count_clear, loc_small_clear, screen= find_oject(screen, small_clear, 0.75)
        if count_clear > 0:
            print("clear:" + str(count_clear))
            c, loc_big_clear, screen = find_oject(screen, big_clear,0.75)
            for pt in zip(*loc_big_clear[::-1]):
                mouse(pt[0], pt[1], w, h)
            for pt in zip(*loc_small_clear[::-1]):
                mouse(pt[0], pt[1], -w, h)

        #施肥
        count_fertilize, loc_small_fertilize, screen= find_oject(screen, small_fertilize, 0.75)
        if count_fertilize > 0:
            print("fertilize:" + str(count_fertilize))
            c, loc_big_fertilize, screen = find_oject(screen, big_fertilize, 0.75)
            for pt in zip(*loc_big_fertilize[::-1]):
                mouse(pt[0], pt[1], w, h)
            for pt in zip(*loc_small_fertilize[::-1]):
                mouse(pt[0], pt[1], -w, h)

        time.sleep(1)

def secret_garden():
    have_plant = False
    count_seed1 = 0
    total_harvest = 0
    t = 0.75 #for harvest
    i = 0
    while True:
        i = i +1
        # 沒有植物
        if have_plant == False:
            if count_seed1 < 1:
                seed = seed3
                sown = sowing3
                count_seed1 = count_seed1 + 1
                print("seed1 start: " + str(count_seed1))
            else:
                seed = seed3
                sown = sowing3
                print("seed3 start: 1")
                count_seed1 = 0
            shop(seed)
            count = 0
            while count < 5:
                if count < 3:
                    count = sowing(seed, sown, 0)
                else:
                    count = count + sowing(seed, sown, 5 * h)
                    break
            have_plant = True
            print("Planted:" + str(count))


        # 澆水
        screen = ImageGrab.grab()
        print("find water" + str(i))
        count_water, loc_small_water, screen = find_oject(screen, small_water, 0.75)
        if count_water > 0:
            print("water:" + str(count_water))
            c, loc_big_water, screen = find_oject(screen, big_water, 0.75)
            for pt in zip(*loc_big_water[::-1]):
                mouse(pt[0], pt[1], w, h)
            for pt in zip(*loc_small_water[::-1]):
                py.moveTo(pt[0] - w, pt[1] + 2 * h, 0.5)
                py.mouseDown()
                time.sleep(2)
                py.mouseUp()
            x,y = py.position()
            py.moveTo(x+120, y)


        # 施肥
        screen = ImageGrab.grab()
        print("find fertilize"+ str(i))
        count_fertilize, loc_small_fertilize, screen = find_oject(screen, small_fertilize, 0.75)
        if count_fertilize > 0:
            print("fertilize:" + str(count_fertilize))
            c, loc_big_fertilize, screen = find_oject(screen, big_fertilize, 0.75)
            for pt in zip(*loc_big_fertilize[::-1]):
                mouse(pt[0], pt[1], w, h)
            for pt in zip(*loc_small_fertilize[::-1]):
                mouse(pt[0], pt[1], -w, 2 * h)
            x, y = py.position()
            py.moveTo(x + 120, y)

        # 收割
        screen = ImageGrab.grab()
        print("find harvest"+str(i)+"t="+str(t))
        if seed == seed1:
            plant = plant1_finish
        else:
            plant = plant3_finish
        count_plant_finish, loc_plant_finish, screen = find_oject(screen, plant, t)
        if count_plant_finish > 0:
            print("harvest:" + str(count_plant_finish))
            c, loc_big_harvest, screen = find_oject(screen, big_harvest, 0.75)
            for pt in zip(*loc_big_harvest[::-1]):
                mouse(pt[0], pt[1], w, h)
            for pt in zip(*loc_plant_finish[::-1]):
                mouse(pt[0], pt[1], w, h)
            total_harvest = total_harvest + count_plant_finish
            print(total_harvest)
            if total_harvest > 1 and total_harvest< 6:
                t = t - 0.05
            if total_harvest >= 6:
                print("seed1 finish: " + str(count_seed1))
                have_plant = False
                total_harvest = 0
                t = 0.75

        time.sleep(1)

if __name__ == "__main__":
    #normal_garden()
    secret_garden()









