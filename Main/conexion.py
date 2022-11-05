#  Atencion para usar este programa debemos incluir ciertas librerias
#--------------------------------------------------------------
#  Para la conexion de la base de datos instalar el conector 
#  metodo de instalacion
#  python -m pip install PyMySQL
#  o
#  pip install PyMySQL 
#--------------------------------------------------------------
#  para la base de datos utilizamos este conector el anterior comentado 
#  metodo de instalacion 
#  pip install mysql-connector-python
#--------------------------------------------------------------
#  Colorama para dar color al texto en la consola
#  metodo de instalacion 
#  python -m pip install colorama  
#  o
#  pip install colorama
# -------------------------------------------------------------
#  Base de datos
#  la base de datos de este proyecto es remota 
#  la direccion :   mgalarmasserver1.ddns.net
#  puerto : 3306
#  Base de datos nombre : inmobiliaria                                    
#  Usuario : ispc_inmobiliaria     
#  Contraseña : ispc_inmobiliaria 


#import pymysql                         # importo el conector de python con Mysql
import mysql.connector                  # importo el conector de python con Mysql
from mysql.connector import Error
import funciones
# import time                     # importo la libreria rutinas de delay






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
        #         cursor.close() 12
        #         self.inmobiliaria.close()
        #         print("Conexion base de datos cerrada !!")
        #         print()

    def prueba_conexion(self):
            try:
                    self.inmobiliaria.connect()
                    db_Info = self.inmobiliaria.get_server_info()               # informacion de servicio
                    funciones.color_amarillo()
                    print()                                                     # salto de linea
                    print("Version: ", db_Info) 
                    print()
                    print("Conexion Exitosa !!!")   
                    funciones.color_blanco()  
                    print()    
                    self.inmobiliaria.close()
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return 


    def carga_propiedad(self,tipo,estado,operacion,propietario,direccion,habitaciones,banio,patio,garage):
    #def carga_propiedad(self):
        dao= DAO()
        try:
            dao.inmobiliaria.connect()
            cursor1=dao.inmobiliaria.cursor() 
            sql= "INSERT INTO `inmobiliaria`.`Propiedad` \
                (`Id_Tipo`,\
                `Id_Estado`,\
                `Id_Operacion_Comercial`,\
                `Id_Propietario`,\
                `Direccion`,\
                `Habitaciones`,\
                `Baños`,\
                `Patio`,\
                `Cochera`) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            val = (tipo,estado,operacion,propietario,direccion,habitaciones,banio,patio,garage)
            cursor1.execute(sql,val) 
            dao.inmobiliaria.commit()
            dao.inmobiliaria.close()
        except ValueError as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return



    def modifica_propiedad(self,direccion):
    #def carga_propiedad(self):
        dao= DAO()
        try:
            dao.inmobiliaria.connect()
            envio=dao.inmobiliaria.cursor() 
            sql = "SELECT * FROM Propiedad WHERE Direccion = %s"
            val = (direccion,)
            envio.execute(sql,val) 
            Resul = envio.fetchall()
            for x in Resul: 
                adress = x[0]
  
            sql= "UPDATE `inmobiliaria`.`Propiedad` \
                SET \
                `Id_Tipo`,\
                `Id_Estado`,\
                `Id_Operacion_Comercial`,\
                `Id_Propietario`,\
                `Direccion`,\
                `Habitaciones`,\
                `Baños`,\
                `Patio`,\
                `Cochera` \
                 WHERE  Id_Propiedad= %s;"
            val = (adress)
            envio.execute(sql,val) 
            dao.inmobiliaria.commit()
            dao.inmobiliaria.close()
        except ValueError as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def borra_propiedad(self,direccion):
        dao= DAO()
        try:
            dao.inmobiliaria.connect()
            envio=dao.inmobiliaria.cursor() 
            sql = "SELECT * FROM Propiedad WHERE Direccion = %s"
            val = (direccion,)
            envio.execute(sql,val) 
            Resul = envio.fetchall()
            for x in Resul: 
                adress = x[0]

            sql = "DELETE FROM Propiedad WHERE Id_Propiedad = %s"
            val = (adress,)
            envio.execute(sql,val)
            dao.inmobiliaria.commit()
            dao.inmobiliaria.close()
        except ValueError as e:
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
                Propietario.Id_Propietario, \
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad, Propietario, Tipo, Estado \
                WHERE Propiedad.Id_Propietario = Propietario.Id_Propietario \
                AND Propiedad.Id_Tipo = Tipo.Id_Tipo \
                AND Propiedad.Id_Estado = Estado.Id_Estado;"
                envio = self.inmobiliaria.cursor()
                envio.execute(sql)
                Resul = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                self.inmobiliaria.close()
                return Resul
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def listado_alquiladas(self):
            try:
                self.inmobiliaria.connect()
                envio = self.inmobiliaria.cursor()
                sql =  "SELECT\
                Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Tipo.Nombre_Tipo,\
                Estado.Nombre_Estado,\
                Propietario.Id_Propietario, \
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 2 \
                AND Propiedad.Id_Estado = Estado.Id_Estado \
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario \
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                self.inmobiliaria.close()
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                
    def listado_vendidas(self):
            try:
                self.inmobiliaria.connect()
                envio = self.inmobiliaria.cursor()
                sql =  "SELECT\
                Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Tipo.Nombre_Tipo,\
                Estado.Nombre_Estado,\
                Propietario.Id_Propietario, \
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 4\
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                self.inmobiliaria.close()
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def listado_en_alquiler(self):
            try:
                self.inmobiliaria.connect()
                envio = self.inmobiliaria.cursor()
                sql =  "SELECT\
                Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Tipo.Nombre_Tipo,\
                Estado.Nombre_Estado,\
                Propietario.Id_Propietario, \
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 1\
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                self.inmobiliaria.close()
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                       
    def listado_en_venta(self):
            try:
                self.inmobiliaria.connect()
                envio = self.inmobiliaria.cursor()
                sql =  "SELECT\
                Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Tipo.Nombre_Tipo,\
                Estado.Nombre_Estado,\
                Propietario.Id_Propietario, \
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad,Estado,Propietario,Tipo WHERE Propiedad.Id_Estado = 3 \
                AND Propiedad.Id_Estado = Estado.Id_Estado\
                AND Propiedad.Id_Propietario= Propietario.Id_Propietario\
                AND Propiedad.Id_Tipo= Tipo.Id_Tipo;"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                self.inmobiliaria.close()
                return Resultado
            except Error as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return