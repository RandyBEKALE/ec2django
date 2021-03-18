from django.shortcuts import render
from django.http import HttpResponse      #gere les requetes https
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('index2.html')
    #variable de Template
    #dans un dictionnaire

    data = {"name": "Randy BEKALE", "Age": 31, "materielinfo": ["mac", "pc", 'imprimant'],
            "skill": "Ingénieur Vision par Ordinateur - Consultant DevOps - Développeur Python",
            "adress":"146 Route de Versailles",
            "city":"91160 Champlan",}

    return HttpResponse(template.render(data))


def somme(request):

    return HttpResponse("la somme de 12 + 12 = {}".format(12+12))