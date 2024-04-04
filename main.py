from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao
from file_attente.File_attente import File
from file_attente.File_dao import FileAttente
from salle_cinema.reservation import SalleCinema
from salle_cinema.reservation_dao import ReservationDao



#personnes, message = ListePersonneDao.afficher_personne()
#print(message)
#for personne in personnes:
#    print(f"Nom : {personne[0]}, Age : {personne[1]}")
#    print("----------------------------")
#per = Personne("John","32")
#data = ListePersonneDao.ajouter_personne(per)
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