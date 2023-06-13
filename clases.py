from clases import Fecha

class Persona:
    def __init__(self, apellido = "" , nombre = "", nacimiento:Fecha = None):
        self.apellido = apellido
        self.nombre = nombre
        self.dia = nacimiento
