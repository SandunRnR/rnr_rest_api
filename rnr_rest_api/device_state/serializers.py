from rest_framework import serializers
from .models import DeviceState
from django.views.decorators.csrf import csrf_exempt

class DeviceStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceState
        fields = '__all__'
