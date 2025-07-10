from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # <-- esto es esencial
    path('api-auth/', include('rest_framework.urls')),  # 👈 ESTA LÍNEA PERMITE LOGIN DESDE DRF
]


schema_view = get_schema_view(
   openapi.Info(
      title="Registro de Fútbol API",
      default_version='v1',
      description="Documentación de la API para el proyecto de fútbol",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[TokenAuthentication],  # 👈 Esto lo puedes agregar si quieres visibilidad
)


urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
