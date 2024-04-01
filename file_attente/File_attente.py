import mysql.connector as mysql

connexion_params = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'liste_objet'
    }
class FileAttente:
    def __init__(self, connexion_params):
        self.connexion = mysql.connect(**connexion_params)
        self.cursor = self.connexion.cursor()

    def ajouter_personne_en_attente(self, nom, prioritaire=False):
        try:
            requete = "INSERT INTO fileattente (nom) VALUES (%s)"
            self.cursor.execute(requete, (nom,int(prioritaire)))
            self.connexion.commit()
            etat = "prioritaire" if prioritaire else "normale"
            print(f"{nom} a été ajouté(e) à la file d'attente comme une personne {etat}.")
        except mysql.Error:
            print(f"Erreur lors de l'ajout à la file d'attente: ")
            
    def ajouter_personne_prioritaire(self, nom):
        self.ajouter_personne_en_attente(nom, prioritaire=True)

    def supprimer_personne_de_attente(self):
        try:
            # Sélectionner la première personne de la file (FIFO)
            requete_selection = "SELECT id, nom FROM fileattente ORDER BY id ASC LIMIT 1"
            self.cursor.execute(requete_selection)
            personne = self.cursor.fetchone()

            if personne:
                id_personne, nom_personne = personne
                # Supprimer la première personne de la file
                requete_suppression = "DELETE FROM fileattente WHERE id = %s"
                self.cursor.execute(requete_suppression, (id_personne,))
                self.connexion.commit()
                print(f"{nom_personne} a été supprimé(e) de la file d'attente.")
            else:
                print("La file d'attente est vide.")
        except mysql.Error:
            print(f"Erreur lors de la suppression de la file d'attente: ")

file = FileAttente(connexion_params)
#file.ajouter_personne_en_attente("Bob")
#file.ajouter_personne_en_attente("Alice")
#file.supprimer_personne_de_attente()

