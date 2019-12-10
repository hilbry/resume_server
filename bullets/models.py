from django.contrib.localflavor.us.models import USStateField
from django.db import models

# Create your models here.
class personal_Info(model.model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    e_add = models.CharField(max_length=50)
    Home_add = models.CharField(max_length=30)
    cell = models.CharField(max_length=10)
    links = models.CharField(max_length=500)

    def __unicode__(self):
        return self.f_name

class Education_Background(model.models):
    gpa = 
    school_name =
    school_location =
    school_state =
    degree = 
    major = 
    start_date = 
    end_date = 
    gradution_date = 


class Work_Experience(model.models):
    employer = 
    city = 
    state = 
    job_title = 
    start_date = 
    end_date = 
    job_Responsabilities = 

class skills(model.models):
    school = 
    city = 
    state = 
    degree = 
    major = 
    graduation_date = 

class your_Project(model.models):
    


class Award(model.models):
    award_name = 
    award_date = 
    awarder = 
    Summary =
    
