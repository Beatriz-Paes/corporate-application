from rest_framework import serializers
from apps.colaboradores.models import Colaborador
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class ColaboradorSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)

    class Meta:
        model = Colaborador
        fields = ['nome', 'id', 'departamentos', 'empresa', 'imagem', 'total_horas_extra', 'registrohoraextra_set']
