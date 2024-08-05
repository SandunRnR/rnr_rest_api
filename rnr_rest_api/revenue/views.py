from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Center
from .serializers import RevenueSerializer

# Create your views here.

@api_view(['GET'])
def show_all_revenues(request):
    centers = Center.objects.all()
    serializer = RevenueSerializer(centers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_revenue(request):
    serializer = RevenueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_revenue(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RevenueSerializer(center)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_revenue(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RevenueSerializer(center, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_revenue(request, pk):
    try:
        center = Center.objects.get(pk=pk)
    except Center.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    center.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)