import mysql.connector as mysql

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.liste_personne = []

class ListePersonne:
    def __init__(self, connexion_params):
        self.connexion = mysql.connect(**connexion_params)
        self.cursor = self.connexion.cursor()
        self.liste_personne = []

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.liste_personne.append(nouvelle_personne)
        try:
            sql = "INSERT INTO personnes (nom, age) Values (%s,%s)" #(?,?)
            self.cursor.execute(sql, (nom, age))
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

    def rechercher_personne(self, nom):
        try:
            sql = "SELECT nom, age FROM personnes WHERE nom = %s"
            self.cursor.execute(sql, (nom,))
            resultats = self.cursor.fetchall()
            if resultats:
                for (nom, age) in resultats:
                    print(f"Nom: {nom}, Age: {age}")
            else:
                print("Personne non trouvée.")
        except mysql.Error:
            print("Erreur lors de la recherche: ")

    def filtre_age(self, min_age, max_age):
        try:
            sql = "SELECT nom, age FROM personnes WHERE age BETWEEN %s AND %s"
            self.cursor.execute(sql, (min_age, max_age))
            resultats = self.cursor.fetchall()
            if resultats:
                for (nom, age) in resultats:
                    print(f"Nom: {nom}, Age: {age}")
            else:
                print("Aucune personne trouvée dans cette tranche d'âge.")
        except mysql.Error:
            print("Erreur lors du filtrage: ")


connexion_params = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'liste_objet'
    }

liste_personne = ListePersonne(connexion_params)
#liste_personne.ajouter_personne("Ginette", 64)
#liste_personne.ajouter_personne("Bob", 52)
liste_personne.afficher_personne()
liste_personne.rechercher_personne("Alice")
liste_personne.filtre_age(53,64)