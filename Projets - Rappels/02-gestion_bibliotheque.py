'''Gestion d'une petite bibliotheque'''
'''Fonctionnalités suivantes :'''
'''
    - Ajout des livres
    - Liste des livres
    - Emprunter un livre
    - Retourner un livre
    - Suppresion des livres
'''

bibliotheque = []

# creation des fonctions

def ajouter_livre(titre, auteur, editeur): 
    """ajout d'un livre sous forme de dictionnaire dans la bibliotheque"""
    livre = {"titre": titre, "auteur": auteur, "editeur": editeur}
    bibliotheque.append(livre)

    print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")

def afficher_livres():
    """affiche la liste des livres dans la bibliotheque"""
    if not bibliotheque: 
        print("La bibliothèque est vide.")
    else:
        print("Liste des livres dans la bibliothèque :")
        for livre in bibliotheque:
            statut = "Disponible" if livre.get("emprunteur") is None else f"Emprunté par {livre['emprunteur']}"
            print(f"Titre: {livre['titre']}, Auteur: {livre['auteur']}, Editeur: {livre['editeur']}, Statut: {statut}")


#afficher_livres()