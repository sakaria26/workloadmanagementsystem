from django.shortcuts import render
from .forms import *

# Create your views here.
def all_teaching_workloads(request):
    return render(request, 'teaching_workload/teaching_workload.html')

def add_teaching_workloads(request):
    form = TeachingWorkloadForm()
    context = {'form': form}
    return render(request, 'teaching_workload/teaching_workload_form.html', context)