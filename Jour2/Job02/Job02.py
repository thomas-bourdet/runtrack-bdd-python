import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1",
    database="laplateforme"  # Specify the database you want to work with
)

# Create a cursor object
cursor = conn.cursor()

# Create the "etage" table
cursor.execute("""
CREATE TABLE etage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    numero INT,
    superficie INT
)
""")

# Create the "salle" table
cursor.execute("""
CREATE TABLE salle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id)
)
""")

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Tables 'etage' and 'salle' created successfully.")
