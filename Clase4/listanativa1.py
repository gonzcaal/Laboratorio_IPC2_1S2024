listaVacia=[]

listaNumeros= [1,2,3,4,5,6,7,8,9]
listaCaracteres=['a', 'b','c']
listaDecimales=[1.1, 3.3, 100.1222, -23.05]
listaListas=[[1,2,3,4,5,6,7,8,9], ['a', 'b','c'], [1.1, 3.3, 100.1222, -23.05]]


print("LISTA_VACIA_________________________________")
print(listaVacia)

print("agregar elemento a la lista vacia")
listaVacia.append("JOsue")
listaVacia.append(12222)
listaVacia.append("Micasita")
print(listaVacia)

print("Eliminar elemento de la lista vacia")
listaVacia.pop(0)
print("lista sin ultimo elemento")
print(listaVacia)
print()


print("acceder a un elemento caracteres_______________________________")
print(listaCaracteres[2])
print()


print("LISTA_NUMEROS_______________________________")
print(listaNumeros)
print()

print("LISTA_CARACTERES____________________________")
print(listaCaracteres)
print()

print("LISTA_DECIMALES_____________________________")
print(listaDecimales)
print()

print("LISTA_DE_LISTAS_____________________________")
print(listaListas)
print()


print("RECORRER LISTA_DECIMALES_____________________________")

for item in listaDecimales:
    print(item)
    
print("recorrer lista de listas____________________________")

for item1 in listaListas:
    print(item1[0])