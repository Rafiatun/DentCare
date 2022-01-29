from django.db import models

# Create your models here.

class Team_Information(models.Model):
    name=models.CharField(max_length=100, null=True,blank=True)
    role= models.CharField(max_length=100, null=True,blank=True)
    picture=models.ImageField(upload_to="media")