from django.shortcuts import render
from .models          import Segmento,Evento

# Create your views here.

def pagina(request):
    segmentos = Segmento.objects.all()
    tipos     = Evento.TIPO_CHOICES
    eventos   = Evento.objects.all()

    data = {
        'segmentos': segmentos,
        'tipos'    : tipos,
        'eventos'  : eventos
        }

    return render(request, 'miapp/base.html',data)