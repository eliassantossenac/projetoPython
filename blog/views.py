from django.shortcuts import render

# Create your views here.
def blog(request):
    print('Passei pelo blog')
    contexto = {
        'title' : 'Blog | By Elias'
    }
    return render(
        request,
        'blog/index.html',
        contexto
        )

def artigos(request):
    print('Passei pelo artigos')
    contexto = {
        'title' : 'Artigos | By Elias'
    }
    return render(
        request,
        'blog/artigo.html',
        contexto
        )


''' 
Removido:
from django.http import HttpResponse

return HttpResponse('<body bgcolor="blue">Artigos</body>')

def doc(request):
    print('Passei pelo doc')
    contexto = {
        'title' : 'Documentos | By Elias'
    }

'''