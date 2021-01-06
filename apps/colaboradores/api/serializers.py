from rest_framework import serializers
from apps.colaboradores.models import Colaborador


class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['nome', 'departamentos', 'empresa', 'imagem']
