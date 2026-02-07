import math

plateau = [
    [" ", " ", " "," "," "," "," "],
    [" ", " ", " "," "," "," "," "],
    [" ", " ", " "," "," "," "," "],
    [" ", " ", " "," "," "," "," "],
    [" ", " ", " "," "," "," "," "],
    [" ", " ", " "," "," "," "," "],
]

def afficher_jeu(plateau):

    print(" ", end="")
    for col in range(7):
        print(col, end=" ")
    print()

    for ligne in plateau:
        print("|",end="")
        for case in ligne:
            print(case, end="|")
        print()
    
    print("-" * 15)

tour_joueur = 0

def ordre_joueur(tour_joueur):
    if tour_joueur % 2 == 0:
        return "X"
    else:
        return "O"
    
def adversaire_symbole(joueur):
    adversaire = 'O' if joueur == 'X' else 'X'
    return adversaire 
    

vecteur = {
        "vertical":(+1, 0),
        "horizontal": (0, +1),
        "diag_1": (+1, +1),
        "diag_2": (+1, -1)
    }

def count(plateau, ligne, colonne, joueur, dl, dc):
    win = 0
    l, c = ligne + dl, colonne + dc
    while 0 <= l < len(plateau) and 0 <= c < len(plateau[0]) and plateau[l][c] == joueur:
        win += 1
        l += dl
        c += dc
    return win
    

def get_fenetre(plateau, ligne, colonne, dl, dc):
    fenetre = []
    for i in range(4):
        l = ligne + i*dl
        c = colonne + i*dc
        if not (0 <= l < len(plateau) and 0 <= c < len(plateau[0])):
            return None
        fenetre.append(plateau[l][c])
    return fenetre

def score_fenetre(fenetre, joueur):
    adversaire = "O" if joueur == "X" else "X"

    nb_joueur = fenetre.count(joueur)
    nb_adversaire = fenetre.count(adversaire)

    if nb_adversaire > 0:
        return 0
    if nb_joueur == 4:
        return 1000
    if nb_joueur == 3:
        return 10
    if nb_joueur == 2:
        return 3
    if nb_joueur == 0 and nb_adversaire == 3:
        return -80
    return 0

def score_position(plateau, joueur):
    score = 0
    for l, ligne in enumerate(plateau):
        for c, colonne in enumerate(plateau[l]):
            for dl, dc in vecteur.values():
                fenetre = get_fenetre(plateau, l, c, dl, dc)
                if fenetre is not None:
                    score += score_fenetre(fenetre, joueur)
                if c == 3 and plateau[l][c] == joueur:
                    score += 2

    return score

def score_position_both(plateau, joueur):
    adversaire = "O" if joueur == "X" else "X"
    heuristique = score_position(plateau, joueur) - score_position(plateau, adversaire)
    return heuristique


def jouer_coup(plateau, colonne, joueur):
    if plateau[0][colonne] != " ":
        return None

    nouveau_plateau = [ligne[:] for ligne in plateau]

    ligne = len(plateau) - 1
    while ligne >= 0:
        if nouveau_plateau[ligne][colonne] == " ":
            nouveau_plateau[ligne][colonne] = joueur
            return nouveau_plateau
        ligne -= 1

    return None


def coup_valide(plateau):
    liste_coup = []
    for c in range(len(plateau[0])):
        if plateau[0][c] == " ":
            liste_coup.append(c)

    return liste_coup

def etat_terminal(plateau):
    for l in range(len(plateau)):
        for c in range(len(plateau[0])):
            joueur = plateau[l][c]
            if joueur == " ":
                continue

            for dl, dc in vecteur.values():
                sens_1 = count(plateau, l, c, joueur, dl, dc)
                sens_2 = count(plateau, l, c, joueur, -dl, -dc)
                total = sens_1 + sens_2 + 1

                if total >= 4:
                    return joueur

    if not coup_valide(plateau):
        return "draw"

    return None

def minimax(plateau, profondeur, maximizing_player):
    etat = etat_terminal(plateau)

    if etat == "O":
        return 10_000
    elif etat == "X":
        return -10_000
    elif etat == "draw":
        return 0

    if profondeur == 0:
        return score_position_both(plateau, "O")
    
    if maximizing_player:
        valeur = -math.inf
        for coup in coup_valide(plateau):
            nouveau_plateau = jouer_coup(plateau, coup, "O")
            valeur = max(valeur, minimax(nouveau_plateau, profondeur - 1, False))
        return valeur
    else :
        valeur = math.inf
        for coup in coup_valide(plateau):
            nouveau_plateau = jouer_coup(plateau, coup, "X")
            valeur = min(valeur, minimax(nouveau_plateau, profondeur - 1, True))
        return valeur

def choisir_coup_minimax(plateau, profondeur):
    meilleur_score = -math.inf
    meilleur_coup = None

    for coup in coup_valide(plateau):
        nouveau_plateau = jouer_coup(plateau, coup, "O")
        score = minimax(nouveau_plateau, profondeur - 1, False)

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup

    return meilleur_coup

            
while tour_joueur <= 42:
    
    joueur = ordre_joueur(tour_joueur)
    adversaire = adversaire_symbole(joueur)
    score = score_position_both(plateau, joueur)
    score_X = score_position(plateau, "X")
    score_O = score_position(plateau, "O")

    afficher_jeu(plateau)  
    print(f'La position actuelle pour je joueur X a un score de {score_X}')
    print(f'La position actuelle pour je joueur O a un score de {score_O}')
    print(f'Au tour du joueur {joueur}')

    if joueur == "O":
        colonne_ia = choisir_coup_minimax(plateau, profondeur=4)
        print(f"l'IA choisit la colonne {colonne_ia}")
        ligne = 5

        while ligne >= 0:
            case_vide = plateau[ligne][colonne_ia]
            if case_vide == " ":
                plateau[ligne][colonne_ia] = joueur
                tour_joueur += 1
                break
            else:
                ligne -= 1

        etat = etat_terminal(plateau)
        if etat:
            afficher_jeu(plateau)
            print(f"Le joueur {etat} a gagné !" if etat != "draw" else "Match nul")
        break

    else: 
        valeur = input('Choississez une colonne (0-6) : ')
        try:
            colonne = int(valeur)
            if colonne < 0 or colonne > 6:
                print('Le choix de colonne est invalide')  
            
            elif plateau[0][colonne] != " ":
                print('La colonne est déjà pleine !')
                
            else:
                ligne = 5

                while ligne >= 0:
                    case_vide = plateau[ligne][colonne]
                    if case_vide == " ":
                        plateau[ligne][colonne] = joueur
                        tour_joueur += 1
                        break
                    else:
                        ligne -= 1
                
                
            etat = etat_terminal(plateau)
            if etat:
                afficher_jeu(plateau)
                print(f"Le joueur {etat} a gagné !" if etat != "draw" else "Match nul")
            break


            
        except ValueError:
            print("Ce n'est pas un chiffre !")


















