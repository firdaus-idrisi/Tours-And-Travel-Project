from django.db import models
from django.conf import settings

# Create your models here.
class Hotels_data(models.Model):
    City=models.CharField(max_length=150,blank=True)
    # Hotel_Name = models.CharField(max_length=150,blank=True)
    # Check_In=models.one(blank=True)
    Check_In=models.DateField(blank=True)
    Check_Out=models.DateField(blank=True)
    Rooms=models.IntegerField(blank=True)
    Adult=models.IntegerField(blank=True)
    Children=models.IntegerField(blank=True)   

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
    

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

class hotel_list(models.Model):
    City=models.CharField(max_length=150,blank=True)
    Hotel_Name=models.CharField(max_length=100)
    # Check_In=models.DateField(blank=True)
    # Check_Out=models.DateField(blank=True)
    Room=models.IntegerField(default=None)
    Adult=models.IntegerField(blank=True)
    Children=models.IntegerField(blank=True)  
    Hotel_Image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    
    def __str__(self):
        return self.City

class Booking_details(models.Model):
    Hotel_Image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    Hotel_Name=models.ForeignKey(hotel_list,on_delete=models.CASCADE)
    Hotel_Price=models.IntegerField()
    Hotel_Rating=models.IntegerField()

class all_hotels_list(models.Model):
    
    City=models.CharField(max_length=150,blank=True)
    hotel_name=models.CharField(max_length=150)
    hotel_price=models.IntegerField()
    hotel_img=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    hotel_rating=models.IntegerField()
    def __str__(self):
        return self.City