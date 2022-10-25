import mysql.connector
from mysql.connector import Error


class BD_inmobiliaria():
    def __init__(self):
        try:
            self.inmobiliaria = mysql.connector.connect(host='mgalarmasserver1.ddns.net',  # direccion de la base de datos
                                         database='inmobiliaria',           # nombre de la base de datos
                                         user='ispc_inmobiliaria',          # usuario de la bd
                                         password='ispc_inmobiliaria')      # password de la bd
            if self.inmobiliaria.is_connected():                                   # condicional de inmobiliaria
                db_Info = self.inmobiliaria.get_server_info()                      # informacion de servicio
                print()                                                     # salto de linea
                print("Conexion Exitosa !!! ")                              # imprimo mensaje
                print("Version: ", db_Info)                                 # imprimo mensaje + db_Info
                cursor = self.inmobiliaria.cursor()                                # inicio cursor de la bd
                cursor.execute("select database();")                        # selecciono la base de datos declarada
                record = cursor.fetchone()                                  # grabo en record el retorno de cursor
                print("Conectado a la base de datos: ", record)             # imprimo mensaje + nombre de la BD conectada
                print()                                                     # salto de linea
        except Error as e:                                                  # exception error
            print("No de pudo conectar a la base de datos !!", e)
        finally:
            if self.inmobiliaria.is_connected():
                cursor.close()
                self.inmobiliaria.close()
                print("Conexion base de datos cerrada !!")
                print()










        