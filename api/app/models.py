from django.db import models

# Create your models here.
class Project_user(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    place=models.TextField()