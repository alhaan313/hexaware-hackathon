from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserListAPIView, ProfileListAPIView  # Importing views

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
