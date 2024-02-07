import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1",
    database="laplateforme"  # Specify the database you want to work with
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

total_capacity = cursor.fetchone()[0]

print(f"La capacité de toutes les salles est de :{total_capacity}")

cursor.close()
conn.close()
