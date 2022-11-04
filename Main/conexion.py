#import pymysql                  # importo el conector de python con Mysql
import mysql.connector                  # importo el conector de python con Mysql
from mysql.connector import Error
import funciones


class DAO():
    def __init__(self):
        try:
            self.inmobiliaria = mysql.connector.connect(
                host='mgalarmasserver1.ddns.net',                           # direccion de la base de datos
                database='inmobiliaria',                                    # nombre de la base de datos
                user='ispc_inmobiliaria',                                   # usuario de la bd
                password='ispc_inmobiliaria')                               # password de la bd
            if self.inmobiliaria.connect():                                 # condicional de inmobiliaria
                db_Info = self.inmobiliaria.get_server_info()               # informacion de servicio
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

        # finally:
        #     if self.inmobiliaria.connect():
        #         cursor.close()
        #         self.inmobiliaria.close()
        #         print("Conexion base de datos cerrada !!")
        #         print()

    def prueba_conexion(self):
            try:
                    self.inmobiliaria.connect()
                    funciones.color_amarillo()
                    print()
                    print("Conexion Exitosa !!!")   
                    funciones.color_blanco()      
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return 

    def listado_propiedades(self):
            try:
                self.inmobiliaria.connect()
                sql =  "SELECT\
                Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Tipo.Nombre_Tipo,\
                Estado.Nombre_Estado,\
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad, Propietario, Tipo, Estado\
                WHERE Propiedad.Id_Propietario = Propietario.Id_Propietario \
                AND Propiedad.Id_Tipo = Tipo.Id_Tipo\
                AND Propiedad.Id_Estado = Estado.Id_Estado"
                envio = self.inmobiliaria.cursor()
                envio.execute(sql)
                Resul = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resul
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def listado_alquiladas(self):
        if self.inmobiliaria.connect():
            try:
                envio = self.inmobiliaria.cursor()
                sql = "SELECT Propiedad.Direccion, \
                Propiedad.Habitaciones, \
                Propiedad.`Baños`, \
                Propiedad.Patio, \
                Propiedad.Cochera, \
                Estado.Nombre_Estado, \
                Propietario.Nombre, \
                Propietario.Contacto, \
                Tipo.Nombre_Tipo \
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 2 \
                AND Propiedad.Id_Estado = Estado.Id_Estado \
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario \
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                
    def listado_vendidas(self):
        if self.inmobiliaria.connect():
            try:
                envio = self.inmobiliaria.cursor()
                sql = "SELECT Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Estado.Nombre_Estado,\
                Propietario.Nombre,\
                Propietario.Contacto,\
                Tipo.Nombre_Tipo\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 2\
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def listado_en_alquiler(self):
        if self.inmobiliaria.connect():
            try:
                envio = self.inmobiliaria.cursor()
                sql = "SELECT Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Estado.Nombre_Estado,\
                Propietario.Nombre,\
                Propietario.Contacto,\
                Tipo.Nombre_Tipo\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 2\
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                       
    def listado_en_venta(self):
        if self.inmobiliaria.connect():
            try:
                envio = self.inmobiliaria.cursor()
                sql = "SELECT Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Estado.Nombre_Estado,\
                Propietario.Nombre,\
                Propietario.Contacto,\
                Tipo.Nombre_Tipo\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 2\
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
