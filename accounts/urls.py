from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .api_views import ProfileListAPIView  # Import the API view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, next_page='logged_home'), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/access-denied/', views.profile_access_view, name='profile_access_denied'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
    # API route for profiles
    path('api/profiles/', ProfileListAPIView.as_view(), name='profile-list'),
]

