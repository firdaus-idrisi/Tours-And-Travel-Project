from django.urls import path
from .import views


urlpatterns = [
   
   path("flight", views.flight, name="flight"),
   path("booking", views.booking, name="booking"),

   # path("search_flight", views.search_flight, name="search_flight"),
   
   # path("search", views.search, name="search"),
]
