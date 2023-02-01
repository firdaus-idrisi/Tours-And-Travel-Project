from django.urls import path
from .import views


urlpatterns = [
   path("Hotel", views.hotel, name="Hotel"),
   path("book", views.Book, name="Book"),
   path("search", views.search, name="search"),
   
]
