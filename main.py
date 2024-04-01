from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao



personnes, message = ListePersonneDao.afficher_personne()
for personne in personnes:
    print(f"Nom : {personne[0]}, Age : {personne[1]}")
    print("----------------------------")
#per = Personne("John","32")
#data = ListePersonneDao.ajouter_personne(per)
#print(data)