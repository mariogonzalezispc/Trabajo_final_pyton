from multiprocessing import context
import mysql.connector          # importo conector de mysql.connector
import time                     # importo la libreria rutinas de delay
# importo libreria para darle color al texto
from Archivo.Inmobiliaria import color_amarillo, color_blanco, color_rojo

# genera la conexion a la base de datos remota
def prueba_conexion():
    try:
        inmobiliaria = mysql.connector.connect(host='mgalarmasserver1.ddns.net',
                                           user='ispc_inmobiliaria',
                                           password='ispc_inmobiliaria',
                                           db='inmobiliaria')

        if inmobiliaria.is_connected():
            color_amarillo()
            print("Conexión exitosa !!!")
            print()
            time.sleep(2)
            color_blanco()
    except:
        color_rojo()
        print("NO tiene conexion a la base de datos !!!!!!!")
        print()
        time.sleep(6)

    finally:
        if inmobiliaria.is_connected():
            inmobiliaria.close()
            color_rojo()
            print("conexion cerrada")
            color_rojo()
        
