from rest_framework import serializers
from .models import DeviceUpdate
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


class DeviceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceUpdate
        fields = '__all__'    
    
    @classmethod
    def create_object(cls, updated_value):
        try:
            entity = cls.Meta.model.objects.create(
                updated_value=updated_value,
                updated_date_and_time=timezone.now()
            )

            return {
                "id": entity.id,
                "updated_value": entity.updated_value,
                "updated_date_and_time": entity.updated_date_and_time
            }
        
        except Exception as e:
            return {"error": f"Could not save data: {str(e)}"}