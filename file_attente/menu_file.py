from file_attente.File_attente import File
from file_attente.File_dao import FileAttente

def menu_file():
    while True:
        print("\nMenu File d'Attente")
        print("1. Ajouter une personne à la file d'attente")
        print("2. Ajouter une personne prioritaire à la file d'attente")
        print("3. Supprimer une personne de la file d'attente")
        print("4. Quitter")
        
        choix = input("Choisissez une option: ")

        if choix == "1":
            nom = input("Entrez le nom de la personne à ajouter à la file d'attente : ")
            nouvelle_personne = File(nom=nom, prioritaire=False)
            message = FileAttente.ajouter_personne_en_attente(nouvelle_personne)
            print(message)

        elif choix == "2":
            nom = input("Entrez le nom de la personne prioritaire à ajouter à la file d'attente : ")
            personne_prioritaire = File(nom=nom, prioritaire=True)
            message = FileAttente.ajouter_personne_prioritaire(personne_prioritaire)
            print(message)
            
        elif choix == "3":
            message = FileAttente.supprimer_personne_de_attente()
            print(message)
            
        elif choix == "4":
            print("Au revoir !")
            return
        else:
            print("Option invalide. Veuillez choisir une option valide.")
