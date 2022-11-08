from django.db import models
from appauth.models import Staff_Member
from courses.models import Course, Course_Group
from students.models import Student
# Create your models here.


NOVELTIES = (
    ('New to Course', 'NEW TO COURSE'),
    ('New to University', 'NEW TO UNIVERSITY'),
    ('Old to Course', 'OLD TO COURSE'),
    ('Old to University', 'OLD TO UNIVERSITY'),
)

class Teaching_Load(models.Model):
    teaching_load_id = models.AutoField(primary_key=True)
    staff_member = models.ForeignKey(Staff_Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Course_Group, on_delete=models.CASCADE)
    novelty_of_course = models.CharField(max_length=255, choices=NOVELTIES, default='New to Course')
    contact_time_per_week = models.IntegerField()

    def __str__(self):
        return str(self.staff_member.staff.first_name + ' ' + self.staff_member.staff.last_name + ' ' + str(self.course))

class Honors_Supervision_Load(models.Model):
    honors_supervision_load_id = models.AutoField(primary_key=True)
    staff_member = models.ForeignKey(Staff_Member, on_delete=models.CASCADE, default=0)
    honors_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.honors_student

class Teaching_Load_Remove_Request(models.Model):
    remove_request_id = models.AutoField(primary_key=True)
    teaching_load = models.ForeignKey(Teaching_Load, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.teaching_load.staff_member.staff.first_name + ' ' + self.teaching_load.staff_member.staff.last_name + ' ' + str(self.teaching_load.course))

class Honors_Supervision_Load_Remove_Request(models.Model):
    remove_request_id = models.AutoField(primary_key=True)
    honors_supervision_load = models.ForeignKey(Honors_Supervision_Load, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.staff_member.staff.first_name + ' ' + self.staff_member.staff.last_name + ' ' + self.honors_supervision_load.honors_student)