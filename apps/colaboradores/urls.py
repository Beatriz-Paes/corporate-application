from django.urls import path
from .views import ColaboradoresList

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),

]
