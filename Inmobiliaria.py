import pymysql
import time
# import mysql.connector

try:
	inmobiliaria = pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='inmobiliaria')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)


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


limpia()
cabecera_presentacion()
limpia()






