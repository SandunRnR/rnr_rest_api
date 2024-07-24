from django.db import models

# Create your models here.

class Color(models.Model):
    color = models.CharField(max_length=255)
    color_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

def __str__(self):
    return self.color_name