from django.db import models

# Create your models here.

class Center(models.Model):
    center_number = models.CharField(max_length=100)
    price = models.FloatField()
    capacity = models.IntegerField()
    total_revenue = models.FloatField()
    age = models.IntegerField()

    def __str__(self):
        return self.center_number