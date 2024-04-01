from database import connexion_db
import database as db
from liste_personnes.liste import Personne
class ListePersonneDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass
        

    @classmethod
    def ajouter_personne(cls, per:Personne):
        sql = "INSERT INTO personnes (nom, age) Values (%s,%s)"
        params = (per.nom, per.age)
        try:
            ListePersonneDao.cursor.execute(sql,params)
            ListePersonneDao.connexion.commit()
            ListePersonneDao.cursor.close()
            message = f"Ajout de {per.nom} avec succès."
        except Exception as ex:
            message = "Erreur de l'ajout."
        return message
    
    @classmethod
    def afficher_personne(cls):
        sql = "SELECT * FROM personnes"
        try:
            ListePersonneDao.cursor.execute(sql)
            personnes = ListePersonneDao.cursor.fetchall()
            
            message = "Succes"
        except Exception as ex:
            print(ex)
            personnes = []
            message = "Erreur lors de la récupération des données."
        return personnes, message
    
    @classmethod
    def rechercher_personne(cls, nom):
        sql = "SELECT nom, age FROM personnes WHERE nom = %s"
        try:
            ListePersonneDao.cursor.execute(sql, (nom,))
            resultat = ListePersonneDao.cursor.fetchone()
            ListePersonneDao.cursor.close()
            message = "Success"
        except Exception as ex:
            resultat = []
            message = "Erreur lors de la recherche: "
        return resultat, message
    
    @classmethod
    def filtre_age(cls, min_age, max_age):
        sql = "SELECT nom, age FROM personnes WHERE age BETWEEN %s AND %s"
        try:
            ListePersonneDao.cursor.execute(sql, (min_age, max_age))
            resultat = ListePersonneDao.cursor.fetchall()
            ListePersonneDao.cursor.close()
            message = "Success"
        except Exception as ex:
            resultat = []
            message = "Erreur lors du filtrage par âge."
        return resultat, message
            


liste_personne = ListePersonneDao()
#liste_personne.ajouter_personne("Ginette", 64)
#liste_personne.ajouter_personne("Bob", 52)
liste_personne.afficher_personne()
liste_personne.rechercher_personne("Alice")
liste_personne.filtre_age(53,64)