import logging
from django.contrib import messages
import sys
from django.shortcuts import render
from .forms import PasajeroFormulario, TarjetaFormulario
from .models import Pasajero, Tarjeta
from django.shortcuts import render,redirect,get_object_or_404


def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    messages.success(request,'Bienvenido')
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Pasajero GUARDADO correctamente')

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    data = {
        #'form' : PasajeroFormulario(instance=pasajeros)
        'pasajero': pasajeros
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Pasajero MODIFICADO correctamente')
            return redirect(to="pasajeros")

    return render(request,'pasajerosEdit.html',data)

def pasajerosView(request, id):
    pasajero = get_object_or_404(Pasajero, id = id)
    data = {
        'datos' : pasajero
    }
    return render(request,'pasajerosView.html',data)

def pasajerosEliminar(request, id):
    pasajero = get_object_or_404(Pasajero, id = id)
    #pasajero = Pasajero.objects.get(id = id)
    pasajero.delete()
    messages.warning(request,'Pasajero ELIMINADO correctamente')
    return redirect(to="pasajeros")

def tarjetas(request):
    messages.success(request,'Bienvenido')
    data = TarjetaFormulario()    
    tarjetas = Tarjeta.objects.all()
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Tarjeta GUARDADA correctamente')

    return render(request,"tarjetas.html",{"tarjetas":tarjetas, 'form':data})

def tarjetasEdit(request, id):
    tarjetas = get_object_or_404(Tarjeta, id = id)
    data = {
        'form' : TarjetaFormulario(instance=tarjetas)
    }
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, instance=tarjetas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Tarjeta MODIFICADA correctamente')
            return redirect(to="tarjetas")

    return render(request,'tarjetasEdit.html',data)

def tarjetasView(request, id):
    tarjeta = get_object_or_404(Tarjeta, id = id)
    data = {
        'datos' : tarjeta
    }
    return render(request,'tarjetasView.html',data)

def tarjetasEliminar(request, id):
    tarjeta = get_object_or_404(Tarjeta, id = id)
    tarjeta.delete()
    messages.warning(request,'Tarjeta ELIMINADA correctamente')
    return redirect(to="tarjetas")
