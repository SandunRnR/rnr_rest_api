from django.db import models

# Create your models here.
class Service(models.Model):
    service_url = models.URLField(max_length=500)  
    def __str__(self):
        return self.service_url
