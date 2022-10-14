import pymysql
import time
# import mysql.connector

# try:
# 	inmobiliaria = pymysql.connect(host='localhost',
#                                 user='root',
#                                 password='1234',
#                                 db='inmobiliaria')
# 	print("Conexión correcta")
# except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
# 	print("Ocurrió un error al conectar: ", e)


def cabecera_presentacion():
    print("-------------------------------------------------------------------")
    print("| ISPC TS Telecomunicaciones                                      |")
    print("| Materia: Programacion  Lenguaje : Python                        |")
    print("| Alumno : Mario Gonzalez                                         |")
    print("-------------------------------------------------------------------")
    print()
    print()
    time.sleep(2)


def limpia():
    from os import system
    system("cls")


def conexion():


try:
    inmobiliaria = pymysql.connect(host='localhost',
                                   user='root',
                                   password='1234',
                                   db='inmobiliaria')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
return


def two():
    return "February"


def three():
    return "March"


def four():
    return "April"


def five():
    return "May"


def six():
    return "June"


def seven():
    return "July"


def eight():
    return "August"


def nine():
    return "September"


def ten():
    return "October"


def eleven():
    return "November"


def twelve():
    return "December"


limpia()
cabecera_presentacion()
limpia()


print()
print()
opcion = input("Ingrese opcion : ")
print("Opcion ingresada : " + opcion)


switcher = {
    "0": conexion,
    # "1": ingresa_propiedad,
    # "2": modifica_propiedad,
    # "3": elimina_propiedad,
    # "4": consulta_propiedad,
    # "5": listado_propiedades,
    # "6": listado_en_venta,
    # "7": listado_en_alquiler,
    # "8": listado_vendidas,
    # "9": listado_alquiladas,
}


switcher[opcion]()
