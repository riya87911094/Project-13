from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index.html'),
    path('register/',views.register),
    path('login/',views.login),
    path('register/reg_done/',views.reg_done),
    
    
  
    
]
