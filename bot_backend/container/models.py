from django.db import models


RED = 'Red'
GREEN = 'Green'
BLUE = 'Blue'
COLORS = [
    (GREEN, 'Green'),
    (RED, 'Red'),
    (BLUE, 'Blue')
]

# Create your models here.
class Container(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    full_green = models.BooleanField()
    full_blue = models.BooleanField()
    full_red = models.BooleanField()
    is_active = models.BooleanField()
    token = models.CharField(max_length=256, null=True)


class Report(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    red_sensor = models.BooleanField()
    blue_sensor = models.BooleanField()
    green_sensor = models.BooleanField()
    proximity_sensor_1 = models.BooleanField()
    proximity_sensor_2 = models.BooleanField()
    proximity_sensor_3 = models.BooleanField()
    servomotor_1 = models.BooleanField()
    servomotor_2 = models.BooleanField()
    servomotor_3 = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)