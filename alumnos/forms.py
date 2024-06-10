from django import forms
from .models import Ramo, Seccion

from django.forms import ModelForm

class RamoForm(ModelForm):
    class Meta:
        model = Ramo
        fields = "__all__"

class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = "__all__"