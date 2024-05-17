from rest_framework import serializers
from . models import Device_1

class Device1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Device_1
        fields = '__all__'