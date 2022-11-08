from django import forms
from django.forms import ModelForm
from .models import *

class CommunityWorkloadForm(ModelForm):
    class Meta:
        model= CommunityWorkload
        fields ='__all__'

        widgets = {
            'staff_member': forms.Select(attrs={'class': 'form-control'}),
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'hours_per_semester': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class CommunityWorkloadEditForm(ModelForm):
    class Meta:
        model = CommunityWorkload
        fields = ['activity_name', 'semester', 'hours_per_semester']

        widgets = {
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'hours_per_semester': forms.NumberInput(attrs={'class': 'form-control'}),
        }