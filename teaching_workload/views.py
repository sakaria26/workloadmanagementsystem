from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def all_teaching_workloads(request):


    # teaching_loads = Teaching_Load.objects.all().filter(staff_member__staff=request.user)
    # teaching_load_count = teaching_loads.count()
    # staff_member = Staff_Member.objects.get(staff=request.user)
    # context = {'teaching_workloads': teaching_loads, 'staff_member': staff_member, 'teaching_load_count': teaching_load_count}
    return render(request, 'teaching_workload/teaching_workload.html', {})

@login_required(login_url='login')
def add_teaching_workloads(request):
    form = TeachingWorkloadForm(request.POST or None)
    message = None
    if form.is_valid():
        message = messages.success(request, 'Teaching Workload Added Successfully')
        form.save()
        return redirect('teaching_load')

    context = {'form': form, 'message': message}
    return render(request, 'teaching_workload/teaching_workload_form.html', context)

@login_required(login_url='login')
def edit_teaching_workloads(request, teaching_load_id):
    teaching_load = Teaching_Load.objects.get(teaching_load_id=teaching_load_id)
    form = TeachingWorkloadEditForm(request.POST or None, instance=teaching_load)
    message = None
    if form.is_valid():
        message = messages.success(request, 'Teaching Workload Edited Successfully')
        form.save()
        return redirect('teaching_load')

    context = {'form': form, 'message': message}
    return render(request, 'teaching_workload/edit_teaching_workload.html', context)

# def remove_teaching_workloads(request):
#     teaching_load = Teaching_Load.objects.get(staff_member__staff=request.user)
#     if request.method == 'POST':
#         teaching_load.delete()
#         message = messages.success(request, 'Teaching Workload Deleted Successfully')
#         return redirect('teaching_load')

#     context = {'item': teaching_load, 'message': message}
#     return render(request, 'teaching_workload/teaching_workload.html', context)