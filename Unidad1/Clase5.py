class rectangulo:
    def __init__(self, ancho, largo):
        self._ancho = ancho
        self._largo=largo

    #get
    @property
    def Ancho (self):
        return self._ancho

    @Ancho.setter
    def Ancho(self,ancho):
        if ancho < 5:
            self._ancho = ancho
        else:
            print('error')

    def CalcularArea(self):
        return self._ancho * self._largo

    def CalcularPerimetro(self):
        return (self._ancho)
    
class Cuadrado:
    def __init__(self, ancho):
        self._ancho = ancho

    #get
    @property
    def Ancho (self):
        return self._ancho

    @Ancho.setter
    def Ancho(self,ancho):
        if ancho < 5:
            self._ancho = ancho
        else:
            print('error')

    def CalcularArea(self):
        return self._ancho * self._largo

    def CalcularPerimetro(self):
        return (self._ancho)