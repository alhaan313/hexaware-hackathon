from django.shortcuts import render
from .models import Course
from .forms import CourseFilterForm
from .ai_utils import *
import requests
from bs4 import BeautifulSoup

from django.core.cache import cache
import requests
from bs4 import BeautifulSoup

# Function to fetch and cache the course image
def fetch_course_image(url):
    # Try fetching the image from cache first
    cached_image = cache.get(url)
    if cached_image:
        return cached_image
    
    # If not cached, fetch from the external URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_image_tag = soup.find('meta', property='og:image')
        if meta_image_tag:
            image_url = meta_image_tag['content']
            # Cache the image URL with the course link as the key
            cache.set(url, image_url, timeout=60 * 60 * 24)  # Cache for 1 day (adjust timeout as needed)
            return image_url
    
    return "https://via.placeholder.com/300x200"


def course_list(request):
    all_courses = Course.objects.all()
    enrollable_courses = all_courses.filter(enrollable=True)[:5]
    other_courses = all_courses.filter(enrollable=False)
    
    if request.user.is_authenticated:
        user_profile = request.user.profile  # Assuming you have a user profile with certifications
        recommended_courses = recommend_courses(user_profile)
    else:
        recommended_courses = []  # If the user is not logged in

    form = CourseFilterForm(request.GET or None)
    
    if form.is_valid():
        if form.cleaned_data['platform']:
            other_courses = other_courses.filter(platform=form.cleaned_data['platform'])
        if form.cleaned_data['level']:
            other_courses = other_courses.filter(level=form.cleaned_data['level'])

    for course in other_courses:
        course.image_url = fetch_course_image(course.link)

    context = {
        'recommended_courses': recommended_courses,
        'enrollable_courses': enrollable_courses,
        'other_courses': other_courses,
        'form': form
    }
    return render(request, 'courses/course_list.html', context)