from django.urls import path
from django.contrib import admin

# from icProject.icApp import views
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('home/details/', views.details, name='base'),
    path('home/about/', views.about, name='about'),
]