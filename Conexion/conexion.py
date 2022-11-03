import pymysql                  # importo el conector de python con Mysql



class DAO():
    def __init__(self):
        try:
            self.inmobiliaria = pymysql.connect(host='mgalarmasserver1.ddns.net',  # direccion de la base de datos
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
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:                                                 # exception error
            print("No de pudo conectar a la base de datos !!", e)
        finally:
            if self.inmobiliaria.is_connected():
                cursor.close()
                self.inmobiliaria.close()
                print("Conexion base de datos cerrada !!")
                print()



    def listado_propiedades(self):
        if self.inmobiliaria.is_connected():
            try:
                cursor = self.inmobiliaria.cursor()
                cursor.execute("select * from propiedades")
                envio = self.inmobiliaria.cursor()
                sql = "SELECT Propiedad.Direccion,\
                Propiedad.Habitaciones,\
                Propiedad.`Baños`,\
                Propiedad.Patio,\
                Propiedad.Cochera,\
                Propietario.Id_Propietario,\
                Propietario.Nombre,\
                Propietario.Contacto\
                FROM Propiedad, Propietario\
                WHERE Propiedad.Id_Propietario = Propietario.Id_Propietario"
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                
    def listado_alquiladas(self):
        if self.inmobiliaria.is_connected():
            try:
                cursor = self.inmobiliaria.cursor()
                cursor.execute("select * from propiedades")
                envio = self.inmobiliaria.cursor()
                sql = "SELECT "
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                
    def listado_vendidas(self):
        if self.inmobiliaria.is_connected():
            try:
                cursor = self.inmobiliaria.cursor()
                cursor.execute("select * from propiedades")
                envio = self.inmobiliaria.cursor()
                sql = "SELECT "
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return

    def listado_en_alquiler(self):
        if self.inmobiliaria.is_connected():
            try:
                cursor = self.inmobiliaria.cursor()
                cursor.execute("select * from propiedades")
                envio = self.inmobiliaria.cursor()
                sql = "SELECT "
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                       
    def listado_en_venta(self):
        if self.inmobiliaria.is_connected():
            try:
                cursor = self.inmobiliaria.cursor()
                cursor.execute("select * from propiedades")
                envio = self.inmobiliaria.cursor()
                sql = "SELECT "
                envio.execute(sql)
                Resultado = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
                return Resultado
            except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
                print("No de pudo conectar a la base de datos !!", e)
                print("Ocurrió un error al conectar")
                return
                






        