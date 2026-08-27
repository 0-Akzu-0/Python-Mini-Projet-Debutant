def demande_oui_non(question):
        reponse = input(question).strip().lower()
        while reponse not in ["oui", "non"]:
            print("Il faut répondre soit par 'oui' soit par 'non'.")
            reponse = input(question).strip().lower()
        return reponse

def demander_nombre():
    while True:
        try:
            nombre_1 = float(input("Choisissez un nombre :\n"))
            nombre_2 = float(input("Choisissez un deuxième nombre :\n"))
        except ValueError:
            print("La valeur entrée est invalide. Il faut saisir un nombre.")
        else:
            print(f"Vous avez choisi : {nombre_1} et {nombre_2}")
            break
    return nombre_1, nombre_2


print("---CALCULATRICE---")

while True:
    nombre_1, nombre_2 = demander_nombre()

    question = "Voulez-vous modifier ?\n"
    demande = demande_oui_non(question)

    while demande != "non":
        if demande == "oui":
            nombre_1, nombre_2 = demander_nombre()
        demande = demande_oui_non(question)
    

    operateur = input("Choisissez l'opération (+, -, *, /):\n")

    while operateur not in ["+", "-", "*", "/"]:
        print("L'opérateur que vous avez saisi n'est pas valide. Veuillez choisir entre +, -, *, /")
        operateur = input("Choisissez l'opération (+, -, *, /):\n")
    if operateur == "+":
        resultat = nombre_1 + nombre_2
        print(f"Le résultat : {nombre_1} {operateur} {nombre_2} = {resultat}")
    elif operateur == "-":
        resultat = nombre_1 - nombre_2
        print(f"Le résultat : {nombre_1} {operateur} {nombre_2} = {resultat}")
    elif operateur == "*":
        resultat = nombre_1 * nombre_2
        print(f"Le résultat : {nombre_1} {operateur} {nombre_2} = {resultat}")
    elif operateur == "/":
        if nombre_2 == 0:
            print("Erreur : Impossible de diviser par 0.")
        else:
            resultat = nombre_1 / nombre_2
            print(f"Le résultat : {nombre_1} {operateur} {nombre_2} = {resultat}")

    autre_calcul = demande_oui_non(question = "Voulez-vous faire un autre calcul ?\n")

    if autre_calcul == "non":
        break
