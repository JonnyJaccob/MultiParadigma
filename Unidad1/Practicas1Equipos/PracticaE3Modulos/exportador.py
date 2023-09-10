def matriz_a_diccionario(matriz):
    diccionario = {}
    for fila in matriz:
        if len(fila) == 2:
            clave, valor = fila
            diccionario[clave] = valor
    return diccionario

# Ejemplo de uso:
matriz_ejemplo = [['a', 1], ['b', 2], ['c', 3]]
diccionario_resultante = matriz_a_diccionario(matriz_ejemplo)
print(diccionario_resultante)

def duplas_a_matriz(duplas):
    matriz = [list(dupla) for dupla in duplas]
    return matriz

# Ejemplo de uso:
duplas_ejemplo = [(1, 2), (3, 4), (5, 6)]
matriz_resultante = duplas_a_matriz(duplas_ejemplo)
print(matriz_resultante)

def set_a_lista(conjunto):
    return list(conjunto)

 