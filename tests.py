import time

Utilisateurs_DB = {
    879654: {"Age": "57",
    "Ville": "Villeurbanne",
    "Orientation": "Hétéro",
    "Nom": "Roger"}, 
    874426: {"Age": "62",
    "Ville": "Villeurbanne",
    "Orientation": "Hétéro",
    "Nom": "Micheline"}
}

async def send_friend_request_notification(id_recepteur, id_demandeur):
    DicoInfoRecepteur = Utilisateurs_DB[id_recepteur]
    DicoInfoDemandeur = Utilisateurs_DB[id_demandeur]
    await print(f"{DicoInfoRecepteur['Nom']}, {DicoInfoDemandeur['Nom']}, {DicoInfoDemandeur['Age']} ans, qui habite a {DicoInfoDemandeur['Ville']} et qui est {DicoInfoDemandeur['Orientation']} vous demande en ami!")
    await time.sleep(3)

send_friend_request_notification(874426, 879654)
send_friend_request_notification(879654, 874426)