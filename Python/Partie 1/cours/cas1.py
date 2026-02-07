prix = int(input("Quel est le prix de vos articles ?"))
age = int(input("Quel est votre âge ?"))
reduc_1 = 0.7
reduc_2 = 0.85
etud = False

if age < 25 and age >= 18 :
    est_etud = input('Etes vous étudiant ? [o/n]')
    if est_etud == 'o' :
        etud = True

if age < 18 :
    prix = prix * reduc_1
elif age < 25 and etud == True :
    prix = prix * reduc_2
else : 
    prix = prix

print(f'Vous devez payer {prix} euros.')


############################
# CORRECTION
# prix = float(input("Quel est le prix de vos articles ? "))
# age = int(input("Quel est votre âge ? "))

# if age < 18:
#     prix *= 0.7

# elif age < 25:
#     est_etud = input("Êtes-vous étudiant ? [o/n] ").lower()
#     if est_etud == 'o':
#         prix *= 0.85

# print(f"Vous devez payer {prix:.2f} euros.")
