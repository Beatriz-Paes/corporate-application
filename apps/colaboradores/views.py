import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Colaborador
from django.urls import reverse_lazy


class ColaboradoresList(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)


class ColaboradorEdit(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']


class ColaboradorDelete(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('list_colaboradores')


class ColaboradorCreate(CreateView):
    model = Colaborador
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        colaborador = form.save(commit=False)
        username = colaborador.nome.split(' ')[0] + colaborador.nome.split(' ')[1]
        colaborador.empresa = self.request.user.colaborador.empresa
        colaborador.user = User.objects.create(username=username)
        colaborador.save()

        return super(ColaboradorCreate, self).form_valid(form)


def relatorio_colaboradores(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.drawString(250, 810, "Lista de Colaboradores")

    # palavras = ['palavra1', 'palavra2', 'palavra3']
    colaboradores = Colaborador.objects.filter(empresa=request.user.colaborador.empresa)

    str_ = 'Nome: %s | Hora Extra: %sh'

    y = 750

    for c in colaboradores:
        p.drawString(10, y - 20, str_ % (c.nome, c.total_horas_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
