"""
Demander à l'utilisateur la longueur du mot de passe à générer.
Demander si l'utilisateur veut 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nombre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbole = ["&", "~", "'", "(", ")", "-", "_", "^", "@", "#", "{", "}", "[", "]", "|", "\"", "$", "*", "?", ",", ";", ".", ":", "/", "!", "§"]
"""

import random
import string

alphabet = string.ascii_letters
nombre = string.digits
symbole = string.punctuation

def demander_longueur(longueur_mdp):
    while True:
        try:
            longueur_mdp = int(input("Quel sera la longueur du mot de passe à générer ?\n"))
        except ValueError:
            print("Il faut entrer un nombre entier")
            continue

        if longueur_mdp < 0:
            print("Il faut entrer un nombre positif.\n")
        elif 0 < longueur_mdp <= 3:
            print("La longueur du mot de passe ne doit pas être inférieur ou égale à 3.\n")
        else:
            return longueur_mdp

def generer_mot_de_passe(longueur_mdp, mdp):
    mdp = [
        random.choice(alphabet),
        random.choice(nombre),
        random.choice(symbole)
    ]

    mdp += random.choices(alphabet + nombre + symbole, k=longueur_mdp-3)
    random.shuffle(mdp)
    mdp = "".join(mdp)
    return mdp



while True:
    print("\n---Générateur de Mot De Passe---")

    mdp = [
    random.choice(alphabet),
    random.choice(nombre),
    random.choice(symbole)
    ]

    while True:
        try:
            longueur_mdp = int(input("Quel sera la longueur du mot de passe à générer ?\n"))
        except ValueError:
            print("Il faut entrer un nombre entier.\n")
            continue

        if longueur_mdp <= 0:
            print("Il faut entrer un nombre positif.\n")
        elif 0 < longueur_mdp <= 3:
            print("La longueur du mot de passe ne peut pas être inférieur ou égale à 3.\n")
        else:
            break

    mdp += random.choices(alphabet + nombre + symbole, k=longueur_mdp-3)
    random.shuffle(mdp)
    mdp = "".join(mdp)

    print(f"Voici le mot de passe généré : {mdp}\n")

    generer = input("Voulez-vous généré un autre mot de passe ?\n").strip().lower()
    while generer != "oui" and generer != "non":
        print("Veuillez répondre par oui ou par non.\n")
        generer = input("Voulez-vous généré un autre mot de passe ?\n").strip().lower()
    if generer == "non":
        break

