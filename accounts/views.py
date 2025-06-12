from django.shortcuts import render
from rest_framework import generics
from . serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProtectedHelloView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"message":f"Hello {request.user.username}! This is protected"})