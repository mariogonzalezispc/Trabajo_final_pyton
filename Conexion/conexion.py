import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='mgalarmasserver1.ddns.net',  # direccion de la base de datos
                                         database='inmobiliaria',           # nombre de la base de datos
                                         user='ispc_inmobiliaria',          # usuario de la bd
                                         password='ispc_inmobiliaria')      # password de la bd
    if connection.is_connected():                       # condicional de connection
        db_Info = connection.get_server_info()          # informacion de server
        print()                                         # salto de linea
        print("Conexion Exitosa !!! ")                  # imprimo mensaje
        print("Version: ", db_Info)                     # imprimo mensaje + db_Info
        cursor = connection.cursor()                    # inicio cursor de la bd
        cursor.execute("select database();")            # selecciono la base de datos declarada
        record = cursor.fetchone()                      # grabo en record el retorno de cursor
        print("Conectado a la base de datos: ", record) # imprimo mensaje + nombre de la BD conectada
        print()                                         # salto de linea
except Error as e:                                      # exception error
    print("No de pudo conectar a la base de datos !!", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion base de datos cerrada !!")
        print()