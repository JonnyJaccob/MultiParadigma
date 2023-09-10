#Palabras = input("Introduce palabras, porfavor xd \n")
#keys = Palabras.split()
#diccionario = {}
#for i in range(len(keys)):
#    valor = diccionario.__contains__(keys[i])
#    if valor:
#        diccionario[keys[i]] = diccionario[keys[i]] + 1
#    else:
#        diccionario[keys[i]] = 1
#
#print(diccionario)

Palabras = input("Introduce palabras, por favor: ")

# Divide la entrada en palabras
keys = Palabras.split()

# Crea un diccionario para contar las palabras
diccionario = {}

# Itera a través de las palabras y cuenta su frecuencia
for palabra in keys:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(diccionario)
