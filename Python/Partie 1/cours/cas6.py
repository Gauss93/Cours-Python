import random
import time 
from statistics import mean

liste = []
lancer = 1
while lancer < 11:
    resultat = random.randint(1,6)
    print(f'Lancer {lancer} : {resultat}')
    liste.append(resultat)
    lancer += 1
    time.sleep(0.5)

print(f'Résultats : {liste}')
plus_grand = max(liste)
print(f'Plus grand résultat : {plus_grand}')
moyenne = mean(liste)
print(f'Moyenne : {moyenne}')

####################################################
#CORRECTION
# import random
# import time

# resultats = []

# for lancer in range(1, 11):
#     valeur = random.randint(1, 6)
#     print(f"Lancer {lancer} : {valeur}")
#     resultats.append(valeur)
#     time.sleep(0.5)

# print(f"Résultats : {resultats}")

# # Calcul du max
# max_val = resultats[0]
# total = 0

# for v in resultats:
#     total += v
#     if v > max_val:
#         max_val = v

# moyenne = total / len(resultats)

# print(f"Plus grand résultat : {max_val}")
# print(f"Moyenne : {moyenne}")
