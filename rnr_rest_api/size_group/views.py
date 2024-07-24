from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Size
from .serializers import SizeSerializer

# Create your views here.

@api_view(['GET'])
def show_all_sizes(request):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_size(request):
    serializer = SizeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SizeSerializer(size)
    return Response(serializer.data)

@api_view(['PUT'])
def update_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SizeSerializer(size, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    size.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)