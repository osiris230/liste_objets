import mysql.connector as mysql


connection= mysql.connect(
    user='root',
    password= '',
    host='localhost',
    database='ecole'
)

cursor = connection.cursor()

def insertion(code_permanent,nom,prenom,date_naissance,spécialite):
    sql_insert = "INSERT INTO etudiant (code_permanent, nom, prenom, date_naissance,spécialite) VALUES (%s, %s, %s, %s, %s)"
    param = (code_permanent,nom,prenom,date_naissance,spécialite)
    cursor.execute(sql_insert, param)
    connection.commit()

def afficher():
    sql_affiche = "SELECT * from etudiant"
    cursor.execute(sql_affiche)
    resultat = cursor.fetchall()
    print("-----------------------------------------------")
    for i in resultat:
        print(
            "Code Permanent :",i[0],
            "\nNom : ",i[1], 
            "\nPrenom :", i[2],
            "\nDate de naissance :",i[3], 
            "\nSpécialité :",i[4],
            "\n-----------------------------------------------")
"""

code_permanent = input("Entrez le code permanent : ")
nom = input("Entrez le nom : ")
prenom = input("Entrez le prénom : ")
date_naissance = input("Entrez la date de naissance au format aaaa-mm-jj : ")
spécialite = input("Entrez la spécialité : ")


insertion(code_permanent,nom,prenom,date_naissance,spécialite)
"""
afficher()
