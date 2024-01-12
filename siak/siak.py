import keyboard
import mouse 
import time 
import sys
import pyautogui

#Point(x=379, y=989)
#Point(x=936, y=926)
#Point(x=1350, y=988)
#
#


def press_key():
    print(pyautogui.position())

while True:
    keyboard.wait('!')
    for i in range(1):
        press_key()
        print("programme lancé")
        