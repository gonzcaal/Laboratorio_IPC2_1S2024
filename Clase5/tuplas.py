#crear tupla
mi_tupla = (1, "dos", 3.0, True,[6,7,8])

#acceder a los elementos de la tupla
print("Elementos de la tupla: ")
for item in mi_tupla:
    print(item, " tipo: ", type(item))

#acceder a un elemento especifico por indice
#posicion2
print("\n Posicion en especifico")
print(mi_tupla[2])

#slice
print ("\n Slice: ", mi_tupla[1:3])


print("cantidad de elementos de la tupla: ", len(mi_tupla))