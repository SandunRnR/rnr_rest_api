from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    product_version = models.FloatField()
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    data_area = models.CharField(max_length=100)
    product_rec_id = models.CharField(max_length=100)

def __str__(self):
    return self.name