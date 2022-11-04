from colorama import Fore, init # importo libreria para darle color al texto
#from datetime import datetime   # importo la libreria de fecha y hora

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
        for i in range(100):
            if i < 99:
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


