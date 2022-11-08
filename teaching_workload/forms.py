from django import forms
from django.forms import ModelForm
from .models import *

class TeachingWorkloadForm(ModelForm):
    class Meta:
        model = Teaching_Load
        fields = '__all__'
        widgets = {
            'staff_member': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'novelty_of_course': forms.Select(attrs={'class': 'form-control'}),
            'contact_time_per_week': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class TeachingWorkloadEditForm(ModelForm):
    class Meta:
        model = Teaching_Load
        fields = [ 'course', 'group', 'contact_time_per_week', 'novelty_of_course']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'contact_time_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'novelty_of_course': forms.Select(attrs={'class': 'form-control'}),
        }
