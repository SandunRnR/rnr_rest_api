from django.db import models

# Create your models here.

class Forecasting(models.Model):
    forecast_item_id = models.IntegerField()
    forecasting_type_id = models.IntegerField()
    forecasting_value = models.FloatField()
    forecast_date_time = models.DateTimeField()
    created_date_time = models.DateTimeField()
    updated_date_time = models.DateTimeField()
    is_active = models.CharField()

 