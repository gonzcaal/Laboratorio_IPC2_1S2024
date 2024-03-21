from flask import Flask, jsonify, request

app =Flask(__name__)


@app.route('/', methods=['GET'])
def funcion1():
    return jsonify({"valor1": "Hola mundo, estoy en la raiz"})

@app.route('/prueba', methods=['GET'])
def funcion2():
    return jsonify({"mensaje": "Esta es una prueba 2"})

@app.route('/obtenerDatos/', methods=['POST'])
def funcionObtenerDatos():
    datos= request.get_json()

    #obteniendo los datos
    nombre = datos.get('nombre_json')
    apellido = datos.get('apellido_json')
    edad = datos.get('edad_json')
    sexo = datos.get('sexo_json')

    print("Nombre recibido: ", nombre)
    print("Apellido recibido: ", apellido)
    print("Edad recibida: ", edad)
    print("Sexo: ", sexo)

    return jsonify({"status": 200})

@app.route('/enviar-formulario', methods=['POST'])
def recibir_formulario():
    nombre= request.form['nombre']
    correo= request.form['correo']
    mensaje= request.form['mensaje']

    print("Nombre recibido: ", nombre)
    print("correo recibido: ", correo)
    print("mensaje recibido: ", mensaje)

    return jsonify({"status":200})

    

if __name__ == "__main__":
    app.run(port=4700, debug=True)