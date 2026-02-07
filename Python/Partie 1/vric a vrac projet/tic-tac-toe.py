import math

plateau = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
           ]

def afficher_jeux(plateau):

    for ligne in plateau:
        print("|",end="")
        for case in ligne:
            print(case, end="|")
        print()

    print("-" * 7)

tour_joueur = 0

def ordre_joueur(tour_joueur):
    if tour_joueur % 2 == 0:
        return "X"
    else:
        return "O"
    
def jouer_coup(plateau, ligne, colonne, joueur):

    if plateau[ligne][colonne] == " ":
        nouveau_plateau = [ligne[:] for ligne in plateau]
        nouveau_plateau[ligne][colonne] = joueur
        return nouveau_plateau
    
    return None

def coup_valide(plateau):
    liste_coup = []
    for l in range(len(plateau)):
        for c in range(len(plateau[0])):
            if plateau[l][c] == " ":
                liste_coup.append((l, c))

    return liste_coup

def etat_terminal(plateau):
    for joueur in ["O", "X"]:
        for i in range(3):
            #ligne
            if all(plateau[i][c] == joueur for c in range(3)):
                return joueur

            #colonne
            if all(plateau[l][i] == joueur for l in range(3)):
                return joueur
        
        #diagonal \
        if all(plateau[i][i] == joueur for i in range(3)):
            return joueur
        
        #diagonal /
        if all(plateau[i][2-i] == joueur for i in range(3)):
            return joueur
        
    if not coup_valide(plateau):
        return "draw"
    
    return None
        
def minimax(plateau, maximizing_player):
    etat = etat_terminal(plateau)

    if etat == "O":
        return 10_000
    elif etat == "X":
        return -10_000
    elif etat == "draw":
        return 0
    
    
    if maximizing_player:
        valeur = -math.inf
        for coup in coup_valide(plateau):
            nouveau_plateau = jouer_coup(plateau, *coup, "O")
            valeur = max(valeur, minimax(nouveau_plateau, False))
        return valeur
    else :
        valeur = math.inf
        for coup in coup_valide(plateau):
            nouveau_plateau = jouer_coup(plateau, *coup, "X")
            valeur = min(valeur, minimax(nouveau_plateau, True))
        return valeur
    
def choisir_coup_minimax(plateau):
    meilleur_score = -math.inf
    meilleur_coup = None

    for coup in coup_valide(plateau):
        nouveau_plateau = jouer_coup(plateau, *coup, "O")
        score = minimax(nouveau_plateau, False)

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup

    return meilleur_coup

while True:
    
    afficher_jeux(plateau)

    joueur = ordre_joueur(tour_joueur)

    if joueur == "O":
        
        choix_ia = choisir_coup_minimax(plateau)
        ligne_ia, colonne_ia = choix_ia
        plateau[ligne_ia][colonne_ia] = joueur 
        tour_joueur += 1

        etat = etat_terminal(plateau)
        if etat:
            afficher_jeux(plateau)
            print(f"Le joueur {etat} a gagné !" if etat != "draw" else "Match nul")
            break

    else:

        try :

            ligne = int(input("Veullez choisir sur quelle ligne jouer (0, 1 ou 2): "))
            colonne = int(input("Veuillez choisir sur quelle colonne jouer (0, 1 ou 2) : "))

            if ligne < 0 or ligne > 2:
                print("La ligne choisie n'existe pas !")
            
            elif colonne < 0 or colonne > 2:
                print("La colonne choisie n'existe pas !")

            elif plateau[ligne][colonne] != " ":
                print("La case est déjà prise !")

            else:
                plateau[ligne][colonne] = joueur 
                tour_joueur += 1

            etat = etat_terminal(plateau)
            if etat:
                afficher_jeux(plateau)
                print(f"Le joueur {etat} a gagné !" if etat != "draw" else "Match nul")
                break

        except ValueError:
                print("Ce n'est pas un chiffre !")


