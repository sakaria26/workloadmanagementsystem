from django.db import models
from courses.models import Programme
# Create your models here.
class Student(models.Model):
    student_number = models.IntegerField()
    student_firstname = models.CharField(max_length=255)
    student_lastname = models.CharField(max_length=255)
    student_program = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.student_number
