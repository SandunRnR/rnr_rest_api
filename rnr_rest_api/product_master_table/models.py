from django.db import models

# Create your models here.

class Product(models.Model):
    product_number = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_dimension = models.CharField(max_length=255)

def __str__(self):
    return self.product_name