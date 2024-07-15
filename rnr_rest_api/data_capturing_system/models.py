from django.db import models
from django.utils import timezone 

# Create your models here.

class DataCapture(models.Model):
    file_name = models.CharField(max_length=255, null=True)
    upload_date_time = models.DateTimeField(default=timezone.now)
    next_action = models.CharField(max_length=50, default='Pending')
    invoice_id = models.CharField(max_length=255,null=True)
    data_id = models.CharField(max_length=255,null=True)
    data = models.CharField(max_length=255,null=True)
    position = models.CharField(max_length=255,null=True)
    x = models.CharField(max_length=255,null=True)
    y = models.CharField(max_length=255,null=True)
    table_data = models.CharField(max_length=255,null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)

    def __str__(self):
        return self.invoice_id
