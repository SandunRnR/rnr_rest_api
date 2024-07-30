# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import DataCapture
# from rest_framework import status
# from .serializers import DataCaptureSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from datetime import datetime
# from .firebase import upload_file_to_firebase


# # Create your views here.

# @api_view(['POST'])
# def create_data(request):
#     if request.method == 'POST':
#         serializer = DataCaptureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# # Get All Details from the database 
# @api_view(['GET'])
# def get_all_data(request):
#     if request.method == 'GET':
#         # Retrieve all invoice data from the database
#         data = DataCapture.objects.all()
        
#         # Serialize the data
#         serializer = DataCaptureSerializer(data, many=True)
        
#         # Return a response with serialized data
#         return Response(serializer.data)
    
# @api_view(['POST'])
# def file_uploaded(request):
#     if request.method == 'POST':
#         file = request.FILES.get('file')
        
#         if not file:
#             return Response({"error": "file is required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         original_file_name = file.name
        
#         try:
#             # Upload the file to Firebase and get the file URL
#             file_url = upload_file_to_firebase(file, original_file_name)
            
#             # Save the original file name and other details to the database
#             data_capture = DataCapture(
#                 file_name=original_file_name,
#                 upload_date_time=datetime.now(),
#                 next_action='AI'  # Initially set to 'AI'
#             )
            
#             data_capture.save()
            
#             return Response({"message": "File uploaded and processed successfully"}, status=status.HTTP_201_CREATED)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# # # Get Details using Id
# # @api_view(['GET'])
# # def get_data_by_id(request, id):
# #     if request.method == 'GET':
# #         try:
# #             # Retrieve data by ID from the database
# #             data = DataCapture.objects.get(pk=id)
# #         except DataCapture.DoesNotExist:
# #             return Response(status=status.HTTP_404_NOT_FOUND)
        
# #         # Serialize the data
# #         serializer = DataCaptureSerializer(data)
        
# #         # Return a response with serialized data
# #         return Response(serializer.data)

# # @api_view(['DELETE'])
# # def delete_data_by_id(request, id):
# #     if request.method == 'DELETE':
# #         try:
# #             # Retrieve the data by its ID
# #             data = DataCapture.objects.get(pk=id)
            
# #             # Delete the data
# #             data.delete()
            
# #             return Response({"message": f"Data with id {id} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# #         except DataCapture.DoesNotExist:
# #             return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
# #         except Exception as e:
# #             return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# # @api_view(['PUT'])
# # def update_data_by_id(request, id):
# #     if request.method == 'PUT':
# #         try:
# #             # Retrieve the data by its ID
# #             data = DataCapture.objects.get(pk=id)
            
# #             # Deserialize the updated data
# #             serializer = DataCaptureSerializer(data, data=request.data)
            
# #             if serializer.is_valid():
# #                 serializer.save()  # Save the updated data
# #                 return Response(serializer.data, status=status.HTTP_200_OK)
            
#             # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# #         except DataCapture.DoesNotExist:
# #             return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
# #         except Exception as e:
# #             return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
