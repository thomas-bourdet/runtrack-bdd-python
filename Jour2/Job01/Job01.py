import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqllpf1"
)

# Allow the code to connect to MySQL and give it the ability to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries :
cursor.execute("SHOW DATABASES LIKE 'laplateforme'")

# Fetch the result
result = cursor.fetchone()

# Check if the database exists
if result:
    print("The 'laplateforme' database exists.")
else:
    print("The 'laplateforme' database does not exist.")

# Close the cursor and connection
cursor.close()
conn.close()
