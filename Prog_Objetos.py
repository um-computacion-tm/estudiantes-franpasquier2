#van las CLASES
class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_calse(self):
        self.asistencia += 1

    
class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado 
        super().__init__(param_nombre, param_email)

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia  += 1

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)
    def cursando(self, materia):
        self.materias_cursando.append(materia)
        
#van los OBJETOS
profesor_Lautaro = Profesor("Lautaro", "l.toneatti@alumno.um.edu.ar", "62395")
print(id(profesor_Lautaro))
print(profesor_Lautaro.nombre)
profesor_Lautaro.cambiar_nombre("Luciana")

print("el nombre es: ")
print(profesor_Lautaro.nombre)
print("el email es: ")
print(profesor_Lautaro.email)
print("Legajo: ")
print(profesor_Lautaro.legajo_empleado)

print("su asistencia es: ")
print(profesor_Lautaro.asistencia)
print("El profesor no se hizo el boludo, vino a clase...")
profesor_Lautaro.asistencia_clase()
profesor_Lautaro.asistencia_clase()
profesor_Lautaro.asistencia_clase()
profesor_Lautaro.asistencia_clase()
profesor_Lautaro.asistencia_clase()
print(profesor_Lautaro.asistencia)
print("    ")

profesor_Lautaro.cambiar_nombre("Luciano")
print(profesor_Lautaro.nombre)

print("   ")

profesor_Franquisia = Profesor("Franquisia", "f.pasquier@alumno.um.edu.ar", "62341")
print(id(profesor_Franquisia))
print(profesor_Franquisia.nombre)
profesor_Franquisia.cambiar_nombre("Francisco")

print("el nombre es: ")
print(profesor_Franquisia.nombre)
print("el email es: ")
print(profesor_Franquisia.email)
print("El legajo es: ")
print(profesor_Franquisia.legajo_empleado)

print("su asistencia es: ")
print(profesor_Franquisia.asistencia)
print("El profesor no se hizo el boludo, vino a clase...")
profesor_Franquisia.asistencia_clase()
profesor_Franquisia.asistencia_clase()
profesor_Franquisia.asistencia_clase()
profesor_Franquisia.asistencia_clase()
profesor_Franquisia.asistencia_clase()
profesor_Franquisia.asistencia_clase()

print(profesor_Franquisia.asistencia)
print("    ")


profesor_Franquisia.cambiar_nombre("Francisco")
print(profesor_Franquisia.nombre)

print("     ")

profesor_Bebote = Profesor("Bebote", "n.lopez@alumno.um.edu.ar", "62132")
print(id(profesor_Bebote)) 
print(profesor_Bebote.nombre)
profesor_Bebote.cambiar_nombre("Nicolas")

print("el nombre es: ")
print(profesor_Bebote.nombre)
print("el email es: ")
print(profesor_Bebote.email)
print("Su legajo es: ")
print(profesor_Bebote.legajo_empleado)

print("su asistencia es: ")
print(profesor_Bebote.asistencia)
print("El profesor no se hizo el boludo, vino a clase...")
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()
profesor_Bebote.asistencia_clase()

print(profesor_Bebote.asistencia)
print("    ")


profesor_Bebote.cambiar_nombre("Nicolas")
print(profesor_Bebote.nombre)

''''
print(id(profesor_Lautaro))
print(profesor_Lautaro.nombre)

print(id(profesor_Franquisia))
print(profesor_Franquisia.nombre)

print(id(profesor_Bebote))
print(profesor_Bebote.nombre)'''
