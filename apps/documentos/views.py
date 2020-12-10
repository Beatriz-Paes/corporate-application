from django.urls import reverse_lazy

from .models import Documento
from django.views.generic import CreateView, DeleteView


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['colaborador_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# class DocumentoDelete(DeleteView):
#     model = Documento
#     success_url = reverse_lazy('list_documents')
