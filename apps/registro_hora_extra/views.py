import csv
import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.registro_hora_extra.models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

import xlwt


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return RegistroHoraExtra.objects.filter(colaborador__empresa=empresa_logada)


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    # def get_success_url(self):
    #     return reverse_lazy('list_hora_extra', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        colaborador = self.request.user.colaborador

        response = json.dumps({'mensagem': 'Requisição Executada.',
                               'horas': float(colaborador.total_horas_extra)})

        return HttpResponse(response, content_type='application/json')


class NaoUtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        colaborador = self.request.user.colaborador

        response = json.dumps({'mensagem': 'Requisição Executada.',
                               'horas': float(colaborador.total_horas_extra)})

        return HttpResponse(response, content_type='application/json')


class ExportarParaCsv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_hora_extra = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Nome', 'Motivo', 'Horas'])

        for registro in registro_hora_extra:
            writer.writerow([registro.id, registro.colaborador, registro.motivo, registro.horas])

        return response


class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        collumns = ['Id', 'Colaborador', 'Motivo', 'Horas']

        for col_num in range(len(collumns)):
            ws.write(row_num, col_num, collumns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.colaborador.nome, font_style)
            ws.write(row_num, 2, registro.motivo, font_style)
            ws.write(row_num, 3, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response
