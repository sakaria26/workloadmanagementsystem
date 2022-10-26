from django.db import models

# Create your models here.
class Course_Group(models.Model):
    course_group_id = models.AutoField(primary_key=True)
    course_group_name = models.CharField(max_length=255)
    course_group_number = models.IntegerField()
    course_group_size = models.IntegerField()
    def __str__(self):
        return self.name

class Novelty(models.Model):
    novelty_id = models.AutoField(primary_key=True)
    novelty_name = models.CharField(max_length=255)
    novelty_description = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Course_Teaching_Load(models.Model):
    course_teaching_load_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=255)
    course_group = models.ForeignKey(Course_Group, on_delete=models.CASCADE)
    novelty_of_course = models.CharField(max_length=255)
    contact_time_per_week = models.IntegerField()


    def __str__(self):
        return self.name

class Honors_Supervision_Load(models.Model):
    honors_supervision_load_id = models.AutoField(primary_key=True)
    honors_student_number = models.IntegerField()
    honors_student_firstname = models.CharField(max_length=255)
    honors_student_lastname = models.CharField(max_length=255)
    honors_student_program = models.CharField(max_length=255)
    contact_time_per_week = models.IntegerField()
    def __str__(self):
        return self.name

