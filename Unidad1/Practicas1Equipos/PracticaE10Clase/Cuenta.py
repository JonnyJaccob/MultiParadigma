class Cuenta:
    def __init__(self, titular="", cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad

    def mostrar(self):
        return f"Titular: {self._titular} --- Cantidad: {self._cantidad}"

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad >= 0:
            self._cantidad -= cantidad