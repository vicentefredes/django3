from django import forms
from .models import Ramo, Seccion

from django.forms import ModelForm

class RamoForm(ModelForm):
    class Meta:
        model = Ramo
        fields = ['ramo', 'creditos', 'escuela']
        labels = {'ramo': 'Ramo',
                  'creditos': 'Créditos',
                  'escuela': 'Escuela'}
        widgets = {
            'ramo': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'escuela': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ['codigo_seccion', 'id_ramo']
        labels = {'codigo_seccion': "Código de Sección", 
                  'id_ramo': "Ramo"}
        widgets = {
            'codigo_seccion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ramo': forms.Select(attrs={'class': 'form-control'}),
        }