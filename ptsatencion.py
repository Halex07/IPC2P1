

from escritorios import escritorios


class ptsatencion:
    def __init__(self, puntoAtencion = None, nombre=None, direccion=None) -> None:
        self.puntoAtencion = puntoAtencion
        self.nombre = nombre
        self.direccion = direccion
        self.escritorio = escritorios()
        self.siguiente = None
        
