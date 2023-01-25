from django.urls import path
from .import views


urlpatterns = [
   path("flight", views.flight, name="flight"),
   # path("search", views.search, name="search"),
]
