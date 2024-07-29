from django.db import models
from django.utils import timezone

class ChatMessage(models.Model):
    patient_message = models.TextField(max_length=255, default='null')
    device_id = models.CharField(max_length=255, default='null')
    doctor_response = models.TextField(max_length=255, default='null')
    next_action = models.CharField(max_length=20, default='null') 
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"ChatMessage({self.patient_message}, {self.doctor_response}, {self.next_action})"
    
