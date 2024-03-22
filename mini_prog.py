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
        try:
            requete = "INSERT INTO personnes (nom, age) Values (%s,%s)" #(?,?)
            self.cursor.execute(requete, (nom, age))
            self.connexion.commit()
        except mysql.Error:
            print("Erreur de l'ajout.")

    def insert(nom, age):
        sql = "INSERT INTO personnes (nom, age) Values (%s,%s)" #(?,?)
        cursor = mysql.connect().cursor()
        infos =  (cursor.lastrowid, nom, age)
        cursor.execute(sql,infos)

    def afficher_personne(self):
        try:
            self.cursor.execute("SELECT nom, age FROM personnes")
            for (nom, age) in self.cursor:
                print(f"Nom: {nom}, Age: {age}")
        except mysql.Error:
            print("Erreur de l'affichage.")


connexion_params = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'liste_objet'
    }

liste_personne = ListePersonne(connexion_params)
liste_personne.ajouter_personne("Ginette", 64)
liste_personne.ajouter_personne("Bob", 52)
liste_personne.afficher_personne()