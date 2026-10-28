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

def emprunter_livre(titre, emprunteur):
    """permet l'emprunt du livre si il est disponible"""
    for livre in bibliotheque:
        if livre["titre"] == titre:
            if livre.get("emprunteur") is None:
                livre["emprunteur"] = emprunteur
                print(f"Le livre '{titre}' a été emprunté par {emprunteur}.")
                return
            else:
                print(f"Le livre '{titre}' est déjà emprunté par {livre['emprunteur']}.")
                return
    print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

def retourner_livre(titre):
    """permet de retourner un livre emprunté"""
    for livre in bibliotheque:
        if livre["titre"] == titre:
            if livre.get("emprunteur") is not None:
                print(f"Le livre '{titre}' a été retourné.")
                del livre["emprunteur"]
                return
            else:
                print(f"Le livre '{titre}' n'est pas emprunté.")
                return
    print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

def supprimer_livre(titre):
    """permet de supprimer un livre de la bibliotheque"""
    for livre in bibliotheque:
        if livre["titre"] == titre:
            bibliotheque.remove(livre)
            print(f"Le livre '{titre}' a été supprimé de la bibliothèque.")
            return
    print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

def modifier_livre(titre, nouveau_titre=None, nouvel_auteur=None, nouvel_editeur=None):
    """permet de modifier les informations d'un livre"""
    for livre in bibliotheque:
        if livre["titre"] == titre:
            if nouveau_titre:
                livre["titre"] = nouveau_titre
            if nouvel_auteur:
                livre["auteur"] = nouvel_auteur
            if nouvel_editeur:
                livre["editeur"] = nouvel_editeur
            print(f"Le livre '{titre}' a été modifié.")
            return
    print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Gallimard")


afficher_livres()