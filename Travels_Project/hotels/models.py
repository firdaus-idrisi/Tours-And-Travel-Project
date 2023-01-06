from django.db import models

# Create your models here.
class Hotels_data(models.Model):
    Hotel_Name=models.CharField(max_length=150)
    Check_In=models.IntegerField()
    Check_Out=models.IntegerField()
    Rooms=models.IntegerField()
    Adult=models.IntegerField()
    Children=models.IntegerField()