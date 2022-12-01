import os
import time
from os import listdir

import cv2  # used for the confidence level of the detection
import keyboard
import pyautogui
import win32gui
from pyautogui import *

#######################
# DEBUG Screenshots
getDetectedCross = True
getNextAd = True
getFinalAd = True
getAdArea = True
#######################

screen_x = int(pyautogui.size()[0]/2 - 250)
path = os.path.dirname(os.path.abspath(__file__))+"/".replace("\\", "/")
blockScrolling = False
numberOfClickedAds = 0

# The Area of the entire BlueStacks window
bluestacks_window = [pyautogui.getWindowsWithTitle('BlueStacks')[
    0].left, pyautogui.getWindowsWithTitle("BlueStacks")[0].top + 33, pyautogui.getWindowsWithTitle("BlueStacks")[0].width - 33, pyautogui.getWindowsWithTitle("BlueStacks")[0].height - 33]
# left, top, width, height
# 33 px because of bluestacks overlay

# Left Side
X_left = bluestacks_window[0], bluestacks_window[1], 50, 50
# Right Side
X_right = bluestacks_window[0] + \
    bluestacks_window[2] - 50, bluestacks_window[1], 50, 50


def clickAds():
    Ad_location = pyautogui.locateOnScreen(
        path+"src/WatchAd.png", region=(bluestacks_window))
    if Ad_location is not None:
        pyautogui.click(Ad_location)
        numberOfClickedAds += 1
        blockScrolling = True
        print("Clicked Ad: " + str(numberOfClickedAds)+"/8")
        time.sleep(35)
    else:
        return


def scroll():
    if blockScrolling is False:
        pyautogui.moveTo(bluestacks_window[2]/2, bluestacks_window[3]/2)
        pyautogui.scroll(-100)
        print("Could not find Next Ad, scrolling down")
    else:
        return


def clickX():
    cross = listdir(path + "src/cross")
    for i in cross:
        x_location = pyautogui.locateOnScreen(
