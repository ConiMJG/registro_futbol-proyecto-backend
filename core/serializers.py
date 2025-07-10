from rest_framework import serializers
from .models import Equipo, Jugador
from .models import Torneo, EquipoTorneo
from .models import Partido
from .models import Pais, Torneo

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class JugadorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'posicion']

class EquipoSerializer(serializers.ModelSerializer):
    jugadores = JugadorSimpleSerializer(many=True, source='jugador_set', read_only=True)

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'entrenador', 'pais', 'escudo', 'jugadores']


class EquipoConJugadoresSerializer(serializers.ModelSerializer):
    cantidad_jugadores = serializers.SerializerMethodField()

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'entrenador', 'pais', 'cantidad_jugadores']

    def get_cantidad_jugadores(self, equipo):
        return equipo.jugador_set.count()

class TorneoSerializer(serializers.ModelSerializer):
    equipos = serializers.SerializerMethodField()

    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'pais', 'equipos']

    def get_equipos(self, torneo):
        equipos_torneo = EquipoTorneo.objects.filter(torneo=torneo)
        equipos = [et.equipo for et in equipos_torneo]
        return EquipoConJugadoresSerializer(equipos, many=True).data


class PartidoSerializer(serializers.ModelSerializer):
    equipo_local = serializers.StringRelatedField()
    equipo_visitante = serializers.StringRelatedField()
    torneo = serializers.StringRelatedField()

    class Meta:
        model = Partido
        fields = ['id', 'fecha', 'torneo', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante']


class PaisDetalleSerializer(serializers.ModelSerializer):
    equipos = serializers.SerializerMethodField()
    jugadores = serializers.SerializerMethodField()
    torneos = serializers.SerializerMethodField()

    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'equipos', 'jugadores', 'torneos']

    def get_equipos(self, pais):
        equipos = pais.equipo_set.all()
        return EquipoSerializer(equipos, many=True).data

    def get_jugadores(self, pais):
        jugadores = pais.jugador_set.all()
        return JugadorSerializer(jugadores, many=True).data

    def get_torneos(self, pais):
        torneos = pais.torneo_set.all()
        return TorneoSerializer(torneos, many=True).data
