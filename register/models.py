from django.db import models
from datetime import datetime

# Create your models here.
class MUser(models.Model):
    Student_Name = models.CharField(max_length=70)
    Project_Name = models.CharField(max_length=70)
    Roll_No = models.CharField(max_length=10)
    Description = models.TextField()
    Upload = models.FileField(null=True)

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)