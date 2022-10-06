from escritorios import escritorios
from ptsatencion import ptsatencion
from listatransacciones import transacciones

class listad:
    def __init__(self) -> None:
        self.raiz = escritorios()
        self.ultimo = escritorios()


    def append(self, nuevoescritorio):
        if self.raiz.escritorio is None:
            self.raiz = nuevoescritorio
            self.ultimo = nuevoescritorio
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoescritorio
            self.ultimo = nuevoescritorio
        else:
            self.ultimo.siguiente = nuevoescritorio
            self.ultimo = nuevoescritorio

    def print(self):
        nodoAux = self.raiz

        cadena = ''

        while True:
            if nodoAux.escritorio is not None:
                cadena += "(" + nodoAux.escritorio + " " + nodoAux.identificacion + " " + nodoAux.encargado + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        print(cadena)

        

    
    




