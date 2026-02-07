# def minimum(a, b):
#     if a > b:
#         return b
#     else:
#         return a 

# print(minimum(5, 6))
# print(minimum(10, 3))
# print(minimum(8, 8))

#######################################################

# import time

# nb = int(input('Entrez un nombre positif > '))

# if nb <= 0:
#     print('Nombre invalide')
# else:
#     while nb > 0:
#         print(nb)
#         nb -= 2
#         time.sleep(0.3)
#     print('Terminé')

########################################################

# import random

# résultats = []

# for lancer in range(1,9):
#     valeur = random.randint(1,10)
#     print(f'lancer {lancer} : {valeur}')
#     résultats.append(valeur)

# print(résultats)

# sept = 0
# total = 0
# for seven in résultats:
#     total += seven
#     if seven == 7:
#         sept += 1

# moyenne = total / len(résultats)

# print(f'Il y a eu {sept} sept.')
# print(f'La moyenne du tirage est de {moyenne}.')

#########################################################

# phrases = []

# while True :
#     phrase = input('Veuillez entrer une phrase (STOP pour arrêter le programme !) > ')
#     if phrase == 'STOP':
#         break
#     elif len(phrase) < 5:
#         print('Phrase trop courte !')
#     else :
#         phrases.append(phrase)   

# with open('journal.txt', 'a') as fichier:
#     for p in phrases:
#         fichier.write(p + '\n')

# with open('journal.txt', 'r') as fichier:
#     lignes = len(fichier.readlines())

# print(f'Le journal contient {lignes} lignes.')

##########################################################

# eleve = {
#     "nom": "lucas",
#     "classe": "6eC",
#     "notes": []
# }

# numero = 1
# total = 0
# while numero < 4:
#     note = float(input(f'Veuillez me donner la note n°{numero} > '))
#     if note > 20 or note < 0:
#         print('Veuillez entrer une note valide')
#     else:
#         eleve["notes"].append(note)
#         total += note
#         numero += 1

# moyenne = total / len(eleve["notes"])

# print(eleve)
# print(f'La moyenne de {eleve["nom"]} est de {moyenne}.')