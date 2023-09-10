import exportador
import importador

# Supongamos que tienes una matriz inicial
matriz_inicial = [['a', 1], ['b', 2], ['c', 3]]

# Llamamos a los métodos de exportador.py para convertir la matriz en un diccionario, duplas en matriz y conjunto en lista
diccionario_resultante = exportador.matriz_a_diccionario(matriz_inicial)
matriz_resultante = exportador.duplas_a_matriz([(1, 2), (3, 4), (5, 6)])
lista_resultante = exportador.set_a_lista({1, 2, 3, 4, 5})

# Imprimimos los resultados
print(diccionario_resultante)
print(matriz_resultante)
print(lista_resultante)

# Luego, llamamos a los métodos de importador.py para convertir el diccionario en matriz, lista en conjunto y matriz en tupla
matriz_resultante_2 = importador.matriz_a_diccionario([['a', 1, 2], ['b', 3, 4], ['c', 5, 6]])
conjunto_resultante = importador.lista_a_set([1, 2, 3, 4, 5])
tupla_resultante = importador.matriz_a_tupla([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprimimos los resultados
print(matriz_resultante_2)
print(conjunto_resultante)
print(tupla_resultante)
 