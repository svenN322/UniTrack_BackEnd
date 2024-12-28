import mysql.connector

# Configuración de la conexión a la base de datos MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="BD_PROYUSER"
)

# Crea un cursor para ejecutar consultas SQL
mycursor = mydb.cursor()

