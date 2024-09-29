from django import forms
from .models import Course

class CourseFilterForm(forms.Form):
    platform = forms.ChoiceField(
        choices=Course.PLATFORM_CHOICES,
        required=False,
        label='Platform',
    )
    level = forms.ChoiceField(
        choices=[('All Levels', 'All Levels'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')],
        required=False,
        label='Level',
    )
