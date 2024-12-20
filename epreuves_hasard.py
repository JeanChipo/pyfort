from random import choice,randint

def bonneteau():
    """
    Jeu du bonneteau.
    Jeu qui consiste a trouver la bonne réponce entre 3 possibilité, le joueur n'a que 2 chance et a chaque chance la bonne réponce est replacé

    :return: booléen, True si le joueur a gagné, False sinon.
    """
    win = False # initialisation de la win a False car si le joueur ne gagne pas cette valeur ne sera pas modifier
    print("dans ce jeu vous aurez le choix entre 3 choix (A, B, C), il faudra que vous trouviez la bonne proposition, vous n'aurez que 2 chance et pour chaque chance le bon choix sera replacer aléatoirement")

    for i in range(2): # boucle du nombre de chance qu'a le joueur de gagner
        bonne_reponce = choice(["A","B","C"]) # choix aléatoir de la bonne réponce
        print(f"vous avez encor {2 - i} chance") # affichage du nombre de cahnce qu'il reste

        while True: # boucle qui demande en boucle une saisie si elle n'est pas A, B ou C (ce qui évite de pèrdre une tentative au joueur si il fait un erreur de frape)
            choix = input(f"Veuillez choisire entre les trois choix possible (A, B, C) : ")
            if (len(choix) == 1 and 'A' <= choix <= 'C'):
                break
            else:
                print("Saisie incorrect")

        if choix == bonne_reponce: # regarde si le choix du joueur est la  réponce
            print("Bravo vous avez trouvé la bonne réponse") # affichage de win
            win = True # changement de win a True pour signifier que le joueur a gagner
            break

    if not win: # affichage de défète si le joueur ne trouve pas la bonne réponce a tout ses essay
        print("Vous avez perdu")

    return win

def jeu_lance_des():
    """
    jeu du lancer de dé
    Jeu qui consiste a lancer un dé et le premier qui tombe sur 6 gagne

    :return: booléen, True si le joueur gagne et False si il perd
    """

    win = None
    for i in range(6): # nombre de coup du joueur et du maitre
        de = randint(1,6) # valeur du dé lancer
        if i%2 == 0: # c'est au tour du joueur quand la valeur de la boucle est paire
            print(f"\nVous avez encor {int((6-i)/2)} tentative") # affichage du nombre de tentative
            exe = input("appuiler sur entrer pour lancer votre dé : ") # input qui permet d'afficher le dé uniquement quand le joueur apuis sur entré
            print(f"votre dé est tomber sur {de}") # affichage du dé
            if de == 6: # si le dé est égale a 6 le jouer gagner et la boucle s'arrète
                print("vous avez gagné\n")
                win = True
                break

        else: # c'est au tour du maitre quand la valeur de la boucle est impaire
            print(f"\nLe maitre joue son dé \nSon dé tombe sur {de} ") # affichage du tour du maitre et sur quel face son dé est tombé
            if de == 6: # si le dé du maitre tombe sur 6, la boucle s'arrète et le joueur a perdu
                print("vous avez perdu\n")
                win = False
    if win == None: # si la valeur de win n'a pas changer cela veut dire que personne n'a gagné et donc on relance le jeu
        print("Match nul\nLe jeu redémarde")
        return jeu_lance_des()
    else:
        return win
