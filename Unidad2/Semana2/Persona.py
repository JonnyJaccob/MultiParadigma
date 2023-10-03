from logger_base import log 

class Persona: 
    def __init__(self,id_persona=None,nombre=None,apellido = None,email = None, telefono = None) -> None:
        #python si uno tiene un valor por defecto, todos deben tener ese valor por defecto
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono

    def __str__(self) -> str:
        return f"""
            ID PERSONA {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email},
            Telefono: {self._telefono}
        """
    
    @property
    def idPersona(self):
        return self._id_persona
    @property.setter
    def idPersona(self, id):
        self._id_persona = id
    
    @property
    def Nombre(self):
        return self._nombre
    @property.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def Apellido(self):
        return self._apellido
    @property.setter
    def Apellido(self, apellido):
        self._apellido = apellido

    @property
    def Email(self):
        return self._email
    @property.setter
    def Email(self, email):
        self._email = email

    @property
    def Telefono(self):
        return self._telefono
    @property.setter
    def Telefono(self, telefono):
        self._telefono = telefono

if __name__ == "__main__":
    persona1 = Persona(1,"Juan","Perez","j@gmail.com","7171578")