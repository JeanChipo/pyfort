from random import randint, choice

def factorielle(n:int)->int:
    fact = 1
    for i in range(2,n+2):
        fact *= i-1
    return fact

def epreuve_math_factorielle()->bool:
    n = randint(1,10)
    reponse = int(input(f"calculer la factorielle de {n}"))
    if reponse ==  factorielle(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False

##################################################

def roulette_mathematique(joueur:str)->bool:
    """
    :param joueur: nom du joueur
    :return: le nombre de clés gagnées
    """
    nombres = [randint(1,20) for _ in range(5)]
    op = choice(['+','-','*'])
    print(f"Nombres sur la roulette : {nombres}")

    match op:
        case '+':
            result = 0
            for n in nombres:
                result += n
            print(f"{joueur}, calculez le résultat en combinant ces nombres avec une addition")
        case '-':
            result = 0
            for n in nombres:
                result -= n
            print(f"{joueur}, calculez le résultat en combinant ces nombres avec une soustraction")
        case '*':
            result = 1
            for n in nombres:
                result *= n
            print(f"{joueur}, calculez le résultat en combinant ces nombres avec une multiplication")
        case _:
            result = -1

    reponse = int(input("Votre réponse : "))
    if reponse == result:
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux! Vous perdez la clé.")
    return False
