liste = []
name = ''
while name != 'STOP':
    name = input('Entrez une phrase (STOP pour finir) : ')
    liste.append(name)
    with open("journal.txt", "a") as fichier:
        fichier.write(f'{name}\n')

with open("journal.txt", "r") as entre:
    nb_entre = len(entre.readlines())

print('Journal mis à jour !')
print(f"Nombre total d'entrées : {nb_entre}")

######################################################
#CORRECTION
# phrases = []

# while True:
#     phrase = input("Entrez une phrase (STOP pour finir) : ")
#     if phrase == "STOP":
#         break
#     phrases.append(phrase)

# with open("journal.txt", "a") as fichier:
#     for p in phrases:
#         fichier.write(p + "\n")

# with open("journal.txt", "r") as fichier:
#     nb_entrees = len(fichier.readlines())

# print("Journal mis à jour !")
# print(f"Nombre total d'entrées : {nb_entrees}")
