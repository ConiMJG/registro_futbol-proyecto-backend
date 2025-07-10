import django_filters
from .models import Jugador, Partido

class JugadorFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    posicion = django_filters.CharFilter(lookup_expr='icontains')
    equipo__nombre = django_filters.CharFilter(field_name='equipo__nombre', lookup_expr='icontains')

    class Meta:
        model = Jugador
        fields = ['nombre', 'posicion', 'equipo__nombre']

class PartidoFilter(django_filters.FilterSet):
    fecha_min = django_filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_max = django_filters.DateFilter(field_name='fecha', lookup_expr='lte')

    class Meta:
        model = Partido
        fields = ['fecha_min', 'fecha_max', 'torneo', 'equipo_local', 'equipo_visitante']
