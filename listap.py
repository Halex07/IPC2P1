from ptsatencion import ptsatencion

class listap:
    def __init__(self) -> None:
        self.raiz = ptsatencion()
        self.ultimo = ptsatencion()


    def append(self, nuevopuntoAtencion):
        if self.raiz.puntoAtencion is None:
            self.raiz = nuevopuntoAtencion
            self.ultimo = nuevopuntoAtencion
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevopuntoAtencion
            self.ultimo = nuevopuntoAtencion
        else:
            self.ultimo.siguiente = nuevopuntoAtencion
            self.ultimo = nuevopuntoAtencion

    def print(self):
        nodoAux = self.raiz

        cadena = ''

        while True:
            if nodoAux.puntoAtencion is not None:
                cadena += "(" + nodoAux.puntoAtencion + " " + nodoAux.nombre + " " + nodoAux.direccion + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        print(cadena)
