from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.contrib.localflavor.us.models import USStateField
from django.db import Models
from djang.db import datetime

# Create your models here.
class personal_Info(Models.Model):
    f_name = Models.CharField(max_length=30)
    l_name = Models.CharField(max_length=30)
    e_add = Models.CharField(max_length=50)
    home_add = Models.IntegerField(max_length=30)
    cell = Models.CharField(max_length=10)
    links = Models.CharField(max_length = 10**10)

    def __unicode__(self):
        return self.f_name

class Education_Background(Models.Model):
    gpa = Models.FloatField(max_length=4)
    school_name = Models.CharField(max_length=50)
    school_location = Models.IntegerField(max_length=100)
    school_state = Models.CharField(max_length=50)
    degree = Models.CharField(max_length=50)
    major = Models.CharField(max_length=50)
    start_date = Models.DateField(max_length=50)
    end_date = Models.DateField(max_length=50)
    gradution_date = Models.DateField(max_lenght=8)


class Work_Experience(Models.Model):
    employer = Models.CharField(max_lenght=20)
    city = Models.CharField(max_length=10)
    state = Models.CharField(max_lenght=10)
    job_title = Models.CharField(max_length=10)
    start_date = Models.CharField(max_lenght=10)
    end_date = Models.DateField(max_lenght=8)
    job_Responsabilities = Models.CharField(max_length=10)

class skills(Models.Model):
    school = Models.CharField(max_lenght=10)
    city = Models.CharField(max_lenght=10)
    state = Models.CharField(max_lenght=10)
    degree = Models.CharField(max_length=10)
    major = Models.CharField(max_length=10)
    graduation_date = Models.DateField(max_length=10)

class your_Project(Models.Model):
    N_proj = Models.CharField(max_length=100**100)
    
class Award(Models.Model):
    award_name = Models.CharField(max_length=50)
    award_date = Models.DateField(max_length=10)
    awarder = Models.CharField(max_lenght=10)
    Summary = Models.CharField(max_length=100)