from personas.models import persona, Domicilio
from django.forms import EmailInput, ModelForm, TextInput


class PersonaForm(ModelForm):
    class Meta:
        model = persona
        fields = '__all__'
        widgets = {
            'email':EmailInput(attrs={'type': 'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle' : TextInput(attrs={'type':'number'})
        }