import re
from tabulate import tabulate
import aon


def entrada():
    
    """función que recibe la entrada del teclado que retorna un str"""

    correcto = False
    entrada = ""
    while not correcto:
        try:
            entrada = str(
                input(
                    "------------------------------------------------------------------------------------\nIngrese un comando:\n"
                )
            )
            correcto = True
        except:
            print("Error, en la entrada")

    return entrada
def asterisco(opcion):
    asterisco = False
    if re.search(r"\*", opcion, re.IGNORECASE):
        asterisco = True
    return asterisco
def busca(palabra, opcion):
    if re.search(palabra, opcion, re.IGNORECASE):
        return True
    else: 
        return False
    
tokens=[]
setEnUso=""

def encontrar():
    opcion = entrada()
    #---------------------------1. CREATE SET < ID >
    if re.match(r"CREATE", opcion, re.IGNORECASE) and busca("SET", opcion): 
        print("Match")
        encontrar()
    #***************************2. LOAD INTO < set_id > FILES < id > [ , <id> ] +    
    elif re.match(r"LOAD", opcion, re.IGNORECASE) and busca("INTO", opcion): 
        print("Match")
        encontrar()
    #--------------------------3. USE SET < set_id >    
    elif re.match(r"USE", opcion, re.IGNORECASE) and busca("SET", opcion): 
        
        encontrar()
    #--------------------------4. SELECT < atributo > [ , <atributo>] + [ WHERE < condiciones > ]
    elif re.match(r"SELECT", opcion, re.IGNORECASE): 
        if asterisco(opcion) & busca(" WHERE",opcion):  # SELECCIONAR * DONDE A = "--"

            
            encontrar()
        elif busca("DONDE",opcion):  # SELECCIONAR A, C, D DONDE A = "--"

            
            encontrar()
        elif asterisco(opcion):  # SELECCIONAR *

            #print(tabulate(data, headers="keys", showindex=True, tablefmt="fancy_grid"))  # imprime todos        
            pass
        encontrar()            
    else:
        print("Not a Math!")
        encontrar()
encontrar()
#print(tabulate(aon.adfAON(entrada()), headers="keys", showindex=True, tablefmt="fancy_grid"))
#print(aon.adfAON(entrada()))

