from rest_framework import serializers
from accounts.models import Profile  # Assuming you have a Profile model in your accounts app

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # This will include all fields of the Profile model
        # Alternatively, you can specify the fields you want to include
        # fields = ['id', 'user', 'bio', 'profile_image']  # Example
