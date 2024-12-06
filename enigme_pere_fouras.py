import json
from random import randint

def charger_enigmes(fichier:str)->list[dict]:
    """
    :param fichier: le chemin d'accès au fichier json contenant les énigmes
    :return: une liste de dictionnaires contenus dans le fichier
    """
    with open(fichier, 'r', encoding='utf-8') as file:
        enigmes = json.load(file)
    file.close()
    return enigmes

def enigme_pere_fouras()->bool:
    """
    :parameter: None
    :return: True si une clé est gagnée, False sinon
    """
    print("Père fouras: Voici les 4 définitions, écoutez bien.")
    l = charger_enigmes('./data/enigmesPF.json')
    choix = randint(0,len(l)-1)
    print(l[choix]['question'])
    nb_essai = 3
    while nb_essai > 0:
        reponse = input("Votre réponse : ")
        if reponse.lower() == l[choix]['reponse'].lower():
            print("Père fouras: Bravo ! vous gagnez une clé")
            return True
        else:
            nb_essai -= 1
            if nb_essai == 1 : print(f"Père fouras: Réponse incorrecte, il vous reste {nb_essai} essai") #enlever le pluriel
            else : print(f"Père fouras: Réponse incorrecte, il vous reste {nb_essai} essais")
    print(f"Père fouras: Et non ! la bonne réponse était {l[choix]['reponse']}...",
          "Vous perdez donc la clé.")
    return False