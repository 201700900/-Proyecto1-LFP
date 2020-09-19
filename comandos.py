import re
from tabulate import tabulate
import aon
import createSet
import automatas
import math
from colorama import Back, Fore, init
init()


#BLUE, RED, GREEN, YELLOW, ORANGE y PINK
        
    
def entrada():
    
    """función que recibe la entrada del teclado que retorna un str"""

    correcto = False
    entrada = ""
    while not correcto:
        #try:
        entrada = str(input("------------------------------------------------------------------------------------\nIngrese un comando:\n"))
        encontrar(entrada)
        if entrada.lower()=='salir':
            correcto = True
        #except:
        #    print("Error, en la entrada")

    
def asterisco(opcion):
    asterisco = False
    if re.search(r"\*", opcion, re.IGNORECASE):
        asterisco = True
    return asterisco

    

setEnUso=""
def Lista_Usando():
    if setEnUso!="":
        for obj in createSet.sets:
            if obj.getnombre()==setEnUso:
                return obj.getLista()
                break
            else:
                print("SET ",setEnUso," no encontrado")
            break        
    else:
        print("seleccione el SET a usar")


def encontrar(opcion):
    global setEnUso
    
    #---------------------------1. CREATE SET < ID >
    if re.match(r"CREATE", opcion, re.IGNORECASE) and automatas.busca("SET", opcion): 
        automatas.create_Set(opcion)
        lista = opcion.split()
        nuevo = createSet.Paquete(lista[-1])
        createSet.sets.append(nuevo)
        for obj in createSet.sets:
            print(obj.getnombre())

    #***************************2. LOAD INTO < set_id > FILES < id > [ , <id> ] +    
    elif re.match(r"LOAD", opcion, re.IGNORECASE) and automatas.busca("INTO", opcion):
        try: 
            listaLoad=[]
            listaLoad = automatas.load(opcion)
            archivos = listaLoad[1]
            for path in archivos:
                diccionario = aon.afdAON(path)
                for obj in createSet.sets:
                    if obj.getnombre()==listaLoad[0]:
                        obj.addElement(diccionario)
                        print(tabulate(obj.getLista(), headers="keys", showindex=True, tablefmt="fancy_grid"))
                        break
                    else: 
                        print("El set ",listaLoad[0]," no existe")
        except IndexError:
            print("error en la carga")            
            
    #--------------------------3. USE SET < set_id >    
    elif re.match(r"USE", opcion, re.IGNORECASE) and automatas.busca("SET", opcion):
        seUsa = automatas.use_Set(opcion)
        if len(createSet.sets)==0:
            print("Ningun set creado aún")
    
        for obj in createSet.sets:
            
            if obj.getnombre()==seUsa:
                setEnUso = seUsa
                print("**usando set ",seUsa,"**")
                break
            else:
                print("set",seUsa, "no creado aún")    

    #--------------------------4. SELECT < atributo > [ , <atributo>] + [ WHERE < condiciones > ]
    elif re.match(r"SELECT", opcion, re.IGNORECASE): 
        if asterisco(opcion) & automatas.busca(" WHERE",opcion):  # SELECT * WHERE A = "--"
            pass
            
    
        elif automatas.busca("WHERE",opcion):  # SELECT A, C, D WHERE A = "--"
            pass
            
    
        elif asterisco(opcion):  # SELECT *
            try:
                print(tabulate(Lista_Usando(), headers="keys", showindex=True, tablefmt="fancy_grid"))  # imprime todos        
            except:
                print("ERROR")    
        
            
    #--------------------------5. LIST ATTRIBUTES
    elif re.match(r"LIST", opcion, re.IGNORECASE) and automatas.busca("ATTRIBUTES", opcion):
        print("USANDO SET",setEnUso)
        automatas.list_Atrubutes(opcion)
        try:
            dic = (Lista_Usando())
            d=dic[0]
            key=list(d.keys())
            print(key)
            print(type(key))
            
        except:
            print("Error")    


    #--------------------------6. PRINT IN <color>    
    elif re.match(r"PRINT", opcion, re.IGNORECASE) and automatas.busca("IN", opcion):
        
        com = opcion.split()
        if len(com)==3:
            color = automatas.print_in(opcion)
            if color.lower() == "blue":
                print(Back.RESET + Fore.BLUE + "BLUE")
            elif color.lower() == "red":
                print(Back.RESET + Fore.RED + "RED")
            elif color.lower() == "green":
                print(Back.RESET + Fore.GREEN + "GREEN")        
            elif color.lower() == "yellow":
                print(Back.RESET + Fore.YELLOW + "YELLOW")     
            elif color.lower() == "orange":
                print(Back.RED + Fore.YELLOW + "ORANGE")
            elif color.lower() == "pink":
                print(Back.RESET + Fore.MAGENTA + "PINK")
            else:
                print("color no aceptado")    
        else:
            print("introduzca el color")
    
    #--------------------------7. MAX < atributo > | MIN < atributo >        
    elif re.match(r"MIN|MAX", opcion, re.IGNORECASE):
        min_max=automatas.min_max(opcion)
        valores=[]
        try:
            for dic in Lista_Usando():
                valor = dic.get(min_max[1], "")
                valores.append(valor)
        
            try:            
                if min_max[0].lower()=='min':
                    print("MIN DE",min_max[1],"=",min(valores))
                elif min_max[0].lower()=='max':
                    print("MAX DE",min_max[1],"=",max(valores))
            except:
                print(valor, "no encontrado")        
        except:
            print("error")
        
    #--------------------------8. SUM < atributo > [, <atributo> ] +    
    elif re.match(r"SUM", opcion, re.IGNORECASE):
        sumas=automatas.sum_(opcion)
        if sumas[0]=='*':
            dic = (Lista_Usando())
            d=dic[0]
            
            sumas=list(d.keys())
        
        salida=[]
        #try:
        for at in sumas:
            resultado=0
            try:
                for dic in Lista_Usando():
                    
                    valor = dic.get(at, "")
                    
                    resultado = resultado + valor
            except:
                pass
            salida.append({at:resultado})
                        
                        
        print(tabulate(salida, headers="keys", tablefmt="fancy_grid"))
        for d in salida:
            print(d)        
        #except:
        #    print("error")
        
        
    #--------------------------9. COUNT < atributo > [, < atributo > ] +    
    elif re.match(r"COUNT", opcion, re.IGNORECASE):
        cuentas = automatas.count(opcion)
        if cuentas[0]=='*':
            dic = (Lista_Usando())
            d=dic[0]
            
            cuentas=list(d.keys())
        
        salida=[]
        for c in cuentas:
            for dic in Lista_Usando():
                
                print("número de registros cargados = " + str(len(data)))
        pass      
    else:
        print("Not a Math!")
        

#print(tabulate(aon.adfAON(entrada()), headers="keys", showindex=True, tablefmt="fancy_grid"))
#print(aon.adfAON(entrada()))

entrada()