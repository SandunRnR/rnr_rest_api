from rest_framework import serializers
from .models import Forecasting
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

class ForecastingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forecasting
        fields = '__all__'    
