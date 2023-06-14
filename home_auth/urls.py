from django.contrib import admin
from django.urls import path
from .views import home, register, log_out, signin
urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('signin/',signin,name='signin'),
    path('logout/',log_out,name='logout'),
]
 