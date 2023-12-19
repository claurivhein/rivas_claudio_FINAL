from django import forms
from serialApp.models import Inscritos, Institucion

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre', 'codigo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un codigo'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una dirección'}),
        }

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = ['nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horaInscripcion', 'estado', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un teléfono'}),
            'fechaInscripcion': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Seleccione la fecha'}),
            'institucion': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione una institucion'}),
            'horaInscripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la hora'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el estado'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una observacion', 'rows':'3'}),
        }