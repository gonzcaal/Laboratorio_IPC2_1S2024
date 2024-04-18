from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#ruta para obtener todas las personas
@app.route('/obtenerPersonas', methods=['GET'])
def obtener_personas():
    try:
        with open('archivoSRV.json') as file:
            personas= json.load(file)
        return jsonify (personas)
    except FileNotFoundError:
        return 'Error: no se encuentra el archivo'
    
#ruta para agregar una nueva persona
@app.route('/agregarPersona', methods=['POST'])
def agregar_persona():
    nueva_persona=request.json
    try:
        with open ('archivoSRV.json', 'r') as file:
            personas=json.load(file)
    except FileNotFoundError:
        personas=[]

    personas.append(nueva_persona)


    with open('archivoSRV.json', 'w') as file:
        json.dump(personas, file, indent=4)
    return 'persona agregada correctamente', 201


app.run(debug=True, port=8080)
