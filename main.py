from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao



personnes, message = ListePersonneDao.afficher_personne()
print(personnes,message)