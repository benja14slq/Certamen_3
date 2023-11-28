from django.shortcuts import render
from .models          import Segmento,Evento

# Create your views here.

def pagina(request):
    segmentos = Segmento.objects.all()
    tipos     = Evento.TIPO_CHOICES
    eventos   = Evento.objects.all().order_by('fecha_inicio')

    segmento_seleccionado = request.GET.get('segmento')
    tipo_seleccionado = request.GET.get('tipo')

    if segmento_seleccionado:
        eventos = eventos.filter(segmento__segmento_nombre=segmento_seleccionado).order_by('fecha_inicio')

    if tipo_seleccionado:
        eventos = eventos.filter(tipo= tipo_seleccionado).order_by('fecha_inicio')


    data = {
        'segmentos': segmentos,
        'tipos'    : tipos,
        'eventos'  : eventos,
        'segmento_seleccionado': segmento_seleccionado,
        'tipo_seleccionado': tipo_seleccionado,
        }

    return render(request, 'miapp/base.html',data)