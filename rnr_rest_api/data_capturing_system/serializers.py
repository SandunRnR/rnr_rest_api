from rest_framework import serializers
from .models import DataCapture

class DataCaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCapture
        fields = '__all__'
