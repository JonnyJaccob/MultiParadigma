diccionario = {'PLATANO':1.35, 'MANZANA':0.80, 'PERA':0.85, 'NARANJA':0.7}
while True:
    try:
        fruta, kilos = input('Introduce el nombre de la fruta y el numero de kilos que quieres separados por ( - ).\n').split(" - ")
    except ValueError:
        print("Parece que introduciste el formato incorrecto, intenta de nuevo...")
    try:
        kilosf = float(kilos)
        break
    except TypeError:
        print("Parece que el dato de kilos no es un numero, intenta de nuevo...")
    except ValueError:
        print("Parece que el dato de kilos no es un numero, intenta de nuevo...")

bandera = False
for key in diccionario:
    if key == fruta:
        bandera = True
        print(f"Recibo:\nNombre de la fruta: {fruta},\nPrecio: {'{:.2f}'.format(diccionario[fruta])},\nCosto total: {'{:.2f}'.format(diccionario[fruta]*kilosf)}")
if bandera == False:
    print("Parece que introduciste una fruta que no esta en la lista, por favor, introduce cualquiera de las sig... (PLATANO, MANZANA, PERA, NARANJA)")