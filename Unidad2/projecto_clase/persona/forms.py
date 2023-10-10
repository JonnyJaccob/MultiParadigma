from django.forms import ModelForm,EmailInput
from persona.models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        widget = {
            'email':EmailInput(
                attrs={
                    'type':'email',
                    'class':'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }