from django.shortcuts import render

# Create your views here.
def all_community_workloads(request):
    return render(request, 'community_workload/community_workload.html', {})
