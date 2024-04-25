from flask import Flask, request, jsonify, send_file
import os
from xml.etree import ElementTree as ET

app = Flask(__name__)

contenido_xml=None
contenido_xml="abc"


#ruta para borrar las mascotas
@app.route ('/borrar-datos', methods=['DELETE'])
def borrar_datos():
    global contenido_xml
    print ("contenido: ", contenido_xml)

    contenido_xml=None
    print ("contenido: ", contenido_xml)

    return jsonify({'message':'Datos de mascotas borrados correctamente'})

#ruta para cargar el archivo XML
@app.route ('/cargar-xml', methods=['POST'])
def cargar_xml():
    global contenido_xml
    file = request.files['file']

    # se lee el contenido y se almacena en la variable global
    contenido_xml= file.read() 
    print ("contenido: ", contenido_xml)
    return jsonify({'message':'XML cargado correctamente'})


#ruta para cargar procesar los datos
@app.route ('/procesar-datos', methods=['GET'])
def procesar_datos():
    global contenido_xml
    if contenido_xml is None:
        return jsonify({'error': 'No hay XML cargado'})
    # parsear el archivo XML y lo filtramos por perros gatos conejos
    root = ET.fromstring(contenido_xml)
    animales=[]

    for animal in root:
        if animal.tag in ['perro', 'gato', 'conejo']:
            animal_info={}
            for child in animal:
                animal_info[child.tag]=child.text
            animales.append(animal_info)
    print("animales: ", animales)
    return jsonify(animales)

if __name__ == '__main__':
    app.run(debug=True, port=5000)