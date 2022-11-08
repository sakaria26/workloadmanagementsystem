from django import forms
from django.forms import ModelForm
from .models import *

class ResearchWorkloadForm(ModelForm):
    
    class Meta:
        model = Research_Load
        fields = '__all__'
        
        widgets = {
            'researcher': forms.Select(attrs={'class': 'form-control'}),
            'research_topic': forms.TextInput(attrs={'class': 'form-control'}),
            'research_status': forms.Select(attrs={'class': 'form-control'}),
            'co_researcher': forms.Select(attrs={'class': 'form-control'}),
            'researching_funding': forms.Select(attrs={'class': 'form-control'}),
            'research_load_description': forms.TextInput(attrs={'class': 'form-control'}),
            'expected_research_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResearchWorkloadEditForm(ModelForm):
    
    class Meta:
        model = Research_Load
        fields = [ 'research_topic', 'research_status', 'expected_research_time']

        widgets = {
            'research_topic': forms.TextInput(attrs={'class': 'form-control'}),
            'research_status': forms.Select(attrs={'class': 'form-control'}),
            'expected_research_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }
