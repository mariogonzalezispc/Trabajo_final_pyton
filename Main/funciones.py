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



from datetime import datetime   # importo la libreria de fecha y hora
from colorama import Fore, init # importo libreria para darle color al texto
import time                     # importo la libreria rutinas de delay

#----------------------------------------------------------------
# rutinas de servicio
#----------------------------------------------------------------
def limpia():                   # limpia la pantalla de la consola
    from os import system
    system("cls")

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
        for i in range(114):
            if i < 113:
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
            print("Ocurrió un error cargar el color Amarillo ", e)
    return

def muestra(mostrar):
    try:
        tiempo = datetime.now()     # genero objeto tiempo para fecha y hora
        dato_dia = tiempo.strftime("%d/%m/%Y %H:%M:%S")# formato de fecha y hora
        limpia()
        rellenar3()                 # relleno los espacios para poner el tabulador
        print("| Sistema de gestion Inmobiliaria              Listado general de propiedades                 " +
        dato_dia+" |")        # declaro fecha y hora de apertura
        rellenar3()                 # relleno los espacios para poner el tabulador
        print("|   Direccion Propiedad  | Hab | Baño | Patio | Garage |    Tipo     |    Estado   |   Propietario   |  Contacto  |" )
        rellenar3()                 # relleno los espacios para poner el tabulador
        for x in mostrar:           # inicio el recorrido de la lista de regreso de la BD
                init()  
                relleno = 22-len(x[0])              # calculo cantidad de relleno  
                print(Fore.WHITE +"| ", end="")     # tabulador de campo izquierdo
                print(Fore.MAGENTA + x[0],end="")   # Propiedad 
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador
                relleno = 2-len(x[1])               # calculo cantidad de relleno
                print(Fore.YELLOW + " "+x[1],end="")# Habitaciones
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador

                relleno = 2-len(x[2])               # calculo cantidad de relleno
                print(Fore.YELLOW +"  "+ x[2],end="")# Baños
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador

                relleno = 3-len(x[3])               # calculo cantidad de relleno
                if x[3]=='1':                       # si es 1 en el arreglo SI tiene patio
                    Patio=" Si"                     # cargo SI a la variable que imprimo en consola
                    print(Fore.GREEN + Patio,end="") 
                else:                               # si es 0 en el arreglo NO tiene patio
                    Patio=" No"                     # cargo NO a la variable que imprimo en consola   
                    print(Fore.RED + Patio,end="")  # Patio
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador

                relleno = 3-len(x[4])               # calculo cantidad de relleno
                if x[4]=='1':                       # si es 1 en el arreglo SI tiene Garage
                    Garage="  Si"                   # cargo SI a la variable que imprimo en consola
                    print(Fore.GREEN + Garage,end="")
                else:                               # si es 0 en el arreglo NO tiene Garage
                    Garage="  No"                   # cargo NO a la variable que imprimo en consola
                    print(Fore.RED + Garage,end="") # Garage
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador

                relleno = 11-len(x[5])              # calculo cantidad de relleno
                print(Fore.GREEN + x[5],end="")     # Tipo de propiedad para administrar
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador 
 
                relleno = 11-len(x[6])              # calculo cantidad de relleno
                print(Fore.GREEN + x[6],end="")     # Estado de la propiedad para administrar
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador 

                relleno = 15-len(x[7])              # calculo cantidad de relleno
                print(Fore.GREEN + x[7],end="")     # Propietario
                rellenar1(relleno)                  # relleno los espacios para poner el tabulador

                relleno = 10-len(x[8])              # calculo cantidad de relleno
                print(Fore.GREEN + x[8],end="")     # Contacto
                rellenar2(relleno)                  # relleno los espacios para poner el tabulador
        rellenar3()                                 # relleno los espacios para poner el tabulador          
        opcion = input("Presione ENTER para continuar : ")
    except  (ValueError) as e:                      # tratamo el error y lo cargamos en variable "e"
            color_rojo()                            # cambio color del print a rojo
            print(e)                                # imprimo el error
            print()                                 # salto de linea
            color_blanco()                          # cambio el color del print a blanco
            time.sleep(3)