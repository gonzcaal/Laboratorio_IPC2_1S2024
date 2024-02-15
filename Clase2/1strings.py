cadena  = "ABcDssssSs_12"
cadena2 ="1234___//***''¡¡2'043"
cadenaEjemplo="Introduccion a la programacion y computacion 2"

cMultilinea= '''
Linea1
Linea2
Linea3
'''

print(cadena)
print(cadena2)
print(cMultilinea)

#acceder a un caracter en especifico
print(cadenaEjemplo[0])


#longitud de una cadena
print("Longitud de cadena: ", len(cadena))

print ("####################################################")
#iterar una cadena
for caracter in cadena:
    print (caracter)


print ("####################################################")

for c in range(len(cadena)):
    print(cadena[c])



print ("####################################################")
print(cadena.upper())
print(cadena.lower())
print(cadena.find("1"))

print (cadena)
print(cadena.replace("12", "IPC2_replace"))

print(cadena[0:11])

print(cadena[5:])
