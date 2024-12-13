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
    entier = True
    nb_de_points = 0
    for e in n:
        if e == '.':    # cas où n est un décimal
            nb_de_points += 1
        else:
            if not(ord('0') <= ord(e) <= ord('9')) or nb_de_points > 1:
                entier = False
                break
    if nb_de_points == 1:
        entier = False
    return entier