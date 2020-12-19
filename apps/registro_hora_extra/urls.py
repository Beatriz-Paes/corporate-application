from django.urls import path
from .views import HoraExtraList, HoraExtraCreate, HoraExtraEdit, HoraExtraDelete, HoraExtraEditBase

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
