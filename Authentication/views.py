from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'deleted': 1}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


    def perform_create(self, serializer):
        serializer.save()  # Additional logic can be added here if needed


