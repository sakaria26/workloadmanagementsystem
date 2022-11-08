from django.forms import ModelForm
from .models import *

class CommunityWorkloadForm(ModelForm):
    class Meta:
        model= CommunityWorkload
        fields ='__all__'

class CommunityWorkloadEditForm(ModelForm):
    class Meta:
        model = CommunityWorkload
        fields = ['activity_name', 'semester', 'hours_per_semester']