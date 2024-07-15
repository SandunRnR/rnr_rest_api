from django.db import models
from forecast_products.models import Product
import datetime

# Create your models here.

class ProductForecastStage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='product_id')
    operation_number = models.IntegerField(default=0)
    operation = models.CharField(max_length=255, default='null')
    resident = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    production_order_number = models.IntegerField(default=0)
    production_order_type = models.CharField(max_length=255, default='null')

    def __str__(self):
        return f"{self.product.product_id} - {self.operation_number}"