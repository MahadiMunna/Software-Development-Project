from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('static_app/', include('static_app.urls')),
    path('', views.home),
]
