from listatransacciones import transacciones


class clientes:
    def __init__(self, dpi, nombre) -> None:
        self.dpi = dpi
        self.nombre=nombre
        self.transaccion = transacciones()

        