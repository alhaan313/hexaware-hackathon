from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mentor_page, name='mentor_page'),  # Root URL for mentor
    #path('gemini-ai/', views.gemini_ai_query, name='gemini_ai_query'),  
]
