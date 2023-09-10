def Chargerliste(emplacement_liste: str):
    result = []
    file = open(emplacement_liste)
    for elt in file:
        result.append(elt)
    return result

print(Chargerliste("fichier.txt"))
