from PIL import Image, ImageGrab

i = 0
while True:
    # 对整个屏幕进行截屏
    screen = ImageGrab.grab()

    # 保存截图到文件
    screen.save("screenshop/screenshot" + str(i) + ".png")
    i = i +1

    flag = 0
    while flag == 0:
        screen1 = ImageGrab.grab()
        perfect_loc = find_oject(screen1, perfect, 0.87)
        if len(perfect_loc[0]) > 0:
            flag = 1
            keyboard.send_keys('{VK_CONTROL down}')
            keyboard.send_keys('{VK_CONTROL up}')