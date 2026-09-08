# Python_Calculator

Une calculatrice en ligne de commande qui effectue les 4 opérations de base, avec validation des entrées et gestion des erreurs.

## Fonctionalités

- Opérations : addition, soustraction, multiplication, division
- Saisie de deux nombres, avec possibilité de les modifier avant de calculer
- Validation des deux entrées : rejette les valeurs non numériques et les réponses oui/non mal formulées, en rebouclant jusqu'à obtenir une entrée valide
- Gestion de la division par zéro (message d'erreur au lieu d'un crash)
- Possibilité d'enchaîner plusieurs calculs sans relancer le programme

## Comment lancer le programme 

\'\'\'bash
python caculatrice.py
\'\'\'

## Ce que j'ai appris

Ce projet m'a permis de pratiquer :

- **La gestion des erreurs avec try/except** : la saisie des nombres est entourée d'un bloc try/except pour intercepter une 'ValueError' si l'utilisateur tape autre chose qu'un nombre, sans faire planter le programme.
- **La validation par boucle 'while'** : plutôt que de valider une fois, j'ai utilisé des boucles 'while' qui redemandent la saisie tant qu'elle n'est pas valide (pour les réponses oui/non et pour l'opérateur)
- **La factorisation en fonctions** : j'ai remarqué que je demandais une confirmation oui/non à deux endroits différents dans le programme (pour modifier les nombres, et pour relancer un calcul). Plutôt que de dupliquer cette logique, je l'ai extraite dans une fonction 'demande_oui_non' réutilisable.
