#from django.forms import widgets
from rest_framework import serializers
from structure.models import *


class UserSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url',
     read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        field = ('username')

class ResumeSerializer(serializers.ModelSerializer):
    resume = serializers.RelatedField(many=True)
    class Meta:
        model = Resume
        field = ('title','personal_info','education_background',
        'work_experience','skills','your_project','award')
        depth = 1

class Personal_InfoSerializer(serializers.ModelSerializer):
    personal_info = serializers.RelatedField(many=True)
    class Meta:
        model = Personal_Info
        field = ('f_name','l_name','e_add','all','link')
        
class Education_BackgroundSerializer(serializers.ModelSerializer):
    education_background = serializers.RelatedField(many=True)
    class Meta:
        model = Education_Background
        field = ('gpa','school_name','school_location',
        'school_state','degree','major','start_date','end_date',
        'graduation_date')

class Work_ExperienceSerializer(serializers.ModelSerializer):
    work_experience = serializers.RelatedField(many=True)
    class Meta:
        model = Work_Experience
        field = ('employer','city','state','job_title',
        'start_date','end_date','job_resposability')

class skillSerializer(serializers.ModelSerializer):
    skill = serializers.RelatedField(many=True)
    class Meta:
        model = Skill
        field = ('school','city','state','degree','major',
        'graduation_date')

class your_projectSerializer(serializers.ModelSerializer):
    your_project = serializers.RelatedField(many=True)
    class Meta:
        model = Your_Project
        field = ('n_proj')

class AwardSerializer(serializers.ModelSerializer):
    award = serializers.RelatedField(many=True)
    class Meta:
        model = Award
        field = ('award_name','award_date','awarder','summary')
