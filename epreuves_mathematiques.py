from random import randint, choice

##################################################

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
    reponse = int(input(f"Calculer la factorielle de {n}"))
    if reponse ==  factorielle(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

##################################################

def roulette_mathematique()->bool:
    """
    :param: None
    :return: True si une clé est gagnée, False sinon
    """
    nombres = [randint(1,20) for _ in range(5)]
    op = choice(['+','-','*'])
    print(f"Nombres sur la roulette : {nombres}")

    match op:
        case '+':
            result = 0
            for n in nombres:
                result += n
            print("Calculez le résultat en combinant ces nombres avec une addition")
        case '-':
            result = 0
            for n in nombres:
                result -= n
            print("Calculez le résultat en combinant ces nombres avec une addition")
        case '*':
            result = 1
            for n in nombres:
                result *= n
            print("Calculez le résultat en combinant ces nombres avec une addition")
        case _:
            result = -1

    reponse = int(input("Votre réponse : "))
    if reponse == result:
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

##################################################

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
    print(x)
    reponse = int(input(f"Résoud l'équation suivante (si c'est une fraction arrondir \
à 2 chiffres après la virgule) : {a}x + {b} = 0 : "))
    if reponse ==  x:
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
    print(f"Épreuve de Mathématiques: Trouver le nombre premier le plus proche de {n}")
    while True:
        reponse = input("Votre réponse: ")
        if '0' <= reponse <= '100':
            reponse = int(reponse)
            break   # réponse valide
        else:   # réponse non valide
          print("Saisie incorrect")
    if reponse == premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False