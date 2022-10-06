from listad import listad
from listatransacciones import transacciones
from ptsatencion import ptsatencion

class empresa:
    def  __init__(self,  empresa=None, nombre=None, abreviatura=None)-> None:
        self.empresa = empresa
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.puntoAtencion = ptsatencion()
        self.siguiente = None