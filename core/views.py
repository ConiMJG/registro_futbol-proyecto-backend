from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework import filters

from .models import Jugador
from .forms import JugadorForm

from .models import Equipo
from .forms import EquipoForm

from rest_framework import generics
from .serializers import JugadorSerializer, EquipoSerializer

from .models import Torneo
from .serializers import TorneoSerializer

from .models import Partido
from .serializers import PartidoSerializer

from .models import Pais
from .serializers import PaisDetalleSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import JugadorFilter


def jugador_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores/jugador_list.html', {'jugadores': jugadores})

def jugador_create(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
    else:
        form = JugadorForm()
    return render(request, 'jugador_form.html', {'form': form})

def jugador_update(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'jugadores/jugador_form.html', {'form': form})

def jugador_delete(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        jugador.delete()
        return redirect('jugador_list')
    return render(request, 'jugadores/jugador_confirm_delete.html', {'jugador': jugador})


def equipo_list(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/equipo_list.html', {'equipos': equipos})

def equipo_create(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipo_list')
    else:
        form = EquipoForm()
    return render(request, 'equipos/equipo_form.html', {'form': form})

def equipo_update(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipo_list')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'equipos/equipo_form.html', {'form': form})

def equipo_delete(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipo_list')
    return render(request, 'equipos/equipo_confirm_delete.html', {'equipo': equipo})

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = JugadorFilter
    search_fields = ['nombre', 'posicion', 'equipo__nombre']
    ordering_fields = ['nombre', 'posicion', 'equipo__nombre']
    ordering = ['nombre']

class EquipoListAPIView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'entrenador', 'pais__nombre']
    ordering_fields = ['nombre', 'entrenador', 'pais__nombre']
    ordering = ['nombre']

class EquipoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TorneoListAPIView(generics.ListCreateAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']
    ordering = ['nombre']


class PartidoListAPIView(generics.ListCreateAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['equipo_local__nombre', 'equipo_visitante__nombre']
    ordering_fields = ['fecha', 'equipo_local__nombre']
    ordering = ['fecha']


class PaisDetailAPIView(generics.RetrieveAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisDetalleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
