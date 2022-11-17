from django.shortcuts import render
from teaching_workload.models import Teaching_Load
from research_workload.models import Research_Load
from admin_workload.models import AdminWorkload
from community_workload.models import CommunityWorkload
import plotly.graph_objects as go
# Create your views here.
def workload_summary(request):
    teaching_load = Teaching_Load.objects.all().filter(staff_member__staff=request.user).count()
    research_load = Research_Load.objects.all().filter(researcher__staff=request.user).count()
    admin_load = AdminWorkload.objects.all().filter(staff_member__staff=request.user).count()
    community_load = CommunityWorkload.objects.all().filter(staff_member__staff=request.user).count()

    colors = ['#253769', '#13285E', '#1E397D', '#1D3D8E']
    names=['Teaching Load', 'Research Load', 'Admin Load', 'Community Load']
    values=[teaching_load, research_load, admin_load, community_load]
    fig = go.Figure(data=[go.Pie(labels=names, values=values, hole=.4)])
    fig.update_traces(textposition='inside', textinfo='percent+label', hoverinfo='label+percent', textfont_size=12, marker=dict(colors=colors, line=dict(color='#f8f9f9', width=1)))
    chart = fig.to_html(full_html=False, default_height=500, default_width=600)

    context = {'chart': chart}
    return render(request, 'dashboard/dashboard.html', context)