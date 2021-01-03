from django.urls import path
from .views import ColaboradoresList, ColaboradorEdit, ColaboradorDelete, ColaboradorCreate,\
    relatorio_colaboradores, Pdf

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('novo/', ColaboradorCreate.as_view(), name='create_colaborador'),
    path('editar/<int:pk>/', ColaboradorEdit.as_view(), name='update_colaborador'),
    path('deletar/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),
    path('relatorio-colaboradores', relatorio_colaboradores, name='relatorio_colaboradores'),
    path('relatorio-colaboradores-html', Pdf.as_view(), name='relatorio_colaboradores_html'),

]
