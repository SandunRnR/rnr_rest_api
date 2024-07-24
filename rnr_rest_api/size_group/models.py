from django.db import models

# Create your models here.

class Size(models.Model):
    size = models.CharField(max_length = 255)
    size_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

def __str__(self):
    return self.size_name