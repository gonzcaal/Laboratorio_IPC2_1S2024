import xml.etree.ElementTree as ET

#buscar el archivo XML (ubicacion)
tree = ET.parse('archivo_entrada.xml')

#se obtiene toda la raiza del archivo xml 
root = tree.getroot()

#iterar o recorre el elemento "senal" (esto se hace uno por uno)
for senal in root.findall("senal"):

    #para obtener el nombre de la senal
    nombre=senal.get('nombre')

    #buscar color
    color = senal.get("color")
    print(nombre)
    print (color)
    print()


    #iterar cada elemento "dato", que esta dentro de cada "senal"
    for dato in senal.findall("dato"):
        tiempo  = dato.get('t')
        amplitud= dato.get('A')
        valor= dato.text
        print("tiempo: ", tiempo, " amplitud: ", amplitud, " VALO INTERNO: ", valor)
        

