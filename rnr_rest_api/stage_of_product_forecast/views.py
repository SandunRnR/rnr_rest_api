from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProductForecastStage
from .serializers import ProductForecastStageSerializer

# @api_view(['GET'])
# def get_product_forecast_stages(request):
#     stages = ProductForecastStage.objects.all()
#     serializer = ProductForecastStageSerializer(stages, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def create_product_forecast_stage(request):
#     serializer = ProductForecastStageSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_product_forecast_stage(request, pk):
#     try:
#         stage = ProductForecastStage.objects.get(pk=pk)
#     except ProductForecastStage.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductForecastStageSerializer(stage, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_product_forecast_stage(request, pk):
#     try:
#         stage = ProductForecastStage.objects.get(pk=pk)
#     except ProductForecastStage.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     stage.delete()
#     return Response({'message': 'Successfully Deleted !'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_product_forecast_stages(request):
    stages = ProductForecastStage.objects.all()
    serializer = ProductForecastStageSerializer(stages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product_forecast_stage(request):
    serializer = ProductForecastStageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product_forecast_stage(request, pk):
    try:
        stage = ProductForecastStage.objects.get(pk=pk)
    except ProductForecastStage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductForecastStageSerializer(stage, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product_forecast_stage(request, pk):
    try:
        stage = ProductForecastStage.objects.get(pk=pk)
    except ProductForecastStage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    stage.delete()
    return Response({'message': 'Successfully Deleted!'}, status=status.HTTP_204_NO_CONTENT)