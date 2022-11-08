from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_teaching_workloads(request):

    teaching_loads = Teaching_Load.objects.all().filter(staff_member__staff=request.user)
    staff_member = Staff_Member.objects.get(staff=request.user)
    print(staff_member.staff_position)
    context = {'teaching_workloads': teaching_loads, 'staff_member': staff_member}
    return render(request, 'teaching_workload/teaching_workload.html', context)

login_required('login')
def add_teaching_workloads(request):
    form = TeachingWorkloadForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('teaching_load')

    context = {'form': form}
    return render(request, 'teaching_workload/teaching_workload_form.html', context)