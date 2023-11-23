from django import forms
from .models import Evento, Segmento

class EventoForm(forms.ModelForm):
    class meta:
        model = Evento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['segmento'].queryset = Segmento.objects.filter(
            segmento_nombre__in=[choice[0] for choice in Segmento.SEGMENTOS_CHOICES]
        )