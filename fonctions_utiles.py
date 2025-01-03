
##########

def bold(text:str)->str:
    return "\033[1m" + text + "\033[0m"

def introduction():
    print(
        bold("🎙️ Denis brognard :") +'\n'
        "Salut tout le monde, et bienvenue dans l’incroyable aventure de Fort Boyard ! \n"
        "Aujourd’hui, nos candidats vont devoir se dépasser pour relever des défis et, surtout, \n"
        "décrocher leur ticket pour la fameuse Salle du Trésor. \n"
        "Rien ne sera facile, mais avec un peu de courage et de stratégie, tout est possible. \n"
        '\n' +
        bold("💡 Les règles, c’est simple :") +'\n'
        "Votre équipe doit gagner 3 clés pour ouvrir les portes de la Salle du Trésor. \n"
        "Pour ça, vous allez affronter différentes épreuves – certaines demanderont de la force, \n"
        "d’autres de la réflexion, et parfois... un brin de folie. À chaque défi, un joueur est choisi pour y aller. \n" 
        "Et si vous réussissez, hop, une clé pour l’équipe ! \n",
        '\n' +
        bold("🔑 Trois clés, et après ?") +'\n'
        "Une fois les trois clés en poche, les portes de la Salle du Trésor s’ouvrent. \n"
        "Mais attention, ce n’est que le début : la vraie chasse au trésor ne commencera qu’une fois à l’intérieur. \n" 
        "Alors, chaque clé compte, et chaque épreuve est un pas de plus vers la victoire. \n",
        '\n' +
        bold("🎉 Allez, c’est parti !") +'\n'
        "Prenez une grande inspiration, serrez les coudes, et donnez tout. \n" 
        "Le Fort est rempli de surprises – certaines sympas, d’autres... un peu moins. \n" 
        "Mais une chose est sûre : vous allez vivre une aventure que vous n’oublierez pas de sitôt ! \n"
        "Prêts ? Alors, que l’aventure commence ! \n"
        )

def composer_equipe()->list[dict]:
    liste_joueurs = []
    n = input("Combien de joueurs se joindrons à l'aventure ? (PS: le bateau ne peut accueillir que 3 joueurs max) : ")
    while not (ord('1') <= ord(n) <= ord('3')):
        n = input("Le bateau doit transporter entre 1 et 3 joueurs. \n"
                  "Merci de saisir un nombre de joueur valide : ")

    leader_present = False
    for i in range(int(n)):
        print(f"Joueur n°{i+1}, nous avons besoin de quelques informations sur vous.")
        nom = input("Quel est votre nom ? \n>")
        profession = input("Quel est votre profession ? \n>")
        if not leader_present :
            leader = input("Etes-vous le leader de l'équipe (V/F) ? \n>")
            while leader != "V" and leader != "F":
                leader = input("Merci de saisir 'V' ou 'F' : ")
            match leader:
                case "V":
                    liste_joueurs.append({"nom":nom, "profession":profession, "est_leader":True, "cles_gagnees":0})
                    leader_present = True
                case "F":
                    liste_joueurs.append({"nom":nom, "profession":profession, "est_leader":False, "cles_gagnees":0})
                    leader_present = False
        else:   # si il y a déjà un leader, on ne redemande pas
            liste_joueurs.append({"nom": nom, "profession": profession, "est_leader": False, "cles_gagnees": 0})

    if not leader_present:
        print(liste_joueurs[0]["nom"] + ", vous êtes le leader de l'équipe puisque personne ne s'est porté volontaire.")
        liste_joueurs[0]["est_leader"] = True

    return liste_joueurs
