import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1",
    database="laplateforme"  # Specify the database you want to work with
)

cursor = conn.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

rows = cursor.fetchall()

print("Noms et Capacités des Salles : ")
print("-" * 20)
for row in rows:
    print(f"{row[0]}\t\t{row[1]}")

conn.commit()

cursor.close()
conn.close()

print("Queries executed successfully.")
