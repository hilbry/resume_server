from rest_framework import serializers
from bulets.models import *

class personal_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = personal_Info
        field = ['f_name','l_name','e_add','all','link']
class Education_BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_Background
        field = ['gpa','school_name','school_location','school_state','degree','major','start_date','end_date','graduation_date']
class Work_Experienceerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        field = ['employer','city','state','job_title','start_date','end_date','job_resposability']
class skillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        field = ['school','city','state','degree','major','graduation_date']
class your_projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = your_project
        field = ['n_proj']
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        field = ['award_name','award_date','awarder','summary']