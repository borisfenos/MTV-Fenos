from urllib import request
from multiprocessing import context
from django.shortcuts import render
from modelos.models import Familiares

# Create your views here.

def familiares(request):
    nuevo_familiar = Familiares.objects.create(
        name = 'Lucas Rodriguez',
        dni = 80706050,
        birth_date = '2000-05-24'
        )
    context={'nuevo_familiar':nuevo_familiar}
    return render(request, 'template.html', context=context)