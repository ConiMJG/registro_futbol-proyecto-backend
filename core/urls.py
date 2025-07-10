from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet

router = DefaultRouter()
router.register(r'api/jugadores', JugadorViewSet, basename='jugador')


urlpatterns = [
    path('jugadores/', views.jugador_list, name='jugador_list'),
    path('jugadores/crear/', views.jugador_create, name='jugador_create'),
    path('jugadores/<int:pk>/editar/', views.jugador_update, name='jugador_update'),
    path('jugadores/<int:pk>/eliminar/', views.jugador_delete, name='jugador_delete'),
    path('equipos/', views.equipo_list, name='equipo_list'),
    path('equipos/crear/', views.equipo_create, name='equipo_create'),
    path('equipos/<int:pk>/editar/', views.equipo_update, name='equipo_update'),
    path('equipos/<int:pk>/eliminar/', views.equipo_delete, name='equipo_delete'),
    # API Equipos
    path('api/equipos/', views.EquipoListAPIView.as_view(), name='api_equipo_list'),
    path('api/equipos/<int:pk>/', views.EquipoDetailAPIView.as_view(), name='api_equipo_detail'),
    # API Torneos
    path('api/torneos/', views.TorneoListAPIView.as_view(), name='api_torneo_list'),
    # API Partidos
    path('api/partidos/', views.PartidoListAPIView.as_view(), name='api_partido_list'),
    # API País específico
    path('api/paises/<int:pk>/', views.PaisDetailAPIView.as_view(), name='api_pais_detail'),
]


urlpatterns += router.urls
