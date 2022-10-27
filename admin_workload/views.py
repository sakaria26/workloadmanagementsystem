from django.shortcuts import render

# Create your views here.
def all_admin_workloads(request):
    return render(request, 'admin_workload/admin_workload.html', {})