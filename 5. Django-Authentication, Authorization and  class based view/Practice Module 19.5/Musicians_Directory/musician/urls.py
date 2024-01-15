from django.urls import path
from . import views

urlpatterns=[
    path('add_musician/', views.AddMusicianCreateView.as_view(), name='add_musician'),
    path('edit_musician/<int:id>/', views.UpdateMusicianView.as_view(), name='edit_musician'),
]