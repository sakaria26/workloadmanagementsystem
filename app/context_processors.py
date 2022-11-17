from admin_workload.models import AdminWorkload
from appauth.models import Staff_Member
from community_workload.models import CommunityWorkload
from research_workload.models import Research_Load
from teaching_workload.models import Teaching_Load

def global_workload_summary(request):
    teaching_loads = Teaching_Load.objects.all().filter(staff_member__staff=request.user)
    research_loads = Research_Load.objects.all().filter(researcher__staff=request.user)
    admin_loads = AdminWorkload.objects.all().filter(staff_member__staff=request.user)
    community_loads = CommunityWorkload.objects.all().filter(staff_member__staff=request.user)

    teaching_load_count = teaching_loads.count()
    research_load_count = research_loads.count()
    admin_load_count = admin_loads.count()
    community_load_count = community_loads.count()

    total = teaching_load_count + research_load_count + admin_load_count + community_load_count
    teaching_load_variance = round(teaching_load_count / total * 100, -1)
    research_load_variance = round(research_load_count / total * 100, -1)
    admin_load_variance = round(admin_load_count / total * 100, -1)
    community_load_variance = round(community_load_count / total * 100, -1)

    staff_member = Staff_Member.objects.get(staff=request.user)
    return {
        'teaching_loads': teaching_loads, 
        'research_loads': research_loads, 
        'admin_loads': admin_loads, 
        'community_loads': community_loads, 
        'staff_member': staff_member,
        'teaching_load_variance': teaching_load_variance,
        'research_load_variance': research_load_variance,
        'admin_load_variance': admin_load_variance,
        'community_load_variance': community_load_variance,}
 