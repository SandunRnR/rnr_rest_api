from django.db import models

# Create your models here.

class DeviceState(models.Model):
    device_id = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    command = models.CharField(max_length=100)