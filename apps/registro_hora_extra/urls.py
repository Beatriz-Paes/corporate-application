from django.urls import path
from .views import HoraExtraList
    # HoraExtraCreate, HoraExtraUpdate, HoraExtraDelete

urlpatterns = [
    path('list', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    # path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='update_hora_extra'),
    # path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
