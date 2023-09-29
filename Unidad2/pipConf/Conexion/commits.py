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
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO cliente(nombre,id_cliente) values(%s,%s)"
    valores=("Juan",4)
    cursor.execute(sentencia,valores)

    log.debug("Sentencia Insert")
    #commit manual
    conexion.commit()
    update = "UPDATE cliente SET nombre=%s WHERE id_cliente=%s"
    valores=("Hugo",4)
except Exception as e:
    conexion.rollback()
    log.error(e)