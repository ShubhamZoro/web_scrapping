import pyautogui
from PIL import ImageGrab

import time



def Collision(data):
    # Check colison for birds
    for i in range(300, 415):
        for j in range(410, 540):
            if data[i, j] < 171:
                pyautogui.press("down")
                return
    # Check colison for cactus
    for i in range(300, 415):
        for j in range(540, 640):
            if data[i, j] < 100:
                pyautogui.press("up")
                return
    return
#
#

time.sleep(3)
pyautogui.press('space')

# image = ImageGrab.grab().convert('L')
# data = image.load()
while True:

    try:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        Collision(data)
    except KeyboardInterrupt:
        print('\n')
# #
# for i in range(200, 305):
#          for j in range(563, 610):
#              data[i, j]=0
#                  # pyautogui.press("down")
# image.show()