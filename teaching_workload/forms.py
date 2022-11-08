from django.forms import ModelForm
from .models import *

class TeachingWorkloadForm(ModelForm):
    class Meta:
        model = Teaching_Load
        fields = '__all__'

class TeachingWorkloadEditForm(ModelForm):
    class Meta:
        model = Teaching_Load
        fields = [ 'course', 'group', 'contact_time_per_week', 'novelty_of_course']