#Función que abre el archivo e ingresa la información en una lista

def cargar_archivo(SML):

    Lista_Datos=[] #Lista donde se almacenaran los datos

    #Lectuctura del archivo

    file=open(SML) 

    archivo=file.read()

    file.close()

    #Variables para extraccion de informacion del archivo

    linea=''

    temp=''

    flag=False

    #for que lee cada letra del archivo para ingresar los datos a la lista

    for char in archivo:

        if char=='\n' or char==';': #revisa si es el final de la sentencia o no

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

    Lista_Datos=evalua(Lista_Datos,0)

    return Lista_Datos

    

#Funciones que evaluan la lista o expresiones



#revisa la lista con los datos y realiza las conversiones necesarias con ayuda de una serie de funciones auxiliares      

def evalua(lista,c):

    for linea in lista:

        var=linea[1]

        if var[0:2]=='if':

            linea[1]=if_if(var,lista[:c]) #LLama a funcion auxiliar para realizar los cambios necesarios

        #Busca algun elemento relacionado con comparaciones booleanas

        elif var.find('<=')!=-1 or var.find('>=')!=-1 or var.find('orelse')!=-1 or var.find('andalso')!=-1 or var.find('<')!=-1 or var.find('>')!=-1 or var.find('=')!=-1 or var.find('<>')!=-1:

            linea[1]=bool_bool(var,lista[:c]) #Llama a funcion auxiliar para realizar cambios necesarios

        #Si la primer letra de la linea es un corchete de lista llama a las funciones auxiliares para convertir la linea en una lista

        elif var[0]=="[" :

            contenido=estructuras(var[1:-1])

            contenido=convertir(contenido,lista[:c])

            linea[1]=contenido

        #Si la primer letra de la linea es un corchete de tupla llama a las funciones auxiliares para convertir la linea en una tupla

        elif var[0]=="(":

            contenido=estructuras(var[1:-1])

            contenido=convertir(contenido,lista[:c])

            linea[1]=tuple(contenido)

        #Cambia las variavles y convierte los valores

        else:

            contenido=convertir([var],lista[:c])

            linea[1]=contenido[0]

        c+=1

    return lista

    

#funcion que evalua las expresiones numericas, los operadores y las variables, las ingresa todas a una lista, invoca a una funcion

#y devuelve el resultado de la operacion

def evalua_expresiones(exp, lista):

    List=[] #almacena la expresion

    n='' #variable q guardara el numero

    var=''

    cont=0

    c=0

    flag=False

    largo=len(exp)

    while cont!=largo:

        if exp[cont]=='~':

            flag=True

        if exp[cont].isdigit(): #si la letra es un numero o es negativo el numero

            n+=exp[cont]

        elif (exp[cont]=='+') or (exp[cont]=='-') or (exp[cont]=='*') or (exp[cont]==')') or ((exp[cont]=='d') and  (exp[cont:cont+3]=='div')) and (exp[cont:cont+3]=='mod')): 

            if n.isdigit():

                N= convertir_var([n], List)

                List+=[N[0]]

                n=''

            elif var!='':

                var=vambia_var(var,List)#funcion pao obtengo el valor de la variable

                if flag:

                    flag=False

                    var=-1*var

                List+=[var]

                var=''

            if exp[cont]== 'd':

                List+=['/']

            elif exp[cont]=='m':

                List+=['%']

            else:

                List+=[exp[cont]]

        elif (exp[cont]=='('):

            List+=[exp[cont]]

        cont+=1

    if n.isdigit():

        if flag:

            flag=False

            n='~'+n

        N= convertir([n],lista)

        List+=[Numero[0]]

    elif var!='':

        var=cambia_var(var,lista)

        List+=[var]

        var=''

    val_exp= Operaciones(List)

    return val_exp    



#Le ingresa una lista con la expresion y va desarrollando cada operacion, es recursiva

def Operaciones(Lista):

    if len(Lista)==1:

        return Lista

    elif len(Lista)==2:

        return [Lista[0]+Lista[1]]

    else:

        cont=0

        for op in Lista:

            if op=='(':

                c=0

                for e in Lista[cont:]:

                    if e==')':

                        break

                    c+=1

                resultado=Operaciones(Lista[cont+1:c+cont])

                Lista=Lista[:cont]+resultado+Lista[cont+c+1:]

                break

            elif  (op=='/' or op=='*' or op=='%'):

                resultado=ResultOP(Lista[cont-1:cont+2])

                Lista=Lista[:cont-1]+resultado+Lista[cont+2:]

                break

            elif  (op=='+' or op== '-'):

                resultado=ResultOP(Lista[cont-1:cont+2])

                Lista=Lista[:cont-1]+resultado+Lista[cont+2:]

                break

            cont+=1

        return Operaciones(Lista)

    

#retorna el resultado de aplicar el operador a los dos numeros                

def ResultOP(op):

    Resultado=0 #almacena el resultado

    if op[1]=='+': #si el operador es suma

        Resultado= op[0]+ op[2]

    elif op[1]=='-': #si el operador es resta

        Resultado= op[0]-op[2]

    elif op[1]=='*': #si el operador es multiplicacion

        Resultado= op[0]*op[2]

    elif op[1]=='/': #si el operador es division

        Resultado= op[0]/ op[2]

    elif op[1]=='%': #si el operador es modulo

        Resultado= op[0]% op[2]

    return [Resultado]    

    

def evalua_lista(lista):

    Tipo=''

    if type(Lista[0])== int:    #si el primer elemento es de tipo int, es int list

        Tipo+= 'int list'

    elif type(Lista[0])== bool:   #si el primer elemento es de tipo bool, es bool list

        Tipo+= 'bool list'

    elif type(Lista[0])== tuple:	#si el primer elemento es de tipo tupla, se llama a la funcion evalua tipo tupla y se le agrega el list

        tipo_tupla= Evalua_Tipo_Tupla(Lista[0])

        Tipo+= tipo_tupla+' list'

    elif type(Lista[0])== list:		#si el primer elemento es de tipo list llama de nuevo a evalua tipo lista

        tipo=evalua_lista(Lista[0])

        Tipo+= tipo+' list'

    return Tipo

    

def evalua_tupla(tupla):

    Tipo=''

    for e in tupla:

        if type(e)==tuple:		#si la tupla contiene otra tupla, llama otra vez a la funcion de evalua tipo tupla

            res=evalua_tupla(e)

            Tipo+='*'+res		#Agrega

        elif type(e)==int:		#Si es de tipo int y Tipo esta vacio agrega int sino agrega *int

            if Tipo=='':

                Tipo+='int'

            else:

                Tipo+='*int'

        elif type(e)==bool:		#Si es de tipo bool y Tipo esta vacio agrega bool sino agrega *bool

            if Tipo=='':

                Tipo+='bool'

            else:

                Tipo+='*bool'

        elif type(e)==list:		#Si es de tipo lista llama a la funcion evalua tipo lista con la lista 

            res=evalua_lista(e)

            if Tipo=='':

                Tipo+=+res		#Agrega resultado

            else:

                Tipo+='*'+res     

    return '('+Tipo+')'

    

#Funciones que se encargan del cambio de valores



# Separa los elementos que se encuentran en una lista o tupla

def estructuras(var):

    lista_elementos=[]

    val=""       

    for e in var:

        if e!=",":

             val+=e

        else:

            if val[0]=="[":

                val+=i

            elif val[0]=="(":

                val+=i

            else:

                lista_elementos+=[val]

                val=""

    lista_elementos+=[val]

    return lista_elementos

    

#funcion que separa la variable y el valor

def variable_valor(linea,var,val,cont):

        while linea[cont]!= "=":

            var+=linea[cont]

            cont+=1

        val=linea[cont+1:]

        return [[var,val]]



#Funcion que convierte las expresiones a sus respectivos valores, con uso de algunas funciones extra

def convertir(Lista,var):

    lista_convertida=[]

    for e in Lista:

        if var.isdigit():

            lista_convertida+=[int(e)]

        elif e[:2]=='if':

            lista_convertida+=[if_if(e,var)]

        elif e.find('<=')!=-1 or e.find('orelse')!=-1 or e.find('andalso')!=-1 or e.find('<=')!=-1 or e.find('<')!=-1 or e.find('>')!=-1 or e.find('=')!=-1 or e.find('<>')!=-1:

            lista_convertida+=[bool_bool(e,var)]

        elif e.find('+')!=-1 or e.find('-')!=-1 or e.find('*')!=-1 or e.find('/')!=-1 or e.find('div')!=-1 or e.find('mod')!=-1:

            lista_convertida+=[evaluarExpresionesN(e, var)[0]]#############################################3revisar nombre funcion

        elif e[0]=='[':

            lista_var=convertir(estructuras(e[1:-1]),var)

            lista_convertida+=[lista_var]

        elif e[0]=='(':

            tupla=convertir(estructuras(e[1:-1]),var)

            lista_convertida+=[tuple(x)]

        elif e=='True':

            lista_convertida+=[True]

        elif e=='False':

            lista_convertida+=[False]

        else:

            lista_convertida+=[cambia_var(e,var)]

    return lista_convertida



#funcion que cambia las variables por el valor real    

def cambia_var(var,lista_var):

    result=var

    if var.find('#')!=-1: #si es un elemento de una tupla

        for e in var:

            if not var.isdigit() and e!='#' and e!= '(' and i!= ')':

                result=cambia_var(e,lista_var)

                if not isinstance(result,tuple):

                    result= var

                else:

                    result=cambia_tupla(result, var)

    else:

        for e in lista_var:

            if e[0]==var:

                result=e[1]

    return result



#funcion que obtiene el elemento de la tupla

def cambia_tupla(resul,var):

    if len (var)==3 or len (var)==2:

        cant=int(var[1])-1

        return result[cant]

    else:

        cont=0

        for e in  var:

            if e=='(':

                cont2=cont

                for i in var[cont:]:

                    if i== ')':

                        break

                    cont2+=1

                result=cambia_tupla(result,var[cont+1:cont2-1] )

                return cambia_tupla(result,var[:cont])

            cont+=1







#Funciones que se encargan de las condiciones booleanas y las resuelven para devolver el valor cambiado

def bool_bool(var,lis):

		if var[0]=='(' and var[-1]==')':

            var=var[1:-1]

        if var.find('<=')!=-1:

            n=var.find('<=')

            m=n+2

            signo='<='

            Primer=convertir([var[:n]],lis)        

            Segundo=convertir([var[m:]],lis)

            nueva_var=bool_bool_aux(Primer[0],Segund[0],signo,lis)

        elif Exp.find('>=')!=-1:

            n=Exp.find('>=')

            m=n+2

            signo='>='

            Primer=convertir([Exp[:n]],lista)      

            Segundo=convertir([Exp[m:]],lista)

            nueva_var=bool_bool_aux(Primer[0],Segund[0],signo,lista)

        elif Exp.find('<')!=-1:

            n=Exp.find('<')

            m=n+1

            signo='<'

            Primer=convertir([Exp[:n]],lista)        

            Segundo=convertir([Exp[m:]],lista)

            nueva_var=bool_bool_aux(Primer[0],Segund[0],signo,lista)

        elif Exp.find('>')!=-1:

            n=Exp.find('>')

            m=n+1

            signo='>'

            Primer=convertir([Exp[:n]],lista)        

            Segundo=convertir([Exp[m:]],lista)

            nueva_var=bool_bool_aux(Primer[0],Segund[0],signo,lista)

        elif Exp.find('=')!=-1:

            n=Exp.find('=')

            m=n+1

            signo='='

            Primer=convertir([Exp[:n]],lista)        

            Segundo=convertir([Exp[m:]],lista)

            nueva_var=bool_bool_aux(Primer[0],Segund[0],signo,lista)

    return nueva_var



#Funcion auxiliar de las condiciones auxiliares

def bool_bool_aux(Primero,Segundo,Signo,lista):

    if not isinstance(Primero,int):

        cambia_var(Primero,lista)

    if not isinstance(Segundo,int):

        cambia_var(Segundo,lista)

    if Segundo=="":

        return Primero

    if Signo=='<':

        return Primero < Segundo

    elif Signo=='>':

        return Primeor > Segundo

    elif Signo =='=':

        return Primero == Segundo

    elif Signo =='<=':

        return Primero<= Segundo

    elif Signo =='>=':

        return Primero >= Segundo

    elif Signo =='<>':

        return Primero!=Segundo

    else:

        return 'Error'



#Funciones auxiliares para listas, las cuales se encargan de realizar los calculos necesarios para devolver su respectivo resulado

def if_if(var,lis):

    if var[:2]=='if':

        separa=var[2:].partition('then')

        convert=convertir([separa[0]],lis)

        if convert[0]==True:

            result=if_if_aux(separa[2])

            return convertir([result[0]],lis)[0]

        else:

			#En caso de haber otro condicional dentro del que se esta evaluando se analiza antes de continuar

            return if_if(Div[2],lis)         

    else:

        convert=if_if_aux(var)

        if convert[1]=="elseif":

                convert=convert[2].partition('then')

                convert_2=convertir([convert[0]],lis)

                if convert_2[0]==True:

                    result=if_if_aux(convert[2])

                    return convertir([result[0]],lis)[0]

                else:

                    return if_if(convert[2],lis)

        else:

            if convert[1]=="else":

                result=convert[2]

                if convert[2][:3]=='(if':

                    result=convert[2][1:-1]

                return convertir([result],lis)[0]

    

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

    str=""

    for char in var:

        if char!=")":

            str+=char

        else:

            str+=char

            if evalua_tuplas(str,"(",")"):

                lista_element+=[str]

                str=""

    return lista_element
