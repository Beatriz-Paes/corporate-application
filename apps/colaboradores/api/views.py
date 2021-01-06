from rest_framework import viewsets, permissions
from apps.colaboradores.models import Colaborador
from apps.colaboradores.api.serializers import ColaboradorSerializer
from rest_framework.authentication import TokenAuthentication


class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows colaboradores to be viewed or edited.
    """
    queryset = Colaborador.objects.all().order_by('nome')
    serializer_class = ColaboradorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
