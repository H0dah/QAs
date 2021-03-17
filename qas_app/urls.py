from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='qas-home'),
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('friends/', views.friends, name='friends'),
    path('notifications/', views.notifications, name='notifications'),
]