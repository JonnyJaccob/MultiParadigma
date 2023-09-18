lista = []
for i in range(0,10):
    sublista = []
    for j in range(1,11):
        sublista.append((i*10) + j) 
    lista.append(sublista)

for sublista in lista:
    print(sublista)

def SumaPosicion(posicion):
    if posicion >= 0 and posicion <=9:
        listax = lista[posicion]
        x = 0
        for i in listax:
            x+= i 
        return x
    elif posicion == 10:
        y = 0
        listatemp = []
        for i in range(0,10):
            y += lista[i][i]
            #listatemp.append(lista[i][i])
        for i in range(10):
            l = 9 - i
            m = i 
            y += lista[l][m]
            #listatemp.append(lista[l][m])
        print(listatemp)
        return y
    else:
        raise Exception("El numero supera el rango")

pregunta = input("Introduce la posicion que quieres sumar (0~10):\n")
try:
    numero = int(pregunta)
    print(f"La suma de toda la posicion {numero}: {SumaPosicion(numero)}")
except Exception as e:
    print(e)
