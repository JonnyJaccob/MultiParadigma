diccionario = {'PLATANO':1.35, 'MANZANA':0.80, 'PERA':0.85, 'NARANJA':0.7}

fruta, kilos = input('Introduce el nombre de la fruta y el numero de kilos que quieres separados por ( - ).\n').split(" - ")
print(f"Recibo:\nNombre de la fruta: {fruta},\nPrecio: {diccionario[fruta]},\nCosto total: {diccionario[fruta]*(int(kilos))}")