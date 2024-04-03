import database as db
from salle_cinema.reservation import SalleCinema

class ReservationDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, rsv:SalleCinema):
        if ReservationDao.nombre_places_disponibles() > 0: 
            sql = "INSERT INTO reservation (nom, place) VALUES (%s, %s)"
            params = (rsv.nom, rsv.place)
            try:
                ReservationDao.connexion.cursor()
                ReservationDao.cursor.execute(sql, params)
                ReservationDao.connexion.commit()
                message = f"Ajout de {rsv.nom} à la place {rsv.place} avec succès."
            except Exception as ex:
                message = f"Erreur lors de l'ajout: {ex}"
        else:
            message = "Aucune place disponible."
        return message
    
    @classmethod
    def afficher_places_reservees(cls):
        sql = "SELECT place FROM reservation"
        try:
            ReservationDao.cursor.execute(sql)
            reservations = ReservationDao.cursor.fetchall()
            ReservationDao.cursor.close()
            message = "Success"
        except Exception as ex:
            message = f"Erreur lors de la récupération des réservations: {ex}"
        return reservations, message
    
    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale = 30
        sql = "SELECT COUNT(*) FROM reservation"
        try:
            ReservationDao.cursor.execute(sql)
            (nombre_reservations,) = ReservationDao.cursor.fetchone()
            places_disponibles = capacite_totale - nombre_reservations
            message = f"Nombre de places disponibles : {places_disponibles}"
        except Exception as ex:
            print(f"Erreur lors du calcul des places disponibles : {ex}")
        return message