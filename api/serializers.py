from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add any other fields you want to serialize

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'skills', 'experience']  # Adjust fields as necessary
