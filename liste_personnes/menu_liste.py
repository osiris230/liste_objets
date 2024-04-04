from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao

def menu_liste():
    while True:
        print("\nMenu Liste de personnes.")
        print("1. Ajouter une personne à la liste.")
        print("2. Afficher la liste.")
        print("3. Chercher dans la liste.")
        print("4. Filtrer la liste par age.")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-4): ")

        if choix == '1':
            nom = input("Entrez le nom de la personne : ")
            age = input("Entrez l'âge de la personne : ")
            personne = Personne(nom, age)
            message = ListePersonneDao.ajouter_personne(personne)
            print(message)
            
        elif choix == '2':
            personnes, message = ListePersonneDao.afficher_personne()
            if personnes:
                for personne in personnes:
                    print(f"Nom : {personne[0]}, Age : {personne[1]}")
            else:
                print(message)
        elif choix == '3':
            nom = input("Entrez le nom de la personne à rechercher : ")
            resultats, message = ListePersonneDao.rechercher_personne(nom)
            if resultats:
                    print(f"Nom : {resultats[0]}, Age : {resultats[1]}")
            else:
                print(message)
        elif choix == '4':
            min_age = input("Entrez l'âge minimum : ")
            max_age = input("Entrez l'âge maximum : ")
            resultat, message = ListePersonneDao.filtre_age(int(min_age), int(max_age))
            if resultat:
                for personne in resultat:
                    print(f"Nom : {personne[0]}, Age : {personne[1]}")
            else:
                print(message)
        elif choix == '5':
            print("Au revoir !")
            return
        else:
            print("Choix invalide, veuillez réessayer.")