from django.db import models

class Group(models.Model):
    title = models.TextField()
    
    def __str__(self):
        return (self.title)
   
    
class Bullet(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()

    def __str__(self):
        return (self.text)
# Create your models here.