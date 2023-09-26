import random

def imprimirMatrizSimetrica(longitud,lista):
    count = 0
    if longitud == (2*2):
        matriz = [[0,0],[0,0]]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = lista[count]
                count+=1
            print(matriz[i])
    elif longitud <= (3*3):
        # Crear una matriz 3x3 llena de ceros
        matriz = [[0 for _ in range(3)] for _ in range(3)]
        coincidencias = [[0, 0], [0, 2], [1,1] ,[2, 0], [2, 2]]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                for coincidencia in coincidencias:
                    if i == coincidencia[0] and j == coincidencia[1]:
                        if count < len(lista):
                            matriz[i][j] = lista[count]
                            count += 1
                        break  # Rompe el bucle for cuando se encuentra una coincidencia
            print(matriz[i])
    elif longitud <= (4*4):
        matriz = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                    if ((i == 0 or i == 3) and (j == 0 or j == 3)) or ((i == 1 or i == 2) and (j == 1 or j == 2)):
                        if count < len(lista):
                            matriz[i][j] = lista[count]
                            count += 1
                        break  
            print(matriz[i])
    elif longitud <= (5*5):
        pass 
    elif longitud <= (6*6):
        pass
    elif longitud <= (7*7):
        pass 
    elif longitud <= (8*8):
        pass
    elif longitud <= (9*9):
        pass
    else:
        pass 



numero = input("Introduce el numero de numeros aleatorios entre (4~100): ")
numero = int(numero)
if int(numero) >= 4 and int(numero) <= 100:
    lista = []
    for i in range(0,numero):
        lista.append(random.randint(1, 100))
    #print(lista)
    imprimirMatrizSimetrica(numero,lista)
else:
    print("Debes colocar un numero entre 4~100")