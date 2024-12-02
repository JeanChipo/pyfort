from random import randint, choice

def roulette_mathematique(joueur:str)->int:
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
        print("Bonne réponse! Vous avez gagné une clé.")
        return 1
    else:
        print("Mauvaise réponse! Vous avez perdu la clé.")
        return 0