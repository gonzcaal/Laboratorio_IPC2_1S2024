#libreria para el manejo de estructuras json
import json

#abrir el archivo "archivo1.json" y leerlo
with open('archivo1.json') as archivo:
    datos= json.load(archivo)

nombre= datos["persona"]["nombre"]
edad= datos["persona"]["edad"]
ciudad= datos["persona"]["ciudad"]
trabajo= datos["persona"]["trabajo"]
intereses= datos["persona"]["intereses"]
email= datos["persona"]["contacto"]["email"]
telefono= datos["persona"]["contacto"]["telefono"]

print("nombre ", nombre)
print("edad ", edad)
print("ciudad ",ciudad )
print("trabajo ",trabajo )
print("trabajo ", trabajo)
print("intereses ",intereses )
print("email ",email )
print("telefono ", telefono)