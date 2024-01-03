
import keyboard
import mouse 
import time 
import sys
import pyautogui

#1 Point(x=620, y=909)
#2 Point(x=766, y=968)
#3 Point(x=751, y=371)
#4 Point(x=788, y=964)

def main_programm():
    pyautogui.moveTo(620, 909)
    mouse.click('left')
    time.sleep(0.5)
    pyautogui.moveTo(766,968)
    mouse.click('left')
    time.sleep(0.5)
    pyautogui.moveTo(751, 371)
    mouse.click('left')
    time.sleep(0.5)
    pyautogui.moveTo(788, 964)
    mouse.click('left')
    time.sleep(0.5)


while True:
    keyboard.wait('!')
    while True:
        main_programm()
        print("programme lancé")
        if keyboard.is_pressed('p'):  # Ici on vérifie si 'p' est pressée
            print("Arrêt du programme")
            sys.exit()

