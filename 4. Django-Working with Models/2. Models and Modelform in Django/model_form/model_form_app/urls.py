from django.urls import path
from model_form_app.views import home

urlpatterns = [
    path('', home, name='home'),
]
