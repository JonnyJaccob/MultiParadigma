import psycopg2

print("Arrancando...\n")
conexion = psycopg2.connect(
    user="postgres",
    password="contra",
    host="127.0.0.1",
    port="5433",
    database="clase_db"
)
print("Estado conexion: ")
print(conexion)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM cliente")
resultado = cursor.fetchall()
print(resultado)