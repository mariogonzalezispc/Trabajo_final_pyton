import time
import time                     # importo la libreria rutinas de delay
from datetime import datetime   # importo la libreria de fecha y hora
from colorama import Fore, init # importo libreria para darle color al texto
from Conexion.conexion import BD_inmobiliaria

def cabecera_presentacion():    # inicio funcion con parte grafica para consola
    print("-------------------------------------------------------------------")
    print("| ISPC Tecnico Superior en Telecomunicaciones        Cohorte 2022 |")
    print("-------------------------------------------------------------------")
    print("| Materia  : Programacion           Lenguaje : Python 1er año     |")
    print("| Profesor : Lisandro Lanfranco                                   |")
    print("| Profesor : Kevin  Kessler                                       |")
    print("| Repositorio :                                                   |")
    color_verde()
    print("| https://github.com/mariogonzalezispc/Trabajo_final_pyton        |")
    color_blanco()
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
        print(Fore.RED,end="")
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color ROJO ", e)
    return

def color_verde():
    try:
        init()
        print(Fore.GREEN,end="")
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color VERDE ", e)
    return

def color_blanco():
    try:
        init()
        print(Fore.WHITE,end="")
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color BLANCO ", e)
    return

def color_amarillo():
    try:
        init()
        print(Fore.YELLOW,end="")
    except  (ValueError) as e:
            print("Ocurrió un error cargar el color BLANCO ", e)
    return

def menu_principal():
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
                time.sleep(3)   

limpia()
cabecera_presentacion()
menu_principal()