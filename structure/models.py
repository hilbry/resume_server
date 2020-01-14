#from django.contrib.localflavor.us.us_states import STATE_CHOICES
#from django.contrib.localflavor.us.models import USStateField
from django.db import models
#from django.db import datetime


class User(models.Model):
    username = models.TextFeild()

    def __unicode__(self):
        return self.username

class Resume(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='resumes',
        related_query_name="resume",
    )

    title = models.TextField()
    personal_info = models.ManyToManyField('Personal_Info')
    education_background = models.ManyToManyField('Education_Background',on_delete,)
    work_experience = models.ManyToManyField('Work_Experience',on_delete,)
    skill = models.ManyToManyField('Skill',on_delete,)
    your_project = models.ManyToManyField('Your_Project',on_delete,)
    award = models.ManyToManyField('User',on_delete,)
    date_created = models.ManyToManyField('User',on_delete,)

    def __unicode__(self):
        return self.title


# Create your models here.
class Personal_Info(models.Model):
    user_id = models.ForeignKey('Resume',on_delete=models.CASCADE,)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    e_add = models.CharField(max_length=50)
    home_add = models.IntegerField(max_length=30)
    cell = models.CharField(max_length=10)
    links = models.CharField(max_length = 10**10)


class Education_Background(models.Model):
    user_id = models.ForeingKey('Resume',on_delete=models.CASCADE,)
    gpa = models.FloatField(max_length=4)
    school_name = models.CharField(max_length=50)
    school_location = models.IntegerField(max_length=100)
    school_state = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    start_date = models.DateField(max_length=50)
    end_date = models.DateField(max_length=50)
    gradution_date = models.DateField(max_lenght=8)


class Work_Experience(models.Model):
    user_id = models.ForeingKey('Resume',on_delete=models.CASCADE,)
    employer = models.CharField(max_lenght=20)
    city = models.CharField(max_length=10)
    state = models.CharField(max_lenght=10)
    job_title = models.CharField(max_length=10)
    start_date = models.CharField(max_lenght=10)
    end_date = models.DateField(max_lenght=8)
    job_Responsabilities = models.CharField(max_length=10)

    def __unicode__(self):
        return self.employer

class Skill(models.Model):
    user_id = models.ForeingKey('Resume',on_delete=models.CASCADE,)
    school = models.CharField(max_lenght=10)
    city = models.CharField(max_lenght=10)
    state = models.CharField(max_lenght=10)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=10)
    graduation_date = models.DateField(max_length=10)

    def __unicode__(self):
        return self.

class Your_Project(models.Model):
    user_id = models.ForeingKey('Resume',on_delete=models.CASCADE,)
    N_proj = models.CharField(max_length=100**100)
    
class Award(models.Model):
    user_id = models.ForeingKey('Resume',on_delete=models.CASCADE,) 
    award_name = models.CharField(max_length=50)
    award_date = models.DateField(max_length=10)
    awarder = models.CharField(max_lenght=10)
    Summary = models.CharField(max_length=100)
