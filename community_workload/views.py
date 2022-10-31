from django.shortcuts import render
from .forms import CommunityWorkloadForm

# Create your views here.
def all_community_workloads(request):
    return render(request, 'community_workload/community_workload.html', {})

def add_community_workload(request):
    form = CommunityWorkloadForm()
    context = {"form": form}
    return render(request, 'community_workload/add_community_load.html', context)