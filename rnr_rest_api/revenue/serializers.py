from rest_framework import serializers
from .models import Center

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'
