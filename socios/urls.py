from django.contrib import admin
from django.urls import path
from .views import become_member
urlpatterns = [
       path('becomeMember/',become_member,name='createMember'),
] 