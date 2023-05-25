from django import forms
from .models import *


class AddCargoForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))


class UpdateCargoForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nombre del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cargo
        fields = ['name']