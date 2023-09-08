from typing import Any
import selfcord
import discord

# 'class' sert essentiellement a regrouper des fonctions, ici on en crée une pour le bot
class GiveawayFarmerBot(discord.Client):
    
    async def on_ready(self):
        '''
        Cette fonction est appelée dès que le login est validée et que le bot est "prêt"
        '''
        print("Enregistré en tant que: ", self.user)
    
    async def on_message(message):
        '''
        Cette fonction est appelée dès que le bot recoit un message
        '''
        #Crée une liste de tout les bouts de message susceptibles d'indiquer qu'on a gagner un giveaway
        WonGiveawayMsgParts = ["giveaway", "won", "congrats", "congratulations", "bravo", "gg", "gagner", "gagné"]
        
        # Si un bout de message susceptibles d'indiquer qu'on a gagner un giveaway est dans le contenu du message
        if any(WonGiveawayMsgParts in message.content): 
            # Envoyer le message dans le terminal en lui indiquant l'auteur du message et son contenu
            print(f"Vous avez (peut être) gagner un giveaway! Nouveau message de {message.author}: {message.content}")

# Facon de créer une boucle qui s'éxécute jusqu'a ce qu'elle soit arreter par le code avec un "break"
# Similaire a dire "Tant que 1 est égal à 1" ou "while True == True", la condition sera vraie tout le temps
while True:
    # Demande a l'utilisateur son token discord
    TOKEN = str(input('Quel est ton token discord? Envoyer "EXIT" pour quitter'))
    
    # Si ce que l'utilisateur vient de rentré est "EXIT"
    if TOKEN == 'EXIT':
        # Arrête notre input loop
        break

    # Si le code dans le bloc du "try" ne fait pas d'erreur, il s'éxècute normallement
    try:
        # Crée une instance du bot et l'éxécute en s'identifiant avec le Token
        client = GiveawayFarmerBot()
        client.run(TOKEN)
    # Mais, si le code renvoie une erreur de login discord (discord.errors.LoginFailure), on appelle ce qu'il y a dans le bloc du "except"
    except discord.errors.LoginFailure as e:
        # Dit a l'utilisateur que le token qu'il vient de rentrer est invalide
        print("Token invalide")
        # Le code va se relancer depuis le début de la boucle