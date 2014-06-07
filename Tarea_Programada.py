# -*- coding: cp1252 -*-
################################################################################
#Función que abre el archivo e ingresa la información en una lista
def cargar_archivo(SML):
    Lista_Datos=[]
    file=open(SML)
    archivo=file.read()
    file.close()
    linea=''
    temp=''
    flag=False
    for char in archivo:
        if char=='\n' or char==';':
            if linea!='':
                if Lista_Datos==[]:
                    Lista_Datos+=[linea]
                    linea=''
                    flag=False
                    temp=''
                else:
                    pos=Lista_Datos[-1].find('let')
                    if char[:3]!='val' or (char[:3]=='val' and Lista_Lineas[-1][pos:]=='let'):
                        Lista_Datos+=[linea]
                    else:
                        Lista_Datos+=[linea]
                    linea=''
                    flag=False
                    temp=''
            else:
                pass
        else:
            if char==' ' and temp[0:len(temp)]=='val':
                flag=True
                #linea+=char
            elif char=='=':
                linea+=' '
            elif char!=' ' and flag:
                linea+=char
            elif char!= ' ': 
                temp+=char
            else:
                pass
    if linea!='':
        Lista_Datos+=[char]
    for i in range(len(Lista_Datos)):
        Lista_Datos[i]=Lista_Datos[i].split()
    print Lista_Datos
################################################################################
def evalua_tuplas(var,inicio,final):
    abre=0
    cierra=0
    for char in var:
        if char==inicio:
            abre+=1
        else:
            if char==final:
                cierra+=1
    return abre==cierra
            
def evalua(lista,c):
    for linea in lista:
        var=linea[1]
        if var[0:2]=='if':
            linea[1]=if_if(var,lista[:c])
        elif var.find('<=')!=-1 or var.find('>=')!=-1 or var.find('orelse')!=-1 or var.find('andalso')!=-1 or var.find('<')!=-1 or var.find('>')!=-1 or var.find('=')!=-1 or var.find('<>')!=-1:
            linea[1]=bool_bool(var,lista[:c])
        elif var[0]=="[" :
            contenido=separa_contenido_estructuras(var[1:-1])
            contenido=convertir_elemento(contenido,lista[:c])
            linea[1]=contenido
        elif var[0]=="(":
            contenido=separa_contenido_estructuras(var[1:-1])
            contenido=convertir_elemento(contenido,lista[:c])
            linea[1]=tuple(contenido)
        else:
            contenido=convertir_elemento([var],lista[:c])
            linea[1]=contenido[0]
        c+=1
    return lista
################################################################################
def bool_bool(var,lis):
    if var.find('andalso')!=-1 or var.find('orelse')!=-1:
        if var[0]=="(":
            separar=completa_exp_booleans(var)
            Primer=bool_bool(Div[0],lis)
            if len(separar)==3:
                Segund=bool_bool(separar[2],lis)
            else:
                Segund=bool_bool(separar[1],lis)
            nueva=Booleans(Primer,Segund,separar[1],lis)
        else:
            separar=Divide(var)
            Primer=bool_bool(separar[0],lis)
            Segund=bool_bool(separar[2],lis)
        nueva=Booleans(Primer,Segund,separar[1],lis)
    else:
        if var[0]=='(' and var[-1]==')':
            var=var[1:-1]
        if var.find(' <= ')!=-1:
            n=var.find(' <= ')
            m=n+2
            signo='<='
            Primer=convertir_elemento([var[:n]],lis)        
            Segund=convertir_elemento([var[m:]],lis)
            nueva=Booleans(Primer[0],Segund[0],signo,lis)
        elif Exp.find('>=')!=-1:
            n=Exp.find('>=')
            m=n+2
            signo='>='
            Primer=convertir_elemento([Exp[:n]],lista)      
            Segund=convertir_elemento([Exp[m:]],lista)
            nueva=Booleans(Primer[0],Segund[0],signo,lista)
        elif Exp.find('<>')!=-1:
            n=Exp.find('<>')
            m=n+2
            signo='<>'
            Primer=convertir_elemento([Exp[:n]],lista)        
            Segund=convertir_elemento([Exp[m:]],lista)
            nueva=Booleans(Primer[0],Segund[0],signo,lista)
        elif Exp.find('<')!=-1:
            n=Exp.find('<')
            m=n+1
            signo='<'
            Primer=convertir_elemento([Exp[:n]],lista)        
            Segund=convertir_elemento([Exp[m:]],lista)
            nueva=Booleans(Primer[0],Segund[0],signo,lista)
        elif Exp.find('>')!=-1:
            n=Exp.find('>')
            m=n+1
            signo='>'
            Primer=convertir_elemento([Exp[:n]],lista)        
            Segund=convertir_elemento([Exp[m:]],lista)
            nueva=Booleans(Primer[0],Segund[0],signo,lista)
        elif Exp.find('=')!=-1:
            n=Exp.find('=')
            m=n+1
            signo='='
            Primer=convertir_elemento([Exp[:n]],lista)        
            Segund=convertir_elemento([Exp[m:]],lista)
            nueva=Booleans(Primer[0],Segund[0],signo,lista)
    return nueva

def Booleans(Primer,Segund,Signo,lista):
    if not isinstance(Primer,int):
        Cambia_Variables(Primer,lista)
    if not isinstance(Segund,int):
        Cambia_Variables(Segund,lista)
    if Segund=="":
        return Primer
    if Signo=='<':
        return Primer < Segund
    elif Signo=='>':
        return Primer > Segund
    elif Signo =='=':
        return Primer == Segund
    elif Signo =='<=':
        return Primer<= Segund
    elif Signo =='>=':
        return Primer >= Segund
    elif Signo =='<>':
        return Primer!=Segund
    elif Signo== 'andalso':
        return Primer and Segund
    elif Signo== 'orelse':
        return Primer or Segund
    else:
        return 'Error'
################################################################################
def if_if(var,lis):
    if var[:2]=='if':
        separa=var[2:].partition('then')
        convert=convertir_elemento([separa[0]],lis)
        if convert[0]==True:
            result=if_if_aux(separa[2])
            return convertir_elemento([result[0]],lis)[0]
        else:
            return if_if(Div[2],lis)         
    else:
        convert=DivExpIF(var)
        if convert[1]=="elseif":
                convert=convert[2].partition('then')
                convert_2=convertir_elemento([convert[0]],lis)
                if convert_2[0]==True:
                    result=if_if_aux(convert[2])
                    return convertir_elemento([result[0]],lis)[0]
                else:
                    return if_if(convert[2],lis)
        else:
            if convert[1]=="else":
                result=convert[2]
                if convert[2][:3]=='(if':
                    result=convert[2][1:-1]
                return convertir_elemento([result],lis)[0]
    
def if_if_aux(var):
    if var[:3]=='(if':
        lista_result=[]
        nueva=if_if_aux_aux(var)[0]
        lista_result+=[nueva]
        nueva_2=var.partition(nueva)
        condicional=nueva_2[2].find('elseif')
        condicional_2=nueva_2[2].find('else')
        separada=[]
        if (condicional < condicional_2 and condicional !=-1)or (condicional!=-1 and condicional_2==-1) or (condicional==condicional_2 and (condicional!=-1 and condicional_2!=-1)):
            separada=nueva_2[2].partition('elseif')
        elif (condicional_2 < condicional and condicional_2 !=-1)or (condicional_2!=-1 and condicional==-1):
            separada=nueva_2[2].partition('else')
        else:
            return ['','','']
        lista_result+=separada[1:]
        lista_result[0]=lista_result[0][1:-1]
        return lista_result
    else:
        condicional=var.find('elseif')
        condicional_2=var.find('else')
        separada=[]
        if (condicional < condicional_2 and condicional !=-1)or (condicional_2!=-1 and condicional_2==-1) or (condicional==condicional_2 and (condicional!=-1 and condicional_2!=-1)):
            separada=var.partition('elseif')
        elif (condicional_2 < condicional and condicional_2 !=-1)or (condicional_2!=-1 and condicional==-1):
            separada=var.partition('else')
        else:
            return ['','','']
        return separada

def if_if_aux_aux(var):
    lista_element=[]
    nueva=""
    for char in var:
        if char!=")":
            nueva+=char
        else:
            nueva+=char
            if evalua_tuplas(nueva,"(",")"):
                lista_element+=[nueva]
                nueva=""
    return lista_element
################################################################################
