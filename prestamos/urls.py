from django.contrib import admin
from django.urls import path
from .views import create_cosigner,make_loan,all_loans, replace_cosigner,replace_for_old_cosigner,all_cosigners,loans_cosigner
urlpatterns = [
    path('makeloan/',make_loan,name='make_loan'),
    path('cosigner/',create_cosigner,name='create_cosigner'),
    path('all_loans/',all_loans,name='view_loans'),
    path('all_cosigners/',all_cosigners,name='all_cosigners'),
    path('replace_cosigner/<int:cosigner_id>/',replace_cosigner,name='replace_cosigner'),
    path('loans_cosigner/<int:cosigner_id>/',loans_cosigner,name='loans_cosigner'),
    path('replace_old_cosigner/<int:cosigner_id>/',replace_for_old_cosigner,name='replace_for_old_cosigner'),

]