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


tictactoe("bob")