

from empresas import empresa


class confinicial:
    def __init__(self, id=None, idEmpresa=None, idPunto=None) -> None:
        self.id = id
        self.idEmpresa = idEmpresa
        self.idPunto = idPunto
        self.empresa = empresa()
        