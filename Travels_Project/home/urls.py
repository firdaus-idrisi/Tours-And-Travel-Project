from django.urls import path
from .import views

urlpatterns = [
   path("home", views.home, name="home"),
   path('hotel-detail/<uid>/' , views.hotel_detail , name="hotel_detail"),
   path('check_booking/' , views.check_booking),   
]
