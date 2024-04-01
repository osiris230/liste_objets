import database as db
from file_attente.File_attente import File
class FileAttente:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_personne_en_attente(cls, fil:File, prioritaire=False):
        sql = "INSERT INTO fileattente (nom) VALUES (%s)"
        try:
            FileAttente.cursor.execute(sql, (fil.nom,int(prioritaire)))
            FileAttente.connexion.commit()
            etat = "prioritaire" if prioritaire else "normale"
            print(f"{fil.nom} a été ajouté(e) à la file d'attente comme une personne {etat}.")
        except Exception as ex:
            print(f"Erreur lors de l'ajout à la file d'attente: ")
    @classmethod        
    def ajouter_personne_prioritaire(cls,fil:File):
        FileAttente.ajouter_personne_en_attente(fil.nom, prioritaire=True)

    @classmethod
    def supprimer_personne_de_attente(cls):
        sql = "SELECT id, nom FROM fileattente ORDER BY id ASC LIMIT 1"
        sql_suppression = "DELETE FROM fileattente WHERE id = %s"
        try:
            FileAttente.cursor.execute(sql)
            personne = FileAttente.cursor.fetchone()
            if personne:
                id_personne, nom_personne = personne
                
                FileAttente.cursor.execute(sql_suppression, (id_personne,))
                FileAttente.connexion.commit()
                print(f"{nom_personne} a été supprimé(e) de la file d'attente.")
            else:
                print("La file d'attente est vide.")
        except Exception as ex:
            print(f"Erreur lors de la suppression de la file d'attente: ")


#file.ajouter_personne_en_attente("Bob")
#file.ajouter_personne_en_attente("Alice")
#file.supprimer_personne_de_attente()