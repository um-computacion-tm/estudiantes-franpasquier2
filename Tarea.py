persona_json_1 = {'nombre':'Indiana', 'apellido':'Jones',}
persona_json_2 = {'nombre':'Marito', 'apellido':'Baracus',}

class Persona:
    def __init__ (self, nombre : str = None, apellido : str = None , diccionario : dict = None):
        if not diccionario is None:
            self.apellido = diccionario.get('apellido')
            self.nombre = diccionario.get('nombre')

        if not nombre is None:
            self.nombre = nombre

        if not apellido is None:
            self.apellido = apellido 
    
    def __repr__(self):
        return f'Persona = nombre = {self.nombre} apellido = {self.apellido}' 

if __name__ == '__main__':
    persona_1 = Persona(diccionario = persona_json_1)
    persona_2 = Persona(nombre = 'Tony', apellido = 'Stark')

    print (persona_1)
    print (persona_2)
        
