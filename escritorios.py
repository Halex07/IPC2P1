class escritorios:
    def __init__(self, escritorio=None, idenfificacion=None, encargado=None) -> None:
        self.escritorio=escritorio
        self.identificacion=idenfificacion
        self.encargado=encargado
        self.siguiente=None
        self.anterior=None 