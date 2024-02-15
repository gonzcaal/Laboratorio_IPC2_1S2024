class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre= nombre
        self.edad= edad
        self.genero=genero

print("Este es el programa principal")

p1 = Persona("Rebeca", 16, "Femenino")
p2 = Persona ("Alejando", 21, "Masculino")
p3 = Persona ("Ana Paula", 22, "Femenino")
p4 = Persona ("Ricardo", 18, "Masculino")
p5 = Persona ("Romeo", 34, "Masculino")

arreglo= [p1, p2, p3, p4, p5]


for persona in arreglo:
    print("Datos de Persona")
    print("Nombre: ", persona.nombre)
    print("Edad: ", persona.edad)
    print("Genero: ", persona.genero)
    print("  ")
    print("  ")
