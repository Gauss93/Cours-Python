Nb_animaux = int(input("Combien as-tu d'animaux ? "))
liste = []
num = 0
while True:
    if Nb_animaux > 0:
        num += 1
        animal = input(f"Nom de l'animal n°{num} ")
        liste.append(animal)
        Nb_animaux -= 1
    else :
        break

print(f'Tu as {num} animaux :')

for animal in liste :
    print(f'{liste.index(animal) + 1}) {animal}')

#####################################################
# CORRECTION
# nb_animaux = int(input("Combien as-tu d'animaux ? "))
# animaux = []

# for i in range(1, nb_animaux + 1):
#     nom = input(f"Nom de l'animal n°{i} : ")
#     animaux.append(nom)

# print(f"\nTu as {nb_animaux} animaux :")
# for i, animal in enumerate(animaux, start=1):
#     print(f"{i}) {animal}")

