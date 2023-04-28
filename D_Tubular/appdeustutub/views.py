from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #           referenciar el título de la página
    context = {'title_page': 'Seleccione una opción:'}
    return render(request, 'index.html', context)