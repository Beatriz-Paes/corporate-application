from django.urls import path
from .views import HoraExtraList, HoraExtraCreate, HoraExtraEdit, HoraExtraDelete, HoraExtraEditBase,\
    UtilizouHoraExtra, NaoUtilizouHoraExtra, ExportarParaCsv, ExportarExcel

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('hora-extra-inutilizada/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='hora_extra_inutilizada'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('exportar-csv', ExportarParaCsv.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),

]
