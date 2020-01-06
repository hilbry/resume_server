from rest_framework import serializers
from bullets.models import *

class GroupSerializer(serializers.ModelSerializer):
    bullets = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = ('__all__')

class BulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bullet
        fields = ('__all__')
