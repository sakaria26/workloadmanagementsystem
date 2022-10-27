from django.shortcuts import render

# Create your views here.
def all_teaching_workloads(request):
    return render(request, 'teaching_workload/teaching_workload.html')