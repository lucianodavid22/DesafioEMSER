from django.shortcuts import render
from django.http import HttpResponse

def registro(request):
    return HttpResponse('Respuesta exitosa de registro aca va el form')