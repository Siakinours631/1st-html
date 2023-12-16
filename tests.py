import os.path
import _thread
import requests

help(os.path)
path = "/YOUTUBE-COMMENT-BOT/test.py/LICENCE"


#Raydium-Amm-V3 : programme/ressources version 

StableSwapAMM = "5quBtoiQqxF9Jv6KYKctB59NT3gtJD2Y65kdnB1Uev3h"


#"@solana/web3.js"   API token oauth raydium




# Remplace 'your_api_url' par l'URL d'API à laquelle tu veux te connecter
url = 'your_api_url'

# Si l'API nécessite une clé API ou des tokens, tu les ajoutes ici. Sinon, oust!
headers = {
    'Authorization': 'Bearer your_api_token',
    # 'Autres entêtes': 'Autre valeur'
}

# Un peu comme frapper à la porte avant d'entrer, on fait une requête GET
response = requests.get(url, headers=headers)

# On vérifie si on est les bienvenus (statut 200 OK) ou si c'est porte claquée (error)
if response.status_code == 200:
    # La magie de JSON, tout beau, tout chaud!
    data = response.json()
    print("Voici les données obtenues :")
    print(data)
else:
    # Ah, le doux son de l'échec... musique pour les oreilles de développeurs!
    print(f"Oups! Le serveur a répondu avec une erreur {response.status_code}. Peut-être qu'il a juste un mauvais jour...")

# Un peu de politesse, on ferme la connexion, c'est plus propre.
response.close()