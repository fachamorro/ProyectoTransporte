from django import forms
from .models import Pasajero, Tarjeta

class PasajeroFormulario(forms.ModelForm):
    cedula = forms.CharField(label='Cedula', widget=forms.TextInput(attrs={'class':'form-control','minlength':"10", 'maxlength':"10", 'placeholder': 'Ingrese la Cedula','required':'true'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control', 'minlength':"3", 'maxlength':"10",'placeholder': 'Ingrese el Nombre','required':'true'}))
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class':'form-control','minlength':"3", 'maxlength':"10",'placeholder': 'Ingrese el Apellido','required':'true'}))
    telefono = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'class':'form-control','minlength':"9", 'maxlength':"10",'placeholder': 'Ingrese el Telefono','required':'true'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control', 'minlength':"6", 'maxlength':"30",'placeholder': 'Ingrese el  Email','required':'true'}))
    imagen = forms.ImageField(label='Imagen')
    class Meta:
        model = Pasajero
        fields=["cedula","nombre","apellido", "telefono", "email","imagen"] 

class TarjetaFormulario(forms.ModelForm):
    codigo = forms.CharField(label='Codigo', widget=forms.TextInput(attrs={'class':'form-control','minlength':"1", 'maxlength':"10", 'placeholder': 'Ingrese el Codigo','required':'true'}))
    monto = forms.DecimalField(label='Monto', widget=forms.TextInput(attrs={'class':'form-control', 'minlength':"0.0", 'maxlength':"1000.00",'placeholder': 'Ingrese el Monto','required':'true'}))
    #idPasajero = forms.ChoiceField(label='Pasajero')
    class Meta:
        model = Tarjeta
        fields=["codigo","monto","idPasajero"]
