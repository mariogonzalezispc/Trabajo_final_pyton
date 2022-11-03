# Atencion para usar este programa debemos incluir ciertas librerias

#  Para la conexion de la base de datos instalar el conector 
#  metodo de instalacion
#  python -m pip install PyMySQL
#  o
#  pip install PyMySQL 

#  Colorama para dar color al texto en la consola
#  metodo de instalacion 
#  python -m pip install colorama  
#  o
#  pip install colorama

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
    funciones.limpia()  # limpia la ventana de la consola
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


def opcion_4():
    base = DAO()
    try:
        mostrar = base.listado_propiedades()
        tiempo = datetime.now()     # genero objeto tiempo para fecha y hora
                                     # ordeno la forma de ver fecha y hora
        dato_dia = tiempo.strftime("%d/%m/%Y %H:%M:%S")
        funciones.rellenar3()                 # relleno los espacios para poner el tabulador
        print("| Sistema de gestion Inmobiliaria          Listado general de propiedades       " +
        dato_dia+" |")        # declaro fecha y hora de apertura
        funciones.rellenar3()                 # relleno los espacios para poner el tabulador
        print("|   Direccion Propiedad  | Hab | Baño | Patio | Garage |    Estado   |   Propietario   |  Contacto  |" )
        funciones.rellenar3()                 # relleno los espacios para poner el tabulador
        for x in mostrar:           # inicio el recorrido del array de regreso de la BD
            init()  
            relleno = 22-len(x[0])              # calculo cantidad de relleno  
            print(Fore.WHITE +"| ", end="")     # tabulador de campo izquierdo
            print(Fore.MAGENTA + x[0],end="")   # Propiedad 
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador
            relleno = 2-len(x[1])               # calculo cantidad de relleno
            print(Fore.YELLOW + " "+x[1],end="")# Habitaciones
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador

            relleno = 2-len(x[2])               # calculo cantidad de relleno
            print(Fore.GREEN +"  "+ x[2],end="")# Baños
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador

            relleno = 3-len(x[3])               # calculo cantidad de relleno
            if x[3]=='1':                       # si es 1 en el arreglo SI tiene patio
                Patio=" Si"                     # cargo SI a la variable que imprimo en consola
                print(Fore.GREEN + Patio,end="") 
            else:                               # si es 0 en el arreglo NO tiene patio
                Patio=" No"                     # cargo NO a la variable que imprimo en consola   
                print(Fore.RED + Patio,end="")  # Patio
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador

            relleno = 3-len(x[4])               # calculo cantidad de relleno
            if x[4]=='1':                       # si es 1 en el arreglo SI tiene Garage
                Garage="  Si"                   # cargo SI a la variable que imprimo en consola
                print(Fore.GREEN + Garage,end="")
            else:                               # si es 0 en el arreglo NO tiene Garage
                Garage="  No"                   # cargo NO a la variable que imprimo en consola
                print(Fore.RED + Garage,end="") # Garage
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador
 
            relleno = 11-len(x[6])              # calculo cantidad de relleno
            print(Fore.GREEN + x[6],end="")     # Estado de la propiedad para administrar
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador 

            relleno = 15-len(x[7])              # calculo cantidad de relleno
            print(Fore.GREEN + x[7],end="")     # Propietario
            funciones.rellenar1(relleno)                  # relleno los espacios para poner el tabulador

            relleno = 10-len(x[8])              # calculo cantidad de relleno
            print(Fore.GREEN + x[8],end="")     # Contacto
            funciones.rellenar2(relleno)                  # relleno los espacios para poner el tabulador
            funciones.rellenar3()                             # relleno los espacios para poner el tabulador          
 
            opcion = input("Presione ENTER para continuar : ")
        else:
                 print("NO es una opcion valida")    # ingreso si la opcion no esta en el diccionario
                 print()                             # salto de linea
                 print("Reintente !!!!")             # imprimo el reintento
                 time.sleep(3)                       # demora de 3 segundos para leer consola
    except  (ValueError) as e:                  # tratamo el error y lo cargamos en variable "e"
            funciones.color_rojo()                        # cambio color del print a rojo
            print("El sistema solo acepta numeros ", e) # imprimo texto mas error
            print()                             # salto de linea
            funciones.color_verde()                       # cambio el color del print a verde
            print("Reintente !!!!")             # imprimo texto
            funciones.color_blanco()                      # cambio el color del print a blanco
            time.sleep(3)                       # demora de 3 segundos

funciones.limpia()
cabecera_presentacion()


while True:                     # generamos un while para uso continuo
        funciones.limpia()                # limpia la pantalla de la consola
        menu_opciones()         # llamamos la funcion menu de opciones
        print()                 # salto de linea
        print()                 # salto de linea
        try:                    # inicio del try
            opcion = int(input("Ingrese opcion : "))# Input para que usuario cargue opcion
            if opcion == 0:
                print("Prueba de conexion")
            elif opcion == 1:
                print("Carga de propiedad para administrar")
            elif opcion == 2:
                print("Modifica Propiedad administrar")
            elif opcion == 3:
                print("Borra propiedad")
            elif opcion == 4:
                dame =DAO()
                try:
                    traer = dame.listado_propiedades()
                    print(traer)
                except  (ValueError) as e:                  # tratamo el error y lo cargamos en variable "e"
                    funciones.color_rojo()                        # cambio color del print a rojo
                    print("El sistema solo acepta numeros ", e) # imprimo texto mas error
                    print()                             # salto de linea
                    funciones.color_verde()                       # cambio el color del print a verde
                    print("Reintente !!!!")             # imprimo texto
                    funciones.color_blanco()                      # cambio el color del print a blanco
                    time.sleep(3)                       # demora de 3 segundos
            elif opcion == 5:
                print('PROPIEDADES EN ALQUILER')
            elif opcion == 6:
                print('PROPIEDADES VENDIDAS')
            elif opcion == 7:
                print('PROPIEDADES ALQUILADAS')
            elif opcion == 8:
                print('GRACIAS POR SU CONSULTA')
            elif opcion == 9:
                print('GRACIAS POR SU CONSULTA')
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

