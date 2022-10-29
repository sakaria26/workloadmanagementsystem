import uuid
from django.db import models

# Create your models here.
class CommunityWorkload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    activity_name = models.CharField(max_length=50)
    # evidence = models.FileField()
    # user = models.ManyToManyField()
    hours_per_semester = models.IntegerField()


    def __str__(self):
        return self.activity_name

