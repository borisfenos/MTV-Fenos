from urllib import request
from multiprocessing import context
from django.shortcuts import render
from modelos.models import Familiares

# Create your views here.

def familiares(request):
    familiares = Familiares.objects.all()
    context={'familiares':familiares}
    return render(request, 'template.html', context=context)