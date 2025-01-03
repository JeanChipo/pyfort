from random import randint, choice

################################
## Fonctions de vérification  ##
################################

def est_entier(n:str)->bool:
    """
    :param n: une chaine de caractères
    :return: True si n est entier, False sinon
    """
    if n == '': return False    # cas où on fait un retour à la ligne (caractère de taille 0)
    if n[0] == '-': n = n[1:]   # cas où n est négatif, on enleve le 1er caractère ('-')
    entier = True
    for e in n:
        if not(ord('0') <= ord(e) <= ord('9')):
            entier = False
            break
    return entier

def est_decimal(n:str)->bool:
    """
    :param n: une chaine de caractères
    :return: True si n est decimal, False sinon
    """
    if n == '': return False    # cas où on fait un retour à la ligne (caractère de taille 0)
    if n[0] == '-': n = n[1:]   # cas où n est négatif, on enleve le 1er caractère ('-')
    decimal = True
    nb_de_points = 0
    for e in n:
        if e == '.':    # cas où n est un décimal
            nb_de_points += 1
        else:
            if not(ord('0') <= ord(e) <= ord('9')) or nb_de_points > 1:
                decimal = False
                break
    return decimal

################################
## Épreuve de la factorielle  ##
################################

def factorielle(n:int)->int:
    """
    :param n: la factorielle à calculer
    :return: le résultat de la factorielle donnée en entrée
    """
    fact = 1
    for i in range(2,n+2):
        fact *= i-1
    return fact

def epreuve_math_factorielle()->bool:
    """
    :return: True si une clé est gagnée, False sinon
    """
    n = randint(1,10)
    reponse = input(f"Calculer la factorielle de {n} : ")
    while not est_entier(reponse):
        reponse = input("Merci de saisir un entier : ")
    if int(reponse) == factorielle(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

#####################################
## Épreuve de l'équation linéaire  ##
#####################################

def resoudre_equation_lineaire()->tuple:
    """
    :return: un tuple de 3 elements contenant a, b, et la solution de l'équation ax+b = 0
    """
    a,b = randint(1,10), randint(1,10)
    return a,b, round(-b/a, 2) #car -b/a est solution de l'equation ax+b=0

def epreuve_math_equation()->bool:
    """
    :return: True si une clé est gagnée, False sinon
    """
    (a,b,x) = resoudre_equation_lineaire()
    reponse = input(f"Résoudre l'équation suivante (si c'est une fraction arrondir à 2 chiffres après la virgule) : {a}x + {b} = 0 : ")
    while not est_decimal(reponse):
        reponse = input("Merci de saisir un entier : ")
    if float(reponse) == float(x):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

###################################
## Épreuve des Nombres Premiers  ##
###################################

def est_premier(n:int)->bool:
    """
    :param n: un entier qu'il faut verifier
    :return: True si n est premier, False sinon
    """
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:  # si un nombre inférieur à n le divise
            return False
    return True

def premier_plus_proche(n:int)->int:
    """
    :param n: un entier premier
    :return: l'entier premier le plus proche de n
    """
    m = n+1
    while m > n :
        if est_premier(m):
            return m
        m += 1

def epreuve_math_premier()->bool:
    """
    :return: True si une clé est gagnée, False sinon
    """
    n = randint(10,20)
    print(f"Épreuve de Mathématiques: Trouver le nombre premier le plus proche de {n}.")

    reponse = input("Votre réponse : ")
    while not est_entier(reponse):
        reponse = input("Merci de saisir un entier : ")
    if int(reponse) == premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

##########################################
## Épreuve de la roulette mathematique  ##
##########################################

def roulette_mathematique()->bool:
    """
    :param: None
    :return: True si une clé est gagnée, False sinon
    """
    nombres = [randint(1,20) for _ in range(5)]
    op = choice(['+','-','*'])
    print(f"Nombres sur la roulette : {nombres}.")

    match op:
        case '+':
            result = 0
            for n in nombres:
                result += n
            print("Calculez le résultat en combinant ces nombres avec une addition.")
        case '-':
            result = nombres[0]
            for n in nombres[1:]:
                result -= n
            print("Calculez le résultat en combinant ces nombres avec une soustraction.")
        case '*':
            result = 1
            for n in nombres:
                result *= n
            print("Calculez le résultat en combinant ces nombres avec une multiplication.")
        case _:
            result = -1

    reponse = input("Votre réponse : ")
    while not est_entier(reponse):
        reponse = input("Merci de saisir un entier : ")
    if int(reponse) == result:
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

######################################################
## Fonction epreuve math (selection d'une épreuve)  ##
######################################################

def epreuve_math()->None:
    """ Execute une fonction aléatoire du module epreuves_mathematiques """
    epreuves = [epreuve_math_factorielle, epreuve_math_equation, epreuve_math_premier, roulette_mathematique]
    epreuve = epreuves[randint(0,3)]
    epreuve()