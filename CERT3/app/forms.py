from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class meta:
        model = Evento
        fields = '__all__'