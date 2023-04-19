from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.forms import ProdutosForm
from app.models import Produtos
from django.core.paginator import Paginator


# Pagina Inicial.
def home(request):
    return render(request, 'home.html')


# Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')


# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    #Aqui há o teste de  integridade da senha
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senhas não conferem!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(25)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)


#Formulário do painel de login
def painel(request):
    return render(request, 'painel.html')


#Processamento do login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)


#Página inicial do dashboard
def dashboard(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produtos.objects.filter(categoria__icontains=search)
    else:
        #Essa linha abaixo serve para exibir o banco, caso seja interessante
        #data['db'] = Produtos.objects.all()
        all = Produtos.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'dashboard/home.html', data)


#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')


#Reseta a senha
def changePassword(request):
    user = User.objects.get(email = request.user.email)
    user.set_password('123456')
    user.save()
    logout(request)
    return redirect('/painel/')


#Formulário de cadastro de produtos
def form(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'dashboard/form.html', data)


def createp(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')


def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'dashboard/view.html', data)


def edit(request, pk):
    data = {}
    data ['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'dashboard/form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')


def delete(request,pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('/dashboard/')