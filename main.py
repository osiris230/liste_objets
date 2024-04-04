from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao
from liste_personnes.menu_liste import menu_liste
from file_attente.File_attente import File
from file_attente.File_dao import FileAttente
from file_attente.menu_file import menu_file
from salle_cinema.reservation import SalleCinema
from salle_cinema.reservation_dao import ReservationDao
from salle_cinema.menu_salle import menu_salle


def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Gestion de la file d'attente")
        print("2. Gestion de la liste")
        print("3. Gestion des réservations")
        print("4. Quitter")
        choix = input("Entrez votre choix (1-4): ")

        if choix == '1':
            menu_file()
        elif choix == '2':
            menu_liste()
        elif choix == '3':
            menu_salle()
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

main_menu()

#personnes, message = ListePersonneDao.afficher_personne()
#print(message)
#for personne in personnes:
#    print(f"Nom : {personne[0]}, Age : {personne[1]}")
#    print("----------------------------")
#per = Personne("Rambo","60")
#data = ListePersonneDao.ajouter_personne(per)
#print(data)

#fil = File("Robert", False)
#data = FileAttente.ajouter_personne_en_attente(fil)
#print(data)

#rsv = SalleCinema("Alice", 5)
#data = ReservationDao.reserver_place(rsv)
#print(data)

#reservations, message = ReservationDao.afficher_places_reservees()
#print(message)
#for reservation in reservations:
#    print(reservation)

#message = ReservationDao.nombre_places_disponibles()
#print(message)

#reservations = ReservationDao.filtrer_reservations_par_personne("Bob")

#for reservation in reservations:
#    print(f"Réservations pour {reservation[0]}:")
#    print(f"Nom: {reservation[0]}, Place: {reservation[1]}")

#message = ReservationDao.annuler_reservation("Bob")
#print(message)

#rsv = SalleCinema("John","",1)
#data = ReservationDao.reserver_place_speciale(rsv)
#print(data)