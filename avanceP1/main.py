#para leer el XML
import xml.etree.ElementTree as ET

#para abrir archivos y generar graphviz
import subprocess
from os import startfile


class NodoPatron:
    def __init__(self, codigo, patron):
        self.codigo = codigo
        self.patron = patron
        self.siguiente = None

class NodoPiso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones = ListaEnlazadaPatrones()

    def agregar_patron(self, codigo, patron):
        self.patrones.agregar_nodo(NodoPatron(codigo, patron))

class ListaEnlazadaPatrones:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nodo_patron):
        nodo_patron.siguiente = self.cabeza
        self.cabeza = nodo_patron

    def mostrar_patrones(self):
        actual = self.cabeza
        while actual:
            print(f"Código: {actual.codigo}, Patrón: {actual.patron}")
            actual = actual.siguiente

    def buscar_por_patron(self, codigo_patron):
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo_patron:
                return actual.patron
            actual = actual.siguiente
        return None

    def mostrar_patron(self, codigo_patron):
        patron = self.buscar_por_patron(codigo_patron)
        if patron:
            return patron
        else:
            return None

class ListaEnlazadaPisos:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nodo_piso):
        nodo_piso.siguiente = self.cabeza
        self.cabeza = nodo_piso

    def mostrar_pisos(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}")
            print(f"R: {actual.R}")
            print(f"C: {actual.C}")
            print(f"F: {actual.F}")
            print(f"S: {actual.S}")
            print("Patrones:")
            actual.patrones.mostrar_patrones()
            print()
            actual = actual.siguiente

    def buscar_por_piso(self, nombre_piso):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_piso:
                return actual
            actual = actual.siguiente
        return None

    def mostrar_piso(self, nombre_piso):
        piso = self.buscar_por_piso(nombre_piso)
        if piso:
            print(f"\nMostrar información del piso '{nombre_piso}':")
            print(f"Nombre: {piso.nombre}")
            print(f"R: {piso.R}")
            print(f"C: {piso.C}")
            print(f"F: {piso.F}")
            print(f"S: {piso.S}")
            print("Patrones:")
            piso.patrones.mostrar_patrones()
        else:
            print(f"\nPiso '{nombre_piso}' no encontrado.")

  
    def graficarPatron(self, piso, codigoPatron, nombreArchivo):
        pisoEncontrado= self.buscar_por_piso(piso)
        if pisoEncontrado:
            R=int(pisoEncontrado.R)
            C=int(pisoEncontrado.C)
            F=pisoEncontrado.F 
            S=pisoEncontrado.S

            patronEncontrado=pisoEncontrado.patrones.mostrar_patron(codigoPatron)
            
            #archivo de entrada DOT
            fullNameTxt = nombreArchivo+".dot"

            #imagen de salida
            fullNameImg = nombreArchivo+".jpg"

            if ((R*C)==len(patronEncontrado)):
                cont=0

                try:
                    # Generando código de graphviz en un archivo txt
                    f = open(fullNameTxt, "w")
                    f.write("digraph TablaBasica{\n")
                    f.write("node [shape=plaintext];\n")
                    f.write("Tabla1 [label=<\n")
                    f.write(' <table border="1" cellspacing="0">\n')

                  
                    for y in range(0,R, 1):
                        f.write("<tr>\n")
                       
                        for x in range(0,C,1):
                            if patronEncontrado[cont]=="B":
                                f.write("<td>     </td>\n")
                            if patronEncontrado[cont]=="N":
                                f.write('<td bgcolor="black">     </td>\n')
                            cont+=1
                        f.write("</tr>\n")

                    f.write("</table>>];\n")
                    f.write("}")
                    f.close()
                    
                    # Ejecutando comando para crear la imagen
                    command = ['dot', '-Tjpg', fullNameTxt, '-o', fullNameImg]
                    
                    subprocess.call(command)
                    
                    # Abriendo la imagen
                    startfile(fullNameImg)
                except :        
                    print("Error: .")
                    f.close()

            else:
                print("dimensiones incorrectas")
        else:
            print("No se pudo crear la grafica, piso o patron no encontrado")

# Crear la lista enlazada de pisos
lista_pisos = ListaEnlazadaPisos()

# Agregar nodos (pisos) a la lista principal
piso_ejemplo01 = NodoPiso("ejemplo010", 2, 4, 1, 1)
piso_ejemplo01.agregar_patron("cod11", "BNBNBBBN")
piso_ejemplo01.agregar_patron("cod12", "NBNBBBBB")
piso_ejemplo01.agregar_patron("cod12", "BB")

piso_ejemplo02 = NodoPiso("ejemplo22", 3, 3, 1, 1)
piso_ejemplo02.agregar_patron("cod21", "BNNNBNBBB")
piso_ejemplo02.agregar_patron("cod22", "BBBNBBBN")

piso_ejemplo03 = NodoPiso("ejemplo100", 1, 5, 1000, 1)
piso_ejemplo03.agregar_patron("cod31", "BNNNN")
piso_ejemplo03.agregar_patron("cod32", "NNNBB")

piso_ejemplo04 = NodoPiso("pisojosue", 5, 5, 1000, 1)
piso_ejemplo04.agregar_patron("codigojosue", "BBBBBNNNNNNNNNNBBBBBNBNBN")
piso_ejemplo04.agregar_patron("cod32", "NNNBB")

lista_pisos.agregar_nodo(piso_ejemplo01)
lista_pisos.agregar_nodo(piso_ejemplo02)
lista_pisos.agregar_nodo(piso_ejemplo03)
lista_pisos.agregar_nodo(piso_ejemplo04)


#buscar el archivo XML (ubicacion)
tree = ET.parse('archivo3.xml')

#se obtiene toda la raiza del archivo xml 
root = tree.getroot()

#iterar o recorre el elemento "pisosGuatemala" (esto se hace uno por uno)
for piso in root.findall('piso'):

    #para obtener el nombre de la piso
    nombrePiso=piso.get('nombre')

    #se obtienen los valores de las constantes mencionadas en el enunciado
    valorR=piso.find('R').text.strip()
    valorC=piso.find('C').text.strip()
    valorF=piso.find('F').text.strip()
    valorS=piso.find('S').text.strip()
    variable=NodoPiso(nombrePiso, valorR, valorC, valorF, valorS)

    # Iterar sobre los elementos "patron" dentro de "patrones"
    for patron in piso.findall('.//patron'):
        codigo = patron.get('codigo')
        contenido = patron.text.strip()
        variable.agregar_patron(codigo, contenido)

    lista_pisos.agregar_nodo(variable)

#lista_pisos.mostrar_pisos()


# Menú para que el usuario ingrese piso y patrón
while True:
    print("============================================================")
    print("\nMenú:")
    print("1. Mostrar información de todos los pisos")
    print("2. Buscar por piso")
    print("3. Graficar patron")
    print("4. Salir")
    print("============================================================")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        lista_pisos.mostrar_pisos()
    elif opcion == "2":
        nombre_piso = input("Ingrese el nombre del piso: ")
        lista_pisos.mostrar_piso(nombre_piso)
    elif opcion == "3":
        #METODO PARA GRAFICAR
        lista_pisos.graficarPatron("Banio", "C12","imagen")
        print() 
        
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")