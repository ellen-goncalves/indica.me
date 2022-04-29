from django.http import HttpResponse
from django.shortcuts import render
from templates import *
from core import models

# Create your views here.

def hello (request, nome, idade):
    return HttpResponse('Hello {} de {} anos'.format(nome, idade))

def soma (request, numero1, numero2):
    soma = numero1 + numero2
    return HttpResponse('A soma é {}'.format(soma))

def ideas (request):
    return render('index.html')

def mostrar_idea (request, titulo_ideia):
    return HttpResponse(idea.objects.get(title=titulo_ideia))
