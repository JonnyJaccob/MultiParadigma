x = 1 #Entero
y = 2.2 #Flotante
#z = 3j #Complejos 

#print(type(x),type(y),type(z))
#print(id(x),id(y),id(z))
xflotante = float(x)
ycomplejo = complex(y)
#zentero = int(z) 
print(type(xflotante),type(ycomplejo))

#Boleanos 
#x = True
x = 1
if  x : 
    print('x')
#y = False
y = 0
if not y:
    print('y')
#preg exam
x=[]
if bool(x):
    print('x is list')
x={}
if bool(x):
    print('x is dict')
x = {0}
if bool(x):
    print('x is hash')
"""
x = []: Esto crea una lista vacía en Python. Una lista es una colección ordenada y mutable de elementos. Puedes agregar, eliminar y modificar elementos en una lista. En este caso, x es una lista vacía sin ningún elemento.

x = {}: Esto crea un diccionario vacío en Python. Un diccionario es una colección de pares clave-valor, donde cada clave debe ser única y se usa para acceder a su correspondiente valor. En este caso, x es un diccionario vacío sin ningún par clave-valor.

x = {0}: Esto crea un diccionario con un par clave-valor. La clave es 0 y el valor es None (valor nulo), ya que no se proporciona ningún valor explícito. Si deseas asignar un valor específico, puedes hacerlo utilizando el formato clave-valor, por ejemplo: x = {0: "valor"}.
"""


#Cadenas
x = "Hola Mundo"
print(x)
saludo = f'Saludo: {x}'
print(saludo)
saludo = 'Saludo: '+x + str(y)
print(saludo)

#Multilinea
Texto = """
Hola
Buenas Tardes
Adios
"""
print(Texto)

#Separador
x=5
y=6
z=7
print(x,y,z,sep='--',end='\n')

nombre ="Luis Daniel Castillo"

print(nombre[::-1])
print(nombre[2:2:-1])

print(nombre[-1])
