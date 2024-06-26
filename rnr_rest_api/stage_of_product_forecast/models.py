from django.db import models
from forecast_products.models import Product

# Create your models here.

class ProductForecastStage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='product_id')
    stage_of_product = models.CharField(max_length=255)
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField() 

def __str__(self):
    return f"{self.product.product_id} - {self.stage_of_product}"