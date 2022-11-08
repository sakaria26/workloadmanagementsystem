from django.shortcuts import render, redirect
from .forms import CommunityWorkloadForm
from .models import *

# Create your views here.
def all_community_workloads(request):
    community_loads = CommunityWorkload.objects.all().filter(staff_member__staff=request.user)
    staff_member = Staff_Member.objects.get(staff=request.user)
    context = {'community_workloads': community_loads, 'staff_member': staff_member}
    return render(request, 'community_workload/community_workload.html', context)

def add_community_workload(request):
    form = CommunityWorkloadForm(request.POST or None)
   
    if form.is_valid():
        form.save()
        return redirect('community_load')
    context = {"form": form}
    return render(request, 'community_workload/add_community_load.html', context)