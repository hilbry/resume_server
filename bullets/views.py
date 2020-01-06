from django.shortcuts import render
from bullets.models import *
from bullets.serializers import *
from rest_framework import generics, serializers

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class  = GroupSerializer

class BulletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bullet.objects.all()
    serializer_class  = BulletSerializer

class BulletList(generics.ListCreateAPIView):
    queryset = Bullet.objects.all()
    serializer_class = BulletSerializer


# Create your views here.
