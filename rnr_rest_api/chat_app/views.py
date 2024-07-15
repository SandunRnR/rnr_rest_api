from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChatMessageSerializer
from .models import ChatMessage
from rest_framework import status

from django.shortcuts import get_object_or_404


# @api_view(['POST'])
# def PatientPostMessage(request):
#     data = request.data.copy()
#     data['next_action'] = 'Doctor'
#     serializer = ChatMessageSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def PatientPostMessage(request):
    data = request.data.copy()
    data['next_action'] = 'Doctor'
    serializer = ChatMessageSerializer(data=data)
    if serializer.is_valid():
        chat_message = serializer.save()
        return Response({'id': chat_message.id, 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def DoctorPostMessage(request):
    try:
        chat_message = ChatMessage.objects.filter(next_action='Doctor').last()
        if chat_message:
            chat_message.doctor_response = request.data.get('doctor_response')
            chat_message.next_action = 'Patient'
            chat_message.save()
            return Response(ChatMessageSerializer(chat_message).data, status=status.HTTP_200_OK)
        return Response({'detail': 'No message waiting for doctor response'}, status=status.HTTP_404_NOT_FOUND)
    except ChatMessage.DoesNotExist:
        return Response({'detail': 'No message found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def PatientGetMessage(request, message_id):
    chat_message = get_object_or_404(ChatMessage, id=message_id, next_action='Patient')
    if chat_message.doctor_response:
        return Response({'doctor_response': chat_message.doctor_response}, status=status.HTTP_200_OK)
    return Response({'detail': 'No message waiting for patient'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def PatientGetMessage(request):
#     chat_message = ChatMessage.objects.filter(next_action='Patient').last()
#     if chat_message and chat_message.doctor_response:
#         return Response({'doctor_response': chat_message.doctor_response}, status=status.HTTP_200_OK)
#     return Response({'detail': 'No message waiting for patient'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def DoctorGetMessage(request):
    chat_message = ChatMessage.objects.filter(next_action='Doctor').last()
    if chat_message and chat_message.patient_message:
        return Response({'patient_message': chat_message.patient_message}, status=status.HTTP_200_OK)
    return Response({'detail': 'No message waiting for doctor'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ShowAllMessages(request):
    messages = ChatMessage.objects.all()
    serializer = ChatMessageSerializer(messages, many=True)
    return Response(serializer.data)
