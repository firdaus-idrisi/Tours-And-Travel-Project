from django.contrib import admin


from django.contrib import admin
from .models import Hotels_data,Room,Booking,hotel_list,Booking_details,all_hotels_list

# Register your models here.

admin.site.register(Booking_details)
admin.site.register(Hotels_data)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(all_hotels_list)

# admin.site.register(hotel_list)
