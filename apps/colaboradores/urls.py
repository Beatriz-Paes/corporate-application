from django.urls import path
from .views import ColaboradoresList, FuncionarioEdit

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_colaborador'),

]
