from django.views.generic import ListView
from .models import Colaborador


class ColaboradoresList(ListView):
    model = Colaborador
