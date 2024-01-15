from django.urls import path
from . import views

urlpatterns=[
    path('add_album/', views.AddAlbumCreateView.as_view(), name='add_album'),
    path('edit_album/<int:id>/', views.UpdateAlbumView.as_view(), name='edit_album'),
    path('delete_album/<int:id>/', views.DeleteAlbumView.as_view(), name='delete_album'),
]