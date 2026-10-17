from datetime import datetime
import json

def sauvegarder_users(fichier="USERS.json"):
    # Transformer chaque objet Users en dictionnaire
    data = [u.__dict__ for u in users]
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def id_user():
    if not users:
        return 1
    else:
        return users[-1].id + 1

class Users:
    def __init__(self, id, prenom, nom, telephone, email, motPasse, dateCreation,
                 adress, etat="ACTIF", solde_compte=0,
                 depense=None, ajout=None,
                 derniereConnexion="aucune", premierconnexion=1):
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
        # 🔹 dictionnaires au lieu de simples nombres
        self.depense = depense if depense is not None else []
        self.ajout = ajout if ajout is not None else []
        self.derniereConnexion = derniereConnexion
        self.premierconnexion = premierconnexion

    def ajouter_montant(self, montant):
        """Ajoute un montant avec la date"""
        operation = {
            "montant": montant,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.ajout.append(operation)
        self.solde_compte += montant
        print(f"💰 {montant} ajouté. Nouveau solde : {self.solde_compte}")
    def depenser_montant(self, montant):
        """Enregistre une dépense avec la date"""
        operation = {
            "montant": montant,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.depense.append(operation)
        self.solde_compte -= montant
        print(f"💸 {montant} dépensé. Nouveau solde : {self.solde_compte}")


def charger_users(fichier="USERS.json"):
    try:
        with open(fichier, "r") as f:
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



def connexion(email, motPasse):
    for u in users:
        if u.email == email and u.motPasse == motPasse:
            print(f"✅ Connexion réussie : Bienvenue {u.prenom} {u.nom}")
            u.derniereConnexion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return u
    print("❌ Email ou mot de passe incorrect.")
    return None


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un utilisateur")
        print("2. Se connecter")
        print("3. Afficher tous les utilisateurs")
        print("0. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            add_user()
        elif choix == "2":
            email = input("Email : ")
            motPasse = input("Mot de passe : ")
            u = connexion(email, motPasse)
            if u:
                sous_menu(u)
        elif choix == "3":
            afficher_users()
        elif choix == "0":
            print("👋 Au revoir !")
            break
        else:
            print("Choix invalide.")

def sous_menu(u):
    while True:
        print("\n--- MENU UTILISATEUR ---")
        print("1. Ajouter un montant")
        print("2. Dépenser un montant")
        print("3. Voir solde et historique")
        print("0. Déconnexion")
        choix = input("Votre choix : ")

        if choix == "1":
            montant = int(input("Montant à ajouter : "))
            u.ajouter_montant(montant)
            sauvegarder_users()
        elif choix == "2":
            montant = int(input("Montant à dépenser : "))
            u.depenser_montant(montant)
            sauvegarder_users()
        elif choix == "3":
            print(f"💰 Solde : {u.solde_compte}")
            print("Historique des ajouts :", u.ajout)
            print("Historique des dépenses :", u.depense)
        elif choix == "0":
            print("Déconnexion...")
            break
        else:
            print("Choix invalide.")

menu()