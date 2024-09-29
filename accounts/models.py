from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text=False)
    email = models.EmailField(blank=True)  # Automatically set from User model
    degree_specialization = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    certifications = models.TextField(blank=True)  # For storing certifications info
    skills = models.TextField(blank=True)
    internship_details = models.TextField(blank=True)  # For storing internship details
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)  # For storing resume files

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Automatically set email from the User model
        self.email = self.user.email  # Use email from User model
        super().save(*args, **kwargs)

# Automatically create or update Profile when User is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
