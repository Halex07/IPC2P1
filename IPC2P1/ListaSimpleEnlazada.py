from pruebas import pruebas

class ListaSimpleEnlazada():
    def __init__(self):
        self.raiz = pruebas()
        self.ultimo  = self.raiz
    
    def append(self, nuevopruebas):
        if self.raiz.nombre is None:
            self.raiz = nuevopruebas
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevopruebas
            self.ultimo = nuevopruebas
        else:
            self.ultimo.siguiente = nuevopruebas
            self.ultimo = nuevopruebas
    
    def printListaSimpleEnlazada(self):
        nodoAux = self.raiz

        cadena = ''
        while True:
            if nodoAux.nombre is not None:
                cadena += "(" + nodoAux.nombre + " " + nodoAux.edad + " " + nodoAux.nacionalidad + ")"
                if nodoAux.siguiente is not None:
                    cadena += " -> "
                    nodoAux =  nodoAux.siguiente
                else:
                    break
            else:
                break
        print(cadena)
    
    def buscarpruebas(self, nombre):
        nodoAux = self.raiz

        while nodoAux.nombre != nombre:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux
    