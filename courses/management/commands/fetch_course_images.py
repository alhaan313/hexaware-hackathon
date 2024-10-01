# your_app/management/commands/fetch_course_images.py

from django.core.management.base import BaseCommand
from courses.models import Course
from courses.ai_utils import fetch_course_image  # Assuming your function is in utils.py

class Command(BaseCommand):
    help = 'Fetch course images and save them to the img_url field'

    def handle(self, *args, **kwargs):
        courses = Course.objects.all()
        for course in courses:
            image_url = fetch_course_image(course.link)
            course.img_url = image_url
            course.save()
            self.stdout.write(self.style.SUCCESS(f'Updated image URL for course: {course.name}'))
