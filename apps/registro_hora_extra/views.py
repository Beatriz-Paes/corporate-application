from django.shortcuts import render
from django.views.generic import ListView

from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return RegistroHoraExtra.objects.filter(colaborador__empresa=empresa_logada)