from django.contrib import admin

# Register your models here.
from .models import User,Hotel,Booking,Transaction

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Transaction)

