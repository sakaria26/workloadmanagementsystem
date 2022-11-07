from django.forms import ModelForm
from .models import *

class TeachingWorkloadForm(ModelForm):
    class Meta:
        model = Teaching_Load
        fields = '__all__'