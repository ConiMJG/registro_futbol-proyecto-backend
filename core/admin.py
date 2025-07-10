from django.contrib import admin
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido

from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

admin.site.register(Pais)
admin.site.register(Equipo)
admin.site.register(Torneo)
admin.site.register(EquipoTorneo)
admin.site.register(Jugador)
admin.site.register(Partido)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)