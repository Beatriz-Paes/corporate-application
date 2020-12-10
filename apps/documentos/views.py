from django.urls import reverse_lazy

from .models import Documento
from django.views.generic import CreateView, DeleteView


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documents')