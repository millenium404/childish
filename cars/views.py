from django.shortcuts import render
from django.views.generic import CreateView
from .filters import CarFilter
from .models import CarBrand, CarModel, UserCar

def HomeView(request):
    cars = UserCar.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})


class AddUserCar(CreateView):
    model = UserCar
    template_name = 'cars/add_user_car.html'
    fields = ['car_brand', 'car_model', 'first_reg', 'odometer', 'image']


def search(request):
    car_list = UserCar.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    return render(request, 'cars/car_list.html', {'filter': car_filter})
