import json

#crear un objeto Json 
persona= {
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
#convirtiendo el objeto python a una cadeja JSON
cadena= json.dumps(persona, indent=4)
print()

print (cadena)
print()
print(persona)