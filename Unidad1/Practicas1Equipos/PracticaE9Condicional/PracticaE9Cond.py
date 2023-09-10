pizza = input('¿Quiere comprar una pizza vegetariana? (Y/N): ').strip().lower()

if pizza == 'y':
    ingredientes_disponibles = {'1': 'Pimiento', '2': 'Tofu'}
    while True:
        ingrediente = input('1- Pimiento\n2- Tofu\nElija un ingrediente (1 o 2): ').strip()
        if ingrediente in ingredientes_disponibles:
            break
        else:
            print('Por favor, elija una opción válida.')

    ing = ingredientes_disponibles[ingrediente]
    tipo_pizza = "Pizza Vegetariana"
else:
    ingredientes_disponibles = {'1': 'Peperoni', '2': 'Jamon', '3': 'Salami'}
    while True:
        ingrediente = input('1- Peperoni\n2- Jamon\n3- Salami\nElija un ingrediente (1, 2 o 3): ').strip()
        if ingrediente in ingredientes_disponibles:
            break
        else:
            print('Por favor, elija una opción válida.')

    ing = ingredientes_disponibles[ingrediente]
    tipo_pizza = "Pizza Normal"

print(f"Tipo de Pizza: {tipo_pizza}\nIngredientes:\n1- Mozzarella\n2- Tomate\n3- {ing}\n")
