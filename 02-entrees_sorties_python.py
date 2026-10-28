age = 0
genre = ''

age = int(input("Quel est votre âge ? "))
genre = input("Quel est votre genre ? ")

if genre == 'homme' or genre == 'Homme' or genre == 'H' or genre == 'h':
    if age >= 18:
        print("Vous êtes un homme majeur.")
    else:
        print("Vous êtes un homme mineur.")
elif genre == 'femme' or genre == 'Femme' or genre == 'F' or genre == 'f':
    if age <= 18:
        print("Vous êtes une femme mineure.")
    else:
        print("Vous êtes une femme majeure.")
else:
    print("Vous n'avez pas renseigné un genre valide.")