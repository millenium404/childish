from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView
from .filters import CarFilter
from .models import CarBrand, CarModel, UserCar, SoftDeleteModel
from django.contrib.auth.models import User


class AddUserCar(CreateView):
    model = UserCar
    template_name = 'cars/add_user_car.html'
    fields = ['car_brand', 'car_model', 'first_reg', 'odometer', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def SearchView(request):
    car_list = UserCar.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    return render(request, 'cars/car_list.html', {'filter': car_filter})


def SoftDeleteView(request, pk):
    car = UserCar.objects.get(pk=pk)
    if request.method == 'POST':
        car.soft_delete()
        return redirect('home')
    context = {
        'car': car
    }

    return render(request, 'cars/usercar_confirm_delete.html', context)
