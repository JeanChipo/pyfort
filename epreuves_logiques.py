from random import choice,randint


def saisie_joueur(joueur:str) -> tuple:
    """fonction qui demande et vérifie la saisie de l'utilisateur"""
    while True:
        cordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez jouer : ")
        if len(cordoneeX) == 1 and '1' <= cordoneeX <= '3':
            break
        else:
          print("Saisie incorrect")

    cordoneeX = int(cordoneeX) - 1

    while True:
        cordoneeY = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez jouer : ")
        if len(cordoneeY) == 1 and '1' <= cordoneeY <= '3':
            break
        else:
            print("Saisie incorrect")

    cordoneeY = int(cordoneeY) - 1

    saisie_j = (cordoneeX, cordoneeY)
    return saisie_j

def verif_saisie_est_valide(saisie_j:list, plateau:list, player:int) -> bool:
    """fonction qui vérifie si il n'y a rien sur la case jouer par l'utilisatueer et donc si la saisie et cerrecte"""
    if not plateau[saisie_j[0]][saisie_j[1]] == ".": #regarde si il y a le caractère "." au niveau de la case jouer
        if player == 1:
            print("Coup invalide")
        return False
    else:
        return True

def action(plateau:list,player:int,joueur:str) -> list:
    """
    fonction qui appel les fontion précédente et qui permet de placer les pion sur la grille pour le joueur
    permet aussi de donner une saisie au maitre qui est l'adversaire du joureur

    :param player: Le joueur qui joue (1 pour le joueur humain et -1 pour l'ordinateur)
    :param plateau: Le plateau de jeu
    :return: Le plateau de jeu
    """
    if player == 1: # si c'est au tour de l'utilisateur, demande la saisie du joueur, la vérifie et place le pion sur la grille si elle est correcte
        saisie_j = saisie_joueur(joueur)
        if verif_saisie_est_valide(saisie_j, plateau, player) == False: #vérification de la saisie et refait une boucle si la saisie n'est pas correcte
            action(plateau,player)
        else:
            plateau[saisie_j[0]][saisie_j[1]] = "X"

    else: # sais c'est au tour du maitre on le fait jouer aver 75% de chance de faire la saisie la plus optimiser
        for j in ["O", "X"]: #vérifi si il peut gagner puis véifie si il doit défendre
            # vérification des diagonale
            if (plateau[0][0] == plateau[1][1] == j and plateau[2][2] == ".") and randint(1,100) <= 75:
                saisie_j = [2,2]
            elif(plateau[1][1] == plateau[2][2] == j and plateau[0][0] == ".") and randint(1,100) <= 75:
                saisie_j = [0,0]
            elif(plateau[0][0] == plateau[2][2] == j and plateau[1][1] == ".") and randint(1,100) <= 75:
                saisie_j = [1,1]
            elif(plateau[0][2] == plateau[1][1] == j and plateau[2][0] == ".") and randint(1,100) <= 75:
                saisie_j = [2,0]
            elif (plateau[2][0] == plateau[1][1] == j and plateau[0][2] == ".") and randint(1,100) <= 75:
                saisie_j = [0, 2]
            elif (plateau[0][2] == plateau[1][1] == j and plateau[1][1] == ".") and randint(1,100) <= 75:
                saisie_j = [1, 1]
            else:
                s=0
                for i in range(3): #vérification des lignes et des colones
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
                    elif s == 0 and i == 2: # si aucun choix obtimiser n'est trouvée le maitre jouera a un endroit aléatoir
                        saisie_j = [choice([0,2]), choice([0,2])]


        if verif_saisie_est_valide(saisie_j, plateau, player) == False: # vérifie si la saisie du maitre est correcte
            action(plateau, player)
        else: # si le maitre jouer une saisie correcte, placement du pion sur la grille
            plateau[saisie_j[0]][saisie_j[1]] = "O"
            print("Le maitre a joué")
    return plateau



def verif_win(plateau:list,player:str)-> int:
    """ vérifie si quelqu'un a ganier ou si il y a égalité"""
    if player == 1:
        X = "X"
    else:
        X = "O"
    if (plateau[0][0] == plateau[1][1] == plateau[2][2] == X) or (plateau[0][2] == plateau[1][1] == plateau[2][0] == X): #regarde si le joueeur ou le maitre a gagner sur une diagonale
        return player
    for i in range(3):
        if (plateau[i][0] == plateau[i][1] == plateau[i][2] == X) or (plateau[0][i] == plateau[1][i] == plateau[2][i] == X): #regarde si le joueeur ou le maitre a gagner sur une ligne ou une colone
            return player
    egal = 0
    for i in range(3): #vérifie si tout les case sont occupé
        for j in range(3):
            if plateau[i][j] != "." :
                egal += 1
    if egal == 9: #vérifie si il y a une égalitée
        return 10
    return 0



def tictactoe(joueur):
    """
    Créer un jeu de Tic-Tac-Toe avec une fonction pour jouer et une fonction pour vérifier la victoire

    :param joueur: Le nom du joueur
    :return: epreuve gagner ou perdu avec True or False
    """
    plateau = [[".",".","."],[".",".","."],[".",".","."]]

    #esécution du tout les fonction
    jeu = 0
    player = choice([1,-1])
    while jeu == 0: #boucle qui est jouer tant que le jeu n'est pas fini
        for i in range(3): #affichage de la grille
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i!= 2:
                print("──┼───┼──")

        player = player * -1 #changement de joueur a chaque ligne
        plateau = action(plateau,player,joueur) #modifie la grille en fontion de la saisie du joueur
        jeu = verif_win(plateau,player) # vérifie si le jeux est fini et renvoie qui est le gagnant (1 pour le joueur, -1 pour le maitre, 10 si c'est une égalitée

    #regarde qui a gagner et affiche le nom du gagnant
    if jeu == 1:
        print("Vous avez gagner")
        return True
    elif jeu == -1:
        for i in range(3):
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i!= 2:
                print("──┼───┼──")
        print("Vous avez perdu")
        return False
    else:
        for i in range(3):
            print(f"{plateau[i][0]} │ {plateau[i][1]} │ {plateau[i][2]}")
            if i!= 2:
                print("──┼───┼──")
        print("Egalité, pour déterminer le gagnant une autre partie va être jouée")
        tictactoe(joueur)






# début de la bataille navale


def saisie_joueuer(joueur:int, plateau_joueur:list, player:int) -> list : #fonction qui demande les placements des bateaux au joueur et place les bateaux du maitre
    if player == 0: # affiche les bateau que le joueur va devoir placer
        print("vous devez choisir ou vous allez placer vos 5 bateau")
        print("1        2       3       4       5\n")
        print("X        #       §       Y       O")
        print("X        #       §       Y       O")
        print("X        #       §       Y  ")
        print("X        # ")
        print("X")

    for i in range(1, 6):
        match i:
            case 1: r = 5
            case 2: r = 4
            case 3: r = 3
            case 4: r = 3
            case 5: r = 2
            case _: r = 0

        if player == 0:
            coup = saisie(joueur, i) # met dans coup les information de saisie du joueur
        else:
            coup = [randint(0, 9), randint(0, 9), choice(["droite", "gauche", "bas", "haut"])] # choisie de manière random comme serons placer les bateau du maitre
        verif = verif_bateau(plateau_joueur, coup, r, player) # regarde si les saisie sont possible
        while verif == 1: # tant que la saisie n'est pas possible on redemande au joueur de saisire son choix ou on relance l'aléatoire du maitre
            if player == 0:
                coup = saisie(joueur, i)
            else:
                coup = [randint(0, 9), randint(0, 9), choice(["droite", "gauche", "bas", "haut"])]
            verif = verif_bateau(plateau_joueur, coup, r, player)
        plateau_joueur = modif_table(plateau_joueur, coup, r, i) # maintenant que on sais que la sisie est bonne on place le bateau sur le plateau du joueur ou du maitre
        if player == 0:
            printable(plateau_joueur,0) # affiche ou en est le plateau
    return plateau_joueur # on renvoie le plateau du joueur ou du maitre


def printable(plateau_joueur:list ,plateau_deux:list or int) -> None: #fonction qui permet l'affichage du(des) plateau(x)
    if plateau_deux != 0: # print deux plateaux si on en demande deux
        print("     votre tableau de coup                                                        votre tableau avec vos bateau                        ")
        for k in range(9, -1, -1):
            if k != 9:
                print("─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼────                   ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼────")
            print(
                f"  {plateau_joueur[k][0]}  │  {plateau_joueur[k][1]}  │  {plateau_joueur[k][2]}  │  {plateau_joueur[k][3]}  │  {plateau_joueur[k][4]}  │  {plateau_joueur[k][5]}  │  {plateau_joueur[k][6]}  │  {plateau_joueur[k][7]}  │  {plateau_joueur[k][8]}  │  {plateau_joueur[k][9]}                      {plateau_deux[k][0]}  │  {plateau_deux[k][1]}  │  {plateau_deux[k][2]}  │  {plateau_deux[k][3]}  │  {plateau_deux[k][4]}  │  {plateau_deux[k][5]}  │  {plateau_deux[k][6]}  │  {plateau_deux[k][7]}  │  {plateau_deux[k][8]}  │  {plateau_deux[k][9]}  ")
        print()
    else: # print un seul plateau si on en a que un
        for k in range(9, -1, -1):
            if k != 9:
                print("─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼────")
            print(
                f"  {plateau_joueur[k][0]}  │  {plateau_joueur[k][1]}  │  {plateau_joueur[k][2]}  │  {plateau_joueur[k][3]}  │  {plateau_joueur[k][4]}  │  {plateau_joueur[k][5]}  │  {plateau_joueur[k][6]}  │  {plateau_joueur[k][7]}  │  {plateau_joueur[k][8]}  │  {plateau_joueur[k][9]}")
        print()


def saisie(joueur:int, i:int) -> list: #fonction qui demande la saisie de placement des bateau au joueur et vérifie que ce sont bien les caractère demander
    while True: # vérification si le caractère est bien un cractète qui peut etre transformer en entier et qui est compris entre 1 et 10
        cordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez mettre l'arrière de votre bateau {i} : ")
        if (len(cordoneeX) == 1 and '1' <= cordoneeX <= '9') or cordoneeX == "10":
            cordoneeX = int(cordoneeX) - 1
            break
        else:
            print("Saisie incorrect")
    while True: # vérification si le caractère est bien un cractète qui peut etre transformer en entier et qui est compris entre 1 et 10
        cordoneeY = input(
            f"{joueur} veuillez saisir la colonne dans laquelle vous voulez mettre l'arrière de votre bateau {i} : ")
        if (len(cordoneeY) == 1 and '1' <= cordoneeY <= '9') or cordoneeY == "10":
            cordoneeY = int(cordoneeY) - 1
            break
        else:
            print("Saisie incorrect")
    while True: # vérification si le joueur saisie bien une direction ("haut","bas","droite","gauche")
        turn = input(
            f"{joueur} veuillez saisir si vous ou vous voulez que votre bateau pointe (haut, bas, droite, gauche) : ")
        if turn == "haut" or turn == "bas" or turn == "droite" or turn == "gauche":
            break
        else:
            print("Saisie incorrect")

    coup = [cordoneeX, cordoneeY, turn] # met dans coup tout les information du joueur
    return coup


def verif_bateau(plateau_joueur:list, coup:list, r:int, player:int): # vérifi si le bateau peut etre placer a l'endroit désirer ( si in le dépace pas du plateau et si il n'est pas sur un autre bateau )
    verif = 0
    for j in range(r):
        if coup[2] == "droite": # si l'utilisateur a saisie "droite", tout les n case du coter de la saise son vérifier si elle sont bien libre et dans le tableau
            if 0 <= coup[1] + j < 10 and verif == 0:
                if plateau_joueur[coup[0]][coup[1] + j] != "~" and verif == 0: #parcours les case n case vers la droite de la taille du bateau placer
                    if player == 0:
                        print("Saisie incorrect")
                    verif = 1
            elif verif == 0:
                if player == 0:
                    print("Saisie incorrect")
                verif = 1

        elif coup[2] == "gauche":# si l'utilisateur a saisie "gauche", tout les n case du coter de la saise son vérifier si elle sont bien libre et dans le tableau
            if 0 <= coup[1] - j < 10 and verif == 0:
                if plateau_joueur[coup[0]][coup[1] - j] != "~" and verif == 0:
                    if player == 0:
                        print("Saisie incorrect")
                    verif = 1
            elif verif == 0:
                if player == 0:
                    print("Saisie incorrect")
                verif = 1

        elif coup[2] == "bas":# si l'utilisateur a saisie "bas", tout les n case du coter de la saise son vérifier si elle sont bien libre et dans le tableau
            if 0 <= coup[0] - j < 10 and verif == 0:
                if plateau_joueur[coup[0] - j][coup[1]] != "~" and verif == 0:
                    if player == 0:
                        print("Saisie incorrect")
                    verif = 1
            elif verif == 0:
                if player == 0:
                    print("Saisie incorrect")
                verif = 1

        elif coup[2] == "haut":# si l'utilisateur a saisie "haut", tout les n case du coter de la saise son vérifier si elle sont bien libre et dans le tableau
            if 0 <= coup[0] + j < 10 and verif == 0:
                if plateau_joueur[coup[0] + j][coup[1]] != "~" and verif == 0:
                    if player == 0:
                        print("Saisie incorrect")
                    verif = 1
            elif verif == 0:
                if player == 0:
                    print("Saisie incorrect")
                verif = 1
    return verif # si l'une des vérification n'est pas bonne on renvoie 1 pour dire de redemander la saisie


def modif_table(plateau_joueur, coup, r, i): # fonction qui place les bateau sur la grille
    match i: # regarde quel bateau est placer et choisie par quel caractère il va symboliser le bateau
        case 1: truc = "X"
        case 2: truc = "#"
        case 3: truc = "§"
        case 4: truc = "Y"
        case 5: truc = "O"
        case _: truc = "error"

    for j in range(r): # place en parcourant de la bonne disatnce (n la taille du bateau) et avvec la bonne direction et remplace les terme par le simbole du bateau
        if coup[2] == "droite":
            plateau_joueur[coup[0]][coup[1] + j] = truc

        elif coup[2] == "gauche":
            plateau_joueur[coup[0]][coup[1] - j] = truc

        elif coup[2] == "haut":
            plateau_joueur[coup[0] + j][coup[1]] = truc

        elif coup[2] == "bas":
            plateau_joueur[coup[0] - j][coup[1]] = truc
    return plateau_joueur


def coupplayer(plateau_joueur, plateau_maitre, plateau_des_coup, player, joueur, coupavant): # fonction qui permet de faire tirer le joueur ou le bot sur le plateau de l'adverssaire et d'avoir un historique des coups déja jouer
    if player == 1: # si c'est au tour du joueur

        while True: # on demande tant que la sisie n'est pas corcte de resaisie la valeur
            cordoneeX = input(f"{joueur} veuillez saisir la ligne dans laquelle vous voulez tirer: ")
            if (len(cordoneeX) == 1 and '1' <= cordoneeX <= '9') or cordoneeX == "10":
                cordoneeX = int(cordoneeX) - 1
                break
            else:
                print("Saisie incorrect")

        while True: # on demande tant que la sisie n'est pas corcte de resaisie la valeur
            cordoneeY = input(f"{joueur} veuillez saisir la colonne dans laquelle vous voulez tirer: ")
            if (len(cordoneeY) == 1 and '1' <= cordoneeY <= '9') or cordoneeY == "10":
                cordoneeY = int(cordoneeY) - 1
                break
            else:
                print("Saisie incorrect")

        coup = [cordoneeX, cordoneeY] # met les coordoner de la sisie dans une liste


    else: # permet la saisie du maitre
        if not coupavant[2]: # si la case qui a été jouer avant n'a pas toucher de bateau on joue de manière randome
            coup = [randint(0, 9), randint(0, 9)]
        else: # si la case qui a été jouer avant a toucher un bateau

            # si le coup d'encor avant a aussi toucher on tire sur la case dans la continuiter des deux tire d'avant
            if (0 <= coupavant[1] + 1 < 10 and 0 <= coupavant[1] - 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] + 1] != "■" and plateau_joueur[coupavant[0]][coupavant[1] - 1] == "■":
                coup = [coupavant[0],coupavant[1] + 1]
            elif (0 <= coupavant[1] - 1 < 10  and 0 <= coupavant[1] + 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] - 1] != "■" and plateau_joueur[coupavant[0]][coupavant[1] + 1] == "■":
                coup = [coupavant[0],coupavant[1] - 1]
            elif (0 <= coupavant[0] + 1 < 10 and 0 <= coupavant[0] - 1 < 10) and plateau_joueur[coupavant[0] + 1][coupavant[1]] != "■" and plateau_joueur[coupavant[0] - 1][coupavant[1]] == "■":
                coup = [coupavant[0] + 1,coupavant[1]]
            elif (0 <= coupavant[0] - 1 < 10 and 0 <= coupavant[0] + 1 < 10) and plateau_joueur[coupavant[0] - 1][coupavant[1]] != "■" and plateau_joueur[coupavant[0] + 1][coupavant[1]] == "■":
                coup = [coupavant[0] - 1,coupavant[1]]

            # si on a toucher au tire d'avant on tire sur les case autour de la case toucher
            elif (0 <= coupavant[1] + 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] + 1] != "■":
                coup = [coupavant[0],coupavant[1] + 1]
            elif (0 <= coupavant[1] - 1 < 10) and plateau_joueur[coupavant[0]][coupavant[1] - 1] != "■":
                coup = [coupavant[0],coupavant[1] - 1]
            elif (0 <= coupavant[0] + 1 < 10) and plateau_joueur[coupavant[0] + 1][coupavant[1]] != "■":
                coup = [coupavant[0] + 1,coupavant[1]]
            elif (0 <= coupavant[0] - 1 < 10) and plateau_joueur[coupavant[0] - 1][coupavant[1]] != "■":
                coup = [coupavant[0] - 1,coupavant[1]]

            #si on a toucher au coup d'avant mais que aucune condition est vérifier on tire sur une case aléatoir du plateau
            else:
                coup = [randint(0, 9), randint(0, 9)]

    if player == 1: # si c'est le joueur qui joue
        if (coup[0] < 10 or coup[0] >= 0 or coup[1] < 10 or coup[1] >= 0) and plateau_maitre[coup[0]][coup[1]] != "*": # on vérifie qu'il n'a pas déja tirer sur la meme case

            if plateau_maitre[coup[0]][coup[1]] != "~": # si il touche un bateau énemie on lui dit et on place une * dans le plateau de l'historique de ses coup
                print("vous avez toucher")
                bateau = plateau_maitre[coup[0]][coup[1]]
                if est_coule_bateau(plateau_maitre, bateau): # si le coup que le joueur viens de jouer et sur la dernière case d'un bateau, cela signifie que le joueur viens de couler un bateau donc on le dit au joueur
                    print(f"vous avez couler le bateau {bateau} du maitre")
                plateau_des_coup[coup[0]][coup[1]] = "*"

            else: # si le joueur ne touche pas on met 0 dans le plateau de l'historique
                plateau_des_coup[coup[0]][coup[1]] = "O"
            # on actualise le tire sur le plateau du maitre
            plateau_maitre[coup[0]][coup[1]] = "*"

        else: # si le coup a déja été jouer on redemande au joueur de saisire une case possible
            print("vous avez déjà tirée sur cette endroit")
            return coupplayer(plateau_joueur, plateau_maitre, plateau_des_coup, player, joueur, coupavant)

        return [plateau_maitre, plateau_des_coup] # on actualise le plateau du maitre et le plateau de l'historique des coups dans une seul liste pour retourner une seul variable


    # si c'est au tour du maitre
    elif (coup[0] < 10 or coup[0] >= 0 or coup[1] < 10 or coup[1] >= 0) and plateau_joueur[coup[0]][coup[1]] != "■": # soit le coup n'a jamais été jouer et on place le coup
        coupavant[3] = coupavant[3] + 1 # incrémentation du nombre de tentative

        if plateau_joueur[coup[0]][coup[1]] != "~": # si ça a toucher un bateau du joueur
            coupavant = [coup[0],coup[1],True,0] # on réinitialise les contidions qui permette de savoir que le coup d'avant a toucher un bateau

            # on regarde si le coup que on viens de jouer a fini un bateau du joueur et si c'est le cas on dit que le prochain coup devras etre jouer de manière a abandonner l'hypothèse qu'il reste de coup a jouer autour de la ou on viens de tirer
            bateau = plateau_joueur[coup[0]][coup[1]]
            if est_coule_bateau(plateau_joueur, bateau) == True:
                coupavant[2] = False

        # on actualise le plateau du joueur pour qu'il sache ou en est le maitre a tirer pour l'instant
        plateau_joueur[coup[0]][coup[1]] = "■"

        return [plateau_joueur,coupavant] # on actualise le plateau du joueur et on garde en mémoir ou le coup d'avant a été tirer, si il a toucher ou non et si le nombre de tentative de tire tout ça dans une seul liste pour retourner une seul variable
    # si le coup a déja été jouer on incrmente le nombre de tentative et on redemande au maitre de jouer en appelant a nouveux la fonction
    else:
        coupavant[3] = coupavant[3] + 1
        if coupavant[3] == 3:
            coupavant[2] = False
        return coupplayer(plateau_joueur, plateau_maitre, plateau_des_coup, player, joueur, coupavant)


def est_coule_bateau(plateau_joueur, bateau): # fonction qui permet de savoir si il un bateau vien d'etre couler ( car le bateau choisie pour cette fonction est le bateau sur lequel on est en train de tirer )
    count = 0

    # on parcour tout le tableau pour savoir combien de case du bateau il reste en vie
    for i in range(10):
        for j in range(10):
            if plateau_joueur[i][j] == bateau:
                count = count + 1

    # si il ne reste plus que une case du bateau en vie alors on dit que le bateau viens de couler par un return True
    if count == 1 and bateau != '~':
        return True
    # sinon le bateau n'a pas couler donc on return False
    else:
        return False


def est_la_fin(plateau:list) -> bool: # vérifi si quelqu'un a gagner
    verif = True
    # parcour le tabeau et vérifi si il reste des bateau en vie sur le plateau
    for i in range(10):
        for j in range(10):
            if (plateau[i][j] == "O" or plateau[i][j] == "Y" or plateau[i][j] == "§" or plateau[i][j] == "#" or plateau[i][j] == "X") and verif == False: # si il rest un bateau on return True sinon verif n'est pas changer donc on retourne False
                verif = False
    return verif


def bataille_naval(joueur):
    #initialisation des plateaux
    plateau_joueur = [["~" for _ in range(10)] for _ in range(10)]
    plateau_maitre = [["~" for _ in range(10)] for _ in range(10)]
    plateau_des_coup = [["~" for _ in range(10)] for _ in range(10)]

    #placement des bateaux sur les plateaux
    plateau_joueur = saisie_joueuer(joueur, plateau_joueur, 0)
    plateau_maitre = saisie_joueuer(joueur, plateau_maitre, 1)

    coupavant = [0, 0, False, 0] #initialisation d'une mémoire pour les coup du maitre

    player = choice([1, -1]) #choix aléatoire de qui joue en premier

    print("================================================================") # affichage de début de jeu
    print("début du jeu...")

    while True: # boucle de jeux qui joue tant que personne n'a gagner
        player = player * -1 # changement de joueuer chaque boucle

        if player == 1: # si c'est au tour du joueur
            printable(plateau_des_coup,plateau_joueur) # affiche le plateau du joueru et le plateau des endroits ou le joueur a déjà tirer
            temps = coupplayer(plateau_joueur, plateau_maitre, plateau_des_coup, player, joueur, coupavant) # demande ou le joueur veux tirer et vérifi le coup
            plateau_maitre = temps[0] # change le plateau du maitre en fontion du coup du joueur vias la fonction si-dessue
            plateau_des_coup = temps[1] # change le plateau des coup du joueur pour savoir ou le joueur a déjà tirer

            if est_la_fin(plateau_maitre): # vérifie si le joueur a gagner
                printable(plateau_des_coup, plateau_joueur)  # affiche le plateau pour que le joueur vois qu'il a gagner
                print(f"Vous avez gagné {joueur}") # affichage de win
                break # arrète le jeu

        else: # si c'est ou tour du maitre
            temps = coupplayer(plateau_joueur, plateau_maitre, plateau_des_coup, player, joueur, coupavant) # fait tirer le maitre
            plateau_joueur = temps[0] # modifi le plateau du joueur en fonction du coup du maitre
            coupavant = temps[1] # stoque le coup d'avant pour une meilleur adatation du maitre

            if est_la_fin(plateau_joueur): # vérifie si le maitre a gagner
                printable(plateau_des_coup, plateau_joueur) # affiche le plateau pour que le joueur vois qu'il a perdu
                print(f"Vous avez perdu {joueur}") # affichage de lose
                break # arrète le jeu


bataille_naval("bob")
