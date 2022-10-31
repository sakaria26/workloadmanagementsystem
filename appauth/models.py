from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


Staff_Positions = [ 'Junior Lecturer','Lecturer', 'Senior Lecturer', 'Professor', 'Associate Professor', 'HoD', 'Dean']
class User(AbstractUser):
    staff_position = models.CharField(max_length=100, choices=[(tag, tag) for tag in Staff_Positions], default='Lecturer')