import uuid
from django.db import models
from appauth.models import Staff_Member
# Create your models here.
class CommunityWorkload(models.Model):
    SemesterType = (
        ('1st', 'First Semester'),
        ('2nd', 'Second Semester')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    activity_name = models.CharField(max_length=50)
    # evidence = models.FileField()
    staff_member = models.ForeignKey(Staff_Member, on_delete=models.CASCADE, default=1)
    semester = models.CharField(choices=SemesterType, max_length=20)
    hours_per_semester = models.IntegerField()


    def __str__(self):
        return self.activity_name

