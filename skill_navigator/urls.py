from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),   # Include accounts app URLs
    path('courses/', include('courses.urls')),     # Include course app URLs
    path('api/', include('api.urls')),             # Include api app URLs
    path('mentor/', include('mentor.urls')),
]
