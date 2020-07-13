from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index.html'),
    path('register/', views.register, name='register.html'),
    path('login/', views.login, name='login.html'),
    path('Reg_Done/', views.Reg_Done, name='Reg_Done.html'),

]
