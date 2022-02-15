from django.shortcuts import render
from django.views.generic import CreateView
from .models import CarBrand, CarModel, UserCar

def HomeView(request):
    cars = UserCar.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})


class AddUserCar(CreateView):
    model = UserCar
    template_name = 'cars/add_user_car.html'
    fields = ['car_brand', 'car_model', 'first_reg', 'odometer', 'image']
