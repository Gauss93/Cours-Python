import random


symboles = ['pierre', 'papier', 'ciseaux']

joueur = input('Veuillez choisir entre pierre, papier et ciseaux. ')
ia = random.choice(symboles)



if (joueur == 'pierre' and ia == 'ciseaux') or (joueur == 'papier' and ia == 'pierre') or (joueur == 'ciseaux' and ia == 'papier'):
    print(f'Vous avez joué {joueur} et votre adversaire à joué {ia}. Vous avez gagner.')
elif (joueur == 'pierre' and ia =='papier') or (joueur == 'papier' and ia == 'ciseaux') or (joueur == 'ciseaux' and ia == 'pierre'):
    print(f'Vous avez joué {joueur} et votre adversaire à joué {ia}. Vous avez perdu.')
else :
    print(f'Vous avez joué {joueur} et votre adversaire à joué {ia}. Match nul.')

############################################
# CORRECTION
# import random

# symboles = ['pierre', 'papier', 'ciseaux']
# gagnant = {'pierre': 'ciseaux', 'papier': 'pierre', 'ciseaux': 'papier'}

# joueur = input("Veuillez choisir entre pierre, papier et ciseaux : ").lower()

# if joueur not in symboles:
#     print("Choix invalide.")
# else:
#     ia = random.choice(symboles)
#     if joueur == ia:
#         resultat = "Match nul"
#     elif gagnant[joueur] == ia:
#         resultat = "Vous avez gagné"
#     else:
#         resultat = "Vous avez perdu"

#     print(f"Vous avez joué {joueur} et votre adversaire a joué {ia}. {resultat}.")
