from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    # path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),
    # path('course/<int:course_id>/module/<int:module_id>/', views.module_detail, name='module_detail'),

    path('module/content/<int:module_id>/', views.load_module_content, name='load_module_content'),
    
    path('course_id=<int:course_id>/', views.course_detail, name='course_detail'),
    path('course_id=<int:course_id>/assignment_id=<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('course_id=<int:course_id>/module_id=<int:module_id>/', views.take_test, name='take_test'),

    path('course_id=<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('course_id=<int:course_id>/progress/', views.course_progress, name='course_progress'),
    
    # path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    # path('module/<int:module_id>/', views.module_content, name='module_content'),
    # path('module/<int:module_id>/test/', views.take_test, name='take_test'),
    
    # Other URLs for courses and modules
    # path('module/<int:module_id>/assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    # path('module/<int:module_id>/test/<int:test_id>/', views.submit_test, name='submit_test'),


    # path('submit_test/<int:module_id>/', views.submit_test, name='submit_test'),
    # path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),

]