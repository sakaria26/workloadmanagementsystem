import uuid
from django.db import models
from appauth.models import Staff_Member

# Create your models here.
class AdminWorkload(models.Model):    
    ActivityTypes = models.TextChoices('ActivityTypes', 'Compulsory Major Minor Voluntary')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    staff_member = models.ForeignKey(Staff_Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    activity_type = models.CharField(choices=ActivityTypes.choices, max_length=12)
    hours_per_semester = models.IntegerField()

    def __str__(self):
        return self.name
