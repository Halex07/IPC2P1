

class transacciones:
    def __init__(self, transaccion = None, nombre=None, tiempoAtencion=None) -> None:
        self.transaccion = transaccion
        self.nombre = nombre
        self.timpoAtencion = tiempoAtencion
        self.siguinte = None
        self.anterior = None
        