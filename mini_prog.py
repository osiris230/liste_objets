import mysql.connector as mysql

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonne:
    def __init__(self, connexion_params):
        self.connexion = mysql.connect(**connexion_params)
        self.cursor = self.connexion.cursor()
        self.liste_personne = []

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.liste_personne.append(nouvelle_personne)

    def afficher_personne(self):
        for personne in self.liste_personne:
            personne.afficher()


connexion_params = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'mini_projet'
    }

liste_personne = ListePersonne()
liste_personne.ajouter_personne("Ginette", 64)
liste_personne.ajouter_personne("Bob", 52)
liste_personne.afficher_personne()