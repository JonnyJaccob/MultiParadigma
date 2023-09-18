from Cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion=0.0):
        super().__init__(titular)
        self._bonificacion = bonificacion

    def esTitularValido(self, edad):
        return 18 <= edad < 25

    def retirar(self, cantidad, edad):
        if cantidad >= 0 and self.esTitularValido(edad):
            self._cantidad -= cantidad

    def mostrar(self):
        return super().mostrar() + f" --- Cuenta Joven, Bonificación: {self._bonificacion}%"
