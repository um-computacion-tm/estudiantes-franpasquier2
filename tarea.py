cliente1 = {'nombre':'Nico', 'apellido':'Tellez'}
cliente2 = {'nombre':'Facu', 'apellido':'Messa'}

class ordenador:
    def por_nacimiento(self, personas):
        for externo in range(0, len(personas)-1):
            for interno in range(1, len(personas)):
                if personas[externo].compareTo(personas[interno])>0:
                    personas[externo], personas[interno] = personas[interno], personas[externo] 

class Fecha:
    def compareTo(self, fecha):
        fecha1 = ((self.anho * 100) + self.mes) * 100 + self.dia
        fecha2 = ((fecha.anho * 100) + fecha.mes) * 100 + fecha.dia
        return fecha1 - fecha2


class Persona:
    def __init__(self, persona : dict):
        self.nombre = persona.get('nombre')
        self.apellido = persona.get('apellido')

    def compareTo(self, persona):
        return self.nacimiento.compareTo(persona.nacimiento)

    def __init__ (self, nombre ="", apellido =""):
        self.nombre = nombre
        self.apellido = apellido 

    def __repr__ (self):
        return f"->Persona: [nombre] = {self.nombre} [apellido] = {self.apellido}"
    


if __name__ == '__main__':
    '''p1 = Persona(cliente1)
    p2 = Persona(cliente2)
    print(p1)
    print(p2)
    p3=p1
    p3.nombre = "Jorgito"
    print(p1)'''

Ordenador = ordenador()
personas = []
personas.append(Persona(nombre = 'Bruce', apellido = 'Wayne', nacimiento = Fecha(1925, 4, 2)))
personas.append(Persona(nombre = 'Clarck', apelldio = 'Kent', nacimiento = Fecha(1944, 6, 1)))
personas.append(Persona(nombre ='Barry', apellido = 'Allen', nacimiento = Fecha(1978, 2, 28)))
personas = ordenador.por_nacimiento(personas)
print(personas)
