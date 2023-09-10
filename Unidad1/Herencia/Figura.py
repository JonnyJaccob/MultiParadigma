class Figura : 
    def __init__(self, ancho, largo) -> None:
        self._ancho = ancho
        self._largo = largo 

    def __str__(self) -> str:
        return f"Ancho: {self._ancho}, Largo: {self._largo}"