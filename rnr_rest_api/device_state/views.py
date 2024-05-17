from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import DeviceState
from rest_framework import status
from datetime import datetime
from .serializers import DeviceStateSerializer
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    devices = DeviceState.objects.all()
    serializers = DeviceStateSerializer(devices, many = True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def SaveData(request):
    serializer = DeviceStateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteDeviceState(request,id):
    try:
        device = DeviceState.objects.get(id=id)
    except DeviceState.DoesNotExist:
        return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    
    device.delete()
    return Response({"message": "Deleted successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def UpdateDeviceState(request):
    id = request.data.get('id',None)
    if id is None:
        return Response({"error": "ID parameter is required for updating product"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        device = DeviceState.objects.get(id=id)
    except DeviceState.DoesNotExist:
        return Response({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = DeviceStateSerializer(device,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
