A = [[1,2,3],
    [4,5,6]]

B = [[-1,0],
     [0,1],
     [1,1]]

# Inicializar una matriz vacía para el resultado
resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
# Realizar la multiplicación de matrices
for i in range(len(A)):
    #print(resultado)
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            resultado[i][j] += A[i][k] * B[k][j]

# Mostrar el resultado
for fila in resultado:
    print(tuple(fila))