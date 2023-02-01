from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField()
    password1=models.IntegerField()
    password2=models.IntegerField()


    def __str__(self):
        return self.username
