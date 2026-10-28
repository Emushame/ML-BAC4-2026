# Vérification de la saisie d'un nombre
# Indication si le nombre est positif ou negatif et/ou zero

# declaration des variables
nombre = 0

# Demander de saisir un nombre
nombre = int(input("Veuillez saisir un nombre : "))

# Vérification si le nombre est positif, négatif ou zéro

if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est zéro.")