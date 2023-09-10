print("quieres una pizza vegetariana??")
res = int(input(" 1.- si / 2.- No \n"))
pizza = ["motzarela", "tomate"]
bandera = 0
while bandera == 0:
    if res == 1:
        respuesta = int(input("favor de ingresar el ingrediente que desea \n 1.- pimiento \n 2.- tofu \n "))
        pizza.append("pimiento ") if respuesta == 1 else (pizza.append("tofu") if respuesta == 2 else next)
        if respuesta == 1 or respuesta == 2:
                bandera = 1
        else:
                bandera = 0
    else:
        respuesta = int(input("favor de ingresar el ingrediente que desea \n 1.- pepperoni \n 2.- jamon \n 3.-Salami \n " ))
        pizza.append("pepperoni") if respuesta == 1 else (pizza.append("jamon") if respuesta == 2 else (pizza.append("salami") if respuesta == 3 else next))
        if respuesta == 1 or respuesta == 2 or respuesta == 3 :
                bandera = 1
        else:
                bandera = 0
print(f"{pizza} tipo: vegetariana") if res == 1 else print(f"{pizza} tipo: no vegetariana")