import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1",
    database="laplateforme"  # Specify the database you want to work with
)

cursor = conn.cursor()

##############################################
dataetage = [
    (1, 'RDC', 0, 500),
    (2, 'R+1', 1, 500),
]

cursor.executemany("""
INSERT INTO etage (
    id, nom, numero, superficie)
    VALUES (%s, %s, %s, %s)
""", dataetage)


datasalle = [
    (1, 'Lounge', 1, 100),
    (2, 'Studio son', 1, 5),
    (3, 'Broadcasting', 2, 50),
    (4, 'Bocal pPeda', 2, 4),
    (5, 'Coworkingg', 2, 80),
    (6, 'Studio Video', 2, 5),
]

cursor.executemany("""
    INSERT INTO salle (
    id, nom, id_etage, capacite)
    VALUES (%s, %s, %s, %s)
""", datasalle)






##############################################

conn.commit()

cursor.close()
conn.close()

print("Queries executed successfully.")
