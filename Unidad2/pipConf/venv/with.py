import psycopg2

from logger_base import log 

conexion = psycopg2.connect(
    user="postgres",
    password="contra",
    host="127.0.0.1",
    port="5433",
    database="clase_db"
)

try:
    with conexion.cursor() as cursor:
        sentencia = "Insert INTO cliente (id, nombre) values(%s,%s)"
        valores = {
            ("9","Paco"),
            ("10","Hugo"),
            ("11","Pedro")
        }
        cursor.executemany(sentencia,valores)
        registrosInsertados = cursor.rowcount #RowsAffected 
        log.debug(f"Registros insertados: {registrosInsertados}")
        conexion.commit()
except Exception as e:
    log.error(e)
finally:
    conexion.close()