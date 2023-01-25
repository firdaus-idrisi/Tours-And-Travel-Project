from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
from django.contrib.auth.models import User


class fight_table(models.Model):
    
    From= models.CharField(max_length=150)
    To= models.CharField(max_length=150)
    Check_In = models.DateField()
    Class= models.CharField(max_length=150) 
    Adult= models.IntegerField()
    Children= models.IntegerField()
    
    

    
    
    
