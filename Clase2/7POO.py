class Persona:
    def __init__(self, CUI, nombre, edad):
        self.CUI=CUI
        self.nombre=nombre
        self.edad=edad
    
class Profesor(Persona):
    def __init__(self, CUI, nombre, edad, designacion, titulo):
        super().__init__(CUI, nombre, edad)       
        self.designacion=designacion
        self.titulo = titulo

class Estudiante(Persona):
    def __init__(self, CUI, nombre, edad, carnet, carrera):
        super().__init__(CUI, nombre, edad)
        self.carnet=carnet
        self.carrera= carrera

profesor1= Profesor(123456, "Josue Gonzalez", 27, "Matematica1", "Enseñanza media")
print("El CUI del profesor1 es: ", profesor1.CUI)
print(type(profesor1))
print(type(profesor1.CUI))

print("___________________________________")

print("El nombre del profesor1 es: ", profesor1.nombre)
print(type(profesor1))
print(type(profesor1.nombre))



print("___________________________________")
estudiante1= Estudiante(789456, "Camila Ramirez", 32, 2016487, "Ingenieria en Ciencias y sistemas")
estudiante2= Estudiante(78945645, "Rocio Ramirez", 18, 785544, "Ingenieria Mecanica")
estudiante3= Estudiante(11111, "Carlos del Valle", 24, 222222, "Ingenieria Civil")


arregloEstudiantes=[estudiante1, estudiante2, estudiante3]

for item in arregloEstudiantes:
    print("El CUI del estudiante es: ", item.CUI)
    print("El nombre del estudiante es: ", item.nombre)
    print("La carrera del estudiante es: ", item.carrera)
    print("___________________________________")

