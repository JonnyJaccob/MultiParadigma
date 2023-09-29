import psycopg2

from logger_base import log 

conexion = psycopg2.connect(
    user="postgres",
    password="contra",
    host="127.0.0.1",
    port="5068",
    database="clase_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE cliente SET nombre=%s WHERE id_cliente=%s"
            valores = (
                ("Luis",9),
                ("Eduardo",10)
            )
        cursor.executemany(sentencia,valores)
        registrosActualizados = cursor.rowcount
        log.debug(f"Registros Actualizados: {registrosActualizados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()