import pymysql  # importo el conector de python con Mysql
import time  # importo la libreria rutinas de delay
from datetime import datetime  # importo la libreria de fecha y hora
Sale = False  # declaro variable booleana
Estado = False 


def cabecera_presentacion():  # inicio funcion con parte grafica para consola
    print("-------------------------------------------------------------------")
    print("| ISPC Tecnico Superior en Telecomunicaciones        Cohorte 2022 |")
    print("-------------------------------------------------------------------")
    print("| Materia  : Programacion           Lenguaje : Python 1er año     |")
    print("| Profesor : Lisandro Lanfranco                                   |")
    print("| Profesor : Kevin  Kessler                                       |")
    print("| Alumno   : Mario Gonzalez                                       |")
    print("-------------------------------------------------------------------")
    print()
    print()
    time.sleep(4)

def menu_opciones():          # inicio menu de opciones en grafico para consola
    tiempo = datetime.now()  # genero objeto tiempo para fecha y hora
    # ordeno la forma de ver fecha y hora
    dato_dia = tiempo.strftime("%d/%m/%Y %H:%M:%S")
    limpia()  # limpia la ventana de la consola
    print("-------------------------------------------------------------------")
    print("| Sistema de gestion Inmobiliaria             " +
          dato_dia+" |")  # declaro fecha y hora de apertura
    print("-------------------------------------------------------------------")
    print("| Opcion 0 : Prueba conexion a la base de datos                   |")
    print("-------------------------------------------------------------------")
    print("| Opcion 1 : Carga propiedad para administrar o vender            |")
    print("| Opcion 2 : Modifica propiedad para administrar o vender         |")
    print("| Opcion 3 : Borra propiedad para administrar o vender            |")
    print("| Opcion 4 : Consulta de propiedad                                |")
    print("-------------------------------------------------------------------")
    print("| Opcion 5 : Listado general de propiedades                       |")
    print("| Opcion 6 : Listado de propiedades en venta                      |")
    print("| Opcion 7 : Listado de propiedades en alquiler                   |")
    print("| Opcion 8 : Listado de propiedades vendidas                      |")
    print("| Opcion 9 : Listado de propiedades alquiladas                    |")
    print("| Opcion 10: Sale del programa                                    |")
    print("-------------------------------------------------------------------")

def limpia():                 # limpia la pantalla de la consola 
    from os import system
    system("cls")
    Estado = False

def conecta():                # genera la conexion a la base de datos remota
    inmobiliaria = pymysql.connect(host='mgalarmasserver1.ddns.net',
                                   user='ispc_inmobiliaria',
                                   password='ispc_inmobiliaria',
                                   db='inmobiliaria')

def prueba_conexion():        # prueba en cualquier momento la conexion a la base de datos
    try:
        print("Aguarde comprobando Conexión base de datos")
        conecta()
        time.sleep(2)
        print("Conexión exitosa !!!")
        print()
        time.sleep(2)
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def ingresa_propiedad():      # permite cargar una propiedad
    try:
        conecta()
        print("Carga de propiedad para administrar")
        print()
        direccion = input("Ingrese direccion : ")
        dueno = input("Nombre del dueño : ")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def modifica_propiedad():
    try:
        conecta()
        print("modifica propiedad para administrar")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def borra_propiedad():
    try:
        conecta()
        print("borra propiedad para administrar")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def consulta_propiedad():
    try:
        conecta()
        print("consulta propiedad para administrar")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def listado_propiedades():
    try:
        conecta()
        print("Listado general de propiedades")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def listado_en_venta():
    try:
        conecta()
        print("Listado de propiedades a la venta")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def listado_en_alquiler():
    try:
        conecta()
        print("Listado de propiedades en alquiler")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def listado_vendidas():
    try:
        conecta()
        print("Listado de propiedades VENDIDAS")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def listado_alquiladas():
    try:
        conecta()
        print("Listado de propiedades ALQUILADAS")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conexion_mal()
    return

def sale():
    limpia()
    quit()
    return

def conexion_mal():
    print("NO tiene conexion a la base de datos !!!!!!!")
    print()
    time.sleep(6)
    return

limpia()
cabecera_presentacion()

while Sale == False:
    limpia()
    menu_opciones()
    print()
    print()
    opcion = input("Ingrese opcion : ")

    # while Estado == False:
    #     opcion = input("Ingrese opcion : ")
    #     if (opcion.isnumeric()):
    #         print("Opcion ingresada : " + opcion)
    #         Estado = True
    #     else:
    #         Estado = False
    #         print(" El sistema solo acepta numeros")
    #         print(" Reintente !!!!")
    #         time.sleep(4)
    #         opcion= None

    # print("Opcion ingresada : " + opcion)
    print()
    switch = {
        "0": prueba_conexion,
        "1": ingresa_propiedad,
        "2": modifica_propiedad,
        "3": borra_propiedad,
        "4": consulta_propiedad,
        "5": listado_propiedades,
        "6": listado_en_venta,
        "7": listado_en_alquiler,
        "8": listado_vendidas,
        "9": listado_alquiladas,
        "10": sale
    }
    switch[opcion]()
