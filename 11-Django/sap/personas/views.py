from django.forms import modelform_factory
from django.shortcuts import redirect, render, get_object_or_404
from personas.models import persona, Domicilio
from personas.forms import PersonaForm, DomicilioForm

# Create your views here.
def detallePersona(request,id):
    # persona1 = persona.objects.get(pk=id)
    persona1 = get_object_or_404(persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona1': persona1})

# PersonaForm = modelform_factory(persona,exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')

    else:
        formaPersona = PersonaForm()
    
    return render(request, 'personas/nuevo.html',{'formaPersona': formaPersona}) 

def editarPersona(request,id):
    persona1 = get_object_or_404(persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona1)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')

    else:
        persona1 = get_object_or_404(persona, pk=id)
        formaPersona = PersonaForm(instance=persona1)
    
    return render(request, 'personas/editar.html',{'formaPersona': formaPersona}) 

def eliminarPersona(request,id):
    persona1 = get_object_or_404(persona, pk=id)
    if persona1:
        persona1.delete()
    return redirect('inicio')

#direcciones
def detalleDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    return render(request,'personas/detalleD.html', {'domicilio': domicilio})

def editarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect ('inicioD')
    else:
        domicilio = get_object_or_404(Domicilio, pk=id)
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'personas/editarD.html',{'formaDomicilio':formaDomicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('inicioD')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'personas/nuevoD.html',{'formaDomicilio':formaDomicilio})

def eliminarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('inicioD')