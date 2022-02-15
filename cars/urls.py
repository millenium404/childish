from django.urls import path
from .views import HomeView, AddUserCar

urlpatterns = [
    path('', HomeView, name='home'),
    path('add-user-car/', AddUserCar.as_view(), name='add-user-car'),
]
