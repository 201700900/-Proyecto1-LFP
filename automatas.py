import re
from tabulate import tabulate
import webbrowser
import createSet
import seleccionar
import pandas as pd 



tokens = []
def busca(palabra, opcion):
    if re.search(palabra, opcion, re.IGNORECASE):
        return True
    else: 
        return False
    
tkn_create = {"token":"CREATE", "lexema":"CREATE", "descripcion":"Comando que crea nuevos elementos en memoria"}
tkn_set = {"token":"SET", "lexema":"SET", "descripcion":"elemto en memoria donde se alojan ciertos conjuntos de datos cargados por el usuario."}
def tkn_name_SET(nombre):
    return {"token":"NOMBRE SET", "lexema": nombre, "descripcion":"Nombre de un SET"} 
    
def create_Set(opcion):
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        
        if estado == 0:
            if tmp.lower() == 'create':
                tokens.append(tkn_create)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'set':
                tokens.append(tkn_set)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue
        elif estado == 2:
            if x==';':
                tokens.append(tkn_name_SET(tmp))
                return tmp.lower()
                break
            if x !=' ':
                tmp+=x
                continue
            continue
            

tkn_load = {"token":"LOAD", "lexema":"LOAD", "descripcion":"Comando que carga elementos en el set en memoria."}
tkn_into = {"token":"INTO", "lexema":"INTO", "descripcion":"Palabra reservada que indica en qué set en memoria se ingresa los elementos a cargar."}
tkn_files = {"token":"FILES", "lexema":"FILES", "descripcion":"Palabra reservada que indica los archivos que se van a cargar a memoria."}
tkn_coma = {"token":"coma", "lexema":",", "descripcion":"signo que indica la separación de dos nombres de archivos o atributos."}
def tkn_name_Archivo(nombre):
    return {"token":"ARCHIVO AON", "lexema": nombre, "descripcion":"Nombre de archivo de tipo .AON."} 

def load(opcion):
    estado=0
    tmp=""
    salida = []
    archivos=[]
    index = 0
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        
        if estado == 0:
            if tmp.lower() == 'load':
                tokens.append(tkn_load)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'into':
                tokens.append(tkn_into)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue
        elif estado == 2:
            if x==' ':
                tokens.append(tkn_name_SET(tmp))
                salida.append(tmp.lower())
                tmp=""
                estado=3 
                continue
            
            
            tmp+=x
            estado=2
            continue
        elif estado == 3:
            if tmp.lower() == 'files':
                tokens.append(tkn_files)
                tmp=""
                estado=4 
                continue
            
            if x!=' ':
                tmp+=x
                continue
        elif estado == 4:
            if x==';':
                tokens.append(tkn_name_Archivo(tmp))
                archivos.append(tmp)
                break
            if x == ',':
                tokens.append(tkn_name_Archivo(tmp))
                tokens.append(tkn_coma)
                
                archivos.append(tmp)
                tmp=""
                estado = 4
                continue
            
            if x !=' ':
                tmp+=x
                continue
            continue
    salida.append(archivos)        
    return salida       

tkn_use = {"token":"USE", "lexema":"USE", "descripcion":"Comando que indica el set que se va a estar usando para los comandos"}
                
def use_Set(opcion):
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        
        if estado == 0:
            if tmp.lower() == 'use':
                tokens.append(tkn_create)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'set':
                tokens.append(tkn_set)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue
        elif estado == 2:
            if x==';':
                tokens.append(tkn_name_SET(tmp))
                return tmp
                break
            if x !=' ':
                tmp+=x
                continue
            continue 

tkn_select={"token":"SELECT", "lexema":"SELECT", "descripcion":"Comando la seleccion de un set mostrandola en pantalla"}
tkn_asterisco={"token":"asterisco", "lexema":"*", "descripcion": "automáticamente selecciona todos los campos del registro."}
tkn_where={"token":"WHERE", "lexema":"WHERE", "descripcion": "Muestra que hay una condición para el select."}
tkn_igual={"token":"igual", "lexema":"=", "descripcion": "operación de comparación igual que"}
tkn_m_igual={"token":"menor igual", "lexema":"<=", "descripcion": "operación de comparación menor igual"}
tkn_M_igual={"token":"mayor igual", "lexema":">=", "descripcion": "operación de comparación mayor igual"}
tkn_diferente={"token":"no igual", "lexema":"!=", "descripcion": "operación de comparación diferente que"}
tkn_M={"token":"menor que", "lexema":"<", "descripcion": "operación de comparación menor que"}
tkn_m={"token":"mayor que", "lexema":">", "descripcion": "operación de comparación mayor que"}
tkn_comillas={"token":"comillas", "lexema":'"', "descripcion": "indica el inicio y final de una cadena de caracteres"}
tkn_and={"token":"conjunción", "lexema":"AND", "descripcion": "operador combinador de condiciones"}
tkn_or={"token":"disyunción", "lexema":"OR", "descripcion": "operador combinador de condiciones"}
tkn_xor={"token":"disyunción exclusiva", "lexema":"XOR", "descripcion": "operador combinador de condiciones"}
tkn_regex={"token":"REGEX", "lexema":"REGEX", "descripcion": "recibe una expresión regular"}
def tkn_ER(nombre):
    return {"token":"REGEX", "lexema": nombre, "descripcion":"Expresión regular"} 
def tkn_campo(nombre):
    return {"token":"campo", "lexema": nombre, "descripcion":"campo del registro"} 
def tkn_BOOL(nombre):
    return {"token":"BOOLEANO", "lexema": nombre, "descripcion":"tipo de dato booleano"} 
def tkn_STR(nombre):
    return {"token":"STR", "lexema": nombre, "descripcion":"tipo de dato de cadena de caracteres"}
def tkn_INT(nombre):
    return {"token":"NUMBER", "lexema": nombre, "descripcion":"tipo de dato numerico"} 
def select(opcion):
    estado=0
    tmp=""
    condicion=[]
    salida = []
    atributos=[]
    contenedor=[]
    
    lista = list(opcion)
    lista.append(";")
    for index, x in enumerate(lista):
        
        if estado == 0:
            if tmp.lower() == 'select':
                tokens.append(tkn_select)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            
            if x == '*':
                tokens.append(tkn_asterisco)
                
                if lista[index+1]==';':
                    salida.append('*')
                    
                    break
                    
                continue
            
            if x == ' ':
                if tmp.lower()=="where":
                    tokens.append(tkn_where)
                    salida.append(atributos)
                    estado=2
                    tmp=""
                    continue
                elif len(tmp)>0:
                    atributos.append(tmp)
                    tokens.append(tkn_campo(tmp))
                    tmp=""
                    estado = 1
                    continue
                continue                    
                    
            if x==',':
                tokens.append(tkn_campo(tmp))
                tokens.append(tkn_coma)
                atributos.append(tmp)
                tmp=""
                estado = 1
                continue

            if x !=' ':
                tmp+=x
                estado=1
                
            continue
        elif estado == 2:
            
            if x=='=' or x=='>' or x=='<' or x=='!':
                condicion.clear()
                tokens.append(tkn_campo(tmp))
                condicion.append(tmp)
                tmp = x
                estado = 4
                continue
                                    
                        
            if x==' ':
                condicion.clear()
                tokens.append(tkn_campo(tmp))
                condicion.append(tmp)
                tmp = ""
                estado = 4
                continue
            
            if x!=' ':
                tmp+=x
                estado=2
                continue
            
            
            continue
        elif estado == 3:
            if x==';':
                salida.append(contenedor.copy())
                break
            
            
            if tmp.lower()=="or":
                tokens.append(tkn_or)
                seleccionar.OR=True
                tmp=""
                estado=2
                continue
            elif tmp.lower()=="and":
                tokens.append(tkn_and)
                tmp=""
                seleccionar.AND=True
                estado=2
                continue
            elif tmp.lower()=="xor":
                tokens.append(tkn_xor)
                tmp=""
                seleccionar.XOR=True
                estado=2
                continue
            
            if x != ' ':
                tmp +=x
                continue    
        elif estado == 4:
            if tmp=='<' and x != '=':
                tokens.append(tkn_m)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                tmp = x
                estado=5
                continue
            elif tmp=='>' and x != '=':
                tokens.append(tkn_M)
                condicion.append(tmp)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                tmp = x
                estado=5
                continue
            
            if tmp=='<=':
                tokens.append(tkn_m_igual)
                condicion.append(tmp)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                tmp = x
                estado=5
                continue
            elif tmp == '>=':
                tokens.append(tkn_M_igual)
                condicion.append(tmp)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                tmp = x
                estado=5
                continue
            elif tmp == '!=':
                tokens.append(tkn_diferente)
                condicion.append(tmp)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                tmp = x
                estado=5
                continue
            elif tmp == '=':
                tokens.append(tkn_igual)
                condicion.append(tmp)
                if x=='"':
                    tmp=''
                    estado = 6
                    continue
                
                tmp = x
                estado=5
                continue
            elif tmp.lower()=='regex':
                tokens.append(tkn_regex)
                condicion.append("regex")
                tmp=""
                estado = 7
            
            if x!=' ':
                tmp+=x
                continue
        elif estado == 5:
            if x==';':
                if re.search("true", tmp.strip().lower()):
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_BOOL(tmp))
                    condicion.append(True)
                        
                elif re.search("false", tmp.strip().lower()):
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_BOOL(tmp))
                    condicion.append(False)
                else:
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_INT(tmp))
                    condicion.append(float(tmp))
                contenedor.append(condicion.copy())
                salida.append(contenedor.copy())    
                break
            
            if x == ' ':
                if re.search("true", tmp.strip().lower()):
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_BOOL(tmp))
                    condicion.append(True)
                        
                elif re.search("false", tmp.strip().lower()):
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_BOOL(tmp))
                    condicion.append(False)
                    
                else:
                    tmp=tmp.replace(' ', '')
                    tokens.append(tkn_INT(tmp))
                    condicion.append(float(tmp))
                    
                contenedor.append(condicion.copy())    
                tmp=""    
                estado = 3    
                continue
                
            if x == '"':
                tokens.append(tkn_comillas)
                estado = 6
                continue
            
                
            if x!=' ':
                tmp+=x
                continue
        elif estado == 6:
            if x == '"':
                tokens.append(tkn_STR(tmp))
                tokens.append(tkn_comillas)
                condicion.append(tmp)
                contenedor.append(condicion.copy())
                tmp = ""
                estado=3
            else:
                tmp += x
                estado = 6    
            
            continue
        elif estado == 7:
            if x==']':
                tmp+=x
                tokens.append(tkn_ER(tmp))
                condicion.append(tmp)
                contenedor.append(condicion.copy())
                tmp=""
                estado=3
                continue
            
            tmp+=x
            continue
                
                
    return salida
            
tkn_list={"token":"LIST", "lexema":"LIST", "descripcion": "Crea una lista"}
tkn_attributes={"token":"ATTRIBUTES", "lexema":"ATTRIBUTES", "descripcion": "palabra reservada que refiere a los atributos de los SETs"}

def list_Atrubutes(opcion):
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'list':
                tokens.append(tkn_create)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'attributes':
                tokens.append(tkn_set)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue

tkn_print={"token":"PRINT", "lexema":"PRINT", "descripcion": "Define la impresión que se muestra en pantalla"}
tkn_in={"token":"IN", "lexema":"IN", "descripcion": "palabra reservada que indica el color de la impresión"}
def tkn_color(nombre):
    return {"token":"COLOR", "lexema": nombre, "descripcion":"color"} 


def print_in(opcion):
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'print':
                tokens.append(tkn_print)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'in':
                tokens.append(tkn_in)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue    
        elif estado == 2:
            if x == ';':
                tokens.append(tkn_color(tmp))
                return tmp
                tmp=""
                break
            
            if x !=' ':
                tmp+=x
                estado=2
                
            continue            

tkn_min={"token":"MIN", "lexema":"MIN", "descripcion": "comando que muestra el minimo en el campo seleccionado"}
tkn_max={"token":"MAX", "lexema":"ATTRIBUTES", "descripcion": "comando que muestra el maximo en el campo seleccionado"}

def min_max(opcion):
    estado=0
    salida=[]
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'min':
                tokens.append(tkn_min)
                salida.append("min")
                tmp=''
                estado=1
                continue
            
            if tmp.lower() == 'max':
                tokens.append(tkn_max)
                salida.append("max")
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if x == ';':
                tokens.append(tkn_campo(tmp))
                salida.append(tmp.lower())
                return salida
                break 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue

tkn_sum={"token":"SUM", "lexema":"SUM", "descripcion": "comando que devuelve la suma del campo numerico seleccionado"}
        
def sum_(opcion):
    campos=[]
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'sum':
                tokens.append(tkn_sum)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if x=='*':
                tokens.append(tkn_asterisco)
                campos = ["*"]
                return campos
                break
            
            if x == ';':
                tokens.append(tkn_campo(tmp))
                campos.append(tmp.lower())
                return campos
                break
            
            if x == ',':
                tokens.append(tkn_campo(tmp))
                campos.append(tmp.lower())
                tmp=''
                estado=1
                continue  
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue  

tkn_count={"token":"COUNT", "lexema":"COUNT", "descripcion": "comando que devuelve la CUENTA de registros en el campo seleccionado"}
        
def count(opcion):
    campos=[]
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'count':
                tokens.append(tkn_count)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if x=='*':
                tokens.append(tkn_asterisco)
                campos = ["*"]
                return campos
                break
            
            if x == ';':
                tokens.append(tkn_campo(tmp))
                campos.append(tmp.lower())
                return campos
                break
            
            if x == ',':
                tokens.append(tkn_campo(tmp))
                campos.append(tmp.lower())
                tmp=''
                estado=1
                continue  
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue 

tkn_report={"token":"REPORT", "lexema":"REPORT", "descripcion": "comando que muestra un reporte en html"}
tkn_to={"token":"TO", "lexema":"TO", "descripcion": "indica el nombre del documento donde se va a crear el reporte"}
def tkn_html(nombre):
    return {"token":"HTML", "lexema":nombre, "descripcion": "nombre el archivo html que muestra el reporte"}

def tkn_comando(nombre):
    return {"token":"comando", "lexema": nombre, "descripcion":"comando del que se va a mostrar un reporte"} 
        
def report_id(opcion):
    estado=0
    tmp=""
    salida = []
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        
        if estado == 0:
            if tmp.lower() == 'report':
                tokens.append(tkn_report)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'tokens':
                tokens.append(tkn_tkns)
                
                df= pd.DataFrame(data=tokens)
                f = open ("header.txt",'r')
                header = f.read()
                f.close()
        
                tabla= df.to_html()
                footer="""</div>
                </body>
                </html> """
                html = header+tabla+footer
                f=open('reporte_tokens.html','wb')
                f.write(bytes(html, 'utf-8'))
                f.close()
                webbrowser.open_new_tab("reporte_tokens.html")
                salida.append(tmp)
                break
                
                continue 
            
            if x == ' ':
                tokens.append(tkn_to)
                tmp=''
                estado=2
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue
        elif estado == 2:
            if x == ' ':
                tokens.append(tkn_html(tmp+'.html'))
                salida.append(tmp)
                tmp=''
                estado=3
                continue 
            
            if x !=' ':
                tmp+=x
                estado=2
                continue
        elif estado == 3:
            if x==';':
                tokens.append(tkn_comando(tmp))
                salida.append(tmp)
                break
            
            tmp+=x
            continue
            
    return salida                              

tkn_script={"token":"SCRIPT", "lexema":"SCRIPT", "descripcion": "carga archivos de texto con comandos"}
def tkn_siql(nombre):
    return {"token":"SIQL", "lexema":nombre, "descripcion": "tipo de archivo SIQL con comandos"}

def script(opcion):
    archivos_siql=[]
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'script':
                tokens.append(tkn_script)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            
            if x == ';':
                tokens.append(tkn_siql(tmp))
                archivos_siql.append(tmp)
                return archivos_siql
                break
            
            if x == ',':
                tokens.append(tkn_siql(tmp))
                archivos_siql.append(tmp)
                tmp=''
                estado=1
                continue  
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue

tkn_tkns={"token":"TOKENS", "lexema":"TOKENS", "descripcion": "comando que muestra un reporte en html de los tokens"}

def report_tkn(opcion):
    estado=0
    tmp = ""
    lista = list(opcion)
    lista.append(";")
    for x in lista:
        if estado == 0:
            if tmp.lower() == 'report':
                tokens.append(tkn_report)
                tmp=''
                estado=1
                continue
            
            if x !=' ':
                tmp+=x
                estado=0
                
            continue
        elif estado == 1:
            if tmp.lower() == 'tokens':
                tokens.append(tkn_tkns)
                
                df= pd.DataFrame(data=tokens)
                f = open ("header.txt",'r')
                header = f.read()
                f.close()
        
                tabla= df.to_html()
                footer="""</div>
                </body>
                </html> """
                html = header+tabla+footer
                f=open('reporte_tokens.html','wb')
                f.write(bytes(html, 'utf-8'))
                f.close()
                webbrowser.open_new_tab("reporte_tokens.html")
                
                continue 
            
            if x !=' ':
                tmp+=x
                estado=1
                
            continue    
    
#create_Set("CREATE SET nuevo")
#print(load("LOAD INTO nuevo FILES ejemplo.aon"))        
#print(use_Set("USE SET nuevo"))
print(select('SELECT * WHERE aquello > "esto" and palabra regex [(a|b|c|d)]'))
#list_Atrubutes("LIST ATTRIBUTES")
#print(print_in("PRINT IN BLACK"))
#print(min_max("MIN zapatos"))
#print(sum_("SUM campo1, campo2, campo3"))
#print(count("COUNT *"))
#print(report_id('REPORT TO reporte3 SELECT * WHERE edad != 44'))
#print(script("SCRIPT archivo.siql, archivo.siql"))
#report_tkn("REPORT TOKENS")


print(tabulate(tokens, headers="keys", showindex=True, tablefmt="fancy_grid"))