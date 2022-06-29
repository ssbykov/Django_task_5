from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(max_length=50, null=True)



# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
