from nodoPaciente import Nodo

class ListaPaciente():
    
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def vacia(self):
        return self.inicio == None
    
    def agregarPaciente(self, nombre, columna, fila, inicioX, inicioY, finX, finY):
        Paciente = Nodo(nombre, columna, fila, inicioX, inicioY, finX, finY)
        self.size += 1
        
        if self.vacia():
            self.inicio = self.fin = Paciente
        else:
            aux = self.fin
            self.fin = aux.siguiente = Paciente
        
    def mostrarPacientes(self):
        aux = self.inicio

        while aux != None:
            print("Nombre: ", aux.nombre)
            print("Dimensiones del Paciente: ", aux.columna, "x", aux.fila)
            print("Coordenada de Inicio --> Fila/Columna: ", "(", aux.inicioX, ",", aux.inicioY , ")")
            print("Coordenada de Fin --> Fila/Columna: ", "(", aux.finX, ",", aux.finY , ")")
            print("\n")
            aux = aux.siguiente

    def buscarPaciente(self, nombre):
        aux = self.inicio

        while  aux != None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return None
