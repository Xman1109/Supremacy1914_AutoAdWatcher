from pyautogui import *
import pyautogui
import time
import keyboard
from os import listdir

path = os.path.dirname(os.path.abspath(__file__))+"/".replace("\\", "/")
cross = listdir(path + "src/cross")

while 1:
    if keyboard.is_pressed("F5"):
        break
    # get the x and y coordinates of the bluestacks window
    bluestacks_x = pyautogui.getWindowsWithTitle('BlueStacks')[0].left + 375
    bluestacks_y = pyautogui.getWindowsWithTitle("BlueStacks")[0].top
    bluestacks_width = pyautogui.getWindowsWithTitle("BlueStacks")[
        0].width - 375
    bluestacks_height = pyautogui.getWindowsWithTitle("BlueStacks")[
        0].height - 635
    # now locate the cross.png image on the bluestacks window
    for i in cross:
        if pyautogui.getActiveWindowTitle() == "BlueStacks":
            cross_location = pyautogui.locateOnScreen(
                path+"src/cross/"+i, region=(bluestacks_x, bluestacks_y, bluestacks_width, bluestacks_height), confidence=0.8)
            if path+"cap_area.png" in listdir(path):
                os.remove(path+"cap_area.png")
            screenshot = pyautogui.screenshot(region=(
                bluestacks_x, bluestacks_y, bluestacks_width, bluestacks_height))
            screenshot.save(path+"cap_area.png")
            if cross_location is not None:
                # now check that the found cross is not the one of the whitelisted_cross images
                whitelisted_cross = listdir(path + "src/whitelisted_cross")
                for j in whitelisted_cross:
                    whitelisted_cross_location = pyautogui.locateOnScreen(
                        path+"src/whitelisted_cross/"+j, region=(bluestacks_x, bluestacks_y, bluestacks_width, bluestacks_height), confidence=0.7)
                    if whitelisted_cross_location is not None:
                        # if the cross is whitelisted, then do nothing
                        print("Whitelisted cross found")
                        # if path+"whitelisted_cross_found.png" in listdir(path):
                        #     os.remove(path+"whitelisted_cross_found.png")
                        # screenshot = pyautogui.screenshot(region=(
                        #     whitelisted_cross_location[0], whitelisted_cross_location[1], whitelisted_cross_location[2], whitelisted_cross_location[3]))
                        # screenshot.save(path +
                        #                 "whitelisted_cross_found.png")
                    else:
                        # if the cross is not whitelisted, then click it
                        pyautogui.click(cross_location)
                        print("Clicked cross")
                        # if path+"cross_found.png" in listdir(path):
                        #     os.remove(path+"cross_found.png")
                        # screenshot = pyautogui.screenshot(region=(
                        #     cross_location[0], cross_location[1], cross_location[2], cross_location[3]))
                        # screenshot.save(path +
                        #                 "cross_found.png")
                        time.sleep(1)

    NextAd = pyautogui.locateOnScreen(path+"src/WatchAd.png", confidence=0.9, region=(
        pyautogui.getWindowsWithTitle('BlueStacks')[0].left, pyautogui.getWindowsWithTitle("BlueStacks")[0].top, pyautogui.getWindowsWithTitle("BlueStacks")[
            0].width, pyautogui.getWindowsWithTitle("BlueStacks")[
            0].height))
    if NextAd is not None:
        pyautogui.click(NextAd)
        print("Clicked Next Ad")
        # if path+"NextAd_found.png" in listdir(path):
        #     os.remove(path+"NextAd_found.png")
        # screenshot = pyautogui.screenshot(region=(
        #     NextAd[0], NextAd[1], NextAd[2], NextAd[3]))
        # screenshot.save(path + "NextAd_found"+".png")
    else:
        if pyautogui.getActiveWindowTitle() == "BlueStacks":
            pyautogui.moveTo(pyautogui.getWindowsWithTitle('BlueStacks')[0].left + pyautogui.getWindowsWithTitle("BlueStacks")[
                0].width/2,
                pyautogui.getWindowsWithTitle("BlueStacks")[0].top + pyautogui.getWindowsWithTitle("BlueStacks")[
                0].height/2)
            pyautogui.scroll(-100)
            print("Could not find Next Ad, scrolling down")
    FinalAdCollected = pyautogui.locateOnScreen(path+"src/FinalAdCollected.png", confidence=0.9, region=(
        pyautogui.getWindowsWithTitle('BlueStacks')[0].left, pyautogui.getWindowsWithTitle("BlueStacks")[0].top, pyautogui.getWindowsWithTitle("BlueStacks")[
            0].width, pyautogui.getWindowsWithTitle("BlueStacks")[
            0].height))
    if FinalAdCollected is not None:
        print("Finished collecting ads")
        time.sleep(3)
        exit()
    time.sleep(2)
