from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='login')
def all_community_workloads(request):
    community_loads = CommunityWorkload.objects.all().filter(staff_member__staff=request.user)
    staff_member = Staff_Member.objects.get(staff=request.user)
    context = {'community_workloads': community_loads, 'staff_member': staff_member}
    return render(request, 'community_workload/community_workload.html', context)

@login_required(login_url='login')
def add_community_workload(request):
    form = CommunityWorkloadForm(request.POST or None)
   
    if form.is_valid():
        form.save()
        return redirect('community_load')
    context = {"form": form}
    return render(request, 'community_workload/add_community_load.html', context)

@login_required(login_url='login')
def edit_community_workload(request, id):
    community_workload = CommunityWorkload.objects.get(id=id)
    form = CommunityWorkloadEditForm(request.POST or None, instance=community_workload)
    if form.is_valid():
        form.save()
        return redirect('community_load')
    context = {"form": form}
    return render(request, 'community_workload/edit_community_load.html', context)