"""
1) Demander à l'utilisateur la longueur du mot de passe à générer.
2) Générer un mot de passe avec d'abord 3 caractères des trois catégories pour garantir la diversité
3) Afficher le mot de passe généré
4) Demander de générer un autre mot de passe ou non

"""

import random
import string

alphabet = string.ascii_letters
nombre = string.digits
symbole = string.punctuation

def demander_longueur():
    while True:
        try:
            longueur_mdp = int(input("Quel sera la longueur du mot de passe à générer ?\n"))
        except ValueError:
            print("Il faut entrer un nombre entier")
            continue

        if longueur_mdp <= 0:
            print("Il faut entrer un nombre positif.\n")
        elif 0 < longueur_mdp <= 3:
            print("La longueur du mot de passe ne doit pas être inférieur ou égale à 3.\n")
        else:
            return longueur_mdp

def generer_mot_de_passe(longueur_mdp):
    mdp = [
        random.choice(alphabet),
        random.choice(nombre),
        random.choice(symbole)
    ]

    mdp += random.choices(alphabet + nombre + symbole, k=longueur_mdp-3)
    random.shuffle(mdp)
    mdp = "".join(mdp)
    return mdp

def demander_continuer():
    reponse = input("Voulez-vous généré un autre mot de passe ?\n").strip().lower()
    while reponse !=  "oui" and reponse != "non":
        print("Veuillez répondre par oui ou par non.\n")
        reponse = input("Voulez-vous généré un autre mot de passe ?\n").strip().lower()
    return reponse == "oui"

def main():
    while True:
        print("\n---Générateur de Mot De Passe---")
        longueur_mdp = demander_longueur()
        mdp = generer_mot_de_passe(longueur_mdp)
        print(f"Voici le mot de passe généré : {mdp}\n")

        if not demander_continuer():
            print("Merci d'avoir utiliser le générateur de mot de passe.")
            break

if __name__ == "__main__":
    main()
