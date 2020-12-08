from django.urls import path
from .views import ColaboradoresList, ColaboradorEdit, ColaboradorDelete

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('editar/<int:pk>/', ColaboradorEdit.as_view(), name='update_colaborador'),
    path('delete/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),

]
