from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    path('novo/<int:colaborador_id>', DocumentoCreate.as_view(), name='create_document'),
    # path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='delete_documento'),

]
