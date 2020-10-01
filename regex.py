def regex(er):
    salida=[]
    con=[]
    tmp = ''
    antes=False          
    parentesis=False
    letras=False           
    
    for i, c in enumerate(list(er)):
        if c == '[':
            continue
        elif c == '^':
            #startswith('')
            if er[i+1] == '(':
                continue
            else:
                con.append(['^', er[i+1]])
                continue
        elif c == '+':
            
            if er[i-1] == ')':
                continue
            else:
                con.append(['+',er[i-1]])
                continue
                    
        elif c == '*':
            if er[i-1] == ')':
                continue
            else:
                con.append(['*',er[i-1]])
                continue
        elif c == '?':
            if er[i-1] == ')':
                continue
            else:
                con.append(['?',er[i-1]])
                continue
        elif c == '.':
            if er[i+1]=='+':
                continue
            elif er[i+1]=='*':
                continue
            elif er[i+1]=='?':
                continue
            else:
                con.append(['.'])
                continue
        elif c == '|':
            salida.append(con.copy())
            con.clear()
            continue
        elif c == ']':
            salida.append(con.copy())
            return salida
            break

        if c == '(':
            parentesis=True
            if er[i-1]=='^':
                antes = True
            continue
        elif c == ')':
            if antes:
                con.append(['^',tmp])
            else:
                if er[i+1]=='+':
                    con.append(['+',tmp])
                elif er[i+1]=='*':
                    con.append(['*',tmp])
                elif er[i+1]=='?':
                    con.append(['?',tmp])
                else:
                    con.append([tmp])
            tmp = ''
            parentesis=False
            continue    
        
        if c != '['  or c!='.' or c!='^'or c!='+' or c!='+' or c!='?' or c!='|' or c!='':
            if parentesis:
                tmp += c
            else:
                if er[i+1]=='+':
                    continue
                elif er[i+1]=='*':
                    continue
                elif er[i+1]=='?':
                    continue
                elif er[i-1] == '^':
                    continue
                else:
                    con.append([c])
                    continue

def match(er, condicion):
    expresion = regex(er)
    sigue = False
    for con in expresion:
        for c in con:
            if c[0] == '^':
                if c[1]=='.':
                    return True
                else:
                    if condicion.startswith(c[1]):
                        return True
                    else:
                        sigue=False
                        break
                        
            elif c[0]=='+':
                if c[1]=='.':
                    return True
                else:
                    if condicion.count(c[1])>=1:
                        return True
                    else:
                        sigue= False
                        break
            elif c[0]=='*':
                if c[1]=='.':
                    return True
                else:
                    if condicion.count(c[1])>=0:
                        return True
                    else:
                        sigue= False
                        break
            elif c[0]=='?':
                if c[1]=='.':
                    return True
                else:
                    if condicion.count(c[1])>=0:
                        return True
                    else:
                        sigue= True
                        return True
            else:
                if c[1]=='.':
                    return True
                else:
                    if condicion.count(c[1])>0:
                        return True
                    else:
                        sigue= False
                        break
            
    return sigue            
    
    
    
