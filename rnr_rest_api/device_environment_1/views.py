from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import Device1Serializer
from .models import Device_1
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    devices = Device_1.objects.all()
    serializer = Device1Serializer(devices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def SaveDevice(request):
    serializer = Device1Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteDevice(request,id):
    try:
        device = Device_1.objects.get(id=id)
    except Device_1.DoesNotExist:
        return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    
    device.delete()
    return Response({"message": "Device deleted successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def UpdateDevice(request):
    id = request.data.get('id',None)
    if id is None:
        return Response({"error": "ID parameter is required for updating product"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        device = Device_1.objects.get(id=id)
    except Device_1.DoesNotExist:
        return Response({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = Device1Serializer(device,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
