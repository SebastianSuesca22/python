from django.shortcuts import render
from django.http import HttpResponse
from personas.models import persona, Domicilio

# Create your views here.
def index(request):
    no_personas = persona.objects.count()
    #personas = persona.objects.all()
    personas = persona.objects.order_by('id','nombre')
    return render(request, 'webapp/bienvenido.html',{'no_personas' :no_personas,'personas': personas})

def direccion(request):
    no_direccion = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    # direccion = Domicilio.objects.order_by('id')
    return render(request, 'webapp/domicilio.html',{'no_direccion':no_direccion, 'domicilios': domicilios})