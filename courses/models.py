from django.db import models


Mode_Options = (
    ('Full Time', 'FULL TIME'),
    ('Part Time', 'PART TIME'),
    ('Distance', 'DISTANCE'),
)

Session_Options = (
    ('Theory', 'THEORY'),
    ('Practical', 'PRACTICAL'),
)
# Create your models here.
class Course (models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=255)
    def __str__(self):
        return self.course_name

class Programme (models.Model):
    programme_code = models.CharField(max_length=10, primary_key=True)
    programme_name = models.CharField(max_length=255)
    programme_level = models.IntegerField()
    def __str__(self):
        return self.programme_name

class Course_Group(models.Model):
    course_group_id = models.AutoField(primary_key=True)
    course_group_mode = models.CharField(max_length=255, choices=Mode_Options, default='Full Time')
    course_group_session = models.CharField(max_length=255, choices=Session_Options, default='Theory')
    course_group_number = models.IntegerField(null=True)
    course_group_size = models.IntegerField()
    def __str__(self):
        return str(self.course_group_mode + ' '+ self.course_group_session+ ' '+ str(self.course_group_number))