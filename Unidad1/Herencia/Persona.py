class Persona:
    #Metodo Constructor
    def __init__(self,nombre,edad) -> None:
        self._nombre = nombre
        self._edad = edad
    #Metodo ToString en python
    def __str__(self) -> str:
        return f"Persona: {self._nombre}, Edad: {self._edad}"
    

