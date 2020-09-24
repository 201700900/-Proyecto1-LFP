from tabulate import tabulate
import aon
import createSet
import automatas
import webbrowser
import pandas as pd
import siql
from colorama import Back, Fore, init
init()

L_Reporte=[]

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

    
def titulo(linea):
    t='<div style="padding-top: 80px"><div><p style="font-size: 2.4em; color: #1bbc9b; margin: 0px" class="bold">', linea, '</p></div></div>'        
    return 

    

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
    global L_Reporte
    tmp=''
    for x in list(opcion):
        
        if x==' ':
    
            #---------------------------1. CREATE SET < ID >
            if tmp.lower()=='create': 
                set_nombre = automatas.create_Set(opcion)
                nombres=[]
                lista = opcion.split()
                if set_nombre in createSet.nombres:
                    print(set_nombre,' ya fue creada')  
                else:
                    nuevo = createSet.Paquete(set_nombre)
                    createSet.sets.append(nuevo)
                    L_Reporte=[['set',set_nombre]]
                for n in createSet.nombres:
                    nombres.append([n])
                print(tabulate(nombres, headers=['SETS'], showindex=True, tablefmt="fancy_grid" ))
                break    
                

            #***************************2. LOAD INTO < set_id > FILES < id > [ , <id> ] +    
            elif tmp.lower()=='load':
                try: 
                    listaLoad=[]
                    listaLoad = automatas.load(opcion)
                    archivos = listaLoad[1]
                    if listaLoad[0] in createSet.nombres:
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
                break    
            #--------------------------3. USE SET < set_id >    
            elif tmp.lower()=='use':
                seUsa = automatas.use_Set(opcion)
                if len(createSet.sets)==0:
                    print("Ningun set creado aún")
            
                if tmp.lower() not in createSet.nombres:
                    setEnUso = seUsa.lower()
                    print("**usando set ",tmp,"**")
                        
                else:
                    print("set",tmp, "no creado aún")     
                break
            #--------------------------4. SELECT < atributo > [ , <atributo>] + [ WHERE < condiciones > ]
            elif tmp.lower()=='select': 
                automatas.select(opcion)   
                
                break    
            #--------------------------5. LIST ATTRIBUTES
            elif tmp.lower()=='list':
                print("USANDO SET",setEnUso)
                automatas.list_Atrubutes(opcion)
                try:
                    dic = (Lista_Usando())
                    d=dic[0]
                    keys=[]
                    for key in list(d.keys()):
                        keys.append([key])

                    print(tabulate(keys, tablefmt="fancy_grid"))
                            
                except:
                    print("Error")    

                break
            #--------------------------6. PRINT IN <color>    
            elif tmp.lower()=='print':
                
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
                break
            #--------------------------7. MAX < atributo > | MIN < atributo >        
            elif tmp.lower()=='min' or tmp.lower()=='max':
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
                break

            #--------------------------8. SUM < atributo > [, <atributo> ] +    
            elif tmp.lower()=='sum':
                sumas=automatas.sum_(opcion)
                try:
                    if sumas[0]=='*':
                        dic = (Lista_Usando())
                        d=dic[0]
                        
                        sumas=list(d.keys())
                    
                    salida=[]
                    
                    for at in sumas:
                        resultado=0
                        try:
                            for dic in Lista_Usando():
                                
                                valor = dic.get(at, "")
                                
                                if float(valor).as_integer_ratio():
                                    resultado = resultado + valor
                        except:
                            pass
                        salida.append([at, resultado])
                    
                    print(tabulate(salida, headers=['CAMPO', 'SUMA'], tablefmt="fancy_grid"))
                                
                                
            
                
                except:
                    print("error")
                
                break
            #--------------------------9. COUNT < atributo > [, < atributo > ] +    
            elif tmp.lower()=='count':
                cuentas = automatas.count(opcion)
                if cuentas[0]=='*':
                    dic = (Lista_Usando())
                    d=dic[0]
                    
                    cuentas=list(d.keys())
                
                salida=[]
                for c in cuentas:
                    cuenta=0
                    for dic in Lista_Usando():
                        if (c in dic):
                            cuenta=cuenta+1
                        
                    salida.append([c,len(dic)])                
                    
                
                print(tabulate(salida, headers=['CAMPO', 'CUENTA'], tablefmt="fancy_grid"))
                break
            #--------------------------12. REPORT TOKENS
            #--------------------------10. REPORT TO < id > < comando >  
            elif tmp.lower()=='report':        
                entra = automatas.report_id(opcion)
                if 'tokens' not in entra:
                    try:
                        encontrar(entra[1])
                        
                        
                        
                        df= pd.DataFrame(data = L_Reporte)
                        f = open ("header.txt",'r')
                        header = f.read()
                        f.close()
                        
                        tabla= df.to_html()
                        footer="""</div>
                        </body>
                        </html> """
                        html = header+titulo(entra[1])+tabla+footer
                        path = entra[0]+".html"
                        f=open(path,'wb')
                        f.write(bytes(html, 'utf-8'))
                        f.close()
                        webbrowser.open_new_tab(path)
                    except:
                        pass    
                break
            #--------------------------11.SCRIPT < direccion > [, < direccion > ]
            elif tmp.lower()=='script':
                archivos = automatas.script(opcion)
                for path in archivos:
                    comandos = siql.script(path)
                    try:
                        for comando in comandos:
                            print("*********************************")
                            c=comando.rstrip('\n')
                            print(c)
                            encontrar(c)
                            automatas.tokens.append({"token":"PUNTO y COMA", "lexema":";", "descripcion":"Indica el fin de un comando en el script del archivo .SIQL."})
                    except:
                        pass        
                
                break        
                        
            else:
                print("Not a Math!")
        
        tmp+=x
        continue

#print(tabulate(aon.adfAON(entrada()), headers="keys", showindex=True, tablefmt="fancy_grid"))
#print(aon.adfAON(entrada()))

entrada()