from django.shortcuts import render
from rest_framework import viewsets
from app.models import Evento
from .serializers import EventoSerializer

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer

    def get_queryset(self):
        queryset = Evento.objects.all()
        year = self.request.query_params.get('year', None)
        type = self.request.query_params.get('type', None)
        segment = self.request.query_params.get('segment', None)

        if year:
            queryset = queryset.filter(start_date__year=year)
        if type:
            queryset = queryset.filter(type=type)
        if segment:
            queryset = queryset.filter(segment=segment)

        return queryset