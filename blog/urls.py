from django.urls import path
from . import views

urlpatterns = [ # ESTE NOME TEM QUE SER IGUAL AO DO "CORE"/URLS
    path('', views.home, name="home"), # INFORMAR QUAL A CLASSE QUE VAI TRATAR A REQUISIÇÃO Criado a rota para Home
]
# apos isso registrar dentro do arquivo de urls global "core/urls.py"
