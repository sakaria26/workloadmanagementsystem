from django.shortcuts import render
from .forms import *
# Create your views here.
def all_research_workloads(request):
    return render(request, 'research_workload/research_workload.html', {})

def add_research_workloads(request):
    form = ResearchWorkloadForm()
    context = {"form": form}
    return render(request, 'research_workload/add_research_workload.html', context)
