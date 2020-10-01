from tabulate import tabulate
from copy import deepcopy
import regex


AND = False
OR = False
XOR = False

def array(ListaUsando,atributos,condiciones):
    
    global AND
    global OR 
    global XOR 
    
    try:
        procesar = deepcopy(ListaUsando)
        d=procesar[0]
        opuesto=[]
        
        if len(atributos)!=0:
            for key in list(d.keys()):
                opuesto.append(key)
            
        
            for at in atributos:
                opuesto.remove(at)
        
        copia = deepcopy(procesar)
        for at in opuesto:
            for x in copia:
                try:
                    x.pop(at)
                except:
                    pass    
                

        
        imprimir=[]
        tmp=[]
        doble=[]
        for condicion in condiciones:
            tmp.clear()
            for index, dic in enumerate(ListaUsando):
                try:
                
                    if condicion[1]=='=':
                        if dic.get(condicion[0]) == condicion[2]:
                            tmp.append(copia[index])
                    elif condicion[1]=='!=':
                        if dic.get(condicion[0]) != condicion[2]:
                            tmp.append(copia[index])
                    elif condicion[1]=='<=':
                        if dic.get(condicion[0]) <= condicion[2]:
                            tmp.append(copia[index])
                    elif condicion[1]=='>=':
                        if dic.get(condicion[0]) >= condicion[2]:
                            tmp.append(copia[index])               
                    elif condicion[1]=='<':
                        if dic.get(condicion[0]) < condicion[2]:
                            tmp.append(copia[index])
                    elif condicion[1]=='>':
                        if dic.get(condicion[0]) > condicion[2]:
                            tmp.append(copia[index])
                    elif condicion[1]=='regex':
                        bandera = regex.match(condicion[2], dic.get(condicion[0]))
                        if bandera:
                            tmp.append(copia[index])
                        else:
                            continue
                                
                            
                            
                            
                            
                except:
                    pass            
            #print(tabulate(tmp, headers="keys", showindex=True, tablefmt="fancy_grid"))    

            doble.append(tmp.copy())
            
            
        if XOR == True:
            if len(doble[1])==0:
                imprimir = doble[0].copy()
            elif len(doble[0])==0:
                imprimir = doble[1].copy()
            else:
            
                for dic in doble[0]:
                    if dic not in doble[1]:
                        imprimir.append(dic)
                        
                for d in doble[1]:
                    if d not in doble[0]:
                        imprimir.append(d)
                
            XOR = False
        elif AND == True:
            for a in doble[0]:
                for b in doble[1]:
                    if a == b:
                        imprimir.append(b)
            
            AND = False
        elif OR == True:
            
            for x in doble[1]:
                doble[0].append(x)
                
            for i in doble[0]:
                if i not in imprimir:
                    imprimir.append(i)  
                
            OR=False
        else:
            imprimir = tmp.copy()
            
        
        #print(tabulate(imprimir, headers="keys", showindex=True, tablefmt="fancy_grid"))    
        return imprimir    
    except:
        print("Error")
        

lista = [   {'precio':15.45,'activo':True, 'nombre':'alomate'},
            {'precio':float(12.0),'activo':True, 'nombre':'Omate'},
            {'precio':1.0,'activo':True, 'nombre':'A'},
            {'precio':15.8,'activo':False, 'nombre':'Tomate'}]

#print(array(lista,[],[['edad', '>',11]]))      



