
arregloset = []  #      arreglo de set

salir = False

class Objeto_Set():
    def __init__(self, nombreSet):      #este es el que le pone el nombre, el __init__
        self.nameSet = nombreSet
        self.list_ESet = []

    def addElement(self, objetoesto):
        self.list_ESet.append(objetoesto)


    def getlist(self):
        return self.list_ESet

    def getnombre(self):
        return self.nameSet


for i in range(3):
    x = input("agregar el nombre a la lista")
    nuevoElemento = Objeto_Set(x)     #agrego el nombre al objeto
    arregloset.append(nuevoElemento)  # agregarlo al arreglo
    print(arregloset)                        #imprimir arreglo, pero me va a dar un ubjeto, si quiero el nombre 
                                        #coloco los set o gets


#para imprimirlo
for i in range(3):
    elementolista = arregloset[i]       # hago un parseo al objeto
    print(elementolista.getnombre())      # imprimo el nombre, y asi se puede tambien sacar la lista etc.