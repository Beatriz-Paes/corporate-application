from django.db import models
from django.urls import reverse

from apps.colaboradores.models import Colaborador


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_colaborador', args=[self.pertence.id])

    def __str__(self):
        return self.descricao
