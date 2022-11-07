from django.db import models

from appauth.models import Staff_Member

# Create your models here.
Load_Status = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Completed', 'Completed'),
)

class Co_Researcher(models.Model):
    co_researcher_id = models.AutoField(primary_key=True)
    co_researcher_title = models.CharField(max_length=10)
    co_researcher_firstname = models.CharField(max_length=255)
    co_researcher_lastname = models.CharField(max_length=255)
    co_researcher_email = models.CharField(max_length=255)
    co_researcher_phone = models.CharField(max_length=255)
    def __str__(self):
        return str(self.co_researcher_firstname + " " +self.co_researcher_lastname)

class Funding(models.Model):
    funding_id = models.AutoField(primary_key=True)
    funding_name = models.CharField(max_length=255)
    def __str__(self):
        return self.funding_name

class Research_Load(models.Model):
    research_load_id = models.AutoField(primary_key=True)
    researcher = models.ForeignKey(Staff_Member, on_delete=models.CASCADE, default='')
    research_topic = models.CharField(max_length=255)
    research_status = models.CharField(max_length=255, choices=Load_Status, default='Pending')
    co_researcher = models.ForeignKey(Co_Researcher, on_delete=models.SET_NULL, null=True)
    researching_funding = models.ForeignKey(Funding, on_delete=models.SET_NULL, null=True)
    research_load_description = models.CharField(max_length=255)
    expected_research_time = models.IntegerField()
    def __str__(self):
        return self.research_topic




