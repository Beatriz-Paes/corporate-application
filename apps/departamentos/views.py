from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.colaborador.empresa
        departamento.save()

        return super(DepartamentoCreate, self).form_valid(form)
