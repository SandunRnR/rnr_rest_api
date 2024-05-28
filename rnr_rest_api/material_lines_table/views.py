from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import MaterialSerializer
from .models import Material
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    materials = Material.objects.all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def CreateProduct(request):
    serializer = MaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteProduct(request, id):
    try:
        product = Material.objects.get(id=id)
    except Material.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def UpdateProduct(request):
    id = request.data.get('id', None)
    if id is None:
        return Response({"error": "ID parameter is required for updating product"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Material.objects.get(id=id)
    except Material.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaterialSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)