from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserDataSerializer
import requests
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User


# Create your views here.

# @permission_classes([IsAuthenticated])
# class UserProfileView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserProfileSerializer

#     def get_object(self):
#         return self.request.user
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_data(request, username):
    user_data = get_object_or_404(User, username=username)
    serializer = UserDataSerializer(user_data)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_datas(request):
    user_data = get_list_or_404(User)
    serializer = UserDataSerializer(user_data, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_profile(request, *args, **kwargs):
    # Get the user profile instance based on user ID or any other identifier
    user_profile = User.objects.get(user=request.user)

    # Get the data from the request
    data = request.data

    # Update the serializer instance with the data from the request
    serializer = UserDataSerializer(user_profile, data=data, partial=True)

    # Validate and save the updated data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
