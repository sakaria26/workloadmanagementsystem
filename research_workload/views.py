from django.shortcuts import render
# Create your views here.
def all_research_workloads(request):
    return render(request, 'research_workload/research_workload.html', {})
