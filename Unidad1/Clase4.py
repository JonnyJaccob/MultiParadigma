#While y funciones en python 

#While 
x= 1
while x>0:
    x -=1
    print(x)
x = 5
y = 0
while x > 0 and y<5:
    #if x==2:
        #break;
        #continue
    y+=1
    x-=1
    print(x,y)
else:
    #imprimira solo si termino todas sus interacciones
    print("Fin del calculo")
    #Si se quiebra o se salta no se imprimira.

# en vez de try-catch es try-except
try:
    pass
except:
    pass

try:
    s = {1,2,3}
    s[2] = 10
except Exception as e:
    print(e)
print("Fin de cadena")
#Funciones
def suma(a,b):
    return a+b
print(suma(10,5))
#Estetica de tipo de datos
def suma(a:int,b:int)->int:
    return a+b
print(suma(10,5))

def suma(a:int,b:int)->int:
    return a+b
print(suma(b=10,a=90))

x = 10
z = 50
y = 2 
def multiplicacion(a,b,c=1): #debes tener un valor asignado desde el que usaste hasta el final,
#porque si la ultima no es asignada como la del medio tira error.
    return a * b*c

print(multiplicacion(x,z))

def algo():
    '''
    Esta funcion hace algo
    '''
print(help(print))

lista = [1,2,3,4]
#def suma():
#    x = 1
#    for i in x:
#        suma += 1
#    return suma 
#print(suma(lista))

def suma(*x):
    print(type(x))
    suma(0)
    for i in x: 
        sum += 1
        return suma
    
#pregunta de examen 
print(suma(*(1,2,3,4,5,6)))
   
#mañana doble asterisco
def suma(**c):
    pass
#Hoy
# n parametros con * con el nombre del parametro
def resta(*numeros):
    resta = 0
    for i in numeros:
        resta -= 1
    return resta 
print(resta(1,2,3,4,5,6,7,8,9))

##** = diccionario 
def suma(**kwargs):
    suma=0
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
        suma += value
    return suma

print(suma(a=5,b=2,c=7,d=20))

di = {'a':10,'b':11,'c':12,'d':9}
suma(**di) ##diccionario unpacking, desempaquetado de diccionario

def mifuncion():
    print("Entra")
    return 
    print("") #nunca se ejecuta 

def sumaymedia(*x):
    suma = 0
    for n in x:
        suma+=n
    media = suma / len(x)
    return suma,media

resultadoSuma, resultadoMedia = sumaymedia(1,2,3,4,5,6,7,8,9)

print(resultadoSuma,resultadoMedia)

def function(a,b,*args,**kwargs):
    print('a ',a)
    print('b ',b)
    for arg in args:
        print('args ', arg)
    for key,value in kwargs.items():
        print(key,' = ', value)

function(1,6,'k',4,3,4,"Hola",e=1,c=4,d=10)
numeros = list(range(1,101,1))
def suma(*numeros):
    suma=0
    for n in numeros:
        suma += n
    return suma
print(suma(*numeros))

x = (lambda *n: print(suma(n)))(*list(range(1,101,1)))

def multiplicador(n):
    return lambda a:print(a*n)
duplicador = multiplicador(2)
triplicador = multiplicador(3)
print(duplicador(11))
print(triplicador(11))

suma = None 

try:
    suma = 1 + "1"
    #suma = 1 + 2
except Exception as e:
    print(e)
else:
    print("Else suma ",suma)
finally:
    print("Finally ",suma)  #se ejecuta haya o no excepciones 

