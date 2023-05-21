from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

#Formulário de usuario
def create(request):

    return render(request, 'create.html')

#loja de pontos
def loja(request):
  
    return render(request, 'create.html')

def login(request):

    return render(request, 'login.html')