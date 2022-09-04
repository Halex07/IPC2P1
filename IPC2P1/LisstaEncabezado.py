from doctest import ELLIPSIS_MARKER
from NodoEncabezado import NodoEncabezado


class ListaEncabezdo:
    def __init__(self, tipo= None) -> None:
        self.tipo = tipo
        self.primero: NodoEncabezado = None
        self.ultimo: NodoEncabezado = None
        self.size = 0

    def insertarEncabezado(self, nuevoEncabezado: NodoEncabezado):
        self.size += 1
        if self.primero == None:
            self.primero = nuevoEncabezado
            self.ultimo = nuevoEncabezado

        else:
            #Insertar en orden
            if nuevoEncabezado.id < self.primero.id:
                nuevoEncabezado.siguiente = self.primero
                self.primero.anterior = nuevoEncabezado
                self.primero = nuevoEncabezado
            elif nuevoEncabezado.id > self.ultimo.id:
                self.ultimo.siguiente = nuevoEncabezado
                nuevoEncabezado.anterior = self.ultimo
                self.ultimo = nuevoEncabezado
            else:
                aux = self.primero

                while aux != None:
                    if nuevoEncabezado.id < aux.id:
                        nuevoEncabezado.siguiente = aux
                        nuevoEncabezado.anterior = aux.anterior
                        aux.anterior.siguiente = nuevoEncabezado
                        aux.anterior = nuevoEncabezado
                        break
                    elif nuevoEncabezado.id > aux.id:
                        aux = aux.siguiente
                    else:
                        break

    def mostrarEncabezado(self):
        aux = self.primero
        while aux != None:
            print("Encabezado de 0 en posicion 1". format(self.tipo, aux.id))


encabezadoFila = ListaEncabezdo("FILAS")
n1=NodoEncabezado


