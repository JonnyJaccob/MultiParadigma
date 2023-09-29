import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="contra",
    host="127.0.0.1",
    port="5051",
    database="clase_db"
)

print(conexion)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM cliente")
resultado = cursor.fetchall()
print(resultado)