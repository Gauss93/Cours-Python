contact = {
    "nom": "Jeanne",
    "tel": "0612345678",
    "ville": "Paris"
}

print(f'Nom : {contact['nom']}')
print(f'Téléphone : {contact['tel']}')
print(f'Ville : {contact['ville']}')

profession = input('Entrez la profession : ')
contact["profession"] = profession

print(f'Nom : {contact['nom']}')
print(f'Téléphone : {contact['tel']}')
print(f'Ville : {contact['ville']}')
print(f'Profession : {contact['profession']}')

##################################################
#CORRECTION

# contact = {
#     "nom": "Jeanne",
#     "tel": "0612345678",
#     "ville": "Paris"
# }

# for cle, valeur in contact.items():
#     print(f"{cle.capitalize()} : {valeur}")

# profession = input("Entrez la profession : ")
# contact["profession"] = profession

# print()
# for cle, valeur in contact.items():
#     print(f"{cle.capitalize()} : {valeur}")
