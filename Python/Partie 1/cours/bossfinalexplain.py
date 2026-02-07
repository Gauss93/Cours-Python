# Dimensions du plateau
LIGNES = 6
COLONNES = 7

# Création du plateau vide : chaque ligne est une liste de colonnes
plateau = [[" " for _ in range(COLONNES)] for _ in range(LIGNES)]

# Fonction pour afficher le plateau
def afficher_plateau(plateau):
    # Affichage des indices de colonnes
    print(" ", end=" ")
    for col in range(COLONNES):
        print(col, end=" ")
    print()
    
    # Affichage de chaque ligne
    for ligne in plateau:
        print("|", end="")
        for case in ligne:
            print(case, end="|")
        print()  # Retour à la ligne
    print("-" * (COLONNES * 2 + 1))  # Séparation visuelle

# Test de l'affichage
afficher_plateau(plateau)



