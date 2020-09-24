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
        
        return comandos
            
    else:
        print("sólo archivos .SIQL permitidos")    
    
