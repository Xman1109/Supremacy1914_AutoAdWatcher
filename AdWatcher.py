from pyautogui import *
import pyautogui
import time
import keyboard
import cv2  # used for the confidence level of the detection
import win32gui
from os import listdir

#######################
# DEBUG Screenshots
getDetectedCross = True
getNextAd = True
getFinalAd = True
getAdArea = True
#######################

x = int(pyautogui.size()[0]/2 - 250)
path = os.path.dirname(os.path.abspath(__file__))+"/".replace("\\", "/")

if win32gui.FindWindow(None, "BlueStacks") != 0:  # if BlueStacks is running
    win = win32gui.FindWindow(None, "BlueStacks")
    win32gui.SetForegroundWindow(win)
    win32gui.SetActiveWindow(win)
    if pyautogui.getWindowsWithTitle("BlueStacks")[  # rotate the screen and resize the window
            0].width > pyautogui.getWindowsWithTitle("BlueStacks")[
            0].height:
        keyboard.press_and_release("strg+shift+4")
        time.sleep(1.5)
    win32gui.MoveWindow(win, x, 0, 500, 860, True)
    win32gui.UpdateWindow(win)
else:
    print("BlueStacks not found")
    time.sleep(3)
    exit()

while 1:
    if win32gui.FindWindow(None, "BlueStacks") != 0:
        print("Starting...")
        print("Note: Hold F5 to exit")
        if keyboard.is_pressed("F5"):
            break
        while 1:
            if keyboard.is_pressed("F5"):  # Hold F5 to exit
                break

            # The Area where a button will appear
            bluestacks_x = pyautogui.getWindowsWithTitle('BlueStacks')[
                0].left + 375
            bluestacks_y = pyautogui.getWindowsWithTitle("BlueStacks")[0].top
            bluestacks_width = pyautogui.getWindowsWithTitle("BlueStacks")[
                0].width - 375
            bluestacks_height = pyautogui.getWindowsWithTitle("BlueStacks")[
                0].height - 685

            # The Area of the entire BlueStacks window
            bluestacks_window_x = pyautogui.getWindowsWithTitle('BlueStacks')[
                0].left
            bluestacks_window_y = pyautogui.getWindowsWithTitle("BlueStacks")[
                0].top
            bluestacks_window_width = pyautogui.getWindowsWithTitle("BlueStacks")[
                0].width
            bluestacks_window_height = pyautogui.getWindowsWithTitle("BlueStacks")[
                0].height

            # A List of every X in the src/cross folder
            cross = listdir(path + "src/cross")

            for i in cross:  # Go through all the images in the src/cross folder and compare them to the screen
                cross_location = pyautogui.locateOnScreen(
                    path+"src/cross/"+i, region=(bluestacks_x, bluestacks_y, bluestacks_width, bluestacks_height), confidence=0.75)
                if getAdArea:
                    if path+"ad_cap_area.png" in listdir(path):
                        os.remove(path+"ad_cap_area.png")
                    screenshot = pyautogui.screenshot(region=(
                        bluestacks_x, bluestacks_y, bluestacks_width, bluestacks_height))
                    screenshot.save(path+"ad_cap_area.png")
                if cross_location is not None:  # If the image is found on the screen then click the cross to end the Ad
                    pyautogui.click(cross_location)
                    print("Clicked cross")
                    if getDetectedCross:
                        if path+"cross_found.png" in listdir(path):
                            os.remove(path+"cross_found.png")
                        screenshot = pyautogui.screenshot(region=(
                            cross_location[0], cross_location[1], cross_location[2], cross_location[3]))
                        screenshot.save(path +
                                        "cross_found.png")

                    time.sleep(1)

            # Check if this was the last Ad
            FinalAdCollected = pyautogui.locateOnScreen(path+"src/FinalAdCollected.png", confidence=0.9, region=(
                bluestacks_window_x, bluestacks_window_y, bluestacks_window_width, bluestacks_window_height))
            if path+"cap_area.png" in listdir(path):
                os.remove(path+"cap_area.png")
            screenshot = pyautogui.screenshot(region=(
                bluestacks_window_x, bluestacks_window_y, bluestacks_window_width, bluestacks_window_height))
            screenshot.save(path + "cap_area.png")
            if FinalAdCollected is not None:  # If yes, then close the program
                if getFinalAd:
                    if path+"FinalAdCollected_found.png" in listdir(path):
                        os.remove(path+"FinalAdCollected_found.png")
                    screenshot = pyautogui.screenshot(region=(
                        FinalAdCollected[0], FinalAdCollected[1], FinalAdCollected[2], FinalAdCollected[3]))
                    screenshot.save(path + "FinalAdCollected_found"+".png")
                print("Finished collecting ads")
                time.sleep(3)
                exit()

            # Check if there is another Ad to collect
            NextAd = pyautogui.locateOnScreen(path+"src/WatchAd.png", confidence=0.5, region=(
                bluestacks_window_x, bluestacks_window_y, bluestacks_window_width, bluestacks_window_height))
            if NextAd is not None:
                time.sleep(4)
                pyautogui.click(NextAd)
                print("Clicked Next Ad")
                time.sleep(32)
                if getNextAd:
                    if path+"NextAd_found.png" in listdir(path):
                        os.remove(path+"NextAd_found.png")
                    screenshot = pyautogui.screenshot(region=(
                        NextAd[0], NextAd[1], NextAd[2], NextAd[3]))
                    screenshot.save(path + "NextAd_found"+".png")
            else:  # If there is no next Ad then scroll down the screen and check again
                pyautogui.moveTo(bluestacks_window_x + bluestacks_window_width/2,
                                 bluestacks_window_y + bluestacks_window_height/2)
                pyautogui.scroll(-100)
                print("Could not find Next Ad, scrolling down")
            time.sleep(2)
    else:
        # If BlueStacks is not found exit the program
        if win32gui.FindWindow(None, "BlueStacks") == None:
            print(
                "BlueStacks got closed... \n If this is a bug, please report it on the github page")
            time.sleep(3)
            exit()
        else:
            win = win32gui.FindWindow(None, "BlueStacks")
            win32gui.SetForegroundWindow(win)
            win32gui.SetActiveWindow(win)
            if pyautogui.getWindowsWithTitle("BlueStacks")[
                    0].width > pyautogui.getWindowsWithTitle("BlueStacks")[
                    0].height:
                keyboard.press_and_release("strg+shift+4")
                time.sleep(1.5)
            win32gui.MoveWindow(win, x, 0, 500, 860, True)
            win32gui.UpdateWindow(win)
