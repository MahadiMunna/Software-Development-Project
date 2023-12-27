from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about'),
    path('django_form/', views.djangoForm, name='django_form'),
    path('validation_form/', views.studentForm, name='validation_form'),
    path('password_form/', views.passwordForm, name='pass_form'),
]
