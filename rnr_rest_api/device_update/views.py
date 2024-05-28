from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DeviceUpdate
from rest_framework import status
from datetime import datetime
from .serializers import DeviceUpdateSerializer
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@api_view(['POST'])
def CreateDeviceUpdate(request):
    if request.method == 'POST':
        # Assuming you are passing 'class_name' and 'confidence' in the request data
        serializer = DeviceUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def ShowAll(request):
    updated_devices = DeviceUpdate.objects.all()
    serializers = DeviceUpdateSerializer(updated_devices, many = True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def DeleteUpdatedDevice(request,id):
    try:
        updated_device = DeviceUpdate.objects.get(id=id)
    except DeviceUpdate.DoesNotExist:
        return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    
    updated_device.delete()
    return Response({"message": "Deleted successfully"},status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def UpdateUpdatedDevice(request):
    id = request.data.get('id',None)
    if id is None:
        return Response({"error": "ID parameter is required for updating product"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        device = DeviceUpdate.objects.get(id=id)
    except DeviceUpdate.DoesNotExist:
        return Response({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = DeviceUpdateSerializer(device,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
