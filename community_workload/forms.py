from django.forms import ModelForm
from .models import *

class CommunityWorkloadForm(ModelForm):
    class Meta:
        model= CommunityWorkload
        fields ='__all__'