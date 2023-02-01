from django.urls import path
from .import views


urlpatterns = [
   
   path("flight", views.flight, name="flight"),
   path("flight_search", views.flight_search, name="flight_search"),
   path("query/places/<str:q>", views.query, name="query"),
   path("flight_search/ticket/book", views.book, name="book"),
   path("review", views.review, name="review"),
   path("flight_search/ticket/bookings", views.bookings, name="bookings"),

   # path("search_flight", views.search_flight, name="search_flight"),
   
   # path("search", views.search, name="search"),
]
