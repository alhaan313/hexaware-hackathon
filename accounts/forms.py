from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(help_text=False)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password', help_text=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password', help_text=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Remove help texts
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'degree_specialization', 
            'phone_number', 
            'certifications', 
            'internship_details', 
            'linkedin_profile', 
            'github_profile', 
            'resume',
            'skills'
        ]
