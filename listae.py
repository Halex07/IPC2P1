from empresas import empresa

class listaEmpresa:
    def __init__(self) -> None:
        self.raiz = empresa()
        self.ultimo = empresa()


    def append(self, nuevaempresa):
        if self.raiz.empresa is None:
            self.raiz = nuevaempresa
            self.ultimo = nuevaempresa
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaempresa
            self.ultimo = nuevaempresa
        else:
            self.ultimo.siguiente = nuevaempresa
            self.ultimo = nuevaempresa

    def print(self):
        nodoAux = self.raiz

        cadena = ''

        while True:
            if nodoAux.empresa is not None:
                cadena += "(" + nodoAux.empresa + " " + nodoAux.nombre + " " + nodoAux.abreviatura + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        print(cadena)
