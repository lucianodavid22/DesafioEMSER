from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def registro(request):
    users = Usuario.objects.all()
    return render(request, 'registro.html', {'users': users})

def success(request):    
    name = request.GET['name']
    lastname = request.GET['lastname']
    email = request.GET['email']
    Usuario.objects.create(nombre=name, apellido=lastname, email=email)
    return render(request, 'success.html', {'name': name, 'lastname': lastname, 'email': email})