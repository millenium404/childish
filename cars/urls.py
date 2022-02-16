from django.urls import path
from django.urls import re_path
from .views import AddUserCar, SearchView, SoftDeleteView

urlpatterns = [
    path('', SearchView, name='home'),
    path('add-user-car/', AddUserCar.as_view(), name='add-user-car'),
    path('cars/<int:pk>/delete/', SoftDeleteView, name='car-delete'),
    re_path(r'^search/$', SearchView, name='search')
]
