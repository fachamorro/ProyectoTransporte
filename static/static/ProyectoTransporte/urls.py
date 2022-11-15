"""ProyectoTransporte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from SITU.views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    #path('SITU/', include('SITU.urls')),
    path('pasajeros/', pasajeros, name='pasajeros'),
    path('pasajerosEdit/<id>', pasajerosEdit, name='pasajerosEdit'),
    path('pasajerosView/<id>', pasajerosView, name='pasajerosView'),
    path('pasajerosEliminar/<id>', pasajerosEliminar, name='pasajerosEliminar'),
    #tarjetas
    path('tarjetas/', tarjetas, name='tarjetas'),
    path('tarjetasEdit/<id>', tarjetasEdit, name='tarjetasEdit'),
    path('tarjetasView/<id>', tarjetasView, name='tarjetasView'),
    path('tarjetasEliminar/<id>', tarjetasEliminar, name='tarjetasEliminar'),
]
