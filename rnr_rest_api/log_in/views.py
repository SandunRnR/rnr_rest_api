from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Login
from .serializers import LoginSerializer
from django.contrib.auth.hashers import check_password

# Create your views here.

@api_view(['POST'])
def Login_User(request):
    email = request.data.get('email')
    password = request.data.get('password')

    print(f"Received email: {email}")
    print(f"Received password: {password}")

    try:
        user = Login.objects.get(email=email)
        print(f"User found: {user.email}")
        print(f"Stored password (hashed): {user.password}")

        if check_password(password, user.password):
            serializer = LoginSerializer(user)
            return Response({
                'message': 'Login successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            print("Password does not match")
            return Response({'message': 'Login failed: Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
    except Login.DoesNotExist:
        print("User does not exist")
        return Response({'message': 'Login failed: User does not exist'}, status=status.HTTP_400_BAD_REQUEST)