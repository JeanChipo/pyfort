from random import randint, choice

def resoudre_equation_lineaire():
    """
    :return: un tuple de 3 elements contenant a, b, et la solution de l'équation ax+b = 0
    """
    a,b = randint(1,10), randint(1,10)
    return a,b, round(-b/a,2) #car -b/a est solution de l'equation ax+b=0

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