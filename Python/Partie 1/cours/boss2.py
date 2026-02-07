import random

with open('words.txt', 'r') as fichier:
    words = fichier.read().split()

random_word = random.choice(words)
nb_letter = len(random_word)

print(f'Mot choisi aléatoirement, il contient {nb_letter} lettres.')

letter_use = []
life = 10
find = "_" * len(random_word)
liste_affichage = list(find)

while True:

    letter = input('Choississez une lettre : ').lower()

    if len(letter) > 1:
        print('Plusieurs lettres non acceptées!')
    elif letter in letter_use:
        print('Lettre déjà utilisée!')
    elif letter in random_word:
        nb_letter_use = 0
        for i, l in enumerate(random_word):
            if l == letter:
                liste_affichage[i] = letter
                nb_letter_use += 1
        find_modif = "".join(liste_affichage)
        print(f'{nb_letter_use} {letter} trouvés aux endroits suivants :\n{find_modif}')
        letter_use.append(letter)
        if "_" not in find_modif:
            print(f'Vous avez gagné !')
            break
    else:
        print(f'Pas de {letter} dans le mot.')
        letter_use.append(letter)
        life -= 1
        print(f'Il vous reste {life} vies.')
        if life == 0:
            print(f'Vous avez perdu !\nLe mot était {random_word}.')
            break
    print('Lettres utilisées : ' + " ".join(letter_use))
    
#################################################################
#CORRECTION 
# import random

# # Chargement des mots depuis le fichier
# with open('words.txt', 'r') as fichier:
#     mots = fichier.read().split()

# # Choix aléatoire du mot
# mot_secret = random.choice(mots).lower()
# longueur = len(mot_secret)

# print(f"Mot choisi aléatoirement, il contient {longueur} lettres.")

# # Initialisation des variables du jeu
# vies = 10
# lettres_utilisees = []
# mot_affiche = ["_"] * longueur  # liste pour pouvoir modifier les lettres

# # Boucle principale du jeu
# while vies > 0 and "_" in mot_affiche:

#     lettre = input("Choisissez une lettre : ").lower()

#     # --- Validation de l'entrée ---
#     if len(lettre) != 1 or not lettre.isalpha():
#         print("Veuillez entrer une seule lettre valide.")
#         continue

#     if lettre in lettres_utilisees:
#         print("Lettre déjà utilisée.")
#         continue

#     lettres_utilisees.append(lettre)

#     # --- Vérification dans le mot ---
#     if lettre in mot_secret:
#         occurrences = 0
#         for i, l in enumerate(mot_secret):
#             if l == lettre:
#                 mot_affiche[i] = lettre
#                 occurrences += 1

#         print(f"{occurrences} '{lettre}' trouvé(s) :")
#         print("".join(mot_affiche))
#     else:
#         vies -= 1
#         print(f"Pas de '{lettre}' dans le mot.")
#         print(f"Il vous reste {vies} vies.")

#     # Affichage des lettres déjà utilisées
#     print("Lettres utilisées :", " ".join(lettres_utilisees))
#     print("-" * 30)

# # --- Fin du jeu ---
# if "_" not in mot_affiche:
#     print("Vous avez gagné ! 🎉")
# else:
#     print(f"Vous avez perdu. Le mot était : {mot_secret}")
