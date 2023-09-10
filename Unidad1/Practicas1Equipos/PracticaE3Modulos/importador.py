def matriz_a_diccionario(matriz):
    diccionario = {}
    for fila in matriz:
        if len(fila) >= 2:
            clave = fila[0]
            valor = fila[1:]
            diccionario[clave] = valor
    return diccionario

# Ejemplo de uso:
matriz_ejemplo = [['a', 1, 2], ['b', 3, 4], ['c', 5, 6]]
diccionario_resultante = matriz_a_diccionario(matriz_ejemplo)
print(diccionario_resultante)

def lista_a_set(lista):
    conjunto = set(lista)
    return conjunto

def matriz_a_tupla(matriz):
    tupla = tuple(tuple(fila) for fila in matriz)
    return tupla
