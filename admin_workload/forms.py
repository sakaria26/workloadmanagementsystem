from django.forms import ModelForm
from .models import *

class AdminWorkloadForm(ModelForm):
    class Meta:
        model = AdminWorkload
        fields = '__all__'

class AdminWorkloadEditForm(ModelForm):
    class Meta:
        model = AdminWorkload
        fields = ['name', 'activity_type', 'hours_per_semester']