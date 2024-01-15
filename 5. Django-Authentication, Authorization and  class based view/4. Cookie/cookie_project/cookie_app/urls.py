from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.set_cookie),
    path('', views.set_session),
    # path('get/', views.get_cookie, name='get_cookie'),
    path('get/', views.get_session),
    # path('del/', views.delete_cookie, name='del_cookie'),
    path('del/', views.del_session),
]
