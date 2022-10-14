import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='inmobiliaria')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e) 

from os import system 
system("cls")

print("-------------------------------------------------------------------") 
print("| ISPC TS Telecomunicaciones                                       |")
print("| Materia: Programacion  Lenguaje : Python                         |")
print("| Alumno : Mario Gonzalez I                                        |")
print()
print()
print()


