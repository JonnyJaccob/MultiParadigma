class ControlMatriz:
    def __init__(self,lista):
        self._lista = lista 

    def matriz_a_diccionario(self,matriz):
        diccionario = {}
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                clave = f'L{i}N{j}'
                diccionario[clave] = matriz[i][j]
        return diccionario
    
x = ControlMatriz("")
matriz = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
try:
    y = x.matriz_a_diccionario(matriz)
    print(y)
except Exception as e:
    print(e)
