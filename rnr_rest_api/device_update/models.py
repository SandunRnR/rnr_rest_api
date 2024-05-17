from django.db import models

# Create your models here.

class DeviceUpdate(models.Model):
    updated_value = models.CharField(max_length=100)
    updated_date_and_time = models.DateTimeField(auto_now_add=True)