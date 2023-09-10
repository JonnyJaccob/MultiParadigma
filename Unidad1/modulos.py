#from csv import DictReader
import csv
import random #todos los elementos de random

numRandom = random.randint(0,100)

while True:
    #console.writeline y readline en una sola linea
    numero = int(input("Cual sera el numero entre 0 y 100?: "))
    print(numero)
    if(numero == numRandom): 
        break
    if numero > numRandom:
        print("El numero es mayor")
    else:
        print("El numero capturado es menor")
print(f"El numero era {numRandom}")