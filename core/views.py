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
    return render(request, 'ideias.html', context)

@login_required(login_url='/login/')
def minhas_ideas (request):
    user = request.user
    ideas = Idea.objects.filter(author=user)
    context = {'ideas': ideas, 'bodyId':"page-ideas"}
    return render(request, 'ideias.html', context)

@login_required(login_url='/login/')
def mostrar_idea (request, titulo_ideia):
    idea = Idea.objects.get(id=titulo_ideia)
    context = {'idea': idea, 'bodyId':"page-ideas"}
    return render(request, 'each_idea.html', context)

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