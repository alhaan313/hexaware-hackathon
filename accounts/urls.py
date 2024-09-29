from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/access-denied/', views.profile_access_view, name='profile_access_denied'),
    path('home/', views.logged_home, name='logged_home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
