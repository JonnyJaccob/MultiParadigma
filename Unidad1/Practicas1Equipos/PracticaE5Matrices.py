import random

# Crear la matriz original de 5x4 y la matriz resultante de 5x4, ambas inicializadas con ceros
matriz_original = [[random.randint(1, 30) for _ in range(4)] for _ in range(5)]
matriz_resultante = [[0] * 4 for _ in range(5)]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_original:
    print(fila)

# Recorrer la matriz original y llenar la matriz resultante según las condiciones
for i in range(5):
    for j in range(4):
        valor = matriz_original[i][j]
        if valor % 3 == 0 and valor % 5 == 0:
            matriz_resultante[i][j] = 4
        elif valor % 3 == 0:
            matriz_resultante[i][j] = 2
        elif valor % 5 == 0:
            matriz_resultante[i][j] = 3

# Mostrar la matriz resultante
print("Matriz resultante:")
for fila in matriz_resultante:
    print(fila)
