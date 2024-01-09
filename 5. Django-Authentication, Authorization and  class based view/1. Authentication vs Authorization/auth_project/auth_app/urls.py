from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.userlogout, name='logout'),
    path('change_password/', views.changePass, name='changePass'),
    path('change_password2/', views.changePass2, name='changePass2'),
    path('edit_Profile/', views.editProfile, name='editProfile'),
]