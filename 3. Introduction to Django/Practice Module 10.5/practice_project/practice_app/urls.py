from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.app_page),
    path('contact/', views.contact),
    path('about/', views.about),
    path('same/', views.same),
]
