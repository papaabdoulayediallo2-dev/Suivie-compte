from datetime import datetime
import json

def sauvegarder_users(fichier="USERS.json"):
    # Transformer chaque objet Users en dictionnaire
    data = [u.__dict__ for u in users]
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def id_user():
    if not users:
        return 1
    else:
        return users[-1].id + 1

class Users:
    def __init__(self, id,prenom, nom, telephone, email, motPasse,dateCreation,
                 adress,etat="ACTIF", solde_compte=0, depense=0, ajout=0, derniereConnexion="aucune", premierconnexion=1):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.email = email
        self.motPasse = motPasse
        self.adress = adress
        self.etat = etat
        self.solde_compte = solde_compte
        self.dateCreation = dateCreation
        self.depense = depense
        self.ajout = ajout
        self.derniereConnexion = derniereConnexion
        self.premierconnexion = premierconnexion


def charger_users(fichier="USERS.json"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            # recréer les objets Users à partir des dictionnaires
            return [Users(**d) for d in data]
    except FileNotFoundError:
        return []
    
users = charger_users()   

    
def add_user():
    id = id_user()
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    telephone = int(input("Téléphone : "))
    email = input("Email : ")
    motPasse = input("Mot de passe : ")
    adress = input("Adresse : ")
    dateCreation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    u = Users(id,nom, prenom, telephone, email, motPasse,dateCreation, adress)
    users.append(u)
    sauvegarder_users()
    print(f" Utilisateur ajouté : ID={u.id}, Nom={u.nom}, Date={u.dateCreation}")
    
add_user()

def afficher_users():
    if not users:
        print("Aucun utilisateur enregistré.")
        return
    
    print("\n--- Liste des utilisateurs ---")
    for u in users:
        print(f"ID: {u.id}")
        print(f"Nom: {u.nom}")
        print(f"Prénom: {u.prenom}")
        print(f"Téléphone: {u.telephone}")
        print(f"Email: {u.email}")
        print(f"Adresse: {u.adress}")
        print(f"État: {u.etat}")
        print(f"Solde du compte: {u.solde_compte}")
        print(f"Dépenses: {u.depense}")
        print(f"Ajouts: {u.ajout}")
        print(f"Date de création: {u.dateCreation}")
        print(f"Dernière connexion: {u.derniereConnexion}")
        print(f"Première connexion: {u.premierconnexion}")
        print("-----------------------------")
        
afficher_users()


