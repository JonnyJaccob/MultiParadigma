precioPayaso = 2
precioMuñeca = 3

pesoPayaso = 112
pesoMuñeca = 75

payasos = int(input("Ingrese el numero de payasos vendidos: "))
muñecas = int(input("Ingrese el numero de muñecas vendidas: "))

pesoTotal = (payasos * pesoPayaso) + (muñecas * pesoMuñeca)
costo = (payasos * pesoPayaso) / 100 * precioPayaso + (muñecas * pesoMuñeca) / 75 * precioMuñeca

if pesoTotal < 1000.00:
    print("El peso total del paquete es de: ", pesoTotal, "gramos")
else:
    print("El peso total del paquete es de: ", pesoTotal / 1000.00, "kilo(s)")

print("El costo total del envio es de: $", costo.__round__(2))