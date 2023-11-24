# Juan González Arranz - T1 - ANALISIS DE CARALIBRO
import time

def lectura_ficheros(ruta_principal, ruta_extra):
    # ENT: Las rutas de los ficheros de datos.
    # SAL: La lista con todas las conexiones del sistema y el número de usuarios.
    cadenas_conexiones = []
    with open(ruta_principal) as fichero: 
        cadenas_conexiones = fichero.readlines()
    num_usuarios = int(cadenas_conexiones[0][:-1])

    #Creacion de la estructura red
    red = []
    for fila in range(2, len(cadenas_conexiones)):
        red.append([int(numero) for numero in cadenas_conexiones[fila].split()])

    #Fichero de conexiones extra
    cadenas_conexiones = []
    if ruta_extra != "":
        with open(ruta_extra) as fichero:
            cadenas_conexiones = fichero.readlines()
        for fila in range(len(cadenas_conexiones)):
            red.append([int(numero) for numero in cadenas_conexiones[fila].split()])
    return red, num_usuarios

def crear_usr(red):
    # ENT: La red de usuarios.
    # SAL: Lista que contiene todos los usuarios del sistema.
    usr = []
    for par_de_usuarios in red:
        if par_de_usuarios[0] not in usr:   #Si alguno de los dos usuarios no están en usr se les añade
            usr.append(par_de_usuarios[0])
        if par_de_usuarios[1] not in usr:
            usr.append(par_de_usuarios[1])
    return usr

def crear_grumos(red, usr):
    # ENT: La lista de conexiones (red) y la lista de usuarios.
    # SAL: La lista de grumos de la red.
    grus = []   #Lista de grumos (listas de usuarios)
    asig = []   #Lista de usuarios ya analizados
    for usuario in usr:
        if usuario not in asig:
            grumo = uber_amigos(usuario, red, [usuario])
            grus.append(grumo)
            asig.extend(grumo)
    return grus

def uber_amigos(usuario, red, grumo):
    # ENT: El usuario que se debe analizar, la lista de conexiones y el grumo que se debe hacer crecer.
    # SAL: El grumo que contiene al usuario y todos los usuarios con los que se relaciona.
    for pareja in red:
        if usuario == pareja[0] and pareja[1] not in grumo:
                grumo.append(pareja[1])
                uber_amigos(pareja[1], red, grumo)
        if usuario == pareja[1] and pareja[0] not in grumo:
                grumo.append(pareja[0])
                uber_amigos(pareja[0], red, grumo)
    return grumo

def ordenacion_seleccion(grus, porcentaje, num_usuarios):
    # ENT: La lista de grumos, el porcentaje que buscamos en el grumo más grande y el número total de usuarios.
    # SAL: La lista de grumos ordenada y el índice del último grumo a combinar.
    grus.sort(reverse=True,key=len)  #Ordenamos según la cantidad de elementos que tengan, de mayor a menor
    ultimo_grumo = 0
    tamano_acumulado = len(grus[0])
    while ((tamano_acumulado / num_usuarios)*100 < porcentaje) and (ultimo_grumo < len(grus)-1):
        ultimo_grumo += 1
        tamano_acumulado += len(grus[ultimo_grumo])
    return grus, ultimo_grumo
    
def nuevas_relaciones(grus, ultimo_grumo):
    # ENT: La lista de grumos y el índice del último grumo.
    # SAL: La lista de las conexiones necesarias.
    nuevas_conexiones = []
    for indice_grumo in range(ultimo_grumo):
        nuevas_conexiones.append([grus[indice_grumo][0], grus[indice_grumo+1][1]])
    return nuevas_conexiones

def main():
    print("ANALISIS DE CARALIBRO")
    print("---------------------")
    
    #Lectura del fichero principal
    ruta_principal = input("Fichero principal: ") 
    ruta_extra = input("Fichero de nuevas conexiones (pulse enter si no existe):  ") 
    crono_inicio = time.time()
    red, num_usuarios = lectura_ficheros(ruta_principal, ruta_extra)
    crono_fin = time.time()
    print(str(num_usuarios) + " usuarios, "+str(len(red))+" conexiones")
    print("Lectura fichero: " + str(crono_fin - crono_inicio) + " seg.")

    porcentaje = float(input("Porcentaje tamaño mayor grumo: "))
    
    #Creación de la lista de usuarios
    crono_inicio = time.time()
    usr = crear_usr(red) 
    crono_fin = time.time()
    print("Creacion lista usuarios: " + str(crono_fin - crono_inicio) + " seg.")


    #Creación de la lista de grumos
    crono_inicio = time.time()
    grus = crear_grumos(red, usr)    
    crono_fin = time.time()
    print("Creacion lista grumos: " + str(crono_fin - crono_inicio) + " seg.")
    

    #Ordenación y selección de los grumos
    crono_inicio = time.time()
    grus, ultimo_grumo = ordenacion_seleccion(grus, porcentaje, num_usuarios)
    crono_fin = time.time()
    print("Ordenación y selección de grumos: " + str(crono_fin - crono_inicio) + " seg.")
    print("Existen " + str(len(grus)) + " grumos.")


    #Salvar la lista de nuevas relaciones
    nuevas_conexiones = nuevas_relaciones(grus, ultimo_grumo)
    if len(nuevas_conexiones) == 0:
        print("El mayor grumo contiene " + str(len(grus[0]))+ " usuarios (" + str(len(grus[0])/num_usuarios*100)+"%)")
        print("No son necesarias nuevas relaciones de amistad")
    else:
        print("Se deben unir los " + str(ultimo_grumo+1) + " mayores")
        for indice_grumo in range(ultimo_grumo+1):
            print("#"+str(indice_grumo+1)+": "+str(len(grus[indice_grumo]))+" usuarios ("+str(len(grus[indice_grumo])/num_usuarios*100)+"%)")

        print("Nuevas relaciones de amistad (salvadas en extra.txt)")
        with open("extra.txt", "w") as salida:
            for conexion in nuevas_conexiones:
                print(str(conexion[0]) + " <-> " + str(conexion[1]))          #Por pantalla
                salida.write(str(conexion[0]) + " "+ str(conexion[1]) + "\n") #Por fichero

if __name__ == "__main__":
    main()