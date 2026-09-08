import random

print("---Bienvenue dans le jeu du devine le nombre !---")

def min_max():
    minimum = int(input("Donner le minimum : "))
    maximum = int(input("Donner le maximum : "))
    return minimum, maximum

def demande_oui_non(question):
    reponse = input(question).strip().lower()
    while reponse != "non" and reponse != "oui":
        print("\nIl faut répondre par oui ou par non")
        reponse = input(question).strip().lower()
    return reponse

def intervalle():
    while True:
        minimum, maximum = min_max()
        while maximum < minimum:
            print("Le maximum ne doit pas être inférieur au minimum.")
            minimum, maximum = min_max()
        reponse = demande_oui_non(question=f"\nL'intervalle que vous avez choisi est de [{minimum} , {maximum}]."
                            " Voulez-vous modifier ?\n")
        if reponse == "non":
            return minimum, maximum

nombre_de_parties = 0

while True:
    minimum, maximum = intervalle()
    nombre_de_parties +=1

    nombre_a_deviner = random.randint(minimum, maximum)

    print(f"Merci d'avoir choisi l'intervalle. J'ai choisi le nombre à deviner entre {minimum} et {maximum}.\n")

    nombre_tentatives = 0
    max_tentatives = int(input("Combien de tentatives voulez-vous avoir pour deviner le nombre ?\n"))

    while nombre_tentatives < max_tentatives:
        try:
            proposition_utilisateur = int(input("\nDevinez le nombre que j'ai choisi : "))
        except ValueError:
            print("La valeur entrée est invalide. Veuillez entrer un nombre.")
            continue

        if proposition_utilisateur < minimum or proposition_utilisateur > maximum:
            print(f"Votre proposition doit être comprise entre {minimum} et {maximum}.")
            continue

        nombre_tentatives += 1
        
        if proposition_utilisateur > nombre_a_deviner:
            print("Trop grand ! Réessayez :)")
        elif proposition_utilisateur < nombre_a_deviner:
            print("Trop petit ! Réessayer :)")
        else:
            print(f"\nFélicitation ! Le nombre que j'ai choisi est bien {nombre_a_deviner} ! Vous l'avez deviner en {nombre_tentatives} tentative(s) !")
            break
    else:
        print(f"\nDésolé, vous avez épuisé vos {nombre_tentatives} tentatives. Le nombre que j'avais choisi était {nombre_a_deviner}.")

    rejouer = demande_oui_non(question="\nVoulez-vous rejouer ?\n")

    if rejouer == "non":
        print(f"Merci d'avoir joué {nombre_de_parties} fois ! À bientôt !")
        break
    else:
        print(f"\n---{nombre_de_parties+1}ème partie---")

    

