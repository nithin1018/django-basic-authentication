from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from django.urls import path
from .views import RegisterView,ProtectedHelloView,ForgotPassword,LogoutView,ChangePassword,UserProfile,AdminOnlyView,UserListView,RegisterProfileView,DetailedProfileView,ProfileListView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('hello/',ProtectedHelloView.as_view(),name='hello'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('login/refresh/',TokenRefreshView.as_view(),name='login_refresh'),
    path('forgot-password/',ForgotPassword.as_view(),name='forgot_password'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('change-password/',ChangePassword.as_view(),name='change_password'),
    path('user-profile/',UserProfile.as_view(),name='user_profile'),
    path('admin-only/',AdminOnlyView.as_view(),name='admin_only'),
    path('userlist/',UserListView.as_view(),name='userlist'),
    path('profile-register/',RegisterProfileView.as_view(),name='register_profile'),
    path('profile/',ProfileListView.as_view(),name='list_profile'),
    path('profile/<int:pk>/',DetailedProfileView.as_view(),name='detailed_profile'),
    path('schema/',SpectacularAPIView.as_view(),name='schema'),
    path('docs/swagger/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('docs/redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
]
