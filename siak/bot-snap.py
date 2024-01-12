
import keyboard
import mouse 
import time 
import sys
import pyautogui

#Point(x=379, y=989)
#Point(x=936, y=926)
#Point(x=1350, y=988)

def main_programm():
    pyautogui.moveTo(379,989, duration=2)
    mouse.click('left')
    time.sleep(1)
    pyautogui.moveTo(936,926,duration=1.5)
    mouse.click('left')
    time.sleep(1)
    pyautogui.moveTo(1350,988,duration=1.5)
    mouse.click('left')
    time.sleep(1)
    

while True:
    print("appuyez sur ! pour lancer le programme.")
    keyboard.wait('!')
    while True:
        main_programm()
        if keyboard.is_pressed('p'):  # Ici on vérifie si 'p' est pressée
            print("Arrêt du programme")
            sys.exit()

