from random import choice,randint

#########################
## Épreuve du morpion  ##
#########################

def saisie_joueur(joueur:str) -> tuple:
    """
    fonction qui demande et vérifie la saisie de l'utilisateur
    :param joueur: nom du joueur à qui il faut jouer
    :return: tuple de coordonnées du coup joué par le joueur
    """
    while True: # vérification que la coordonnée X soit valide
        coordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez jouer : ")
        if len(coordoneeX) == 1 and '1' <= coordoneeX <= '3':
            break
        else:
            print("Merci de saisir un entier entre 1 et 3.")

    while True: # vérification que la coordonnée Y soit valide
        coordoneeY = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez jouer : ")
        if len(coordoneeY) == 1 and '1' <= coordoneeY <= '3':
            break
        else:
            print("Merci de saisir un entier entre 1 et 3.")

    coordoneeX = int(coordoneeX) - 1
    coordoneeY = int(coordoneeY) - 1
    return (coordoneeX, coordoneeY)

def est_saisie_valide(saisie_j:list, plateau:list, player:int) -> bool:
    """
    fonction qui vérifie si il n'y a rien sur la case jouée par l'utilisateur et donc si la saisie et correcte
    :param saisie_j: la saisie du joueur sous forme de tuple (X, Y)
    :param plateau: Le plateau de jeu
    :param player: Le joueur qui joue (1 pour le joueur humain et -1 pour l'ordinateur)
    :return: True si la saisie est correcte, False sinon
    """
    if plateau[saisie_j[0]][saisie_j[1]] != ".": # regarde si il y a le caractère "." au niveau de la case jouée
        if player == 1:
            print("Coup invalide")
        return False
    return True

def action(plateau:list,player:int,joueur:str) -> list:
    """
    Fonction qui appelle les fonctions précédentes et qui permet de placer les pions sur la grille pour le joueur.
    Permet aussi de donner une saisie au maître (qui est l'adversaire du joueur).
    :param player: Le joueur qui joue (1 pour le joueur humain et -1 pour l'ordinateur)
    :param plateau: Le plateau de jeu
    :return: Le nouveau plateau de jeu actualisé
    """
    if player == 1: # si c'est au tour de l'utilisateur, demande la saisie du joueur, la vérifie, et place le pion sur la grille si elle est correcte
        saisie_j = saisie_joueur(joueur)
        if not est_saisie_valide(saisie_j, plateau, player): #vérification de la saisie, refait une itération si la saisie n'est pas correcte
            action(plateau,player)
        else:
            plateau[saisie_j[0]][saisie_j[1]] = "X"

    else: # c'est au tour du maître : il joue avec 75% de chance de faire la saisie la plus optimale.
        for j in ["O", "X"]: # vérifie s'il peut gagner puis vérifie s'il doit défendre.
            # vérification des diagonnales
            if (plateau[0][0] == plateau[1][1] == j and plateau[2][2] == ".") and randint(1,100) <= 75:
                saisie_j = [2,2]
            elif (plateau[1][1] == plateau[2][2] == j and plateau[0][0] == ".") and randint(1,100) <= 75:
                saisie_j = [0,0]
            elif (plateau[0][0] == plateau[2][2] == j and plateau[1][1] == ".") and randint(1,100) <= 75:
                saisie_j = [1,1]
            elif (plateau[0][2] == plateau[1][1] == j and plateau[2][0] == ".") and randint(1,100) <= 75:
                saisie_j = [2,0]
            elif (plateau[2][0] == plateau[1][1] == j and plateau[0][2] == ".") and randint(1,100) <= 75:
                saisie_j = [0, 2]
            elif (plateau[0][2] == plateau[1][1] == j and plateau[1][1] == ".") and randint(1,100) <= 75:
                saisie_j = [1, 1]
            else:
                s = 0
                for i in range(3): #vérification des lignes et des colonnes
                    if plateau[i][0] == plateau[i][1] == j and plateau[i][2] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [i, 2]
                    elif plateau[i][0] == plateau[i][2] == j and plateau[i][1] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [i, 1]
                    elif plateau[i][2] == plateau[i][1] == j and plateau[i][0] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [i, 0]

                    elif plateau[0][i] == plateau[1][i] == j and plateau[2][i] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [2, i]
                    elif plateau[0][i] == plateau[2][i] == j and plateau[1][i] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [1, i]
                    elif plateau[1][i] == plateau[2][i] == j and plateau[0][i] == "." and s == 0 and randint(1,100) <= 75:
                        s = 1
                        saisie_j = [0, i]
                    elif s == 0 and i == 2: # si aucun choix optimale n'est trouvé, le maître jouera à un endroit aléatoire
                        saisie_j = [choice([0,2]), choice([0,2])]


        if not est_saisie_valide(saisie_j, plateau, player): # vérifie si la saisie du maître est correcte
            action(plateau, player)
        else: # si le maître joue une saisie correcte, on place un pion sur la grille
            plateau[saisie_j[0]][saisie_j[1]] = "O"
            print("Le maître a joué.")
    return plateau



def verif_win(plateau:list,player:str)-> int:
    """
    vérifie si quelqu'un a ganier ou si il y a égalité
    :param plateau: Le plateau de jeu
    :param player: Le joueur qui joue (1 pour le joueur humain et -1 pour l'ordinateur)
    :return: 1 si le joueur a gagné, 0 si il y a égalité, -1 si aucun des joueurs n'a gagné
    """
    if player == 1: 
        X = "X"
    else: 
        X = "O"

    # regarde si le joueur ou le maître a gagné sur une diagonale
    if (plateau[0][0] == plateau[1][1] == plateau[2][2] == X) or \
       (plateau[0][2] == plateau[1][1] == plateau[2][0] == X): return player 

    # regarde si le joueeur ou le maître a gagné sur une ligne ou une colonne
    for i in range(3):
        if (plateau[i][0] == plateau[i][1] == plateau[i][2] == X) or \
           (plateau[0][i] == plateau[1][i] == plateau[2][i] == X): return player 

    egalité = 0
    for i in range(3): # vérifie si tout les case sont occupées
        for j in range(3):
            if plateau[i][j] != "." :
                egalité += 1
    if egalité == 9: # vérifie s'il y a une égalité
        return 10
    return 0


def tictactoe(joueur:str)->bool:
    """
    Le joueur et le maître du jeu (IA) s'affrontent dans une partie classique de morpion. 
    Le premier à aligner trois symboles identiques (horizontalement, verticalement, ou en
    diagonale) gagne la partie.
    :param joueur: Le nom du joueur
    :return: True si une clé est gagnée, False sinon
    """
    plateau = [[".",".","."],[".",".","."],[".",".","."]]
    jeu = 0
    player = choice([1, -1])

    while jeu == 0: # boucle qui est executée tant que le jeu n'est pas fini
        for i in range(3): # affichage de la grille
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i != 2:
                print("──┼───┼──")

        player *= -1 #changement de joueur a chaque ligne
        plateau = action(plateau, player, joueur) #modifie la grille en fontion de la saisie du joueur
        jeu = verif_win(plateau, player) # vérifie si le jeux est fini et renvoie qui est le gagnant (1 pour le joueur, -1 pour le maître, 10 si c'est une égalitée

    # regarde qui a gagné et affiche le nom du gagnant
    if jeu == 1:
        print("Correct! Vous gagnez une clé.")
        return True
    elif jeu == -1:
        for i in range(3):
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i!= 2:
                print("──┼───┼──")
        print("Faux! Vous perdez la clé.")
        return False
    else:
        for i in range(3):
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i != 2:
                print("──┼───┼──")
        print("Egalité, pour déterminer le gagnant, une autre partie doit être jouée")
        tictactoe(joueur)


####################################
## Épreuve de la bataille navale  ##
####################################

def saisie_joueur(joueur:int, plateau_joueur:list, player:int) -> list :
    """
    Fonction qui demande à l'utilisateur de placer un bateau et place le bateau du joueur
    :param joueur: le nom du joueur
    :param plateau_joueur: le plateau du joueur
    :param player: le joueur (-1 pour le joueur et 1 pour le maître)
    :return: le plateau avec le bateau placé
    """ 
    if player == 0: # affiche les bateaux que le joueur va devoir placer
        print(
        "Choisissez où placer vos 5 bateaux.\n"
        "   1   │   2   │   3   │   4   │   5  \n"
        "───────┼───────┼───────┼───────┼──────\n"
        "   X   │   #   │   §   │   Y   │   O  \n"
        "   X   │   #   │   §   │   Y   │   O  \n"
        "   X   │   #   │   §   │   Y   │      \n"
        "   X   │   #   │       │       │      \n"
        "   X   │   #   │       │       │      \n"
        )

    for i in range(1, 6):
        match i:
            case 1: long_bateau = 5
            case 2: long_bateau = 4
            case 3: long_bateau = 3
            case 4: long_bateau = 3
            case 5: long_bateau = 2
            case _: long_bateau = 0

        if player == 0:
            coup = saisie(joueur, i)
        else:
            coup = [randint(0, 9), randint(0, 9), choice(["droite", "gauche", "bas", "haut"])] # choisit de manière aléatoire comment sont placés les bateaux du maître
        verif = verif_bateau(plateau_joueur, coup, long_bateau, player) # regarde si les saisie sont possibles
        while verif == 1:   # tant que la saisie n'est pas possible, on redemande au joueur de saisir son choix...
            if player == 0:
                coup = saisie(joueur, i)
            else:           #...ou on relance l'aléatoire du maître si c'est le tour du maître
                coup = [randint(0, 9), randint(0, 9), choice(["droite", "gauche", "bas", "haut"])]
            verif = verif_bateau(plateau_joueur, coup, long_bateau, player)
        plateau_joueur = modif_table(plateau_joueur, coup, long_bateau, i) # maintenant que l'on sait que la saisie est valide, on place le bateau sur le plateau du joueur
        if player == 0:
            afficher_plateau(plateau_joueur,0) # affiche le plateau actualisé
    return plateau_joueur # on renvoie le plateau du joueur ou du maître

def afficher_plateau(plateau_joueur:list ,plateau_deux:list|int) -> None: # fonction qui permet l'affichage du(des) plateau(x)
    if plateau_deux != 0: # affiche deux plateaux si on en demande deux
        print(f"votre tableau de coups : {' '*51} votre tableau avec vos bateaux:")
        for k in range(10):
            n = f"{k+1} "
            if k == 9: n = f"{k+1}"

            if k != 0:
                print("──╫─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────                "+
                      "──╫─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────")
            else:
                print(f"  ║  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │ 10   {' '*15}  ║  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │ 10   \n"+
                      f"══╬═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════{' '*15} ══╬═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════")
            print(f"{n}║  {plateau_joueur[k][0]}  │  {plateau_joueur[k][1]}  │  {plateau_joueur[k][2]}  │  {plateau_joueur[k][3]}  │  {plateau_joueur[k][4]}  │  {plateau_joueur[k][5]}  │  {plateau_joueur[k][6]}  │  {plateau_joueur[k][7]}  │  {plateau_joueur[k][8]}  │  {plateau_joueur[k][9]}                  {n}║  {plateau_deux[k][0]}  │  {plateau_deux[k][1]}  │  {plateau_deux[k][2]}  │  {plateau_deux[k][3]}  │  {plateau_deux[k][4]}  │  {plateau_deux[k][5]}  │  {plateau_deux[k][6]}  │  {plateau_deux[k][7]}  │  {plateau_deux[k][8]}  │  {plateau_deux[k][9]}  ")
        print()
    else: # affiche un seul plateau si on n'a pas de deuxième plateau en entrée
        for k in range(10):
            n = f"{k+1} "
            if k == 9: n = f"{k+1}"

            if k != 0:
                print("──╫─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────")
            else:
                print(f"  ║  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │ 10   \n"+
                       "══╬═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════")
            print(f"{n}║  {plateau_joueur[k][0]}  │  {plateau_joueur[k][1]}  │  {plateau_joueur[k][2]}  │  {plateau_joueur[k][3]}  │  {plateau_joueur[k][4]}  │  {plateau_joueur[k][5]}  │  {plateau_joueur[k][6]}  │  {plateau_joueur[k][7]}  │  {plateau_joueur[k][8]}  │  {plateau_joueur[k][9]}")
        print()


def saisie(joueur:int, i:int) -> list:
    """
    Fonction qui demande la saisie de placement des bateaux au joueur et vérifie que ce sont bien les caractères demandés.
    :param joueur: Le nom du joueur
    :param i: Le numéro du bateau
    :return: La coordonnée du joueur pour placer son bateau sous forme de liste
    """
    while True: # vérification si le caractère est bien un caractère qui peut etre transformer en entier et qui est compris entre 1 et 10
        coordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez mettre l'arrière de votre bateau {i} : ")
        if (len(coordoneeX) == 1 and '1' <= coordoneeX <= '9') or coordoneeX == "10":
            coordoneeX = int(coordoneeX) - 1
            break
        else:
            print("Merci de saisir un entier compris entre 1 et 10 inclus")
    while True: # vérification si le caractère est bien un caractère qui peut être transformer en entier et qui est compris entre 1 et 10
        coordoneeY = input(
            f"{joueur} veuillez saisir la colonne dans laquelle vous voulez mettre l'arrière de votre bateau {i} : ")
        if (len(coordoneeY) == 1 and '1' <= coordoneeY <= '9') or coordoneeY == "10":
            coordoneeY = int(coordoneeY) - 1
            break
        else:
            print("Merci de saisir un entier compris entre 1 et 10 inclus")
    while True: # vérification si le joueur saisie bien une direction ("haut","bas","droite","gauche")
        turn = input(
            f"{joueur} veuillez saisir la direction dont vous voulez que votre bateau pointe (haut, bas, droite, gauche) : ")
        if turn in ["haut", "bas", "droite", "gauche"]: 
            break 
        else:
            print("Merci de chhoisir une direction parmis (haut, bas, droite, gauche) : ")

    coup = [coordoneeX, coordoneeY, turn] # renvoie les informations calculées
    return coup


def verif_bateau(plateau_joueur:list, coup:list, long_bateau:int, player:int)->bool:
    """
    vérifie si le bateau peut être placé à l'endroit désiré (si on le dépace pas du plateau et si il n'est pas sur un autre bateau)
    :param plateau_joueur: Le plateau du joueur
    :param coup: La liste des coordonnées du joueur pour placer son bateau
    :param long_bateau: La longueur du bateau
    :param player: Le numéro du joueur
    :return: True si le bateau peut être placé, False sinon
    """
    verif = False
    for j in range(long_bateau):
        if coup[2] == "droite": # si l'utilisateur a saisi "droite", toutes les n case du coté de la saisie sont vérifiés si elles sont bien libres et dans le tableau
            if 0 <= coup[1] + j < 10 and verif == 0:
                if plateau_joueur[coup[0]][coup[1] + j] != "~" and verif == 0: # parcours les n cases vers la droite de la taille du bateau placé
                    if player == 0:
                        print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                    verif = True
            elif verif == 0:
                if player == 0:
                    print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                verif = True

        elif coup[2] == "gauche": # si l'utilisateur a saisi "gauche", toutes les n case du coté de la saisie sont vérifiés si elles sont bien libres et dans le tableau
            if 0 <= coup[1] - j < 10 and verif == 0:
                if plateau_joueur[coup[0]][coup[1] - j] != "~" and verif == 0:
                    if player == 0:
                        print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                    verif = True
            elif verif == 0:
                if player == 0:
                    print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                verif = True

        elif coup[2] == "haut": # si l'utilisateur a saisi "haut", toutes les n case du coté de la saisie sont vérifiés si elles sont bien libres et dans le tableau
            if 0 <= coup[0] - j < 10 and verif == 0:
                if plateau_joueur[coup[0] - j][coup[1]] != "~" and verif == 0:
                    if player == 0:
                        print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                    verif = True
            elif verif == 0:
                if player == 0:
                    print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                verif = True

        elif coup[2] == "bas": # si l'utilisateur a saisi "bas", toutes les n case du coté de la saisie sont vérifiés si elles sont bien libres et dans le tableau
            if 0 <= coup[0] + j < 10 and verif == 0:
                if plateau_joueur[coup[0] + j][coup[1]] != "~" and verif == 0:
                    if player == 0:
                        print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                    verif = True
            elif verif == 0:
                if player == 0:
                    print("Le bateau ne peut pas être placé à l'endroit désiré, merci de le placer sur un endroit libre sur le plateau.")
                verif = True
    return verif # si l'une des vérifications n'est pas bonne on renvoie 1 pour dire qu'il faut redemander la saisie


def modif_table(plateau_joueur:list, coup:list, long_bateau:int, num_bateau:int)->list:
    """
    Fonction qui place les bateaux sur la grille
    :param plateau_joueur: Le plateau du joueur
    :param coup: La liste des coordonnées du joueur pour placer son bateau
    :param long_bateau: La longueur du bateau
    :param num_bateau: Le numéro du bateau
    :return: Le plateau avec le bateau placé
    """
    match num_bateau: # regarde quel bateau est placé et choisi par quel caractère il va symboliser le bateau
        case 1: symbole_bateau = "X"
        case 2: symbole_bateau = "#"
        case 3: symbole_bateau = "§"
        case 4: symbole_bateau = "Y"
        case 5: symbole_bateau = "O"
        case _: symbole_bateau = "error"

    for j in range(long_bateau): # place en parcourant de la bonne disatnce (n la taille du bateau) et avvec la bonne direction et remplace les terme par le simbole du bateau
        if coup[2] == "droite":
            plateau_joueur[coup[0]][coup[1] + j] = symbole_bateau

        elif coup[2] == "gauche":
            plateau_joueur[coup[0]][coup[1] - j] = symbole_bateau

        elif coup[2] == "bas":
            plateau_joueur[coup[0] + j][coup[1]] = symbole_bateau

        elif coup[2] == "haut":
            plateau_joueur[coup[0] - j][coup[1]] = symbole_bateau
    return plateau_joueur


def coupplayer(plateau_joueur:list, plateau_maître:list, plateau_des_coup:list, player:int, joueur:str, coupavant:list)->list:
    """
    Fonction qui permet de faire tirer le joueur ou le maître sur le plateau de l'adversaire et d'avoir un historique des coups déja joués par le joueur
    :param plateau_joueur: Le plateau du joueur
    :param plateau_maître: Le plateau du maître
    :param plateau_des_coup: Le plateau qui affiche les coups déjà joués
    :param player: Le numéro du joueur (0 ou 1)
    :param joueur: Le nom du joueur
    :param coupavant: Le coup précédent joué par le joueur
    :return: La liste des coordonnées du coup joué
    """
    if player == 1: # si c'est au tour du joueur
        while True: # on demande tant que la saisie n'est pas correcte de resaisir la valeur
            coordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez tirer: ")
            if (len(coordoneeX) == 1 and '1' <= coordoneeX <= '9') or coordoneeX == "10":
                coordoneeX = int(coordoneeX) - 1
                break
            else:
                print("Merci de saisir un entier compris entre 1 et 10 inclus")

        while True: # on demande tant que la saisie n'est pas correcte de resaisir la valeur
            coordoneeY = input(f"{joueur} veuillez saisir la colonne dans laquelle vous voulez tirer: ")
            if (len(coordoneeY) == 1 and '1' <= coordoneeY <= '9') or coordoneeY == "10":
                coordoneeY = int(coordoneeY) - 1
                break
            else:
                print("Merci de saisir un entier compris entre 1 et 10 inclus")

        coup = [coordoneeX, coordoneeY] # met les coordonées de la saisie dans une liste


    else: # permet la saisie du maître
        if not coupavant[2]: # si la case qui a été jouée avant n'a pas touchée de bateau, on joue de manière aléatoire
            coup = [randint(0, 9), randint(0, 9)]
        else: # si la case qui a été jouée avant a touché un bateau
            # si le coup d'encore avant a aussi touché on tire sur la case dans la continuitée des 2 tir d'avant
            if (0 <= coupavant[1] + 1 < 10 and 0 <= coupavant[1] - 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] + 1] != "■" and plateau_joueur[coupavant[0]][coupavant[1] - 1] == "■":
                coup = [coupavant[0],coupavant[1] + 1]
            elif (0 <= coupavant[1] - 1 < 10  and 0 <= coupavant[1] + 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] - 1] != "■" and plateau_joueur[coupavant[0]][coupavant[1] + 1] == "■":
                coup = [coupavant[0],coupavant[1] - 1]
            elif (0 <= coupavant[0] + 1 < 10 and 0 <= coupavant[0] - 1 < 10) and plateau_joueur[coupavant[0] + 1][coupavant[1]] != "■" and plateau_joueur[coupavant[0] - 1][coupavant[1]] == "■":
                coup = [coupavant[0] + 1,coupavant[1]]
            elif (0 <= coupavant[0] - 1 < 10 and 0 <= coupavant[0] + 1 < 10) and plateau_joueur[coupavant[0] - 1][coupavant[1]] != "■" and plateau_joueur[coupavant[0] + 1][coupavant[1]] == "■":
                coup = [coupavant[0] - 1,coupavant[1]]

            # si on a toucher au tir d'avant, on tire sur les cases autour de la case touchée
            elif (0 <= coupavant[1] + 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] + 1] != "■":
                coup = [coupavant[0],coupavant[1] + 1]
            elif (0 <= coupavant[1] - 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] - 1] != "■":
                coup = [coupavant[0],coupavant[1] - 1]
            elif (0 <= coupavant[0] + 1 < 10) and plateau_joueur[coupavant[0] + 1][coupavant[1]] != "■":
                coup = [coupavant[0] + 1,coupavant[1]]
            elif (0 <= coupavant[0] - 1 < 10) and plateau_joueur[coupavant[0] - 1][coupavant[1]] != "■":
                coup = [coupavant[0] - 1,coupavant[1]]

            #si on a toucher au coup d'avant mais que aucune condition n'est vérifiée, on tire sur une case aléatoire du plateau
            else:
                coup = [randint(0, 9), randint(0, 9)]

    if player == 1: # si c'est le joueur qui joue
        if (0 <= coup[0] <= 9 or 0 <= coup[1] <= 9) and plateau_maître[coup[0]][coup[1]] != "●": # on vérifie qu'il n'a pas déja tiré sur la même case
            if plateau_maître[coup[0]][coup[1]] != "~": # on lui dit si il touche un bateau ennemi et on place une boule (●) dans le plateau de l'historique de ses coups
                print("vous avez touché")
                bateau = plateau_maître[coup[0]][coup[1]]
                if est_coule_bateau(plateau_maître, bateau): # si le coup que le joueur a joué et sûr la dernière case d'un bateau, cela signifie que le joueur viens de couler un bateau donc on le dit au joueur
                    print(f"vous avez coulé le bateau {bateau} du maître")
                plateau_des_coup[coup[0]][coup[1]] = "●" 

            else: # si le joueur ne touche pas, on met 0 dans le plateau de l'historique
                plateau_des_coup[coup[0]][coup[1]] = "·"
            # on actualise le tir sur le plateau du maître
            plateau_maître[coup[0]][coup[1]] = "●"

        else: # si le coup a déjà été joué on redemande au joueur de saisir une case possible
            print("vous avez déjà tiré à cet endroit")
            return coupplayer(plateau_joueur, plateau_maître, plateau_des_coup, player, joueur, coupavant)

        return [plateau_maître, plateau_des_coup] # on actualise le plateau du maître et le plateau de l'historique des coups dans une seul liste pour retourner une seul variable


    # si c'est au tour du maître
    elif (coup[0] < 10 or coup[0] >= 0 or coup[1] < 10 or coup[1] >= 0) and plateau_joueur[coup[0]][coup[1]] != "■": # soit le coup n'a jamais été joué et on place le coup
        coupavant[3] = coupavant[3] + 1 # incrémentation du nombre de tentative

        if plateau_joueur[coup[0]][coup[1]] != "~": # si ça a toucher un bateau du joueur            coupavant = [coup[0],coup[1],True,0] # on réinitialise les contidions qui permette de savoir que le coup d'avant a toucher un bateau

            # on regarde si le coup que l'on viens de jouer a coulé un bateau du joueur et si c'est le cas on dit que le prochain coup devras 
            # être jouer de manière à abandonner l'hypothèse qu'il reste des coups à jouer autour de là où l'on viens de tirer
            bateau = plateau_joueur[coup[0]][coup[1]]
            if est_coule_bateau(plateau_joueur, bateau):
                coupavant[2] = False

        # on actualise le plateau du joueur pour qu'il sache où le maître a tiré
        plateau_joueur[coup[0]][coup[1]] = "■"

        return [plateau_joueur,coupavant]   # on actualise le plateau du joueur et on garde en mémoire où le coup d'avant a été tiré, s'il a touché ou non, et si le nombre de tentatives de tir dans une liste pour retourner une seule variable
    else:   # si le coup à déjà été joué on incrémente le nombre de tentative et on redemande au maître de jouer en appelant à nouveau la fonction
        coupavant[3] = coupavant[3] + 1
        if coupavant[3] == 3:
            coupavant[2] = False
        return coupplayer(plateau_joueur, plateau_maître, plateau_des_coup, player, joueur, coupavant)


def est_coule_bateau(plateau_joueur:list, bateau:str)->bool: 
    """
    Fonction qui permet de savoir si un bateau viens de couler (car le bateau choisi 
    pour cette fonction est le bateau sur lequel on est en train de tirer).
    :param plateau_joueur: le plateau du joueur
    :param bateau: le bateau choisi pour la vérification
    :return: booléen indiquant si le bateau est coulé ou non
    """
    count = 0
    for i in range(10):  # on parcours tout le tableau pour savoir combien de cases du bateau est encore en vie
        for j in range(10):
            if plateau_joueur[i][j] == bateau:
                count = count + 1

    # s'il ne reste plus que une case du bateau en vie alors on dit que le bateau viens de couler par un retour de 'True'
    if count == 1 and bateau != '~':
        return True
    else: # sinon le bateau n'a pas couler donc on return False
        return False


def est_la_fin(plateau:list) -> bool: 
    """
    vérifie si quelqu'un a gagné
    :param plateau: le plateau du joueur ou du maître
    :return: booléen indiquant si quelqu'un a gagné ou non    
    """
    verif = True
    # parcours le tabeau et vérifie s'il reste des bateaux en vie sur le plateau
    for i in range(10):
        for j in range(10):
            if plateau[i][j] in ["O", "Y", "§", "#", "X"] and verif == True: # s'il reste un bateau on renvoie 'True' sinon 'verif' n'est pas changé donc on retourne 'False'
                verif = False
    return verif


def la_vraie_bataille_navale(joueur:str)->None:
    """
    fonction principale qui lance le jeu de bataille navale
    :param joueur: le nom du joueur
    """
    #initialisation des plateaux
    plateau_joueur = [["~" for _ in range(10)] for _ in range(10)]
    plateau_maître = [["~" for _ in range(10)] for _ in range(10)]
    plateau_des_coup = [["~" for _ in range(10)] for _ in range(10)]

    #placement des bateaux sur les plateaux
    plateau_joueur = saisie_joueur(joueur, plateau_joueur, 0)
    plateau_maître = saisie_joueur(joueur, plateau_maître, 1)

    #initialisation d'une mémoire pour les coup du maître
    coupavant = [0, 0, False, 0] 
    
    #choix aléatoire de qui est le premier à jouer
    player = choice([1, -1]) 

    # affichage de début de jeu
    print(  "┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐\n"+
            "│Instructions:                                                                                                         │\n"+
            "│    Le joueur place cinq bateaux sur une grille et tente de deviner la position des cinq bateaux                      │\n"+
            "│   de son adversaire (le maître du jeu). Le gagnant est celui qui réussit à toucher tous les bateaux adverses.        │\n"+
            "│   Chaque joueur dispose de deux grilles : une pour la position de ses bateaux et une autre pour enregistrer ses tirs.│\n"+
            "│   Le jeu alterne les tours entre les joueurs, chacun cherchant à toucher les bateaux de l'autre.                     │\n"+
            "│   Le jeu se termine lorsque les deux bateaux d'un joueur sont coulés                                                 │\n"+
            "│                                                                                                                      │\n"+
            "│Symboles:                                                                                                             │\n"+
            "│   - O, Y, §, X : Bateaux du joueur 1 sur le tableau de droite.                                                       │\n"+
            "│   - ● : Tir touché sur plateau du maître du jeu (celui de gauche).                                                   │\n"+
            "│   - · : Tir manqué sur plateau du maître du jeu (celui de gauche).                                                   │\n"+
            "│   - ~ : L'eau.                                                                                                       │\n"+
            "└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘\n"
    )

    while True: # boucle de jeu qui tourne tant que personne n'a gagné
        player = player * -1 # changement de joueur à chaque boucle

        if player == 1: # si c'est au tour du joueur
            afficher_plateau(plateau_des_coup,plateau_joueur) # affiche le plateau du joueur et le plateau des endroits où le joueur à déjà tiré
            temps = coupplayer(plateau_joueur, plateau_maître, plateau_des_coup, player, joueur, coupavant) # demande où le joueur souhaite tirer et vérifie que le coup soir valide
            plateau_maître = temps[0] # change le plateau du maître en fontion du coup du joueur vias la fonction ci-dessus
            plateau_des_coup = temps[1] # change le plateau des coups du joueur pour savoir où le joueur a déjà tiré

            if est_la_fin(plateau_maître): # vérifie si le joueur a gagné
                afficher_plateau(plateau_des_coup, plateau_joueur)  # affiche le plateau pour que le joueur puisse voir qu'il a gagné
                print(f"Vous avez gagné {joueur}!") # affichage de victoire
                return True # le joueur a gagné, fin du jeu

        else: # si c'est au tour du maître
            temps = coupplayer(plateau_joueur, plateau_maître, plateau_des_coup, player, joueur, coupavant) # fait tirer un coup au maître
            plateau_joueur = temps[0] # modifie le plateau du joueur en fonction du coup du maître
            coupavant = temps[1] # stock le coup d'avant pour une meilleur adaptation du maître

            if est_la_fin(plateau_joueur): # vérifie si le maître a gagné
                afficher_plateau(plateau_des_coup, plateau_joueur) # affiche le plateau pour que le joueur puisse voie qu'il a perdu
                print(f"Vous avez perdu {joueur}") # affichage de défaite
                return False # le joueur a perdu, fin du jeu

def epreuve_logique(joueur)->None:
    """ Execute une fonction aléatoire du module epreuves_logiques """
    epreuves = [tictactoe, la_vraie_bataille_navale]
    epreuve = epreuves[randint(0,1)]
    epreuve(joueur)