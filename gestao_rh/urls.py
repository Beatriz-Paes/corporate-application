from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from apps.core import views
from apps.colaboradores.api.views import ColaboradorViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Colaboradores API',
        default_version='v1',
        description="Retorna todos os colaboradores"
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/colaboradores', ColaboradorViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('documento/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

