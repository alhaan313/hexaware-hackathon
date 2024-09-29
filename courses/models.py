from django.db import models

class Course(models.Model):
    PLATFORM_CHOICES = [
        ('udemy', 'Udemy'),
        ('coursera', 'Coursera'),
        ('edx', 'edX'),
        ('skillshare', 'Skillshare'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)  # Example: '22 total hours'
    lectures = models.IntegerField()
    level = models.CharField(max_length=50)  # Example: 'All Levels'
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # Example: 4.6
    reviews = models.IntegerField()
    course_code = models.CharField(max_length=10, unique=True)
    link = models.URLField()
    batch_name = models.CharField(max_length=255)
    enrollable = models.BooleanField(default=False)  # To differentiate enrollable courses
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.name
