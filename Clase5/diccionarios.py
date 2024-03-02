#crear un diccionario
mi_diccionario = {}
print(type(mi_diccionario))

#agregar elementos al diccionario
mi_diccionario['nombre']= 'Josue'
mi_diccionario['edad']= 27
mi_diccionario['ciudad']='Guatemala'
mi_diccionario['apellido']= "Gonzalez"

#acceder a los valores mediante las claves
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])
print(mi_diccionario['ciudad'])

print("\n _________________________________")

#edita un elemento por medio de su clave
mi_diccionario['edad']=25
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])
print(mi_diccionario['ciudad'])
print("\n _________________________________")


#imprimir el diccionario completo
print (mi_diccionario)

#verificar si una clave existe en el diccionario
if 'apellido' in mi_diccionario:
    print("El apellido es: ", mi_diccionario['apellido'])
else:
    print("la clave 'apellido' no existe en el diccionario")
    
#eliminar un elemento a travez de la clave
del mi_diccionario['edad']
print(mi_diccionario)