#!python3
# Demonstration of how to send text to the computer

import pyautogui
import time

print("Move your mouse to an empty spot on screen before the countdown finishes!")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
pyautogui.write("Hello world")






