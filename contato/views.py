from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO

#importando a classe Pessoa
from .models import Pessoa

# Create your views here.
def contato(request):
    contexto = {
        'title' : 'Contato | By Elias',
    }
    return render (
        request,
        'contato/contato.html',
        contexto
    )

def gravar(request):
    nome_error  = ""
    idade_error = ""
    email_error = ""
    #img_error   = ""
    if request.method == 'POST':
        nome   = request.POST.get('nome')
        idade  = request.POST.get('idade')
        email  = request.POST.get('email')
       # img = request.FILES.get('img')
        if not nome: nome_error = 'O campo nome é obrigatório. '
        elif Pessoa.objects.filter(nome=nome): nome_error = 'Nome duplicado.'
        
        if not idade: idade_error = 'O campo idade é obrigatório. '
        else:
            try:
                idade = int(idade)
                if idade <= 0: idade_error = 'A idade deve ser um valor positivo. '
            except ValueError: 
                idade_error = 'A idade deve ser um valor numérico. '

        if not email: email_error = 'O campo email é obrigatório. '
        elif Pessoa.objects.filter(email=email): email_error = 'Email duplicado.'

        
        if nome_error or idade_error or email_error or img_error:
            contexto = {
                'nome_error' : nome_error,
                'idade_error': idade_error,
                'email_error': email_error,
                'error' : nome_error+' '+email_error+' '+idade_error+' '+img_error,
                'nome': nome,
                'idade': idade,
                'email': email
            }
            return render(
                request,
                'contato/contato.html',
                contexto,
            )
        
        # Salvar os dados da tela para o banco
        nova_pessoa = Pessoa()
        nova_pessoa.nome  = nome
        nova_pessoa.idade = idade
        nova_pessoa.email = email
        #nova_pessoa.img = SimpleUploadedFile(img.name, img.read()) if img else None
        nova_pessoa.save()

    return contato(request)

def exibe(request):
    
    # Exibir todos as pessoas
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    # Retornar os dados para a página 
    return render(
        request,
        'contato/mostrar.html',
        exibe_pessoas,
    )

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
        request,
        'contato/editar.html',
        {"pessoa": pessoa}
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome  = request.POST.get('nome')
    pessoa.idade = request.POST.get('idade')
    pessoa.email = request.POST.get('email')
    pessoa.save()
    
    return exibe(request)

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    
    return exibe(request)


def localizar_id(request): 
    if request.method == 'POST':
        try : 
            id = request.POST.get('id')
            pessoa = Pessoa.objects.get(id_pessoa=id)
            contexto = {"pessoa": pessoa}
        except: 
            contexto = {"erro": 'Registro não encontrado'}
    else: # se for a primeira vez de carregamento do localizar.html
        contexto = {}

    return render(
        request,
        'contato/localizar.html',
        contexto,
    )


def localizar2(request): 
    try :
        busca = request.POST.get('busca')
        if not busca: # quando chamado a 1a vez ou não digitar valor
            return render(
            request,
            'contato/localizar.html', #não passa contexto
            )
        tbusca = request.POST.get('tbusca')
        
        if tbusca == '1':
            pessoa = Pessoa.objects.get(id_pessoa=busca)
        elif tbusca == '2':
            pessoa=Pessoa.objects.filter(nome=busca)
        else:
            pessoa=Pessoa.objects.filter(email=busca)

        contexto = {"pessoa": pessoa}
    except:
        contexto = {"erro": 'erro'}

    return render(
        request,
        'contato/localizar.html',
        contexto,
    )

def localizar_old(request): 
    if request.method == 'POST':
        try :
            id = request.POST.get('id')
            if not id: # quando chamado a 1a vez ou não digitar valor
                return render(
                request,
                'contato/localizar.html', #não passa contexto
                )
            pessoa = Pessoa.objects.get(id_pessoa=id)
            contexto = {"pessoa": pessoa}
        except:
            contexto = {"erro": 'Registro não encontrado'}

    return render(
        request,
        'contato/localizar.html',
        contexto,
    )


# método get para campo sem repetição
# método filter quando há repetição

def localizar(request): 
    contexto = {}
    erro = None  # Inicialize a variável de erro como None

    if request.method == 'POST':
        selecao = request.POST.get('tbusca')
        busca = request.POST.get('busca')
        pessoas = []  # Inicialize uma lista vazia para armazenar os resultados
        try : 
            if selecao == 'id':
                try:
                    pessoa = Pessoa.objects.get(id_pessoa=busca)
                    pessoas.append(pessoa)
                except ValueError:
                    erro = 'Informe para id um valor numérico'
                    
            elif selecao == 'nome':
               pessoas = Pessoa.objects.filter(nome=busca)
            elif selecao == 'email':
               pessoas = Pessoa.objects.filter(email=busca) 
            
            if not pessoas:  # Verifique se a lista de pessoas está vazia
                raise Pessoa.DoesNotExist  # Lança uma exceção personalizada

        # a exceção não estava funcionando antes porque DoesNotExist não funciona para filter
        # quando usado o filter, precisamos lançar uma exceção personalizada
        except Pessoa.DoesNotExist: 
            if not erro:
                erro = 'Registro não encontrado'

    else: # se for a primeira vez de carregamento do localizar.html
        pessoas = []
        busca = ''

    contexto = {"pessoas": pessoas, "busca": busca, "erro": erro}
    return render(
        request,
        'contato/localizar.html',
        contexto,
    )


def image_view(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES)
        if forms.is_valid():
            return redirect('success')
        else:
            form = PessoaForm()
        return render(request, 'contatomodel.html',{'form':form})

def success(request):
    return HttpResponse('successfully uploaded')