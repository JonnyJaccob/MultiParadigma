
from Cuenta_Joven import *

# Crear una cuenta estándar
cuenta_normal = Cuenta("Juan Pérez", 1000.0)

# Realizar operaciones en la cuenta estándar
cuenta_normal.ingresar(200.0)
cuenta_normal.retirar(300.0)

# Mostrar información de la cuenta estándar
print(cuenta_normal.mostrar())  # Debería mostrar: "Titular: Juan Pérez --- Cantidad: 900.0"

# Crear una cuenta joven
cuenta_joven = CuentaJoven("María López", 10.0)  # Bonificación del 10%

# Realizar operaciones en la cuenta joven
cuenta_joven.ingresar(100.0)
cuenta_joven.retirar(50.0, 22)  # Suponiendo que María tiene 22 años

# Mostrar información de la cuenta joven
print(cuenta_joven.mostrar())  # Debería mostrar: "Titular: María López --- Cantidad: 50.0 --- Cuenta Joven, Bonificación: 10.0%"