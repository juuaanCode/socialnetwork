# Juan González Arranz - T1 - ANALISIS DE CARALIBRO
class Usuario(object):
    """Representa a un usuario del sistema (y de un grumo). 
    Basado en el TAD de Disjoint-Set."""
    def __init__(self, identificador):
        """Crea un objeto Usuario desde un identificador"""
        self.identificador = identificador
        self.padre = self
        self.tamano = 1


    def buscar(self):
        """Devuelve el objeto representativo del grumo que contiene al usuario."""
        #Usando compresión de camino
        if self.padre is not self:
            self.padre = self.padre.buscar()
        return self.padre


    def union(self, usuario_2):
        """Crea una unión entre los dos usuarios, fusionando los grumos. 
        Se retorna la raíz para optimizar la creación de la lista de grumos."""
        raiz_1 = self.buscar()
        raiz_2 = usuario_2.buscar()

        if raiz_1 is not raiz_2: #¿Están en el mismo grumo?
            #Usando unión por tamaño
            if raiz_1.tamano < raiz_2.tamano: 
                raiz_1, raiz_2 = raiz_2, raiz_1
            
            raiz_2.padre = raiz_1
            raiz_1.tamano += raiz_2.tamano

        return raiz_1
    

    def __str__(self):
        return format(self.identificador)