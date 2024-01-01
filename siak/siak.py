import keyboard
import time
import sys

def presskey():
    while True:  # Création d'une boucle infinie
        keyboard.press('e')  # Appuyer sur la touche "e"
        time.sleep(0.01)  # Attendre un peu
        keyboard.release('e')  # Relâcher la touche "e"

        if keyboard.is_pressed('p'):  # Vérifier si la touche "p" est pressée
            print("Le bouton 'P' a été pressé, stoppons cette folie !")
            sys.exit()
