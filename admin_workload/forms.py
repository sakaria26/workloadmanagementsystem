from django import forms
from django.forms import ModelForm
from .models import *

class AdminWorkloadForm(ModelForm):
    class Meta:
        model = AdminWorkload
        fields = '__all__'
        widgets = {
            'staff_member': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_per_semester': forms.NumberInput(attrs={'class': 'form-control'}),
            'activity_type': forms.Select(attrs={'class': 'form-control'}),
        }

class AdminWorkloadEditForm(ModelForm):
    class Meta:
        model = AdminWorkload
        fields = ['name', 'activity_type', 'hours_per_semester']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_type': forms.Select(attrs={'class': 'form-control'}),
            'hours_per_semester': forms.NumberInput(attrs={'class': 'form-control'}),
        }