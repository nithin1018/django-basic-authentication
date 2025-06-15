from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSuperUser
from . serializers import RegisterSerializer,UserSerializer,RegisterProfileSerializer
from .filters import UserFilter
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProtectedHelloView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer
    def get(self,request):
        return Response({"message":f"Hello {request.user.username}! This is protected"})
    
class ForgotPassword(APIView):
    serializer_class = RegisterSerializer
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
            return Response(
                            {'error':'Invalid Email or Password'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        user.set_password(new_password)
        user.save()
        return Response(
            {'message':f'{user.username} You password was reset succesfully'},
            status=status.HTTP_200_OK
        )
    
class LogoutView(APIView):
    serializer_class = RegisterSerializer
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

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer
    def post(self, request):
        user=request.user
        old_password=request.data.get('old_password')
        new_password=request.data.get('new_password')
        if not old_password or not new_password:
            return Response(
                {'error':'Both old password and new password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if old_password == new_password:
            return Response(
                {'error':'Old Password and New Password cannot be the same'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not user.check_password(old_password):
            return Response(
                {'error':'Old password is incorrect'},
                status=status.HTTP_403_FORBIDDEN
            )
        user.set_password(new_password)
        user.save()
        return Response(
            {'message':'Succesfullt updated the password'},
            status=status.HTTP_200_OK
        )
    
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
     
    def put(self, request):
        data = request.data.copy()

    # Block username change attempt
        if 'username' in data and data['username'] != request.user.username:
            return Response(
                {'error': 'You cannot change your username.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(request.user, data=request.data, partial=True,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AdminOnlyView(APIView):
    permission_classes =[IsAuthenticated, IsSuperUser]
    serializer_class = RegisterSerializer
    def get(self, request):
        return Response(
            {'message':'Welcome Admin'}
        )
    
class UserListView(ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

class ProfileView(generics.CreateAPIView):
    serializer_class = RegisterProfileSerializer