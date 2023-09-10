print("---Menú Pizzería: Tipos de Pizza---\n\t1- Vegetariana\n\t2- No Vegetariana\n")
tipoPizza = input("Teclee el número correspondiente al tipo de pizza que desea pedir: ")
#Decisión sobre el tipo de pizza
if tipoPizza == "1":
    print("---INGREDIENTES DE PIZZAS VEGETARIANAS---\n\t1- Pimiento\n\t2- Tofu")
    ingredientePizza = input("Teclee el número correspondiente al ingrediente que desea añadir a su pizza vegetariana: ")
    if ingredientePizza != "1" and ingredientePizza != "2":
        print("ERROR DE CAPTURA: El valor/número que ud. proporcionó no se encuentra dentro de nuestro menú de ingredientes para pizzas vegetarianas (1- Pimiento, 2- Tofu).")
    else:
        print("Pizza Vegetariana con Mozzarella, Tomate y ", end="")
        if ingredientePizza == "1":
            print("Pimiento")
        else:
            print("Tofu")
else:
    if tipoPizza == "2":
        print("---INGREDIENTES DE PIZZAS NO VEGETARIANAS---\n\t1- Pepperoni\n\t2- Jamón\n\t3- Salami")
        ingredientePizza = input("Teclee el número correspondiente al ingrediente que desea añadir a su pizza no vegetariana: ")
        if ingredientePizza != "1" and ingredientePizza != "2" and ingredientePizza != "3":
            print("ERROR DE CAPTURA: El valor/número que ud. proporcionó NO se encuentra dentro de nuestro menú de ingredientes para pizzas NO vegetarianas (1- Pepperoni, 2- Jamón, 3- Salami).")
        else:
            print("Pizza NO Vegetariana con Mozzarella, Tomate y ", end="")
            if ingredientePizza == "1":
                print("Pepperoni")
            elif ingredientePizza == "2":
                print("Jamón")
            else:
                print("Salami")
    else:
        print("ERROR DE CAPTURA: El valor/número que ud. proporcionó no se encuentra dentro de nuestro menú de pizzas (1- Vegetariana, 2- No Vegetariana).")