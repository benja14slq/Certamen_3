from django.shortcuts import render
from rest_framework import viewsets
from app.models import Evento
from .serializers import EventoSerializer

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

    def get_queryset(self):
        queryset = Evento.objects.all()
        año = self.request.query_params.get('año', None)
        tipo = self.request.query_params.get('tipo', None)
        segmento = self.request.query_params.get('segmento', None)

        try:
            if año:
                queryset = queryset.filter(fecha_inicio__year=año)
            if tipo:
                queryset = queryset.filter(tipo=tipo)
            if segmento:
                queryset = queryset.filter(segmento=segmento)
        except ValueError:
            queryset = Evento.objects.none()
        
        queryset = queryset.order_by('fecha_inicio')

        return queryset