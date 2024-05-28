from django.shortcuts import render

# Create your views here.

@api_view(['POST'])
def CreateForecasting(request):
    if request.method == 'POST':
        # Assuming you are passing 'class_name' and 'confidence' in the request data
        serializer = ForecastingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
