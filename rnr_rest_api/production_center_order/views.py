from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Center
from .serializers import CenterSerializer

# Create your views here.

@api_view(['GET'])
def show_all_centers(request):
    centers = Center.objects.all()
    serializer = CenterSerializer(centers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_center(request):
    serializer = CenterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_center(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CenterSerializer(center)
    return Response(serializer.data)

@api_view(['PUT'])
def update_center(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CenterSerializer(center, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_center(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    center.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)