from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Style
from .serializers import StyleSerializer

# Create your views here.

@api_view(['GET'])
def show_all_styles(request):
    styles = Style.objects.all()
    serializer = StyleSerializer(styles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_style(request):
    serializer = StyleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_style(request, pk):
    try:
        style = Style.objects.get(pk=pk)
    except Style.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StyleSerializer(style)
    return Response(serializer.data)

@api_view(['PUT'])
def update_style(request, pk):
    try:
        style = Style.objects.get(pk=pk)
    except Style.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StyleSerializer(style, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_style(request, pk):
    try:
        style = Style.objects.get(pk=pk)
    except Style.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    style.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)