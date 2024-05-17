from django.db import models
from django.db import models

# Create your models here.

class Device_1(models.Model):
    device_id = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)

def __str__(self):
    return self.name