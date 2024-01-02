import keyboard
import time
import sys


print("Programme lancé, appuyez sur 'p' pour arrêter.")

def presskey():
    
    while True:
        keyboard.press('e')
        time.sleep(0.01)
        keyboard.release('e')

        if keyboard.is_pressed('p'):  # Ici on vérifie si 'p' est pressée
            print("Arrêt du programme")
            sys.exit()

presskey()
