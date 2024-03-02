def abrir_o_crear_archivo(nombre_de_archivo):
    try:
        with open(nombre_de_archivo, 'r') as archivo:
            contenido= archivo.read()
            print ("Contenido del archivo: ", nombre_de_archivo)
            print(contenido)
        

    except FileNotFoundError:
        print ("El archivo", nombre_de_archivo, " no existe pero se va a crear...")
        with open (nombre_de_archivo, 'w') as archivo:
            contenido=""
            
    return contenido

def escribir_archivo(nombre_de_archivo, nuevo_contenido):
    with open(nombre_de_archivo, 'w') as archivo:
        archivo.write(nuevo_contenido)
        print("Se agrego correctamente al archivo")
 
nombreArchivo= "file.txt"

contenido=abrir_o_crear_archivo(nombreArchivo)
escribir_archivo(nombreArchivo, "Primea Linea\tSegunda Linea\ntercera Linea")