from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'title' : 'Home | By Elias'
    }
    return render(
        request,
        'home/index.html',
        contexto
    )