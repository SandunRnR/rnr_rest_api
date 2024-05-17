from django.db import models

# Create your models here.

class Device_2(models.Model):
    device_id = models.CharField(max_length=100)
    current_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
