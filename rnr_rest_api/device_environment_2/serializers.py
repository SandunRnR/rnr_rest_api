from rest_framework import serializers
from .models import Device_2
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


class Device2Serializers(serializers.ModelSerializer):

    class Meta:
        model = Device_2
        fields = '__all__'  # Exclude timestamp to auto-update it


    @classmethod
    def SaveDevice(cls, device_id, current_value, timestamp):
        try:
            entity = cls.Meta.model.objects.create(
                device_id = device_id,
                current_value = current_value,
                timestamp = timezone.now()
            )
        
            return {
                "id": entity.id,
                "device_id": entity.device_id,
                "current_value": entity.current_value,
                "timestamp": entity.timestamp
            }
        except Exception as e:
            return {"error": f"Could not save data: {str(e)}"}


# class ObjectSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Object
#         fields = '__all__'    
    
#     @classmethod
#     def create_object(cls, class_name, confidence):
#         try:
#             entity = cls.Meta.model.objects.create(
#                 class_name=class_name,
#                 confidence=confidence,
#                 timestamp=timezone.now()
#             )

#             return {
#                 "id": entity.id,
#                 "class_name": entity.class_name,
#                 "confidence": entity.confidence,
#                 "timestamp": entity.timestamp
#             }
        
#         except Exception as e:
#             return {"error": f"Could not save data: {str(e)}"}

