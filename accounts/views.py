from django.shortcuts import render
from rest_framework import generics,status
from . serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProtectedHelloView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"message":f"Hello {request.user.username}! This is protected"})
    
class ForgotPassword(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        new_password = request.data.get('password')

        if not username or not email or not new_password:
            return Response(
                {'error':'All fields are required'},
                status=status.HTTP_404_NOT_FOUND
                )
        
        try:
            user = User.objects.get(username=username,email=email)
        except User.DoesNotExist:
            return Response({'error':'Invalid Email or Password'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        user.set_password(new_password)
        user.save()
        return Response(
            {'message':f'{user.username} You password was reset succesfully'},
            status=status.HTTP_200_OK
        )
    
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {'message':f'{request.user.username} You are succesfully logout'},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {'error':'Invalid or already used token'},
                status=status.HTTP_400_BAD_REQUEST
            )