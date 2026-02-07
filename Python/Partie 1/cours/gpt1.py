# prix = float(input('Quel est le prix de vos articles ? '))
# age = int(input('Quel est votre age ? '))

# if age < 16 :
#     prix *= 0.75
# elif age < 23 :
#     est_etudiant = input('Etes vous étudiant ? [o/n] ').lower()
#     if est_etudiant == 'o' :
#         prix *= 0.9

# print(f'Vous devez payer {prix:.2f} euros.')


#####################################################################

# num = int(input('Veuillez entrer un nombre entier. '))

# while num >= 0 :
#     print(num)
#     num -= 1
  
# print('Décollage !')

#####################################################################

# import random 

# ia = random.randint(1,50)
# essais = 5

# while essais > 0:
#     num = int(input('Veuillez deviner le nombre. '))
#     essais -= 1
#     if ia > num:
#         print("C'est plus")
#     elif ia < num:
#         print("C'est moins")
#     else:
#         print('Bravo, vous avez devinez !')
#         break

####################################################################

# articles = int(input("Combien d'article voulez vous ? "))
# liste_articles = []

# for i in range(1, articles + 1):
#     nom = input(f'Nom de votre article n°{i} > ')
#     liste_articles.append(nom)

# print(f'Vous voulez {i} articles ')
# for i, article in enumerate(liste_articles, start=1):
#     print(f'{i}- {article}')