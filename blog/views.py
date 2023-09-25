from django.shortcuts import render
from django.http import HttpResponse
# View Minimalista.
#Uma view para o django pode ser uma classe ou um metodo
def home(resquest):
    return HttpResponse("<h1>Hello World!!</h1>")
