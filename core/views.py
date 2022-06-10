from email.errors import MessageParseError
from multiprocessing import context
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.models import Idea
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home (request):
    ideas = Idea.objects.order_by('-created_on')[:3]
    return render(request, 'home.html', {'ideas':ideas})

def login_user(request):
    return render(request, 'login.html')

def submit_login(request): 
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return redirect('/login')
    else:
        return redirect('/login')
    
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def ideas (request):
    user = request.user
    ideas = Idea.objects.all()
    context = {'ideas': ideas, 'bodyId':"page-ideas", 'author':user.username}
    return render(request, 'show_ideas.html', context)

@login_required(login_url='/login/')
def minhas_ideas (request):
    user = request.user
    ideas = Idea.objects.filter(author=user)
    context = {'ideas': ideas, 'bodyId':"page-ideas"}
    return render(request, 'show_ideas.html', context)

@login_required(login_url='/login/')
def mostrar_idea (request, titulo_ideia):
    idea = Idea.objects.get(id=titulo_ideia)
    context = {'idea': idea, 'bodyId':"page-ideas"}
    return render(request, 'show_one_idea.html', context)

@login_required(login_url='/login/')
def adicionar_ideia(request):
    if request.POST:
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.POST.get('image')
        description = request.POST.get('description')
        link = request.POST.get('link')
        author = request.user
        idea = Idea.objects.create(title=title, category=category, image=image, description=description, url=link, author=author)

    return redirect('/')

@login_required(login_url='/login/')
def delete_idea(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    user = request.user
    if user == idea.author:
        idea.delete()
    else:
        return HttpResponse('<h1>Você não é o author dessa ideia.</h1>')

    return redirect('/')

def editar_ideia(request):
    id_idea = request.GET.get('id')

    print(id_idea)
    dados = {}
    if id_idea:
        dados['idea'] = Idea.objects.filter(id=id_idea)
    return render (request, 'add_idea.html', dados)