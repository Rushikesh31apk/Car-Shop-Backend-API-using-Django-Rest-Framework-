from django.db import models

# Create your models here.
class CarList(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_color = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    car_mileage = models.IntegerField()
    car_description = models.TextField()
    car_image = models.ImageField(upload_to='car_images')

    def __str__(self):
        return self.car_name
