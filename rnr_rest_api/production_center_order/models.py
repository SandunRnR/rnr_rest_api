from django.db import models

# Create your models here.

class Center(models.Model):
    center_number = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    production_type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.center_number