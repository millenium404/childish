from django.urls import path
from django.urls import re_path
from .views import HomeView, AddUserCar, search

urlpatterns = [
    path('', search, name='home'),
    path('add-user-car/', AddUserCar.as_view(), name='add-user-car'),
    re_path(r'^search/$', search, name='search')
]
