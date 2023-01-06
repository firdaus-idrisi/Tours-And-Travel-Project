from django.urls import path
from .import views


urlpatterns = [
   path("Hotel", views.hotel, name="Hotel"),
   path("search", views.search, name="search"),
]
