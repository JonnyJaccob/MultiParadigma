import psycopg2

from logger_base import log 

conexion = psycopg2.connect(
    user="postgres",
    password="contra",
    host="127.0.0.1",
    port="5051",
    database="clase_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM cliente WHERE id_cliente IN %s"
            entrada = input("Id's a eliminar")
            valores = (tuple(entrada.split(',')))
            cursor.executemany(sentencia,valores)
            registrosEliminados = cursor.rowcount
        cursor.executemany(sentencia,valores)
        registrosActualizados = cursor.rowcount
        log.debug(f"Registros Actualizados: {registrosActualizados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()