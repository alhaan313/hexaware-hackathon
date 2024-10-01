from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile 


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
    img_url = models.URLField(blank=True, null=True)  # New field for storing image URLs

    

    def __str__(self):
        return self.name


### Enrollable Courses
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Ensure each user can enroll in a course only once

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.course.name}"


class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    documentation = models.TextField()

    def __str__(self):
        return f"Content for {self.module.title}"


class Assignment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"Assignment for {self.module.title}"


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_text = models.TextField(blank=True, null=True)
    submission_file = models.FileField(upload_to='submissions/', blank=True, null=True)
    grade = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Submission for {self.assignment.module.title} by {self.user.username}"


class Test(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Test for {self.module.title}"


class UserTestResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"Response by {self.user.username} for {self.test.module.title}"


class CourseProgress(models.Model):       
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Add foreign key to Profile
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_completed = models.BooleanField(default=False)

    def update_progress(self):
        total_modules = Module.objects.filter(course=self.course).count()
        completed_tests = UserTestResponse.objects.filter(user=self.user, test__module__course=self.course, is_correct=True).count()
        
        self.progress = (completed_tests / total_modules) * 100
        if self.progress == 100:
            self.is_completed = True
        self.save()
