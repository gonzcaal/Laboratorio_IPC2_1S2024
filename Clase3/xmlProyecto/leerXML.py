import xml.etree.ElementTree as ET

#buscar el archivo XML (ubicacion)
tree = ET.parse('entrada.xml')

#se obtiene toda la raiza del archivo xml 
root = tree.getroot()


#iterar o recorre el elemento "pisosGuatemala" (esto se hace uno por uno)
for piso in root.findall('piso'):
    print("___________________________________________________________")
    #para obtener el nombre de la piso
    nombrePiso=piso.get('nombre')

    #se obtienen los valores de las constantes mencionadas en el enunciado
    valorR=piso.find('R').text.strip()
    valorC=piso.find('C').text.strip()
    valorF=piso.find('F').text.strip()
    valorS=piso.find('S').text.strip()

    print("Nombre del Piso: ", nombrePiso)
    print("R: ", valorR)
    print("C: ", valorC)
    print("F: ", valorF)
    print("S: ", valorS)


    # Iterar sobre los elementos "patron" dentro de "patrones"
    for patron in piso.findall('.//patron'):
        codigo = patron.get('codigo')
        contenido = patron.text.strip()
        print("     Patron:", codigo, "Contenido: ", contenido)
    




