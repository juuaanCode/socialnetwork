# Juan González Arranz - T1 - ANALISIS DE CARALIBRO
# Fichero principal
import time
from user_optimized import *
from grumos_optimized import *

def lectura_ficheros(ruta_principal, ruta_extra):
    """Lee los ficheros y devuelve la lista de conexiones del sistema con el número de ususarios."""
    cadenas_conexiones = []
    with open(ruta_principal) as fichero: 
        cadenas_conexiones = fichero.readlines()
    num_usuarios = int(cadenas_conexiones[0][:-1])

    #Creacion de la estructura red
    red = []
    for fila in range(2, len(cadenas_conexiones)):
        red.append([int(numero) for numero in cadenas_conexiones[fila].split()])
    #Fichero de conexiones extra
    if ruta_extra != "":
        with open(ruta_extra) as fichero:
            cadenas_conexiones = fichero.readlines()
        for fila in range(len(cadenas_conexiones)):
            red.append([int(numero) for numero in cadenas_conexiones[fila].split()])
    return red, num_usuarios


def ordenacion_seleccion(grus, porcentaje, num_usuarios):
    """Ordena la lista de grumos y devuelve el índice del último grumo a unir."""
    grus.sort(reverse=True,key=lambda x: x.tamano)
    ultimo_grumo = 0
    tamano_acumulado = grus[0].tamano
    while ((tamano_acumulado / num_usuarios)*100 < porcentaje) and (ultimo_grumo < len(grus)-1):
        ultimo_grumo += 1
        tamano_acumulado += grus[ultimo_grumo].tamano
    return ultimo_grumo


def nuevas_relaciones(grus, ultimo_grumo):
    """Devuelve la lista con los identificadores de usuarios que se deben unir."""
    nuevas_conexiones = []
    for indice_grumo in range(ultimo_grumo):
        nuevas_conexiones.append([grus[indice_grumo], grus[indice_grumo+1]])
    return nuevas_conexiones


def main():
    print("ANALISIS DE CARALIBRO")
    print("---------------------")
    
    #Lectura del fichero principal
    ruta_principal = input("Fichero principal: ") 
    ruta_extra = input("Fichero de nuevas conexiones (pulse enter si no existe):  ") 
    red, num_usuarios = lectura_ficheros(ruta_principal, ruta_extra)
    print(str(num_usuarios) + " usuarios, "+str(len(red))+" conexiones")

    porcentaje = float(input("Porcentaje tamaño mayor grumo: "))
    
    #Crear grumos
    crono_inicio = time.time()
    grumos = Grumos(red, num_usuarios)
    grus = grumos.getListaGrumos()

    #Ordenar y seleccionar grumos
    ultimo_grumo = ordenacion_seleccion(grus, porcentaje, num_usuarios)
    print("TIEMPO DE PROCESAMIENTO: " + str(time.time() - crono_inicio) + " seg.")

    #Salvar la lista de nuevas relaciones
    nuevas_conexiones = nuevas_relaciones(grus, ultimo_grumo)
    print("Existen " + str(len(grus)) + " grumos.")
    if len(nuevas_conexiones) == 0:
        print("El mayor grumo contiene " + str(grus[0].tamano)+ " usuarios (" + str(grus[0].tamano/num_usuarios*100)+"%)")
        print("No son necesarias nuevas relaciones de amistad")
    else:
        print("Se deben unir los " + str(ultimo_grumo+1) + " mayores")
        for indice_grumo in range(ultimo_grumo+1):
            print("#"+str(indice_grumo+1)+": "+str(grus[indice_grumo].tamano)+" usuarios ("+str(grus[indice_grumo].tamano/num_usuarios*100)+"%)")

        print("Nuevas relaciones de amistad (salvadas en extra.txt)")
        with open("extra.txt", "w") as salida:
            for conexion in nuevas_conexiones:
                print(str(conexion[0]) + " <-> " + str(conexion[1]))          #Por pantalla
                salida.write(str(conexion[0]) + " "+ str(conexion[1]) + "\n") #Por fichero

if __name__ == "__main__":
    main()