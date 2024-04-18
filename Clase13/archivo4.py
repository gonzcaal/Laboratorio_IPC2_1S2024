import json

personas=[
    {
        "nombre": "Josue",
        "edad": 27,
        "ciudad" :"Ciudad de Guatemala",
        "trabajo": "Ingeniero en Sistemas",
        "intereses": ["Programacion", "animales", "viajes", "comida"],
        "contacto": {
            "email": "gonzcaal@gmail.com",
            "telefono":"47913289"
        }
    }, 
    {
        "nombre": "kevin",
        "edad": 12,
        "ciudad" :"Ciudad de Guatemala",
        "trabajo": "Ingeniero en Sistemas",
        "intereses": ["Programacion", "animales", "viajes", "comida"],
        "contacto": {
            "email": "kevin@gmail.com",
            "telefono":"47914553289"
        }
    }, {
        "nombre": "Rocio",
        "edad": 24,
        "ciudad" :"Ciudad de Guatemala",
        "trabajo": "Ingeniero en Sistemas",
        "intereses": ["Programacion", "reposteria", "viajes", "comida"],
        "contacto": {
            "email": "rocio@gmail.com",
            "telefono":"122313"
        }
    }
   ]

json_array= json.dumps(personas)

print (json_array)