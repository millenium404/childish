from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(SoftDeleteModel):
    name = models.CharField(max_length=50)
    car_brand = models.ForeignKey(CarBrand, null=True, on_delete=models.CASCADE)
    update_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class UserCar(SoftDeleteModel):

    car_brand = models.ForeignKey(CarBrand, null=True, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, null=True, on_delete=models.CASCADE)
    first_reg = models.CharField(max_length=50)
    odometer = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='')

    def save(self):
        super().save()
        im = Image.open(self.image.path)
        min_size = 256
        x, y = im.size
        size = max(min_size, x, y)
        new_im = Image.new('RGB', (size, size))
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        if new_im.height > 200 or img.width > 200:
            output_size = (200, 200)
            new_im.thumbnail(output_size)
            new_im.save(self.image.path)

    def __str__(self):
        return f'{self.pk} | {self.car_brand} | {self.car_model}'

    def get_absolute_url(self):
        return reverse('home')
