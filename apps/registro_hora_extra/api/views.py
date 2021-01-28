from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from apps.registro_hora_extra.models import RegistroHoraExtra
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registro de horas extra to be viewed or edited.
    """
    queryset = RegistroHoraExtra.objects.all().order_by('colaborador')
    serializer_class = RegistroHoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated]
