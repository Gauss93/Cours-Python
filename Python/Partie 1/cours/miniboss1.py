plateau = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]

tour_joueur = 0


def afficher_jeu(plateau):

    print(" ", end="")
    print()

    for ligne in plateau:
        print("|",end="")
        for case in ligne:
            print(case, end="|")
        print()
    
    print("-" * 7)


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