import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1",
    database="laplateforme"  # Specify the database you want to work with
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

total_area = cursor.fetchone()[0]

print(f"La superficie de La Plateforme est de {total_area} m2")

cursor.close()
conn.close()
