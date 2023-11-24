# Juan González Arranz - T1 - ANALISIS DE CARALIBRO
from user_optimized import *

class Grumos(object):
    """Grumos contiene todos los usuarios del sistema y se encarga de llevar a cabo las uniones correspondientes
    a la lista de conexiones."""
    def __init__(self, red, num_usuarios):
        """Creación de los grumos, dada una lista de conexiones (con los identificadores de los usuarios)."""
        #Leemos red creando usuarios y uniendolos de dos en dos
        transformador = MapaTransformador(num_usuarios*15//10) #Factor de carga max. 0.66
        self.usuarios = []
        for num_conexion in range(len(red)):
            usuario_0 = transformador.comprobar(red[num_conexion][0])
            usuario_1 = transformador.comprobar(red[num_conexion][1])
            self.usuarios.append(usuario_0.union(usuario_1))   
            #Solo guardamos la nueva raíz de los dos: el resto son innecesarios una vez unidos los usuarios

    def getListaGrumos(self):
        """Devuelve una lista con los representantes de cada grumo del sistema."""
        grus = []
        for usuario in self.usuarios:
            if usuario.buscar() not in grus:
                grus.append(usuario.buscar()) 
        return grus


#IMPLEMENTACIÓN PARA EL TRANSFORMADOR ENTERO - USUARIO
class NodoMapaTransformador(object):
    """Par llave - valor, siendo la llave el identificador y
     el valor el objeto Usuario correspondiente."""
    def __init__(self, llave):
        self.llave = llave
        self.valor = Usuario(llave)
        self.sig = None #En caso de que haya una colisión


class MapaTransformador(object):
    """Mapa sencillo útil para la creación de los objetos usuarios."""
    def __init__(self, num_elementos):
        self.num_elementos = num_elementos
        self.almacenamiento = [None] * num_elementos
        
    
    def comprobar(self, llave):
        """Comprueba si esa llave ya tiene un Usuario generado. 
        Si no es así, genera un nuevo usuario para esa llave."""
        index = hash(llave) % self.num_elementos
        if self.almacenamiento[index] is None:
            #Creamos un nuevo usuario
            self.almacenamiento[index] = NodoMapaTransformador(llave)
            return self.almacenamiento[index].valor

        #Ya hay un elemento en esa posición
        nodo = self.almacenamiento[index]
        resultado = None
        while resultado is None:
            if nodo.llave == llave:
                resultado = nodo.valor
            else:
                if nodo.sig:
                    nodo = nodo.sig
                else:
                    nodo.sig = NodoMapaTransformador(llave)
                    resultado = nodo.sig.valor

        return resultado