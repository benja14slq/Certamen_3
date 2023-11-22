from django.contrib import admin
from .models import Evento, Segmento
from .forms import EventoForm

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    form = EventoForm

admin.site.register(Evento, EventoAdmin)
admin.site.register(Segmento)