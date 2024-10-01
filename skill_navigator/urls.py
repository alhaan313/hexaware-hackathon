from django.contrib import admin
from django.urls import path, include
from accounts import views  # Import views from the accounts app


urlpatterns = [
    
    path('', views.redirect_to_home, name='redirect_to_home'),
    path('home/', views.logged_home, name='logged_home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),   # Include accounts app URLs
    path('courses/', include('courses.urls')),     # Include course app URLs
    path('api/', include('api.urls')),             # Include api app URLs
]
