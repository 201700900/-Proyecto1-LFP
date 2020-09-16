class Paquete():
    
    def __init__(self, nombre):
        print ("soy",nombre)
        self.nombre = nombre
        self.lista = []
        
        
lista = ["libros, textos, direcciones"]
objetos=[]
for x in lista:
    nuevo = Paquete(x)       
    objetos.append(nuevo)
    print(objetos)