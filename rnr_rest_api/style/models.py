from django.db import models

# Create your models here.
from django.db import models

class Style(models.Model):
    style = models.CharField(max_length=100)
    style_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.style_name
