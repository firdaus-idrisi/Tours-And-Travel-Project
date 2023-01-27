from django.contrib import admin


from django.contrib import admin
from .models import Amenities,Hotel,HotelImages,HotelBooking

# Register your models here.

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)

# admin.site.register(hotel_list)
