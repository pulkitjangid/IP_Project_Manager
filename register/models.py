from django.db import models

# Create your models here.
class MUser(models.Model):
    Student_Name = models.CharField(max_length=70)
    Project_Name = models.CharField(max_length=70)
    Roll_No = models.CharField(max_length=10)
    Description = models.TextField()