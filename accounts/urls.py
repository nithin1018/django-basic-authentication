from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from django.urls import path
from .views import RegisterView,ProtectedHelloView,ForgotPassword,LogoutView,ChangePassword

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('hello/',ProtectedHelloView.as_view(),name='hello'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('login/refresh/',TokenRefreshView.as_view(),name='login_refresh'),
    path('forgot-password/',ForgotPassword.as_view(),name='forgot_password'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('change-password/',ChangePassword.as_view(),name='change_password'),
]
