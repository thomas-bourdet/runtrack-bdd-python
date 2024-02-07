import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='sqllpf1',
    database='laplateforme',
)

query = "SELECT * FROM employe WHERE salaire >= 3000"
query2 = "SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service FROM employe JOIN service ON employe.id_service = service.id"

cursor = mydb.cursor()
cursor.execute(query)

for employe in cursor:
    print(employe)

cursor.close()

cursor2 = mydb.cursor()
cursor2.execute(query2)


for employe in cursor2:
    print(employe)

cursor2.close()
# Fermer le curseur et la connexion

mydb.close()

class salarie:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def create_employe(self, nom, prenom, salaire, employe_id):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, employe_id)
        self.cursor.execute(query, values)
        self.mydb.commit()
        

    def read_employe(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result :
            for employe in result:
                print(employe)

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_employe(self,employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()


host = "localhost"
user = "root"
password = "root"
database = "LaPlateforme"

employe1 = salarie(host, user, password, database)
employe1.create_employe("Torchut", "Elea", 4200, 1)
employe1.read_employe()
employe1.update_employe(1, 3000)
employe1.delete_employe(10)