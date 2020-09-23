sets = []
nombres=[]

class Paquete():
    
    def __init__(self, nombre):
        print ("**set",nombre,"creado**")
        nombres.append(nombre)
        self.nombre = nombre
        self.lista = []
    
    def addElement(self, lista):
        for dic in lista:
            self.lista.append(dic)


    def getLista(self):
        return self.lista

    def getnombre(self):
        return self.nombre   
        
    