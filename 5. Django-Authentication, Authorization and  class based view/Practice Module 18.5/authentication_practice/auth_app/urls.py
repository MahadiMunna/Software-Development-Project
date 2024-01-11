from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password-with-old-pass/', views.change_pass_with, name='change_pass_with'),
    path('change-password-without-old-pass/', views.change_pass_without, name='change_pass_without'),
]
