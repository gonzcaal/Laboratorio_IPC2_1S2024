class Nodo:
    def __init__(self, valor):
        #atributos que nos van a servir para los nodos
        self.valor =valor
        self.siguiente= None

class ListaSimplementeEnlazada:
    def __init__(self):
        #atributos que nos van a servir para la lista enlazada
        self.inicio = None
        self.final = None
    
    def add(self, valor):
        #sino existe ningun elemento en la lista enlazada hace lo siguiente
        if self.inicio ==None:
            aux = Nodo(valor)
            self.inicio = aux
            self.final = aux
        #si la lista NO esta vacia hace lo siguiente
        else:
            aux = Nodo(valor)
            self.final.siguiente=aux
            self.final=aux

    def printListaEnlazada(self):
        actual =self.inicio
        while actual!=None:
            print(actual.valor)
            print(actual.siguiente)
            print("__________________________________________")
            actual=actual.siguiente

miLista=ListaSimplementeEnlazada()
miLista.add(10)
miLista.add(20)
miLista.add(30)
miLista.add(100.0008)
miLista.add("micasita")
miLista.add(['a', 'b' , 'c'])

miLista.printListaEnlazada()



