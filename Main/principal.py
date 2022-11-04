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

from conexion import DAO
import funciones
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
        funciones.color_verde()
        print("| https://github.com/mariogonzalezispc/Trabajo_final_pyton        |")
        funciones.color_blanco()
        print("| Alumnos  : Barea, Silvana       recursosssbb                    |")
        print("|            Martinez, Mauro      Mauro-Martinez                  |")
        print("|            Gonzalez, Mario      mariogonzalezispc               |")
        print("-------------------------------------------------------------------")
        print()
        print()
        time.sleep(4)

def menu_opciones():            # inicio menu de opciones en grafico para consola
    tiempo = datetime.now()     # genero objeto tiempo para fecha y hora
    # ordeno la forma de ver fecha y hora
    dato_dia = tiempo.strftime("%d/%m/%Y %H:%M:%S")
    funciones.limpia()          # limpia la ventana de la consola
    print("-------------------------------------------------------------------")
    print("| Sistema de gestion Inmobiliaria             " +
          dato_dia+" |")        # declaro fecha y hora de apertura
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

funciones.limpia()
cabecera_presentacion()


while True:                             # generamos un while para uso continuo
        funciones.limpia()              # limpia la pantalla de la consola
        menu_opciones()                 # llamamos la funcion menu de opciones
        print()                         # salto de linea
        print()                         # salto de linea
        try:                            # inicio del try
            opcion = int(input("Ingrese opcion : "))# Input para que usuario cargue opcion
            if opcion == 0:
                dao=DAO()
                traer=dao.prueba_conexion()
                time.sleep(5)               
            elif opcion == 1:
                print("Carga de propiedad para administrar")
            elif opcion == 2:
                print("Modifica Propiedad administrar")
            elif opcion == 3:
                print("Borra propiedad")
            elif opcion == 4:
                dao = DAO()
                try:
                    mostrar = dao.listado_propiedades()
                    funciones.muestra(mostrar) 
                except  (ValueError) as e:                  # tratamos el error y lo cargamos en variable "e"
                    time.sleep(3)                           # demora de 3 segundos
            elif opcion == 5:
                dao = DAO()
                try:
                    mostrar = dao.listado_en_venta()
                    funciones.muestra(mostrar) 
                except  (ValueError) as e:                  # tratamos el error y lo cargamos en variable "e"
                    time.sleep(3)                           # demora de 3 segundos
            elif opcion == 6:
                dao = DAO()
                try:
                    mostrar = dao.listado_en_alquiler()
                    funciones.muestra(mostrar) 
                except  (ValueError) as e:                  # tratamos el error y lo cargamos en variable "e"
                    time.sleep(3)                           # demora de 3 segundos
            elif opcion == 7:
                dao = DAO()
                try:
                    mostrar = dao.listado_vendidas()
                    funciones.muestra(mostrar) 
                except  (ValueError) as e:                  # tratamos el error y lo cargamos en variable "e"
                    time.sleep(3)                           # demora de 3 segundos
            elif opcion == 8:
                dao = DAO()
                try:
                    mostrar = dao.listado_alquiladas()
                    funciones.muestra(mostrar) 
                except  (ValueError) as e:                  # tratamos el error y lo cargamos en variable "e"
                    time.sleep(3)                           # demora de 3 segundos
            elif opcion == 9:
                funciones.limpia()
                break
            else:
                funciones.color_rojo()
                print("NO es una opcion valida")            # ingreso si la opcion no esta en el diccionario
                print()                                     # salto de linea
                print("Reintente !!!!")                     # imprimo el reintento
                funciones.color_blanco()
                time.sleep(2)  
            funciones.limpia()
        except  (ValueError) as e:                          # tratamo el error y lo cargamos en variable "e"
                funciones.color_rojo()                      # cambio color del print a rojo
                print("El sistema solo acepta numeros ", e) 
                # print("El sistema solo acepta numeros ", e) # imprimo texto mas error
                print()                                     # salto de linea
                funciones.color_verde()                     # cambio el color del print a verde
                print("Reintente !!!!")                     # imprimo texto
                funciones.color_blanco()                    # cambio el color del print a blanco
                time.sleep(2)                               # demora de 3 segundos

