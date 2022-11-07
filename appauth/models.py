from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

STAFF_POSITIONS = (
    ('Junior Lectuer', 'JUNIOR LECTURER'),
    ('Lecturer', 'LECTURER'),
    ('Senior Lecturer', 'SENIOR LECTURER'),
    ('Professor', 'PROFESSOR'),
    ('Associate Professor', 'ASSOCIATE PROFESSOR'),
    ('Dean', 'DEAN'),
    ('HoD', 'HEAD OF DEPARTMENT'),
)

# Create your models here.
class Staff_Member(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_number = models.IntegerField(_('staff number'), unique=True)
    staff_position = models.CharField(max_length=25, choices=STAFF_POSITIONS, default='Lecturer')



