import pickle as pk
import os
from aiohttp.client_exceptions import ClientConnectorError
import discord

# 'class' sert essentiellement à regrouper des fonctions, ici on en crée une pour le bot
class GiveawayFarmerBot(discord.Client):
    
    # Définit des attributs de classe, çad des variables accessible avec "self.nom_variable" ex "self.WonGiveawayMsgParts"
    WonGiveawayMsgParts = ["giveaway", "won", "congrats", "congratulations", "bravo", "gg", "gagner", "gagné", "give away"]
    GiveawayChannels = []

    if os.path.exists("GiveawayChannels.pkl"):
        try:
            with open("GiveawayChannels.pkl", "rb") as file:
                GiveawayChannels = pk.load(file)
        except (EOFError, pk.UnpicklingError):
            print("Error loading data from GiveawayChannels.pkl. Using an empty list.")

    async def on_ready(self):
        '''
        Cette fonction est appelée dès que le login est validé et que le bot est "prêt"
        '''
        print(f"Enregistré en tant que: {self.user}")

    async def on_message(self, message):
        '''
        Cette fonction est appelée dès que le bot reçoit un message
        '''

        # Si un bout de message susceptible d'indiquer qu'on a gagné un giveaway est dans le contenu du message
        if any(part in message.content for part in self.WonGiveawayMsgParts):
            # Envoyer le message dans le terminal en lui indiquant l'auteur du message et son contenu
            print(f"Vous avez (peut-être) gagné un giveaway! Nouveau message de {message.author}: {message.content}")

# Façon de créer une boucle qui s'exécute jusqu'à ce qu'elle soit arrêtée par le code avec un "break"
# Similaire à dire "Tant que 1 est égal à 1" ou "while True == True", la condition sera vraie tout le temps
while True:
    # Crée du texte vide pour stocker le token discord de l'utilisateur
    TOKEN = ""
    # Demande a l'utilisateur son entrée dans le terminal
    INPUT = str(input('ENTRER UNE COMMANDE: '))
    # Divise INPUT en list, séparée en fonction des espaces
    INPUT = INPUT.split()

    # Si ce que l'utilisateur vient de rentrer est "EXIT" tout seul
    if INPUT == ['EXIT']:
        # Arrête notre input loop
        break
    # Si le premier mot de INPUT est "LOGIN"
    if INPUT[0] == "LOGIN":
        # Définit le token comme le deuxième mot de INPUT
        TOKEN = INPUT[1]
        # Si le code dans le bloc du "try" ne fait pas d'erreur, il s'exécute normalement
        try:
            # Crée une instance du bot et l'exécute en s'identifiant avec le Token
            client = GiveawayFarmerBot()
            client.run(TOKEN)
        # Mais, si le code renvoie une erreur de login discord (discord.errors.LoginFailure), on appelle ce qu'il y a dans le bloc du "except"
        except discord.errors.LoginFailure as e:
            # Dit à l'utilisateur que le token qu'il vient de rentrer est invalide
            print("Token invalide")
            # Le code va se relancer depuis le début de la boucle donc redemander le token a l'utilisateur et reesayer
        # De même, s'il y a une erreur de connection (ClientConnectorError est spécifique a discord.py-self)
        except ClientConnectorError as e:
            # Dit a l'utilisateur qu'il y a eu une erreur de connection + l'erreur spécifique
            print("Erreur de connection: ", e)
    
    if INPUT[0] == "ADDCHANNEL":
        # Vérifie si le deuxième mot de INPUT est un lien d'une manière rapide mais non infaillible
        if INPUT[1].startswith("https://"):
            # Rajoute le deuxième mot de INPUT a la liste de salon de giveaways
            GiveawayFarmerBot.GiveawayChannels.append(INPUT[1])
            # Sauvegarde la liste du salon de giveaway dans un fichier
            with open("GiveawayChannels.pkl", "wb") as file:
                pk.dump(GiveawayFarmerBot.GiveawayChannels, file)
        # Si la condition du "if" n'est pas respectée
        else:
            # Dit a l'utilisateur que le lien est invalide
            print("Lien invalide")
            
    if INPUT[0] == "CLEARCHANNELS":
        GiveawayFarmerBot.GiveawayChannels = []
        os.remove("GiveawayChannels.pkl")