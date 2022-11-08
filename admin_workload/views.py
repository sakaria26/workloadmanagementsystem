from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def all_admin_workloads(request):
    admin_load = AdminWorkload.objects.all()
    context = {'admin_loads': admin_load}
    return render(request, 'admin_workload/admin_workload.html', context)

def add_admin_workload(request):
    form = AdminWorkloadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_load')

    context = {'form': form}
    return render(request, 'admin_workload/add_admin_workload.html', context)

def edit_admin_workload(request, pk):
    admin_load = AdminWorkload.objects.get(id=pk)
    form = AdminWorkloadEditForm(request.POST or None, instance=admin_load)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin_load')
  

    context = {'form': form}
    return render(request, 'admin_workload/edit_admin_workload.html', context)