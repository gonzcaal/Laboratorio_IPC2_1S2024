import json
json_string='''{
    "persona":{
        "nombre": "Josue",
        "edad": 27,
        "ciudad" :"Ciudad de Guatemala",
        "trabajo": "Ingeniero en Sistemas",
        "intereses": ["Programacion", "animales", "viajes", "comida"],
        "contacto": {
            "email": "gonzcaal@gmail.com",
            "telefono":"47913289"
        }
    }
}'''


#analizar el texto y parsearlo a una estructura json
datos = json.loads(json_string)

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