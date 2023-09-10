producto = input("Introduce el nombre del producto\n")
precio = float(input("Introduce su precio\n"))
unidades = int(input("Introduce su numero de unidades\n"))

strprecio = '{:010,.2f}'.format(precio)
strprecio = strprecio.replace(",", "")
strunitario = '{:03,.0f}'.format(unidades)
strunitario = strunitario.replace(",", "")
costetotal = '{:013,.2f}'.format((precio*unidades))
costetotal = costetotal.replace(",", "")

print(f" Nombre del producto: {producto} ...\n Precio Unitario: {strprecio} ...\n Numero de unidades: {strunitario} ...\n Coste Total: {costetotal}")

#str(round(Precio,3)).zfill(3)


#producto = input('Introduce el nombre del producto: ')
#precio = float(input('Introducde el precio unitario: '))
#unidades = int(input('Introduce el número de unidades: '))
#print('{producto}: {unidades:3d} unidades x {precio:6.2f} = {total:8.2f}'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))