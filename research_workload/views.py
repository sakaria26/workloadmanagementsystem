from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
# Create your views here.
def all_research_workloads(request):
    research_loads = Research_Load.objects.all().filter(researcher__staff=request.user)
    staff_member = Staff_Member.objects.get(staff=request.user)
    context = {'research_loads': research_loads, 'staff_member': staff_member}
    return render(request, 'research_workload/research_workload.html', context)

def add_research_workloads(request):
    form = ResearchWorkloadForm(request.POST or None)
    message = None
    if form.is_valid():
        message = messages.success(request, 'Research Workload Added Successfully')
        form.save()
        return redirect('research_load')

    context = {"form": form}
    return render(request, 'research_workload/add_research_workload.html', context)

def edit_research_workloads(request, research_load_id):
    research_load = Research_Load.objects.get(research_load_id=research_load_id)
    form = ResearchWorkloadEditForm(request.POST or None, instance=research_load)
    message = None
    if request.method == 'POST':
        if form.is_valid():
            message = messages.success(request, 'Research Workload Edited Successfully')
            form.save()
            return redirect('research_load')
   

    context = {"form": form, "research_load": research_load, "message": message}
    return render(request, 'research_workload/edit_research_workload.html', context)
