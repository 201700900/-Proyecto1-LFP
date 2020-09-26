import re

diccionarios=[]
llaves=[]
atributos=[]


def leer(path):
    try: 
        f = open (path,'r')
        cadena = f.read()
        
        f.close()
        return cadena
    except:
        print(path," no encontrado")
    
    
    
tokens = [] 
letra = "[a-z]"
objAbre = "<"
objCierra = ">"
coma = ","
numero = "[0-9]"
corC = r"]"
tmp = ""

def afdAON(path):
    global atributos
    global llaves
    global diccionarios
    
    diccionarios.clear()
    llaves.clear()
    atributos.clear()
    
    try:
        
        
        
        cadena = leer(path)
        
        lista = list(cadena)
        global tokens
        global tmp
        tipo=0
        comillas=0
        estado=0
        
        for x in lista:
            
            if estado==0:
                
                if x=='(':
                    tokens.append("( - tk_parA")
                    estado = 1
                    continue
                    
            elif estado==1:
                if re.match(objAbre, x):
                    tokens.append("< - tk_objA")
                    atributos.clear()
                    llaves.clear()
                    estado = 2
                    continue
                elif x == ',':
                    tokens.append(", - tkn_coma")
                    estado==1
                    continue
                elif x==')':
                    tokens.append(") - tkn_parCierra")
                    estado = 6
                    continue
                else:
                    continue
            elif estado==2:
                if x=='[':
                    tokens.append("[ - tk_corA")
                    estado = 3
                    continue
                else:
                    continue    
                continue    
            elif estado==3:
                if x ==']':
                    tokens.append(tmp+" - tk_llave")
                    llaves.append(tmp)
                    tokens.append("] - tkn_corCierra")
                    tmp = ""
                    estado = 4
                    continue
                else:
                    tmp+=x
                    estado = 3
                    continue
                continue
                
            elif estado == 4:
                if re.match("=", x):
                    tokens.append("= - tkn_igual")
                    estado = 5
                    continue
            elif estado == 5:
                if x == "." or re.match(numero, x):
                    tmp += x
                    tipo = 1
                    estado=5
                    
                elif re.match(letra,x):
                    tmp += x
                    estado = 5        
                elif x == '"':
                    
                    tokens.append(x+" - tkn_Comillas")
                    comillas+=1
                    estado = 6
                    continue
                
                elif re.match(coma, x):
                    
                    if re.search("true", tmp.strip().lower()):
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_BOOLEAN")
                        atributos.append(True)
                        
                    elif re.search("false", tmp.strip().lower()):
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_BOOLEAN")
                        atributos.append(False)
                    elif tipo == 1:
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_INT")
                        atributos.append(float(tmp))
                    
                
                        
                    tokens.append(", - tkn_coma")
                    tmp = ""
                    estado=2
                elif re.match(objCierra, x):
                    if (re.search("true", tmp.strip().lower())):
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_BOOLEAN")
                        atributos.append(True)
                        pass
                    elif re.search("false", tmp.strip().lower()):
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_BOOLEAN")
                        atributos.append(False)
                        pass
                    elif tipo == 1:
                        tmp=tmp.replace(' ', '')
                        tokens.append(tmp.strip()+" - tkn_INT")
                        atributos.append(float(tmp))
                        
                    
                        
                    tmp = ""    
                    tokens.append("> - tkn_objCierra")
                    
                    diccionarios.append(dict(zip(llaves, atributos)))
                    estado=1    
            elif estado == 6:
                if x == '"':
                    comillas = 0
                    tokens.append(tmp.strip()+" - tkn_STR")
                    tokens.append(x+" - tkn_Comillas")
                    atributos.append(tmp)
                    tmp = ""
                    estado=2
                else:
                    tmp += x
                    estado = 6
                    
        return diccionarios            
    except:
        return diccionarios



