from django.forms import ModelForm
from .models import *

class ResearchWorkloadForm(ModelForm):
    
    class Meta:
        model = Research_Load
        fields = '__all__'

class ResearchWorkloadEditForm(ModelForm):
    
    class Meta:
        model = Research_Load
        fields = [ 'research_topic', 'research_status', 'expected_research_time']
