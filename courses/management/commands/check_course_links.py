# your_app/management/commands/check_course_links.py

from django.core.management.base import BaseCommand
from courses.models import Course
import requests

class Command(BaseCommand):
    help = 'Check course links and remove invalid ones'

    def handle(self, *args, **options):
        invalid_courses = []
        all_courses = Course.objects.all()
        
        for course in all_courses:
            try:
                response = requests.get(course.link, timeout=5)  # Set a timeout for the request
                if response.status_code != 200:
                    invalid_courses.append(course)
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.WARNING(f'Error checking {course.link}: {e}'))
                invalid_courses.append(course)

        if invalid_courses:
            for course in invalid_courses:
                self.stdout.write(self.style.ERROR(f'Removing course: {course.name} - {course.link}'))
                course.delete()
            self.stdout.write(self.style.SUCCESS(f'Invalid courses removed: {len(invalid_courses)}'))
        else:
            self.stdout.write(self.style.SUCCESS('No invalid courses found.'))
