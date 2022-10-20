import pymysql                  # importo el conector de python con Mysql
import time                     # importo la libreria rutinas de delay
from datetime import datetime   # importo la libreria de fecha y hora
from colorama import Fore, init # importo libreria para darle color al texto


def cabecera_presentacion():    # inicio funcion con parte grafica para consola
    print("-------------------------------------------------------------------")
    print("| ISPC Tecnico Superior en Telecomunicaciones        Cohorte 2022 |")
    print("-------------------------------------------------------------------")
    print("| Materia  : Programacion           Lenguaje : Python 1er año     |")
    print("| Profesor : Lisandro Lanfranco                                   |")
    print("| Profesor : Kevin  Kessler                                       |")
    print("| Repositorio :                                                   |")
    print("|   https://github.com/mariogonzalezispc/Trabajo_final_pyton      |")
    print("| Alumnos  : Barea, Silvana       recursosssbb                    |")
    print("|            Martinez, Mauro      Mauro-Martinez                  |")
    print("|            Zarate, Tadeo        TadeoZarate                     |")
    print("|            Gonzalez, Mario      mariogonzalezispc               |")
    print("-------------------------------------------------------------------")
    print()
    print()
    time.sleep(4)


def menu_opciones():            # inicio menu de opciones en grafico para consola
    tiempo = datetime.now()     # genero objeto tiempo para fecha y hora
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
    print("-------------------------------------------------------------------")
    print("| Opcion 4 : Listado general de propiedades                       |")
    print("| Opcion 5 : Listado de propiedades en venta                      |")
    print("| Opcion 6 : Listado de propiedades en alquiler                   |")
    print("| Opcion 7 : Listado de propiedades vendidas                      |")
    print("| Opcion 8 : Listado de propiedades alquiladas                    |")
    print("| Opcion 9 : Sale del programa                                    |")
    print("-------------------------------------------------------------------")


def limpia():                   # limpia la pantalla de la consola
    from os import system
    system("cls")


def conecta():                  # genera la conexion a la base de datos remota

    global inmobiliaria
    inmobiliaria = pymysql.connect(host='mgalarmasserver1.ddns.net',
                                   user='ispc_inmobiliaria',
                                   password='ispc_inmobiliaria',
                                   db='inmobiliaria')


def conecta_mal():              # avisa de la mala conexion
    print("NO tiene conexion a la base de datos !!!!!!!")
    print()
    time.sleep(6)
    return


def prueba_conexion():          # prueba en cualquier momento la conexion a la base de datos
    try:
        print("Aguarde comprobando Conexión base de datos")
        conecta()
        print()
        time.sleep(2)
        color_amarillo()        # cambio el color del print amarillo
        print("Conexión exitosa !!!")
        print()
        color_blanco()          # cambio el color del print a blanco
        time.sleep(2)
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def ingresa_propiedad():        # permite cargar una propiedad
    try:
        conecta()
        print("Carga de propiedad para administrar")
        print()
        direccion = str(input("Ingrese direccion : "))
        duenio = str(input("Nombre del dueño : "))
        print("Cargar el tipo de operacion ")
        print("Para alquilar ingrese 1 ")
        print("Para vender   ingrese 2 ")        
        tipo = str(input("Ingrese tipo de operacion : "))

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def modifica_propiedad():
    try:
        conecta()
        print("modifica propiedad para administrar")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def borra_propiedad():
    try:
        conecta()
        print("borra propiedad para administrar")
        print("No tiene funcionalidad todavia")        
        print()
        time.sleep(3)
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def listado_propiedades():
    try:
        conecta()
        envio = inmobiliaria.cursor()
        envio.execute("SELECT * FROM `inmobiliaria`.`Propiedad` LIMIT 10;")
        retorno = envio.fetchall()  # cargo en la variable retorno el array de regreso BD
        limpia()                    # limpia la pantalla
        tiempo = datetime.now()     # genero objeto tiempo para fecha y hora
                                    # ordeno la forma de ver fecha y hora
        dato_dia = tiempo.strftime("%d/%m/%Y %H:%M:%S")
        rellenar3()                 # traza la linea de la consola
        print("| Sistema de gestion Inmobiliaria     Listado general de propiedades  " +
              dato_dia+" |")        # declaro fecha y hora de apertura
        rellenar3()                 # traza la linea de la consola 
        for x in retorno:           # inicio el recorrido del array de regreso de la BD
            init()
            relleno = 18-len(x[5])
            print(Fore.WHITE +"| ", end="")     # tabulador de campo izquierdo
            print(Fore.MAGENTA + x[5],end="")   # Dueño
            rellenar1(relleno)                  # relleno los espacios para poner el tabulador
            relleno = 22-len(x[6])              # calculo cantidad de relleno
            print(Fore.YELLOW + x[6],end="")    # Dueño
            rellenar1(relleno)                  # relleno los espacios para poner el tabulador
            relleno = 10-len(x[7])              # calculo cantidad de relleno
            print(Fore.GREEN + x[7],end="")     # Telefono del dueño
            rellenar2(relleno)                  # calculo cantidad de relleno
            rellenar3()                         # traza la linea de la consola          
    
        opcion = input("Presione ENTER para continuar : ")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def listado_en_venta():
    try:
        conecta()
        print("Listado de propiedades a la venta")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def listado_en_alquiler():
    try:
        conecta()
        print("Listado de propiedades en alquiler")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def listado_vendidas():
    try:
        conecta()
        print("Listado de propiedades VENDIDAS")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def listado_alquiladas():
    try:
        conecta()
        print("Listado de propiedades ALQUILADAS")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return


def sale():                     # inicia funcion de salir del programa
    limpia()                    # limpia la pantalla
    quit()                      # sale del sistema
    return


def rellenar1(relleno):
    try:
        for i in range(relleno):
            if i < relleno:
                print(" ",end="")
        init()        
        print(Fore.WHITE +" | ",end="")
    except  (ValueError) as e:
            print("Ocurrió un error crear la consola ", e)
    return


def rellenar2(relleno):

    try:
        for i in range(relleno):
            if i < relleno:
                print(" ",end="")
        init()        
        print(Fore.WHITE +" |")
    except  (ValueError) as e:
            print("Ocurrió un error crear la consola ", e)
    return


def rellenar3():
    try:
        init()
        print(Fore.WHITE +"-",end="")
        for i in range(90):
            if i < 89:
                print(Fore.WHITE +"-",end="")
        print(Fore.WHITE +"-")
    except  (ValueError) as e:
            print("Ocurrió un error crear la consola ", e)
    return


def color_rojo():
    try:
        init()
        print(Fore.RED)
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color ROJO ", e)
    return


def color_verde():
    try:
        init()
        print(Fore.GREEN)
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color VERDE ", e)
    return


def color_blanco():
    try:
        init()
        print(Fore.WHITE)
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color BLANCO ", e)
    return


def color_amarillo():
    try:
        init()
        print(Fore.YELLOW)
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color BLANCO ", e)
    return


limpia()
cabecera_presentacion()

while True:                     # generamos un while para uso continuo
        limpia()                # limpia la pantalla de la consola
        menu_opciones()         # llamamos la funcion menu de opciones
        print()                 # salto de linea
        print()                 # salto de linea
        try:                    # inicio del try
            opcion = int(input("Ingrese opcion : "))# Input para que usuario cargue opcion
            switch = {                              # Inicia el diccionario
                0: prueba_conexion,                 # opcion 0
                1: ingresa_propiedad,               # opcion 1
                2: modifica_propiedad,              # opcion 2
                3: borra_propiedad,                 # opcion 3
                4: listado_propiedades,             # opcion 4  
                5: listado_en_venta,                # opcion 5
                6: listado_en_alquiler,             # opcion 6
                7: listado_vendidas,                # opcion 7
                8: listado_alquiladas,              # opcion 8
                9: sale                             # opcion 9
                }
            if opcion < len(switch):                # verifico el tamaño del diccionario
                 switch[opcion]()                   # llamo a la funcion del diccionario
            else:
                print("NO es una opcion valida")    # ingreso si la opcion no esta en el diccionario
                print()                             # salto de linea
                print("Reintente !!!!")             # imprimo el reintento
                time.sleep(3)                       # demora de 3 segundos para leer consola
        except  (ValueError) as e:                  # tratamo el error y lo cargamos en variable "e"
                color_rojo()                        # cambio color del print a rojo
                print("El sistema solo acepta numeros ", e) 
                # print("El sistema solo acepta numeros ", e) # imprimo texto mas error
                print()                             # salto de linea
                color_verde()                       # cambio el color del print a verde
                print("Reintente !!!!")             # imprimo texto
                color_blanco()                      # cambio el color del print a blanco
                time.sleep(3)                       # demora de 3 segundos