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
        print(f"Nouveau message de {message.author}: {message.content}")
    

# Demande a l'utilisateur son token discord
TOKEN = str(input("Quel est ton token discord?"))

#Crée une instance du bot et l'éxécute en s'identifiant avec le Token
client = GiveawayFarmerBot()
client.run(TOKEN)
