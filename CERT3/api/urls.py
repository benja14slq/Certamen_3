from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('evento', views.EventoViewSet, basename='evento')

urlpatterns = [
    path('', include(router.urls)),
]