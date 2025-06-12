from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from django.urls import path
from .views import RegisterView,ProtectedHelloView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('hello/',ProtectedHelloView.as_view(),name='hello'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]