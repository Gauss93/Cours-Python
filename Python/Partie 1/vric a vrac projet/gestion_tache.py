def ajouter_tache(taches, description):
    if not description.strip():
        return False

    taches.append({
        "description": description,
        "done": False
    })
    return True


def afficher_taches(taches):
    if not taches:
        print("Votre liste de tâches est vide.")
        return

    for index, tache in enumerate(taches, start=1):
        statut = "[V]" if tache["done"] else "[ ]"
        print(f"{index}. {statut} {tache['description']}")


def terminer_tache(taches, index):
    if index < 0 or index >= len(taches):
        return False

    if taches[index]["done"]:
        return False

    taches[index]["done"] = True
    return True


MENU = """
---- TO DO ----
1. Ajouter une tâche
2. Afficher les tâches
3. Terminer une tâche
4. Quitter
---------------
"""


def menu():
    taches = []

    while True:
        print(MENU)
        choix = input("Choix : ")

        if choix == "1":
            description = input("Description de la tâche : ")
            if not ajouter_tache(taches, description):
                print("Tâche invalide.")

        elif choix == "2":
            afficher_taches(taches)

        elif choix == "3":
            afficher_taches(taches)
            try:
                numero = int(input("Numéro de la tâche : ")) - 1
                if not terminer_tache(taches, numero):
                    print("Impossible de terminer cette tâche.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == "4":
            print("Au revoir.")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
