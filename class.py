utilisateur = []

    #ajouter une utilisateur
def add_user():
    nom_utilisateur = input("Entrer Votre prenom et nom")
    
    if nom_utilisateur == "":
        print("Le nom de l'utilisateur ne peut pas etre vide")
        return
    