import re

def script(path):
    comandos=[]
    
    if re.search(".siql", path):
        try: 
            f = open(path, "r")
            comandos = f.readlines()
            f.close()
        except:
            print(path," no encontrado")
        
        
        
        """comandos.clear()
        tmp=""
        lista = list(cadena)
        
        for x in lista:
            if x ==';':
                #comandos.encontrar(tmp)
                comandos.append(tmp)
                tmp=""
                continue
            
            tmp+=x
            continue"""
        
        return comandos
            
    else:
        print("sólo archivos .SIQL permitidos")    
    
