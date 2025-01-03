from random import choice, randint

def bonneteau():
    """
    Jeu du bonneteau.
    Jeu qui consiste à trouver la bonne réponse parmi 3 possibilités. Le joueur n'a que 2 chances, et à chaque tentative, la bonne réponse est replacée.
    :return: booléen, True si le joueur a gagné, False sinon.
    """
    win = False # initialisation de la win à False car si le joueur ne gagne pas cette valeur ne sera pas modifiée
    print("Dans ce jeu, vous aurez le choix entre 3 options (A, B, C). Il faudra que vous trouviez la bonne proposition. Vous n'aurez que 2 chances, et pour chaque tentative, le bon choix sera replacé aléatoirement.")

    for i in range(2): # boucle du nombre de chances qu'a le joueur de gagner
        bonne_reponse = choice(["A", "B", "C"]) # choix aléatoire de la bonne réponse
        print(f"Vous avez encore {2 - i} chance(s)") # affichage du nombre de chances restantes

        while True: # boucle qui demande en boucle une saisie si elle n'est pas A, B ou C (ce qui évite de perdre une tentative si le joueur fait une erreur de frappe)
            choix = input(f"Veuillez choisir entre les trois options possibles (A, B, C) : ")
            if (len(choix) == 1 and 'A' <= choix <= 'C'):
                break
            else:
                print("Saisie incorrecte")

        if choix == bonne_reponse: # vérifie si le choix du joueur est la bonne réponse
            print("Bravo, vous avez trouvé la bonne réponse") # affichage en cas de victoire
            win = True # changement de win à True pour signifier que le joueur a gagné
            break

    if not win: # affichage de défaite si le joueur ne trouve pas la bonne réponse à toutes ses tentatives
        print("Vous avez perdu")

    return win

def jeu_lance_des():
    """
    Jeu du lancer de dé.
    Jeu qui consiste à lancer un dé, et le premier à tomber sur 6 gagne.
    :return: booléen, True si le joueur gagne, False s'il perd.
    """

    win = None
    for i in range(6): # nombre de tours pour le joueur et le maître
        de = randint(1, 6) # valeur du dé lancé
        if i % 2 == 0: # c'est au tour du joueur quand la valeur de la boucle est paire
            print(f"\nVous avez encore {int((6 - i) / 2)} tentative(s)") # affichage du nombre de tentatives restantes
            exe = input("Appuyez sur Entrée pour lancer votre dé : ") # input qui permet d'afficher le dé uniquement quand le joueur appuie sur Entrée
            print(f"Votre dé est tombé sur {de}") # affichage du résultat du lancer
            if de == 6: # si le dé est égal à 6, le joueur gagne et la boucle s'arrête
                print("Vous avez gagné\n")
                win = True
                break

        else: # c'est au tour du maître quand la valeur de la boucle est impaire
            print(f"\nLe maître joue son dé \nSon dé tombe sur {de}") # affichage du tour du maître et du résultat de son dé
            if de == 6: # si le dé du maître tombe sur 6, la boucle s'arrête et le joueur a perdu
                print("Vous avez perdu\n")
                win = False
    if win == None: # si la valeur de win n'a pas changé, cela veut dire que personne n'a gagné et donc on relance le jeu
        print("Match nul\nLe jeu redémarre")
        return jeu_lance_des()
    else:
        return win

def epreuve_hasard()->None:
    """ Execute une fonction aléatoire du module epreuves_mathematiques """
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = epreuves[randint(0,1)]
    epreuve()