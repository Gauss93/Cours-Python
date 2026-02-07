import random

secret = random.randint(0,100)
essais = 0

while True:
    result = int(input('Veuillez choisir un nombre '))
    essais += 1
    if secret > result:
        print("C'est plus.")
    elif secret < result:
        print("C'est moins.")
    else :
        print(f'Bravo ! Vous avez trouvé en {essais} essais')
        break

#########################################
# CORRECTION 
# import random

# secret = random.randint(0, 100)
# essais = 0
# print("J'ai choisi un nombre entre 0 et 100. Devinez-le.")

# while True:
#     try:
#         proposition = int(input("> "))
#     except ValueError:
#         print("Veuillez entrer un nombre valide.")
#         continue

#     essais += 1

#     if proposition < secret:
#         print("C'est plus.")
#     elif proposition > secret:
#         print("C'est moins.")
#     else:
#         print(f"Bravo ! Vous avez trouvé en {essais} essais.")
#         break
