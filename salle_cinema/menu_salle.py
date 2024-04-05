from salle_cinema.reservation import SalleCinema
from salle_cinema.reservation_dao import ReservationDao

def menu_salle():
    while True:
        print("\nMenu Réservations Cinéma")
        print("1. Réserver une place")
        print("2. Afficher les places réservées")
        print("3. Vérifier le nombre de places disponibles")
        print("4. Filtrer les réservations par personne")
        print("5. Annuler les réservations d'une personne")
        print("6. Réserver une place spéciale")
        print("7. Quitter")
        
        choix = input("Choisissez une option: ")

        if choix == "1":
            nom = input("Entrez le nom de la réservation : ")
            place = input("Entrez le numéro de la place à réserver : ")
            reservation = SalleCinema(nom, place, place_speciale=0)
            message = ReservationDao.reserver_place(reservation)
            print(message)
            
        elif choix == "2":
            reservations, message = ReservationDao.afficher_places_reservees()
            print(message)
            for res in reservations:
                print(f"Place réservée : {res[0]}")
            
        elif choix == "3":
            message = ReservationDao.nombre_places_disponibles()
            print(message)
            
        elif choix == "4":
            nom = input("Entrez le nom pour filtrer les réservations : ")
            reservations = ReservationDao.filtrer_reservations_par_personne(nom)
            for res in reservations:
                print(f"Réservation pour {nom}: Place {res[1]}")
            
        elif choix == "5":
            nom = input("Entrez le nom pour annuler toutes les réservations : ")
            message = ReservationDao.annuler_reservation(nom)
            print(message)
            
        elif choix == "6":
            nom = input("Entrez le nom de la réservation : ")
            place_speciale = input("Entrez le numéro de la place spéciale à réserver : ")
            reservation = SalleCinema(nom, place=None, place_speciale=place_speciale)  # Assurez-vous que votre classe SalleCinema peut gérer cela
            message = ReservationDao.reserver_place_speciale(reservation)
            print(message)

        elif choix == "7":
            print("Au revoir !")
            return
        else:
            print("Option invalide. Veuillez choisir une option valide.")
