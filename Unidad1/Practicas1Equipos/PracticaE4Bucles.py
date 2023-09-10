respuesta = input("Coloca una frase y una letra, para contar el numero de veces que aparece: \n"+
                  "Formato: FRASE - LETRA\n")
c = 0
frase = respuesta.split(" - ")[0]
letra = respuesta.split(" - ")[1].strip() 
c = 0
for i in frase:
    if(i == letra):
        c += 1
    
print("Frase: " + frase + ", Numero de repeticiones: " + f"{c}")

#apariciones = frase.count(letra)