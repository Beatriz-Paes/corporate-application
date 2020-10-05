from django.views.generic import ListView
from .models import Colaborador


class ColaboradoresList(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)