from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('',views.index,name="index"),
   path('index',views.index,name="index"),
   path('index.html',views.index,name="index"),
   path("index2",views.index2,name="index2"),
   path("register", views.register_request, name="register"),
   path("Contact",views.Contact,name="Contact"),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name= "logout"),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
   path("password_reset", views.password_reset_request, name="password_reset")

]