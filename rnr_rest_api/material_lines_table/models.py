from django.db import models

# Create your models here.

class Material(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    product_version = models.FloatField()
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

def __str__(self):
    return self.name