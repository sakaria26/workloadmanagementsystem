from django.forms import ModelForm
from .models import *

class ResearchWorkloadForm(ModelForm):
    
    class Meta:
        model = Research_Load
        fields = '__all__'
