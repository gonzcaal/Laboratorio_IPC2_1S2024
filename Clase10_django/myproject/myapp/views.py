from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def pagina1(request):
    return render(request, 'pagina1.html')