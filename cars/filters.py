from .models import UserCar
import django_filters

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = UserCar
        fields = ['car_brand', 'car_model']
